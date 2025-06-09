
import requests

from flask import request, Flask


app = Flask(__name__)

LLM_GENERATE_URL = "http://localhost:11434/api/generate"
@app.route("/")
def welcome():
    return {'message': "Kira"}

@app.route("/chat", methods = ['POST'])
def chat():
    data = request.get_json()
    message = data.get("messages")

    # communitcate with URL
    responses = requests.post(
        LLM_GENERATE_URL,
        json = {
            "model" : "gemma3:1b",
            "prompt" : message,
            "stream" : False
        }
    )
    output = responses.json().get("response", "").strip()
    #

    return {
        "message" : output
    }
if __name__=='__main__':
    app.run(port = 5000, debug = False)
