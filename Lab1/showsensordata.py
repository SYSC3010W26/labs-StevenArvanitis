from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    temp = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()

    message = f"T:{temp:.1f}C P:{pressure:.1f}hPa H:{humidity:.1f}%"

    sense.show_message(message, scroll_speed=0.07)
    sleep(2)
