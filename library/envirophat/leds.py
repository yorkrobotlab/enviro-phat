from sys import exit

try:
    import board
    import busio
    from adafruit_mcp230xx.mcp23017 import MCP23017
except ImportError:
    exit("This library requires the adafruit_mcp230xx module\nInstall with: sudo pip install adafruit-circuitpython-mcp230xx")

# Set up MCP23017
i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c, address=0x21)
leds_pin = mcp.get_pin(3)
leds_pin.switch_to_output()
leds_pin.value = False

class leds:
    def __init__(self, status=0):
        self.status = status

    def on(self):
        """Turn LEDs on."""
        self.status = 1
        leds_pin.value = True
        return True

    def off(self):
        """Turn LEDs off."""
        self.status = 0
        leds_pin.value = False

    def is_on(self):
        """Return True if LED is on."""
        if self.status == 1:
            return True
        else:
            return False

    def is_off(self):
        """Return True if LED is off."""
        if self.status == 0:
            return True
        else:
            return False
