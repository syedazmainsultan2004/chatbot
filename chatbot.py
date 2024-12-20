from flask import Flask, render_template, request
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

# Initialize the Flask app
app = Flask(__name__)

# Initialize Ollama model (e.g., Mistral or Llama) via Langchain
model = OllamaLLM(model="mistral")

# Template for conversational history
template = """
Here's the conversation so far: {history}

Now, the question: {question}

Answer:
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Initialize conversation history (to store the conversation)
conversation_history = ""

# Home route to handle user input and display responses
@app.route("/", methods=["GET", "POST"])
def chat():
    global conversation_history  # Track conversation history globally
    if request.method == "POST":
        user_input = request.form["user_input"]

        # Add the user's message to the conversation history
        conversation_history += f"\nUser: {user_input}"

        # Create a response using Ollama model with the conversation history
        result = chain.invoke({"history": conversation_history, "question": user_input})
        bot_response = result.strip()

        # Add the bot's response to the conversation history
        conversation_history += f"\nAI: {bot_response}"

        # Return the result and updated history to the HTML page
        return render_template("index.html", result=bot_response, history=conversation_history)
    
    return render_template("index.html", history=conversation_history)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
