import re
import string
from pprint import pprint
from collections import Counter


with open("text.txt") as f:
    content = f.read()


clear_text = re.sub(f"[{string.punctuation}»«]", " ", content.lower())
words = re.split("\s+", clear_text)
stats = Counter(words)

pprint(stats.most_common(20))
