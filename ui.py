import gradio as gr
import requests


def analyze_interface(url):
    try:
        response = requests.post("http://127.0.0.1:8000/api/v1/analyze/url", json={"url": url})
        data = response.json()
        return data["classification"], "\n".join(data["reasons"])
    except:
        return "ERROR", "Backend is offline. Ensure api.py is running on port 8000."


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# CyberShield AI")
    gr.Markdown("### Autonomous Forensic Threat Intelligence Core")

    input_text = gr.Textbox(label="Target Endpoint", placeholder="https://example.com")
    btn = gr.Button("ENGAGE ENGINE", variant="primary")

    output_class = gr.Textbox(label="Classification")
    output_reasons = gr.Textbox(label="Extracted Evidence Vectors")

    btn.click(analyze_interface, inputs=input_text, outputs=[output_class, output_reasons])

if __name__ == "__main__":
    demo.launch()