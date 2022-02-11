from flask import Flask, render_template

# create the Flask app
app = Flask(__name__)

import main_app

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
    app.run(host="0.0.0.0", port=5000)
