from flask import Flask, request, jsonify, render_template
from utils.greetings import handle_greeting
from utils.help import handle_help

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Simple user interface

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.get_json()
    user_input = data.get("query", "").lower()

    # Process query
    if "hello" in user_input:
        response = handle_greeting()
    elif "help" in user_input:
        response = handle_help()
    else:
        response = "Sorry, I didn't understand that."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
