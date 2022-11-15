from pyfiglet import Figlet
from time import sleep
from colorama import Fore, Style

def banner(font):
    f = Figlet(font=font)
    print(f.renderText("Hoodpharm's Bet Tracker"))

def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledlen =  int(length * iteration // total)
    bar = fill * filledlen + '-' * (length - filledlen)
    print(f'\r{Fore.YELLOW}{prefix}{Style.RESET_ALL} |{Fore.YELLOW}{bar}{Style.RESET_ALL} |{Fore.YELLOW}{percent}% {suffix}{Style.RESET_ALL}', end='\r')
    if iteration == total:
        print()
