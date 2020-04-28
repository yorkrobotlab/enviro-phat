# Enviro pHAT

https://shop.pimoroni.com/products/enviro-phat

The Pimoroni Enviro pHAT boast a plethora of sensors and connectivity for measuring your environment.

Modified to work on the [Pi-puck robot platform](https://github.com/yorkrobotlab/pi-puck), using the [YRL Expansion Board](https://github.com/yorkrobotlab/pi-puck-expansion-board).

Enviro pHAT includes:

* An LSM303D accelerometer/magnetometer for detecting orientation, motion and heading
* A BMP280 temperature/pressure sensor
* A TCS3472 colour sensor, for detecting the amount and colour of light
* An ADS1015 analog sensor with four 3.3v tolerant channels for your external sensors
* A 5v power supply pin for powering your sensors, which you can regulate or divide to 3v if needed
* Two LEDs connected to GPIO #4 for illuminating objects over the colour sensor

### Note: for Enviro and Enviro Plus see: https://github.com/pimoroni/enviroplus-python/

## Installing

Clone this repository, `cd` to the library directory, and run:

```bash
sudo python3 setup.py install
```
(or `sudo python setup.py install` whichever your primary Python environment may be)

In all cases you will have to enable the i2c bus.

## Documentation & Support

* Guides and tutorials - https://learn.pimoroni.com/enviro-phat
* Function reference - http://docs.pimoroni.com/envirophat/
* GPIO Pinout - https://pinout.xyz/pinout/enviro_phat
* Get help - http://forums.pimoroni.com/c/support
