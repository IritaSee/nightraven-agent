import requests
from bs4 import BeautifulSoup
import argparse
import json
import os

BASE_URL = "https://timgravid.baysatriow.com"
LOGIN_URL = f"{BASE_URL}/login"

CREDENTIALS = {
    "super_admin": {"email": "super@timgravid.com", "password": "password"},
    "admin": {"email": "admin@timgravid.com", "password": "password"},
    "approver": {"email": "finance@timgravid.com", "password": "password"},
    "pengawas": {"email": "pengawas@timgravid.com", "password": "password"},
}

def get_csrf_token(session):
    response = session.get(LOGIN_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    token_input = soup.find('input', {'name': '_token'})
    if token_input:
        return token_input['value']
    return None

def login(session, role):
    if role not in CREDENTIALS:
        raise ValueError(f"Invalid role: {role}")

    token = get_csrf_token(session)
    if not token:
        raise Exception("Could not find CSRF token")

    payload = {
        "_token": token,
        "email": CREDENTIALS[role]["email"],
        "password": CREDENTIALS[role]["password"]
    }

    response = session.post(LOGIN_URL, data=payload)
    if response.status_code == 200:
        return True
    return False

def main():
    parser = argparse.ArgumentParser(description="TIMGRAVID Client")
    parser.add_argument("--role", choices=CREDENTIALS.keys(), required=True, help="Role to login as")
    parser.add_argument("--action", choices=["dashboard", "orders", "blocks", "articles", "verification", "statistics", "settings", "raw", "qa"], default="dashboard", help="Action to perform")
    parser.add_argument("--url", help="URL for raw action")

    args = parser.parse_args()

    session = requests.Session()

    if login(session, args.role):
        action_map = {
            "dashboard": "/app/dashboard",
            "orders": "/app/orders",
            "blocks": "/app/blocks",
            "articles": "/app/articles",
            "verification": "/app/verification",
            "statistics": "/app/statistics",
            "settings": "/app/settings",
        }

        if args.action == "qa":
            # First, get the dashboard to find available links
            dashboard_response = session.get(BASE_URL + "/app/dashboard")
            soup = BeautifulSoup(dashboard_response.text, 'html.parser')
            sidebar_links = [a['href'] for a in soup.find_all('a', href=True) if '/app/' in a['href']]

            # Remove duplicates and dashboard itself
            sidebar_links = list(set(sidebar_links))

            results = {}
            for link in sidebar_links:
                target_url = link if link.startswith('http') else BASE_URL + link
                response = session.get(target_url)

                is_authorized = response.status_code == 200 and response.url == target_url

                results[link] = {
                    "status_code": response.status_code,
                    "final_url": response.url,
                    "authorized": is_authorized,
                    "title": BeautifulSoup(response.text, 'html.parser').title.string if BeautifulSoup(response.text, 'html.parser').title else "No Title"
                }
            print(json.dumps(results, indent=2))
        else:
            # Original behavior for single action
            response = session.get(BASE_URL + action_map.get(args.action, "/app/dashboard"))
            soup = BeautifulSoup(response.text, 'html.parser')
            for script in soup(["script", "style"]):
                script.decompose()
            print(soup.get_text(separator='\n', strip=True))
    else:
        print("Login failed")

if __name__ == "__main__":
    main()
