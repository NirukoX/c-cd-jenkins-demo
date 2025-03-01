from flask import Flask
import signal
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return "Please"

def handle_shutdown(signal, frame):
    print("Shutting down.")
    sys.exit(0)

# Handle SIGINT (Ctrl+C) and SIGTERM (for Jenkins/Docker)
signal.signal(signal.SIGINT, handle_shutdown)
signal.signal(signal.SIGTERM, handle_shutdown)

if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=5000, debug=False)
