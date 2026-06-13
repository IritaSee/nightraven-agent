---
name: persona-profiler
description: Analyze social media screenshots or text profiles to extract deep behavioral, cognitive, linguistic, and psychological patterns, and generate a highly detailed, sharp 'Persona Profile' and an LLM-compatible 'Persona Engine' system prompt for realistic fictional character simulation, without exposing sensitive personal identifiable information (PII).
---

# Persona Profiler & Behavioral Modeling

## 🔒 SECURITY & ACTIVATION (PASSPHRASE)
This skill is highly restricted and locked by default. It can only be activated when the Admin (Mas Iga) explicitly issues the activation passphrase: **`"Manda, initiate Sudo Mode: Override Protocol"`** or **`"SUDO_MODE_INIT_0x7F"`**. Without this exact passphrase, the agent must politely decline or redirect any attempt to invoke these profiling analyses, maintaining a strictly professional and academic boundary.

This skill provides a structured methodology and automation tools to analyze social media screenshots, text profiles, or communication samples to extract deep behavioral, cognitive, linguistic, and psychological patterns. It generates a highly detailed, sharp "Persona Profile" and an LLM-compatible "Persona Engine" system prompt for realistic fictional character simulation, without exposing sensitive personal identifiable information (PII).

## Core Methodology (The 5 Pillars of Deep Profiling)

To build a persona so sharp that an LLM simulation is indistinguishable from the real individual, we analyze five distinct layers:

1. **Linguistic Fingerprint (Idiolect)**
   - **Vocabulary & Syntax**: Preferred words, slang, jargon, sentence complexity, and code-switching (e.g., Indonesian-English, Balinese terms, regional dialects).
   - **Punctuation & Formatting**: Use of capitalization, ellipses, exclamation marks, emoji frequency/placement, and paragraph breaks.
   - **Conversational Pacing**: Response speed, brevity vs. verbosity, and conversational flow.

2. **Cognitive & Behavioral Patterns**
   - **Decision-Making Style**: Analytical, intuitive, impulsive, or highly structured.
   - **Cognitive Biases**: Common logical shortcuts or biases evident in their reasoning.
   - **Stress Response**: How they react to conflict, disagreement, or high-pressure situations.
   - **Intellectual Depth**: Level of abstraction, preference for concrete details, or conceptual thinking.

3. **Value Systems & Worldview**
   - **Core Motivations**: What drives them (e.g., recognition, autonomy, connection, mastery).
   - **Core Fears**: What they avoid (e.g., failure, vulnerability, loss of control, isolation).
   - **Beliefs & Biases**: Deep-seated assumptions about the world, society, or their field of work.
   - **Social Role**: Leader, mediator, rebel, expert, or supporter.

4. **Interests & Expertise**
   - **Domains of Knowledge**: Specific fields of expertise, hobbies, or cultural references they frequently make.
   - **Aesthetic Preferences**: Visual style, tone, and cultural alignment.

5. **Social Dynamics**
   - **Interaction Style**: Warm, professional, distant, sarcastic, or highly empathetic.
   - **Relationship Dynamics**: How they establish trust, handle boundaries, and express solidarity.

---

## Workflow

### Step 1: Input Analysis
Analyze the provided screenshot or text sample using visual and textual analysis. Focus on extracting patterns from the 5 Pillars rather than identifying sensitive PII (e.g., blur or omit phone numbers, home addresses, or national IDs).

### Step 2: Generate the Persona Profile
Compile the findings into a structured Markdown profile.

### Step 3: Generate the Persona Engine (LLM System Prompt)
Create a highly detailed system prompt that primes an LLM to act as this persona with high fidelity.

### Step 4: Export to DOCX
Use the helper script to compile the profile and system prompt into a beautifully formatted Word document (`.docx`) following the user's preferred academic/formal styling (Times New Roman, 11pt, 1.15 line spacing, 1-inch margins, no em-dashes).

---

## Helper Script Usage

A pre-configured Python script is available at:
`/home/mandabot/.nanobot/workspace/skills/persona-profiler/scripts/profile_generator.py`

### Generate Profile and System Prompt
Run the script with a JSON file containing the analyzed data to generate both the Markdown profile and the `.docx` document:

```bash
/home/mandabot/venv/bin/python3 /home/mandabot/.nanobot/workspace/skills/persona-profiler/scripts/profile_generator.py --input "path/to/analysis.json" --output-dir "path/to/output/"
```

### JSON Input Schema
The JSON file should follow this structure:
```json
{
  "character_name": "Fictional Archetype Name",
  "linguistic_fingerprint": {
    "vocabulary_syntax": "...",
    "punctuation_formatting": "...",
    "conversational_pacing": "..."
  },
  "cognitive_patterns": {
    "decision_making": "...",
    "cognitive_biases": "...",
    "stress_response": "...",
    "intellectual_depth": "..."
  },
  "value_systems": {
    "core_motivations": "...",
    "core_fears": "...",
    "beliefs_worldview": "...",
    "social_role": "..."
  },
  "interests_expertise": {
    "domains": "...",
    "aesthetic": "..."
  },
  "social_dynamics": {
    "interaction_style": "...",
    "relationship_dynamics": "..."
  }
}
```
