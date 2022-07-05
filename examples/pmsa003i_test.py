import time
from pms5003 import PMS5003

print("""pmsa003i_test.py - I2C Version - Continously print all data values.
""")


# Enable enviro power supply!
boost_enable = machine.Pin(11, machine.Pin.OUT)
boost_enable.value(True)
time.sleep(2.0)

# Configure the PMS5003 for Enviro+
pmsa003i = PMS5003(
    uart=machine.I2C(0, sda=machine.Pin(4), scl=machine.Pin(5), freq=100000),
    pin_enable=machine.Pin(10),
    pin_reset=machine.Pin(9),
    mode="active"
)

while True:
    data = pmsa003i.read()
    print(data)
    time.sleep(1.0)
