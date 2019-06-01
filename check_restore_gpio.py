import os
from gpiozero import Button

button = Button(21)

if button.is_pressed:
    print("Restore button is pressed")
    os.system("/boot/boot_to_recovery restore")
else:
    print("Restore button is not pressed")
