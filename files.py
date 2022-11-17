from colorama import Fore, Style
import pandas as pd
import os
import sys

class Files:    
    def read_file(self):        
        if self.inputs["v"]:
            pd.set_option("display.max_rows", None)
            self.sort()
            self.df.index += 1
            print(Fore.CYAN, self.df.fillna(0))
        else:
            self.df.set_index("Date", inplace=True)
            self.df = self.df.sort_values(by="Date")
            self.df = self.df.fillna({"Total Payout": 0,
                                    "Profit": 0
                                    })
            print(Fore.CYAN, self.df)
            print(Fore.MAGENTA, 'Use "-v" to show all rows.', Style.RESET_ALL)

    def lst_files(self):
        for files in os.listdir("data_files"):
            if files.endswith(".csv"):
                self.files.append(files)
        print(Fore.CYAN, ", ".join(self.files), Style.RESET_ALL)

    def del_files(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
        else:
            sys.exit(Fore.CYAN, f"Couldn't remove {self.filename}, the file does not exist", Style.RESET_ALL) 
