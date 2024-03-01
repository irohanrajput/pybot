from flask import Flask, render_template, request
import openai
import json

with open('apikey.json') as f:
    api_key = json.load(f)['key']
    
#create a file 'apikey.json' in the root dir and add  api key in it
#Sample: {"key": "YOUR_API_KEY_HERE"}
#sayonarraaaa

openai.api_key = api_key

app = Flask(__name__)

chat_history = []

@app.route("/")
def home():
    return render_template("index.html", chat_history=chat_history)

@app.route("/get_response", methods=["POST"])
def get_response():
    
    user_prompt = request.form["user_input"]
    prompt_to_be_sent = f"You: {user_prompt}\nAssistant: "
    
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
            prompt=prompt_to_be_sent,
            max_tokens=100,
            temperature=0.7
            )
    assistant_response = response.choices[0].text.strip()
    
    chat_history.append({"user_text":user_prompt, "response_text": assistant_response})
    chat_history.reverse()  # Reverse the order of elements in chat_history
    
    

    return render_template("index.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
