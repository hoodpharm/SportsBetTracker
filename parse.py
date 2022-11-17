import argparse

class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog = "Bet Tracker",
            description = "Track sports betting profits/losses.")

    def parse_args(self): 
        self.parser.add_argument("filename", help="file to append to. Creates new file if doesnt exist, use .csv extention")
        self.parser.add_argument("-b", "--bet", metavar='', help="bet took, e.g. 'Warriors ML' ")
        self.parser.add_argument("-o", "--odds", metavar='', help="american odds", type=int)
        self.parser.add_argument("-w", "--wager", metavar='', help="bet amount", type=float)
        self.parser.add_argument("-O", "--outcome", metavar='', help="W/L?")
        self.parser.add_argument("-v", help="verbose", action="store_true")
        self.parser.add_argument("-l", "--list", help="list files", action="store_true")
        self.parser.add_argument("-d", "--date", metavar='', help="change date of bet. 'YYYY-MM-DD'")
        self.parser.add_argument("--rm", help="remove unwanted file", action="store_true")
        self.parser.add_argument("--read_file", help="read contents of file", action="store_true")
        self.parser.add_argument("--profits", help="calculate total Win/Loss", action="store_true")
        self.parser.add_argument("--total_bets", help="show total number of bets made", action="store_true")
        self.parser.add_argument("--max_win", help="show max win", action="store_true")
        self.parser.add_argument("--max_loss", help="show max loss", action="store_true")
        args = vars(self.parser.parse_args())
        return args