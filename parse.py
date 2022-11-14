import argparse

def parse_args(): 
    parser = argparse.ArgumentParser(
        prog = "Bet Tracker",
        description = "Track sports betting profits/losses. Profits are shown without wager.")
    parser.add_argument("filename", help="file to append to. Creates new file if doesnt exist.")
    parser.add_argument("-b", "--bet", metavar='', help="bet took, e.g. 'Warriors ML' ")
    parser.add_argument("-o", "--odds", metavar='', help="american odds", type=int)
    parser.add_argument("-w", "--wager", metavar='', help="bet amount", type=int)
    parser.add_argument("-O", "--outcome", metavar='', help="W/L?")
    parser.add_argument("--read_file", help="read contents of file", action="store_true")
    parser.add_argument("--profits", help="calculate total Win/Loss", action="store_true")
    parser.add_argument("--total_bets", help="show total number of bets made", action="store_true")
    args = vars(parser.parse_args())
    return args
