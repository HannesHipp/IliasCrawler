import sys


def drawProgressBar(percent, file_name ,barLen = 50):
    # percent float from 0 to 100.
    sys.stdout.write("\r")
    sys.stdout.write("|{:<{}}| {:.0f}%".format("░" * int(barLen * percent * 0.01), barLen, percent) + "  " + file_name)
    sys.stdout.flush()

def write_with_carrige_return(promt):
    sys.stdout.write("\r")
    sys.stdout.write(promt)
    sys.stdout.flush()