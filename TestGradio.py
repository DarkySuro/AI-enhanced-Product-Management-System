import gradio as gd


def call(name):
    return f"Hello {name.upper()}! How are you?"

response = gd.Interface(
    fn=call, 
    inputs="text",
      outputs="text")
response.launch()