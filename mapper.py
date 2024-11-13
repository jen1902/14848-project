import sys
import os

def getFp():
    return os.environ.get("local_mr_file", "")

def countTerms(line):
    words = line.strip().split()
    wordCounts = {}
    for w in words:
        word = w.lower()
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1
    return wordCounts

def outputWordCounts(filepath, wordCounts):
    for word, ct in wordCounts.items():
        print(f"{word}\t{filepath}\t{ct}")

def mapper():
    fp = getFp()
    for line in sys.stdin:
        wordCounts = countTerms(line)
        outputWordCounts(fp, wordCounts)

# Run mapper
if __name__ == "__main__":
    mapper()
