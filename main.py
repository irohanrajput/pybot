from flask import Flask, render_template, request
import openai
import json

with open('/path/to/apikey.json') as f:
    api_key = json.load(f)['api_key']
#create a file called 'apikey.json' in your root direvtory and add your api key in it
#Sample: {"key": "YOUR_API_KEY_HERE"}
#sayonarraaaa

openai.api_key = api_key

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_prompt = request.form["user_input"]
    prompt_to_be_sent = f"You: {user_prompt}\nAssistant: "
    
    
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
            prompt=prompt_to_be_sent,
            max_tokens=100,
            temperature=0
            )
    
    assistant_response = response.choices[0].text.strip()

    return render_template("index.html", user_prompt=user_prompt, response_text=assistant_response)

if __name__ == "__main__":
    app.run(debug=True)
