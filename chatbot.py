from flask import Flask, render_template, request
import openai
import os

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API key (ensure your environment variable is set correctly)
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # You can replace this with another model if needed
            prompt=user_input,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    # Get the port from environment variables (for Render deployment)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
