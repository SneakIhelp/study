import os 
import time


timing = time.time()

while True:
    os.system("uranewprojectbecimsad.py")
    if time.time() - timing > 10.0:
        timing = time.time()
        os.abort('uranewprojectbecimsad.py')