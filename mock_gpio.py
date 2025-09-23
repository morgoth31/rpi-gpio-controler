class GPIO:
    BCM = 1
    OUT = 1
    IN = 1
    LOW = 0
    HIGH = 1

    _pins = {}

    @staticmethod
    def setmode(mode):
        print(f"GPIO.setmode({mode})")

    @staticmethod
    def setwarnings(value):
        print(f"GPIO.setwarnings({value})")

    @staticmethod
    def setup(pin, mode):
        print(f"GPIO.setup({pin}, {mode})")
        GPIO._pins[pin] = GPIO.LOW

    @staticmethod
    def output(pin, value):
        print(f"GPIO.output({pin}, {value})")
        GPIO._pins[pin] = value

    @staticmethod
    def input(pin):
        return GPIO._pins.get(pin, GPIO.LOW)

    @staticmethod
    def cleanup():
        print("GPIO.cleanup()")
        GPIO._pins = {}
