import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "App is currently running!"

if __name__ == '__main__':
    from threading import Timer
    Timer(10, exit).start()  # Exit after 60 seconds
    app.run(host="0.0.0.0", port=5000)
