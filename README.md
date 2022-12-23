# DHT11 Python library (for ODROID WiringPi)

This simple class can be used for reading temperature and humidity values from DHT11 sensor on ODROID SBCs.

Based on [szazo/DHT11_Python](szazo/DHT11_Python), and referenced from [unims77/odroid_c1_dht11](https://github.com/unims77/odroid_c1_dht11).

Tested on ODROID N2+. Might work on other ODROID SBCs, but if there's any issue, please report it!


# Installation

To install, clone this repository and setup:

```
TO_BE_FILLED
```

# Usage

1. Instantiate the `DHT11` class with the pin number as constructor parameter.
2. Call `read()` method, which will return `DHT11Result` object with actual values and error code.

For example:

```python
### TO_BE_CHANGED

import RPi.GPIO as GPIO
import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin = 14)
result = instance.read()

if result.is_valid():
    print("Temperature: %-3.1f C" % result.temperature)
    print("Humidity: %-3.1f %%" % result.humidity)
else:
    print("Error: %d" % result.error_code)
```

For working example, see `dht11_example.py` (you probably need to adjust pin for your configuration)

# License

This project is licensed under the terms of the MIT license.
