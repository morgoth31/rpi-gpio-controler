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

---

## 7. GPIO Pinout (Raspberry Pi 40-pin header)

The web interface provides a list of controllable GPIOs. Below is a complete map of the 40-pin header for reference (using BCM numbering).

| Pin # | Name          | Function      | Pin # | Name              | Function      |
|-------|---------------|---------------|-------|-------------------|---------------|
| 1     | 3.3V          | Power         | 2     | 5V                | Power         |
| 3     | GPIO 2 (SDA)  | I2C           | 4     | 5V                | Power         |
| 5     | GPIO 3 (SCL)  | I2C           | 6     | GND               | Ground        |
| 7     | GPIO 4        | GPIO          | 8     | GPIO 14 (TXD)     | UART          |
| 9     | GND           | Ground        | 10    | GPIO 15 (RXD)     | UART          |
| 11    | GPIO 17       | GPIO          | 12    | GPIO 18           | GPIO          |
| 13    | GPIO 27       | GPIO          | 14    | GND               | Ground        |
| 15    | GPIO 22       | GPIO          | 16    | GPIO 23           | GPIO          |
| 17    | 3.3V          | Power         | 18    | GPIO 24           | GPIO          |
| 19    | GPIO 10(MOSI) | SPI           | 20    | GND               | Ground        |
| 21    | GPIO 9 (MISO) | SPI           | 22    | GPIO 25           | GPIO          |
| 23    | GPIO 11(SCLK) | SPI           | 24    | GPIO 8 (CE0)      | SPI           |
| 25    | GND           | Ground        | 26    | GPIO 7 (CE1)      | SPI           |
| 27    | ID_SD         | EEPROM        | 28    | ID_SC             | EEPROM        |
| 29    | GPIO 5        | GPIO          | 30    | GND               | Ground        |
| 31    | GPIO 6        | GPIO          | 32    | GPIO 12           | GPIO          |
| 33    | GPIO 13       | GPIO          | 34    | GND               | Ground        |
| 35    | GPIO 19       | GPIO          | 36    | GPIO 16           | GPIO          |
| 37    | GPIO 26       | GPIO          | 38    | GPIO 20           | GPIO          |
| 39    | GND           | Ground        | 40    | GPIO 21           | GPIO          |
