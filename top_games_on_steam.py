# Find the currently top games on steam.
# Author: Yuxiao Sean Ran
# Date: 6/27/2019

# import packages
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import sys

# print usage
def print_usage():
	print("Usage: python top_games_on_steam.py [num_games]\n")
	print("Optional Argument:\n  num_games -- positive integer number of games displayed (default 25)")

# check commandline arguments
args = sys.argv
max_num_args = 2
if len(args) > max_num_args:
	print("Wrong number of arguments.\n")
	print_usage()
	sys.exit()

# parse
num_pages = 1
num_games = 25
num_games_on_each_page = 25
if len(args) == max_num_args:
	try:
		num_games = int(args[1])
		if num_games < 0:
			print("num_games should be a positive integer.\n")
			print_usage()
			sys.exit()
		elif num_games == 0:
			num_pages = 1
		else:
			num_pages = (num_games - 1) // num_games_on_each_page + 1

	except ValueError:
		print("num_games should be a positive integer.\n")
		print_usage()
		sys.exit()


# retrieve data from url
def make_soup(url):
	uClient = uReq(my_url)
	page_html = uClient.read()
	page_soup = soup(page_html, features="html.parser")
	uClient.close()
	return page_soup

# find review
def find_review(review):
	return re.findall(r'\d+%', review[0]["data-tooltip-html"])[0]

# main function
# write header to file
filename = "top_games_on_steam.csv"
f = open(filename, "w")
headers = "game_name, released_date, positive_review, original_price, final_price\n"
f.write(headers)

# open up webpage
general_url = 'https://store.steampowered.com/search/?page={}'

count = 0
for i in range(1, num_pages + 1):
	my_url = general_url.format(i)
	print("Inspecting url: " + my_url)
	page_soup = make_soup(my_url)

	# find top games
	container = page_soup.findAll("div", {"id": "search_result_container"})[0]
	games = container.findAll("div")[1].findAll("a")

	for game in games:
		if count >= num_games:
			break

		# name
		game_name = game.findAll("span", {"class": "title"})[0].text

		# released date
		released_list = game.findAll("div", {"class": "col search_released responsive_secondrow"})
		if len(released_list) > 0:
			released = released_list[0].text
			released = released.replace(", ", " - ")
		else:
			released = "NaN"

		# review
		review_p = game.findAll("span", {"class": "search_review_summary positive"})
		review_m = game.findAll("span", {"class": "search_review_summary mixed"})
		review_n = game.findAll("span", {"class": "search_review_summary negative"})
		if len(review_p) > 0:
			p_rate = find_review(review_p)
		elif len(review_m) > 0:
			p_rate = find_review(review_m)
		elif len(review_n) > 0:
			p_rate = find_review(review_n)
		else:
			p_rate = "NaN"

		# price
		price = game.findAll("div", {"class": "col search_price responsive_secondrow"})
		discounted = game.findAll("div", {"class": "col search_price discounted responsive_secondrow"})
		if len(price) > 0:
			# no discount
			final_price = price[0].text.split()[0]
			if final_price in ["Free to Play", "Free Demo", "Free"]:
				# free game
				original_price = "$0"
				final_price = "$0"
			else:
				original_price = final_price
		elif len(discounted) > 0:
			# has discount
			two_prices = re.findall(r'\$\d+\.?\d*', discounted[0].text.split()[0])
			original_price = two_prices[0]
			final_price = two_prices[1]
		else:
			original_price = "NaN"
			final_price = "NaN"

		# write attributes
		f.write(game_name + "," + released + "," + p_rate + "," + original_price + "," + final_price + "\n")
		count += 1

f.close()

# end of file