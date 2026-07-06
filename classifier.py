import os
from dotenv import load_dotenv
import anthropic
from datasets import load_dataset

load_dotenv()
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

if anthropic_api_key:
    client = anthropic.Anthropic(api_key=anthropic_api_key)
else:
    print("API key is not valid, please check.")

CATEGORIES = [
    "Billing and Payments",
    "Customer Service",
    "General Inquiry",
    "IT Support",
    "Product Support",
    "Returns and Exchanges",
    "Sales and Pre-Sales",
    "Service Outages and Maintenance",
    "Technical Support",
]
URGENCY_LEVELS = ["Low", "Medium", "High"]


def classify_ticket(subject: str, body: str) -> dict:
    """Classify a support ticket's category, urgency, and language via Claude."""
    prompt = (
        f"Classify this support ticket. Reply in exactly this format, nothing else:\n\n"
        f"Category: <one of {', '.join(CATEGORIES)}>\n"
        f"Urgency: <one of {', '.join(URGENCY_LEVELS)}>\n"
        f"Language: <the language of the ticket, in English>\n\n"
        f"Ticket subject: {subject}\n"
        f"Ticket body: {body}"
    )

    try:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=100,
            messages=[{"role": "user", "content": prompt}],
        )
        raw_text = response.content[0].text.strip()
    except Exception as e:
        return {
            "category": "Error",
            "urgency": "Error",
            "language": "Error",
            "raw_response": str(e),
        }
    result = {
        "category": "Unknown",
        "urgency": "Unknown",
        "language": "Unknown",
        "raw_response": raw_text,
    }
    for line in raw_text.splitlines():
        if line.startswith("Category:"):
            result["category"] = line.split(":", 1)[1].strip()
        elif line.startswith("Urgency:"):
            result["urgency"] = line.split(":", 1)[1].strip()
        elif line.startswith("Language:"):
            result["language"] = line.split(":", 1)[1].strip()
    return result
