import odroid_wiringpi as wiringpi
import dht11
import time
import datetime

# initialize GPIO
wiringpi.wiringPiSetup()

# read data using pin 4
instance = dht11.DHT11(pin = 4)

try:
  while True:
    result = instance.read()
    if result.is_valid():
      print("Last valid input: " + str(datetime.datetime.now()))

      print("Temperature: %-3.1f C" % result.temperature)
      print("Humidity: %-3.1f %%" % result.humidity)

    time.sleep(6)

except KeyboardInterrupt:
  # WiringPi doesn't need cleanup
  print("KeyboardInterrupt")
