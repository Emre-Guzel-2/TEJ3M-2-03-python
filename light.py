# Emre Guzel
# Feb 24 2026
# Turns on the light

#setting the moudules 
import board
import digitalio
import time

# Set up the pin
pin5 = digitalio.DigitalInOut(board.GP5)
pin5.direction = digitalio.Direction.OUTPUT

# Making the light run in a loop waiting 3 seconds 
while True:
    pin5.value = True   
    time.sleep(3)       
    
    pin5.value = False  
    time.sleep(3) 
          