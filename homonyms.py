import pandas as pd
import pinyin
import sys

NUM_CHARS = 3000

# If no arguments provided use all characters by default
if len(sys.argv) == 1:
	pass

elif len(sys.argv) == 2:
	NUM_CHARS = int(sys.argv[1])

df = pd.read_csv("chars.csv")
df.columns = ["number", "character", "entry"]

# Only consider the number of characters requested by user
df = df.head(NUM_CHARS)

# Add a pinyin column
df["pinyin"] = df["character"].apply(pinyin.get)

# TODO: Investigate characters that don't have pinyin
# Aggregate characters with same pinyin together
df = pd.concat(g for _, g in df.groupby("pinyin") if len(g) > 1)

print(df)





