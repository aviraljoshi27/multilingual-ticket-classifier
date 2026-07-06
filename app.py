import gradio as gr
from classifier import classify_ticket


def run_classifier(subject, body):
    result = classify_ticket(subject, body)
    category = result["category"]
    urgency = result["urgency"]
    language = result["language"]
    return category, urgency, language


response = gr.Interface(
    fn=run_classifier,
    inputs=[gr.Textbox(label="Subject"), gr.Textbox(label="Body")],
    outputs=[
        gr.Textbox(label="Category"),
        gr.Textbox(label="Urgency"),
        gr.Textbox(label="Language"),
    ],
    title="Multilingual Support Ticket Classifier",
    description="Paste a support ticket in any language. Get its category, urgency, and detected language back instantly.",
    examples=[
        [
            "Wesentlicher Sicherheitsvorfall",
            "Sehr geehrtes Support-Team, ich möchte einen gravierenden Sicherheitsvorfall melden, der gegenwärtig mehrere Komponenten unserer Infrastruktur betrifft.",
        ],
        [
            "Refund request",
            "Hi, I was charged twice for my subscription this month. Can I get a refund for the duplicate charge?",
        ],
        [
            "Incidente de seguridad grave",
            "Estimado equipo de soporte, deseo reportar un incidente de seguridad grave.",
        ],
    ],
)
response.launch()
