import sys
from collections import defaultdict

def parse(line):
    word, fp, ct = line.strip().split("\t")
    return word, fp, int(ct)

def updateWordDict(wordDict, word, fp, ct):
    wordDict[word][fp] += ct

def format(postings):
    return ' '.join([f"{doc}:{freq}" for doc, freq in postings.items()])

def outputInvertIdx(wordDict):
    for word, postings in wordDict.items():
        postings_list = format(postings)
        print(f"{word}\t{{{postings_list}}}")

def reducer():
    wordDict = defaultdict(lambda: defaultdict(int))
    for line in sys.stdin:
        word, fp, ct = parse(line)
        updateWordDict(wordDict, word, fp, ct)
    outputInvertIdx(wordDict)

# Run reducer
if __name__ == "__main__":
    reducer()
