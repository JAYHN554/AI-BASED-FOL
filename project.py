import tkinter as tk
from tkinter import scrolledtext

# Knowledge base simulating FOL rules
knowledge_base = {
    "flu": {
        "symptoms": ["fever", "cough", "headache", "tiredness"],
        "advice": "You may have the flu. Stay hydrated, rest, and consult a doctor if symptoms persist."
    },
    "common cold": {
        "symptoms": ["sneezing", "runny nose", "cough", "sore throat"],
        "advice": "It seems like a common cold. Get rest and drink warm fluids."
    },
    "indigestion": {
        "symptoms": ["stomach pain", "nausea", "bloating", "heartburn"],
        "advice": "Sounds like indigestion. Avoid heavy meals and drink water. If it continues, see a doctor."
    },
    "stress": {
        "symptoms": ["tiredness", "headache", "sleep problems", "irritability"],
        "advice": "You might be stressed. Take breaks, sleep well, and consider relaxation exercises."
    },
    "migraine": {
        "symptoms": ["headache", "nausea", "light sensitivity", "throbbing pain"],
        "advice": "This could be a migraine. Rest in a dark room and avoid triggers."
    }
}

def infer_conditions(user_symptoms):
    matched_conditions = []

    for condition, data in knowledge_base.items():
        match_count = sum(symptom in user_symptoms for symptom in data["symptoms"])
        if match_count > 0:
            matched_conditions.append((condition, match_count, data["advice"]))

    matched_conditions.sort(key=lambda x: x[1], reverse=True)
    return matched_conditions

def handle_input():
    user_input = entry.get().strip().lower()
    if not user_input:
        return

    chat_area.config(state='normal')
    chat_area.insert(tk.END, "You: " + user_input + "\n")

    if user_input == "exit":
        chat_area.insert(tk.END, "Bot: Take care! 🩺\n")
        root.quit()
        return

    user_symptoms = [s.strip() for s in user_input.split(",")]
    results = infer_conditions(user_symptoms)

    if not results:
        chat_area.insert(tk.END, "Bot: I couldn't identify a condition. Please consult a doctor.\n")
    else:
        for condition, score, advice in results[:2]:
            chat_area.insert(tk.END, f"Bot: {advice} (matched {score} symptom{'s' if score > 1 else ''})\n")

    chat_area.insert(tk.END, "\n")
    chat_area.config(state='disabled')
    entry.delete(0, tk.END)

# Tkinter GUI setup
root = tk.Tk()
root.title("FOL-Based Medical Chatbot")
root.geometry("600x400")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Arial", 11))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry_frame = tk.Frame(root)
entry_frame.pack(fill=tk.X, padx=10, pady=5)

entry = tk.Entry(entry_frame, font=("Arial", 12))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

submit_button = tk.Button(entry_frame, text="Submit", command=handle_input)
submit_button.pack(side=tk.RIGHT)

# Initial message
chat_area.config(state='normal')
chat_area.insert(tk.END, "👩‍⚕️ Welcome to the Medical Chatbot!\nEnter symptoms separated by commas (e.g. fever, cough)\nType 'exit' to quit.\n\n")
chat_area.config(state='disabled')

root.mainloop()
