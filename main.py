import os
import sys
import traceback
import time
from code2.tts import speak

def kill_processes():
    os.system("kill")


def game():
    try:
        print("Loading loop7.py - july 2023.")
        print("To my mom and dad.")

        from code2.loop7 import run
        run()
    except Exception:
        print(traceback.format_exc())
        print(sys.exc_info()[2])
        kill_processes()


game()