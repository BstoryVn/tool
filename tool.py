from pyfiglet import figlet_format 
import time
import turtle
import colorsys
import time
import sys
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep
from tqdm import tqdm
from colorama import init
from colorama import Fore, Back, Style

print( figlet_format("BstoryIOS", font = "big" ) )
name = input("Username : ")

for _ in tqdm(range(100)):
    desc = "loading...",
    ncols=75
    time.sleep(0.01)
print(Fore.BLUE + 'Done Checking...')
print(Style.RESET_ALL)
time.sleep(0.5)
print("Wellcome To Tool , " + name )

login = input("Enter Your Password : ")
for _ in tqdm(range(100)):
    desc = "loading...",
    ncols=75
    time.sleep(0.02)
print(Fore.RED + 'Successfully logged in as admin')
print(Style.RESET_ALL)
print(Fore.YELLOW + '')
class Loader:
    def __init__(self, desc="Loading...", end="Panel By BstoryIOS", timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


if __name__ == "__main__":
    with Loader("Loading Data File..."):
        for i in range(10):
            sleep(0.25)

    loader = Loader("Loading with object...", "Active Successful", 0.05).start()
    for i in range(10):
        sleep(0.25)
    loader.stop()

print(Fore.CYAN + '')
print("Driver Getting (1/100)              Loading Hwid")
time.sleep(0.5)
print("Driver Getting (2/100)              Loading Hwid")
time.sleep(0.5)
print("Driver Getting (3/100)              Loading Hwid")
time.sleep(0.5)
print("Driver Getting (4/100)              Loading Hwid")
time.sleep(0.5)
print("Driver Getting (5/100)              Loading Hwid")
time.sleep(0.5)
print("Driver Getting (7/100)              Loading Hwid")
time.sleep(0.5)
print("Driver Getting (8/100)              Loading Hwid")
time.sleep(0.5)
print("Driver Getting (9/100)              Loading Hwid")
time.sleep(0.5)
print("Driver Getting (10/100)             Loading Hwid")
time.sleep(0.5)
print("Driver Getting (11/100)             Loading Hwid")
time.sleep(0.5)
print("Driver Getting (13/100)             Loading Hwid")
time.sleep(0.5)
print("Driver Getting (19/100)             Loading Hwid")
time.sleep(0.5)
print("Driver Getting (20/100)             Loading Hwid")
time.sleep(0.5)
print("Driver Getting (24/100)             Loading Hwid")
time.sleep(0.5)
print("Driver Getting (27/100)             Loading Hwid")
time.sleep(0.5)
print("Driver Getting (29/100)             Loading Hwid")
time.sleep(0.5)
print("Driver Getting (30/100)             Loading Hwid")
time.sleep(0.5)
print("Driver Getting (37/100)             Loading Hwid")
time.sleep(0.5)
print("Driver Getting (44/100)             Loading Hwid")
time.sleep(0.5)
print("Driver Getting (45/100)             Loading Hwid")
time.sleep(0.5)
print("Driver Getting (48/100)             Loading Hwid")
time.sleep(0.5)
print("Driver Getting (49/100)             Loading Hwid")
time.sleep(0.5)
print("Driver Getting (60/100)             Loading Hwid")
time.sleep(1)
print("Driver Getting (78/100)             Loading Hwid")
time.sleep(2)
print("Driver Getting (100/100)            Well Done")
time.sleep(3.5)
  
print( figlet_format("Wait Seconds", font = "univers" ) )
time.sleep(7)

print( figlet_format("Bypass Done !", font = "cybermedium" ) )