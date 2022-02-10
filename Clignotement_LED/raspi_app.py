from flask import Flask

from gpiozero import LED

led = LED(17)

# create the Flask app
app = Flask(__name__)


@app.route('/blink_led')
def blink_led():
    """Blink a LED when a video is launched"""
    led.blink(n=3, on_time=0.5, off_time=0.5)
    return {"status": "done"}

if __name__=="__main__":
    print("Starting app...")
    app.run(host="0.0.0.0", port=5003)
