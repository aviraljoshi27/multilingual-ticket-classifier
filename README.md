# Multilingual Support Ticket Classifier

Automatically classifies customer support tickets by **category**, **urgency**, and **language** — using Claude's zero-shot reasoning instead of a trained classifier.

🔗 **Live demo:** _[add your HuggingFace Spaces URL here once deployed]_

---

## Why this exists

Companies with international customers get support tickets in multiple languages, and every ticket has to be manually read, categorized, and routed before anyone can act on it. That triage step is repetitive, slow, and doesn't need a human — it's a textbook use case for an LLM: understand free-form text in any language and output a structured decision.

This project builds that triage layer: given a raw ticket in English or German, it returns the correct routing category, an urgency level, and the detected language — with no fine-tuning, no training data, just a well-designed prompt.

---

## How it works

1. A support ticket (raw text, any supported language) is sent to Claude via the Anthropic API.
2. The prompt instructs Claude to classify the ticket into one of **9 real routing categories** derived directly from the dataset's actual queue values (not invented categories — verified against the data itself).
3. Claude also returns an urgency level and the detected language for the same ticket, in a single call.
4. The result is served through a simple Gradio interface — type or paste a ticket, get an instant classification.

**Dataset:** [Tobi-Bueck/customer-support-tickets](https://huggingface.co/datasets/Tobi-Bueck/customer-support-tickets) (Hugging Face) — 61.8k real support tickets in English and German.

---

## Tech stack

- **Python**
- **Anthropic API** (Claude) — zero-shot classification
- **Gradio** — web interface
- **Hugging Face Spaces** — deployment
- **Hugging Face Datasets** — data source

---

## Project structure

```
multilingual-ticket-classifier/
├── classifier.py      # classify_ticket() — core classification logic
├── app.py             # Gradio interface wrapping classify_ticket()
├── explore_data.py     # dataset exploration (not imported by the app)
├── requirements.txt
├── .env                # local only, not committed
└── README.md
└── .env.example
```

---

## Running it locally

```bash
git clone https://github.com/aviraljoshi27/multilingual-ticket-classifier.git
cd multilingual-ticket-classifier
uv venv .venv
source .venv/bin/activate      
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
ANTHROPIC_API_KEY=your_key_here
```

Then run:

```bash
python app.py
```

This starts a local Gradio server (usually at `http://127.0.0.1:7860`).

---

## Limitations & next steps

- Zero-shot only — no fine-tuning or few-shot examples yet, so edge-case tickets may be misclassified.
- No confidence score returned alongside the classification.

---
