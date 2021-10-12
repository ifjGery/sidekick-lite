# Sidekick lite

This project is basically combining a Pi Zero W and a Pi Pico and is a proof of concecpt.

## Hardware

Wiring the components is straightforward. For Pi-Pico just follow the [PICO documentation](https://datasheets.raspberrypi.org/pico/getting-started-with-pico.pdf) and look for "SWD Port Wiring" + "Powering the board" sections. 

For the screen, use `spi0` and in the `ui/screen.py` you can see the gpio pins used. 

For the buttons, they are currently wired on gpio `27` `18` and `17` teach button is connected to a small `~100k` resistor that are collectively connected to `3v3` on the pi, in hindsight, they should have been connected to ground, but then you have to setup the pins in `ui/hardware.py` as `PULL_DOWN`.

Ir config is the following:
```
dtoverlay=gpio-ir,gpio_pin=26
dtoverlay=gpio-ir-tx,gpio_pin=13
```

# Software 

The idea for the software is to run commands and apps (not yet implemented) from a simple menu. In the `ui/config/menu.yml` you can define the commands, and there are hints for future features in there.

## python dependencies

- RPi (probably installed)
- PIL
- yaml
- ST7735 (for the screen)

![device](img/device.jpg)