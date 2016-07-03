# Chinese-Homonym-Script
Script to extract the homonyms from the 3000 most common Chinese characters and generate a CSV of grouped homonyms.

# Usage
1. Clone the repository
```git clone https://github.com/xueharry/Chinese-Homonym-Script.git```
2. Run the command
```python homonyms.py [n]```
which generates a csv containing homonyms among the first `n` most common Chinese characters. If no argument is supplied, the homonym list for all 3000 characters is generated. The outputted file is titled `homonyms.csv`.

# Character List Source
The original list can be found at http://www.zein.se/patrick/3000char.html.
