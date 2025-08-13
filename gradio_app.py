import gradio as gr
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import threading

# FastAPI app
app = FastAPI()

# Serve React build folder at /ui
app.mount("/ui", StaticFiles(directory="build", html=True), name="ui")

# Gradio app
with gr.Blocks() as demo:
    gr.HTML('<iframe src="/ui" width="100%" height="600px" style="border:none;"></iframe>')
    textbox = gr.Textbox(label="Enter text")
    button = gr.Button("Submit")
    button.click(lambda x: f"Hello, {x}!", inputs=textbox, outputs=textbox)

# Mount Gradio app on /gradio
app = gr.mount_gradio_app(app, demo, path="/gradio")

# Run FastAPI + Gradio
def run():
    uvicorn.run(app, host="0.0.0.0", port=7870)

thread = threading.Thread(target=run)
thread.start()
