from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and its associated view function
@app.route("/")
def hello_world():
    return "PUSHPAK 2.0"

# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

