import os
import sys
import traceback
import time
from code2.tts import speak

def kill_processes():
    os.system("kill")


def game():
    try:
        print("Loading loop4.py - july 2023.")
        print("Coming back after a little while")
        time.sleep(1)
        print("To my mom and dad.")
        # speak
        speak("Let's start","en")
        time.sleep(5)
        from code2.loop7 import run
        run()
    except Exception:
        print(traceback.format_exc())
        print(sys.exc_info()[2])
        kill_processes()


game()