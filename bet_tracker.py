import csv
import sys
import os
import pandas as pd
from parse import parse_args
from os import system, name as op_sys
from datetime import date
from banner import banner
from colorama import Fore, Style
from time import sleep


class Tracker:
    def __init__(self):
        self.filename = parse_args()["filename"]
        self.balance = 0
        self.date = date.today()
        # self.file = "bet_tracker.csv"
        self.df = pd.read_csv(self.filename) if os.path.exists(self.filename) else None

    def write_csv(self, profit):
        inputs = parse_args()
        file_exists = os.path.exists(self.filename)
        header = ["Date", "Bet", "Odds", "Wager", "W/L", "Profit"]
        data = [self.date, inputs["bet"], inputs["odds"], inputs["wager"],inputs["outcome"].upper(), profit]
        if not file_exists:
            print(f"{Fore.YELLOW}Creating file {self.filename}{Style.RESET_ALL}")
            sleep(1)
            with open(self.filename, "w", encoding="UTF-8") as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerow(data)
            
            print('[+]', end='')
            print(*data, sep=", ")
            print(f"{Fore.GREEN}File was created and data Saved to: {f.name}{Style.RESET_ALL}")
        else:
            with open(self.filename, "a", encoding="UTF-8") as f:
                writer = csv.writer(f)
                writer.writerow(data)
            print('[+]', end='')
            print(*data, sep=", ")
            print(f"{Fore.GREEN}Data Saved to: {f.name}{Style.RESET_ALL}")

    def read_file(self):
        print(self.df)

    def max_win(self):
        print(self.df.loc[self.df["Profit"].idxmax()])

    def total_bets(self):
        first_bet_logged = self.df.Date[0]
        print(f"You've made {len(self.df)} bets since {first_bet_logged}.")

    def calculate_profits(self):
        profit = self.df.Profit
        if profit.sum() > 0:
            print(f"Your total winnings as of, {self.df.Date[0]}: {Fore.GREEN}${round(profit.sum(), 2)}{Style.RESET_ALL}")
        else:
            print(f"Since {self.df.Date[0]}, you are down: {Fore.RED}-${-round(profit.sum(), 2)}{Style.RESET_ALL}")

    def main(self):
        inputs = parse_args()
        if inputs["max_win"]:
            self.max_win()
        if inputs["total_bets"]:
            self.total_bets()
        if inputs["read_file"]:
            self.read_file()
        if inputs["profits"]:
            self.calculate_profits()
        if inputs["outcome"]:
            if inputs["outcome"].upper() == "W":
                if inputs["odds"] < 0:
                    profit = 100/-(inputs["odds"]) * float(inputs["wager"])
                    self.write_csv(f"+{round(profit, 2)}")
                else:
                    profit = inputs["odds"]/100 * float(inputs["wager"])
                    self.write_csv(round(profit, 2))
            elif inputs["outcome"].upper() == "L":
                losses = self.balance - (-inputs["wager"])
                self.write_csv(f"-{losses}")
            else:
                print("-O flag must contain 'w' or 'l'.")
        

if __name__ == "__main__":
    t = Tracker()
    if op_sys != "nt":
        system("clear")
        banner()
    else:
        system("cls")
        
    if len(sys.argv) == 2:
        sys.exit("No arguments were given. type -h for help.")
    else:
        t.main()
