import os
import sys
import traceback
import time


def kill_processes():
    os.system("kill")


def game():
    try:
        print("Loading loop4.py - july 2023.")
        print("Coming back after a little while")
        time.sleep(1)
        print("I dedicate this project to my beloved mom and dad.")
        time.sleep(1)
        from code2.loop6 import run
        run()
    except Exception:
        print(traceback.format_exc())
        print(sys.exc_info()[2])
        kill_processes()


game()