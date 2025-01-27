# Flask
# python3.11 -m pip install flask
# python3.11 -m pip install flask_cors

from flask import Flask, request, render_template
from flask_cors import CORS
import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load model (download on first run and reference local installation for consequent runs)
model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
conversation_history = []

#Create an instance of the Flask class and assign it to the variable app
app = Flask(__name__)
CORS(app)    #mitigate CORS errors - a type of error related to making requests to domains other than the one that hosts this webpage.

#Define a route for the homepage by decorating the home() function with the @app.route() decorator
# @app.route('/')
# def home():
#     return 'Hello, World'

# @app.route('/trains')
# def trains():
#     return 'This page has trains'

# @app.route('/cars')
# def cars():
#     return 'This page has cars'

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    data = request.get_data(as_text=True)
    data = json.loads(data)
    print(data)    #DEBUG
    input_text = data['prompt']
    
    # Create conversation history string
    history = "\n".join(conversation_history)
    
    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history, input_text, return_tensors="pt")
    
    # Generate the response from the model
    outputs = model.generate(**inputs, max_length= 60)  # max_length will cause the model to crash at some point as history grows
    
    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    
    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)
    
    return response

#Ensures that the server is only run if the script is executed directly
if __name__ == '__main__':
    app.run()