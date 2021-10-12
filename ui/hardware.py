import RPi.GPIO as GPIO

class Hardware:
    def __init__(self, onButtonDown, onButtonUp):
        self.onButtonDown = onButtonDown
        self.onButtonUp = onButtonUp
        GPIO.setmode(GPIO.BCM)
        buttons = [27, 18, 17]

        for button in buttons:
            GPIO.setup(button, GPIO.IN)
            GPIO.add_event_detect(button, GPIO.BOTH, callback=self.__buttonChange, bouncetime=500)

    def __buttonChange(self, channel):
        if GPIO.input(channel):
            self.onButtonDown(channel)
        else:
            self.onButtonUp(channel)

    def __del__(self):
        GPIO.cleanup()
