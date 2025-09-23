from flask import Flask, render_template, request, redirect, url_for
import RPi.GPIO as GPIO

# --- CONFIGURATION ---
# Numéros BCM des GPIO contrôlés
PINS = [17, 27, 22]

# Initialisation GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for pin in PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# --- FLASK APP ---
app = Flask(__name__)

def get_pin_states():
    """Retourne l’état (0/1) de chaque GPIO."""
    return {pin: GPIO.input(pin) for pin in PINS}

@app.route("/")
def index():
    states = get_pin_states()
    return render_template("index.html", pins=states)

@app.route("/toggle/<int:pin>")
def toggle(pin):
    if pin in PINS:
        current = GPIO.input(pin)
        GPIO.output(pin, not current)  # Inverse l’état
    return redirect(url_for("index"))

@app.route("/set/<int:pin>/<int:state>")
def set_pin(pin, state):
    if pin in PINS and state in [0, 1]:
        GPIO.output(pin, state)
    return redirect(url_for("index"))

@app.route("/cleanup")
def cleanup():
    GPIO.cleanup()
    return "GPIO nettoyés"

app.add_url_rule(
    "/favicon.ico",
    endpoint="favicon",
    redirect_to=url_for("img", filename="favicon.ico"),
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
