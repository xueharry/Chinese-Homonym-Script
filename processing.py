# from bs4 import BeautifulSoup
# import requests
import pandas as pd

# url = "http://www.zein.se/patrick/3000char.html"
# r = requests.get(url)
# soup = BeautifulSoup(r.content, "lxml")

# # Get the table containing the 3000 most common characters
# charTable = soup.find_all('table')

# print(charTable)

# list for each of the columns in the dataframe
# number = []
# character = []
# entry = []

# # Extract each of the characters, skipping over the header
# for row in charTable.find_all('tr'):
# 	print(row)
# 	col = row.find_all('td')
# 	num = col[0].string
# 	number.append(num)
# 	char = col[1].string
# 	character.append(char)
# 	try:
# 		ent = col[2].string
# 	except:
# 		ent = ""
# 	character.append(ent)

# columns = {'number': number, 'character': character, 'entry':entry}
# Create dataframe from columns
# df = pd.DataFrame(columns)





