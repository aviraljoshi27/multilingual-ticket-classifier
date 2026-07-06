from datasets import load_dataset
from classifier import classify_ticket

ds = load_dataset("Tobi-Bueck/customer-support-tickets", split="train")
for row in ds.select(range(3)):
    print(classify_ticket(row["subject"], row["body"]))
    print(f"Priority: {row['priority']}")
    print(f"Queue: {row['queue']}")

subject = "Incident de sécurité majeur"
body = "Madame, Monsieur, je souhaite signaler un incident de sécurité grave."
print(classify_ticket(subject, body))

subject = "Incidente de seguridad grave"
body = "Estimado equipo de soporte, deseo reportar un incidente de seguridad grave."
print(classify_ticket(subject, body))
