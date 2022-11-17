import csv
import sys
import os
import pandas as pd
from files import Files
from parse import *
from os import system, name as op_sys
from datetime import date
from time import sleep
from banner import banner, loadbar
from colorama import Fore, Style


class Tracker(Files):
    def __init__(self):
        self.parser = Parser()
        self.inputs = self.parser.parse_args()
        self.date = date.today()
        self.filename = self.inputs["filename"]
        self.path = os.path.join("data_files", self.filename)
        self.df = pd.read_csv(self.path, parse_dates=["Date"]) if os.path.exists(self.path) else f"Cant Find {self.filename}"
        self.balance = 0
        self.files = []

    def write_csv(self, profit, total):
        file_exists = os.path.exists(self.path)
        header = ["Date", "Bet", "Odds", "Wager", "W/L", "Profit", "Total Payout"]
        data = [self.date, self.inputs["bet"], self.inputs["odds"], self.inputs["wager"],self.inputs["outcome"].upper(), round(float(profit), 2), round(float(total),2)]
        if not file_exists:
            print(f"{Fore.CYAN}Creating file {self.filename}")
            lst = list(range(0,25))
            l = len(lst)
            for i, _ in enumerate(lst):
                sleep(0.1)
                loadbar(i + 1, l, prefix="Progress", suffix="Complete", length=l)
                
            with open(self.path, "w", encoding="UTF-8", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerow(data)

            print(f"{Fore.CYAN}File was created and data Saved to: {f.name}")
            print('[+]', end='')
            print(*data, sep=', ')
            print(Style.RESET_ALL)
        else:
            with open(self.path, "a", encoding="UTF-8", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)
            
            print(Fore.CYAN,'[+]', end='')
            print(*data, sep=", ")
            print(f"{Fore.GREEN}{f' Data Saved to: {f.name} ':#^75}{Style.RESET_ALL}")

    def chdate(self):
        new_date = self.inputs["date"]
        self.date = new_date

    def max_win(self):
        print(Fore.CYAN, self.df.loc[self.df["Profit"].idxmax()].fillna(0))
    
    def max_loss(self):
        print(Fore.CYAN, self.df.loc[self.df["Profit"].idxmin()].fillna(0))

    def sort(self):
        self.df = self.df.sort_values(by="Date").reset_index(drop=True)

    def total_bets(self):
        self.sort()
        first_bet_logged = self.df.Date[0]
        print(Fore.CYAN, f"You've made {len(self.df)} bets since {first_bet_logged}.")

    def calculate_profits(self):
        self.sort()
        profit = self.df.Profit
        if profit.sum() > 0:
            print(Fore.CYAN, f"Your total winnings as of, {self.df.Date[0]}: {Fore.GREEN}${f'{round(profit.sum(), 2):,}'}{Style.RESET_ALL}")
        else:
            print(Fore.CYAN, f"Since {self.df.Date[0]}, you are down: {Fore.RED}-${f'{-round(profit.sum(), 2):,}'}{Style.RESET_ALL}")

    def main(self):
        if self.inputs["rm"]:
            self.del_files()
        if self.inputs["list"]:
            self.lst_files()
        if self.inputs["date"]:
            self.chdate()
        if self.inputs["max_win"]:
            self.max_win()
        if self.inputs["max_loss"]:
            self.max_loss()
        if self.inputs["total_bets"]:
            self.total_bets()
        if self.inputs["read_file"]:
            self.read_file()
        if self.inputs["profits"]:
            self.calculate_profits()
        if self.inputs["outcome"]:
            if self.inputs["outcome"].upper() == "W":
                if self.inputs["odds"] < 0:
                    profit = 100/-(self.inputs["odds"]) * float(self.inputs["wager"])
                    total = profit + self.inputs["wager"]
                    self.write_csv(f"+{round(profit, 2)}", round(total, 2))
                else:
                    profit = self.inputs["odds"]/100 * float(self.inputs["wager"])
                    total = profit + self.inputs["wager"]
                    self.write_csv(round(profit, 3), total)
            elif self.inputs["outcome"].upper() == "L":
                losses = self.balance - (-self.inputs["wager"])
                self.write_csv(f"-{losses}", 0)
            else:
                print('-O flag must contain "w" or "l".')            

if __name__ == "__main__":
    t = Tracker()
    if op_sys != "nt":
        system("clear")
        banner("banner3-D")
    else:
        system("cls")
        banner("banner3-D")
    
    if len(sys.argv) == 2:
        t.parser.parser.print_help()

    if len(sys.argv) <= 3:
        if not os.path.exists(t.path):
            sys.exit(f"Couldn't find {t.filename}")
        else:
            t.filename = t.path
            t.main()
    else:
        t.main()
        

        
