from pyfiglet import Figlet

def banner(font):
    f = Figlet(font=font)
    print(f.renderText("Hoodpharm's Bet Tracker"))

