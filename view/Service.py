import sys


def drawProgressBar(percent, file_name ,barLen = 50):
    # percent float from 0 to 100.
    sys.stdout.write("\r")
    sys.stdout.write("|{:<{}}| {:.0f}%".format("░" * int(barLen * percent * 0.01), barLen, percent) + "  " + file_name)
    sys.stdout.flush()

def yes_no_promt():
    print("Gib 'y' für Yes und 'n' für No ein.")

def user_chooses_yes(promt):
    while True:
        result = input(promt)
        if result == "y":
            return True
        elif result == "n":
            return False
        else:
            print("Falsche Antwort. Probieren wir es noch einmal...")

def write_with_carrige_return(promt):
    sys.stdout.write("\r")
    sys.stdout.write(promt)
    sys.stdout.flush()