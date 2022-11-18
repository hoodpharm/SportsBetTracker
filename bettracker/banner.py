from pyfiglet import Figlet
from time import sleep
from colorama import Fore, Style

def banner(font):
    f = Figlet(font=font)
    print(f'{Fore.MAGENTA}{f.renderText("Sports Bet Tracker")}')
    print(f'code written by @_beatmypockets{Style.RESET_ALL}')

def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledlen =  int(length * iteration // total)
    bar = fill * filledlen + '-' * (length - filledlen)
    print(f'\r{Fore.YELLOW}{prefix}|{bar}|{percent}% {suffix}', end='\r')
    if iteration == length:
        print(f'\r{Fore.GREEN}{prefix} |{bar}|{percent}% {suffix}{Style.RESET_ALL}', end='\r')
        print()
