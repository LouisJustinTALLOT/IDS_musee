from flask import Flask, render_template
from flask_socketio import SocketIO

# create the Flask app
app = Flask(__name__)
socket = SocketIO(app)

import main_app
main_app.socket = socket

@app.route('/')
def index():
    print("Serving index....")
    return render_template("accueil_videos.html")

@app.route("/relaunch_script")
def relaunch_script():
    print("Relaunching listening ...")
    main_app.relaunch_script()
    return {"status": "done"}

if __name__=="__main__":
    print("Starting app...")
    socket.run(app, host="0.0.0.0", port=5000)
