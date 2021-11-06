import sys


def drawProgressBar(percent, barLen = 50):
    # percent float from 0 to 100.
    sys.stdout.write("\r")
    sys.stdout.write("[{:<{}}] {:.0f}%".format("%" * int(barLen * percent * 0.01), barLen, percent))
    sys.stdout.flush()