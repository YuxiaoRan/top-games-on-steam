# top_games_on_steam
Description: A python web-scraping program that finds top games on Steam store.

Usage:
  python top_games_on_steam.py [num_games]
  
Optional Argument:
  num_games -- positive integer number of games displayed (default 25)
  
Output File:
  top_games_on_steam.csv -- a csv file that contains information about top [num_games] games on Steam

Output Format:
  game_name | released_date | positive_review | original_price | final_price
  
Possible Bugs:
  1) num_games exceeds the max number of games displayed on the website
