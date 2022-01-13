import re
import string
from pprint import pprint
from collections import defaultdict


with open("text.txt") as f:
    content = f.read()


clear_text = re.sub(f"[{string.punctuation}»«]", " ", content.lower())
words = re.split("\s+", clear_text)

def return_100():
    return 100

stats = defaultdict(int)
for word in words:
    # if word not in words:
    #     stats[word] = 0
    stats[word] += 1

pprint(stats)
