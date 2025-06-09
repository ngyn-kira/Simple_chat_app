import gradio as gr
import requests

API_URL = "http://127.0.0.1:5000/chat"  # Replace with your real API endpoint


def chat_function(message, history):
    try:
        response = requests.post(API_URL, json={
            "messages": message,
        })
        reply = response.json().get("message", "Error: No reply")
    except Exception as e:
        reply = f"Error: {e}"

    history.append((message, reply))
    return history, history


with gr.Blocks() as demo:
    gr.Markdown("Chat with AI")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Type your message")
    clear = gr.Button("Clear")
    state = gr.State([])
    msg.submit(chat_function, [msg, state], [chatbot, state])
    clear.click(lambda: ([], []), None, [chatbot, state])

demo.launch(share=False)
