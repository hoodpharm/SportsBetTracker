# SportsBetTracker

CLI application to track sports bets profits/losses.

## Usage
```
usage: Bet Tracker [-h] [-b] [-o] [-w] [-O] [-v] [-l] [-d] [--rm] [--read_file] [--profits] [--total_bets] [--max_win] [--max_loss] filename

Track sports betting profits/losses.

positional arguments:
  filename         file to append to. Creates new file if doesnt exist, use .csv extention

optional arguments:
  -h, --help       show this help message and exit
  -b , --bet       bet took, e.g. 'Warriors ML'
  -o , --odds      american odds
  -w , --wager     bet amount
  -O , --outcome   W/L?
  -v               verbose
  -l, --list       list files
  -d , --date      change date of bet. 'YYYY-MM-DD'
  --rm             remove unwanted file
  --read_file      read contents of file
  --profits        calculate total Win/Loss
  --total_bets     show total number of bets made
  --max_win        show max win
```