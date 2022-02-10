from flask import Flask, render_template, url_for
from flask_socketio import SocketIO

# create the Flask app
app = Flask(__name__)
socketio = SocketIO(app)


import main_app

main_app.socketio = socketio


@app.route('/')
def index():
    print("Serving index....")
    return render_template("accueil_videos.html")

if __name__=="__main__":
    print("Starting app...")
    socketio.run(app, host="0.0.0.0", port=5001)
