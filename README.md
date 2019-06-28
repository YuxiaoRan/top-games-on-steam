# top_games_on_steam

Author: Yuxiao "Sean" Ran

Date: 6/27/2019


## Description
A web-scraping python program that finds top games on Steam store and writes their infomation to a csv file


## Usage
```
> python top_games_on_steam.py [num_games]
```

**_num_games_** -- optional argument, a positive integer number of games displayed (default 25)
  
```
> python top_games_on_steam.py
> python top_games_on_steam.py 5
> python top_games_on_steam.py 100
```
  
  
## Output File

  **_top_games_on_steam.csv_** -- a csv file that contains information about top [num_games] games on Steam

  | *game_name* | *released_date* | *positive_review* | *original_price* | *final_price* |
  | --- | --- | --- | --- | --- |
  | Dota2 | Jul 9 - 2013 | 85% | $0 | $0 |
  | FINAL FANTASY XIV Online | Feb 18 - 2014 | 81% | $19.99 | $19.99 |
  | Borderlands: The Handsome Collection | | 92% | $229.48 | $5.90 |
  | ... | ... | ... | ... | ... |
  
  
## Potential Error Cases

- num_games exceeds the max number of games displayed on the website
