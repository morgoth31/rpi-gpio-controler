# Raspberry Pi GPIO Web Controller

This project provides a **Flask web server** that lets you control the **GPIO pins** of a Raspberry Pi from a web interface.

---

## 1. Requirements



---

## 2. Clone the project

```bash
git clone https://github.com/morgoth31/rpi-gpio-controler
cd rpi-gpio-controler
```





## 3. Create and use a virtual environment (venv)

It is recommended to work inside a virtual environment so that dependencies remain isolated.
### 3.1 Create the virtual environment

```bash
python3 -m venv venv
```

### 3.2 Activate the virtual environment

```bash
source venv/bin/activate
```

You should now see (venv) before your terminal prompt.
### 3.3 Deactivate the virtual environment (when done)

```bash
deactivate
```

## 4. Install dependencies

After activating the venv, install the required packages:

```bash
pip install -r requirements.txt
```

## 5. Run the Flask server

python app.py

By default, the server runs on port 8080.
Open a browser on your Raspberry Pi or another device on the same network and visit:

http://192.168.1.24:8080



## 6. Project Structure

gpio_web/
│
├── app.py             # Flask app
├── requirements.txt   # Python dependencies
├── README.md          # Documentation
├── templates/         # HTML pages (Jinja2 templates)
│   └── index.html
└── static/            # Static files (CSS/JS)
    └── style.css

