from flask import Flask, render_template, request

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the homepage
@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        # Get user input from the form
        user_input = request.form["user_input"]

        # For now, just return a simple response
        bot_response = f"You said: {user_input}"

        # Render the HTML template with user input and bot response
        return render_template("index.html", result=bot_response)

    # Render the HTML template for GET requests (initial page load)
    return render_template("index.html")

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
