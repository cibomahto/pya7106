# pya7106: Python library for the A7106 radio module

This library is designed to interface an [Amicom A7106](http://www.amiccom.com.tw/asp/product_detail.asp?CATG_ID=2&PRODUCT_ID=109) 2.4G FSK/GFSK Transceiver with a Rasberry Pi. These are very cheap radios that we found in used E-Ink tags.

## Wiring

![Power and reset](images/power.jpg)

Connect the `RST` pin to `GND` so that the MSP430 stays in reset the whole time.
Connect a jumper to the `VCC` pin to supply 3.3V.

![Data and clock lines](images/wiring.jpg)

Solder jumpers to the six test pads.

![Pi wirings](images/pi.jpg)

Connect the radio to the Pi using the RX pins.
If you have two radios for transceiver testing, connect the second to the TX pins.

| Signal | Pi RX pin | Pi TX pin | Notes |
|--------|-----------|-----------|-------|
| `VCC`  |           |           | 3.3V on the Pi header
| `CS`   | `GPIO2`   | `GPIO10`  | Chip Select
| `CK`   | `GPIO3`   | `GPIO9`   | Clock
| `DA`   | `GPIO4`   | `GPIO11`  | Data from Pi to radio
| `GND`  |           |           | Any of the ground pins on the Pi header
| `IO1`  | `GPIO17`  | `GPIO5`   | Data from radio to Pi, after configuration
| `IO2`  | `GPIO27`  | `GPIO6`   | `WTR` signal from Radio to Pi, high when TX/RX are completed

## Running the RX server

```
./a7106.py --mode rx
```



## References

* Datasheet: https://datasheet.lcsc.com/szlcsc/2001071135_AMICCOM-Elec-A71X06AQFI-Q_C479510.pdf
* Companion library: https://github.com/osresearch/eink-pricetags
* Sample Arduino code: https://www.arduino.cn/thread-49468-1-1.html
* FIFO mode reference code: http://docsplayer.com/134201791-%E5%88%9D%E5%A7%8B%E5%8C%96a7121.html
