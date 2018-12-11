# Add your Python code here. E.g.
from microbit import *
import random

computer_choice = random.randint(0,4)
rock = Image ("00000:"
              "09990:"
              "09990:"
              "09990:"
              "00000:")

paper = Image("99999:"
              "90009:"
              "90009:"
              "90009:"
              "99999:")

scissors = Image("90099:"
                "09099:"
                "00900:"
                "09099:"
                "90099:")

lizard = Image("90000:"
               "90000:"
               "90000:"
               "90000:"
               "99999:")

spock = Image("99999:"
              "90000:"
              "99999:"
              "00009:"
              "99999:")

human_choice = [rock, paper, scissors, lizard, spock]


while True:
    if accelerometer.was_gesture("shake"):
        sleep(100)
        display.show(random.choice(human_choice))
        