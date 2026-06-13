---
name: quantitative-market-validation
description: Evidence-based, data-driven validation workflow using specialized subagents to verify market demand.
---

# Quantitative Market Validation

Use this skill to perform evidence-based market validation that prioritizes quantitative data over qualitative assumptions. This workflow often involves deploying specialized subagents to gather and analyze data.

## When to Use
- Validating a new product concept (e.g., SakuVet).
- Assessing market demand for a specific feature.
- Providing data-driven justification for business decisions.

## Steps

1. **Define Hypotheses**: Identify the core assumptions that need validation (e.g., "Veterinarians need a modular calculator platform").
2. **Identify Data Sources**: Determine where quantitative evidence can be found (e.g., search trends, competitor traffic, survey results, app store data).
3. **Deploy Subagents**: Use specialized subagents or automated scripts to scrape data, perform web searches, or analyze large datasets.
4. **Data Aggregation**: Collect all findings into a structured format (e.g., CSV or JSON).
5. **Statistical Analysis**: Perform analysis to determine significance, trends, and correlations.
6. **Synthesize Evidence**: Create a report that links the quantitative findings back to the original hypotheses.

## Tools
- `web_search`: To gather market trends and competitor data.
- `exec`: To run data analysis scripts (Python/Pandas).
- `write_file`: To document the validation report.

## Example Output
- A summary table showing search volume for "veterinary clinical tools" vs "medical calculators".
- A conversion rate estimate based on similar niche platforms.
- A "Go/No-Go" recommendation backed by specific data points.
