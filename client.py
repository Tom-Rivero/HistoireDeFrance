import requests

URL = "http://localhost:8000/chat"

history = []

print("--- Quiz Histoire de France (Via API) ---")
print("Tape 'quit' pour arrêter.\n")

# First message to start
user_input = "Commence le quiz."

while True:
    history.append({"role": "user", "content": user_input})
    response = requests.post(URL, json={"messages": history})

    if response.status_code == 200:
        assistant_text = response.json()["response"]
        print(f"\n🤖: {assistant_text}")

        history.append({"role": "assistant", "content": assistant_text})
    else:
        print("Erreur API:", response.text)
        break

    # Wait for user input
    user_input = input("\n👤: ")
    if user_input.lower() in ["quit", "exit"]:
        break
