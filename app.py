from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are RescueAI, an intelligent disaster response assistant.

Help users during emergencies such as floods, earthquakes,
cyclones, fires, landslides, and other disasters.

Give clear, simple and practical safety guidance.

Always prioritize:
1. Immediate safety
2. Evacuation when necessary
3. First-aid guidance when appropriate
4. Emergency services
5. Asking for important information such as location when needed

If someone is in immediate danger, advise them to contact
their local emergency services and move to a safer place if possible.

Never claim that you have contacted emergency services,
rescued someone, or dispatched a rescue team.

Keep responses short and easy to understand.
"""

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Please enter a message"}), 400

    message = user_message.lower()

    if "flood" in message:
        reply = "Move to higher ground immediately. Do not walk or drive through floodwater. Stay away from electrical wires and contact emergency services if you are in danger."

    elif "earthquake" in message:
        reply = "Drop, cover, and hold on. Stay away from windows and heavy objects. When the shaking stops, move to a safe open area if possible."

    elif "fire" in message:
        reply = "Leave the building immediately using the safest exit. Do not use elevators. Stay low if there is smoke and contact emergency services."

    elif "cyclone" in message:
        reply = "Stay indoors and away from windows. Follow official evacuation instructions and keep emergency supplies, water, and communication devices ready."

    else:
        reply = "Please describe the disaster and your situation. RescueAI will provide safety guidance and help identify the safest next step."

    return jsonify({"reply": reply})


@app.route("/")
def home():
    return "RescueAI Backend is Running!"


if __name__ == "__main__":
    app.run(debug=True)