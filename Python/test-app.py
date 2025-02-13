import gradio as gr

def greet(name, intensity):
  return "Hello, " + name + "!" * int(intensity)

''' 
Interface object, created for demos and testing (has three class elements)

fn: The function to wrap a user interface (UI) around.
The fn argument is flexible — you can pass any Python function you want to wrap with a UI

inputs: he Gradio component(s) to use for the input. 
The number of components should match the number of arguments in your function.

outputs: The Gradio component(s) to use for the output. 
The number of components should match the number of return values from your function.
'''
demo = gr.Interface(    
  fn=greet,
  inputs=["text", "slider"],
  outputs=["text"],
)
demo.launch()