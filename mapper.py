import sys
import os

def get_file():
    return os.environ.get("local_mr_file", "")

def ct_terms(line):
    words = line.strip().split()
    wordCounts = {}
    for w in words:
        word = w.lower()
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1
    return wordCounts

def word_ct_output(filepath, wordCounts):
    for word, ct in wordCounts.items():
        print(f"{word}\t{filepath}\t{ct}")

def mapper():
    fp = get_file()
    for line in sys.stdin:
        wordCounts = ct_terms(line)
        word_ct_output(fp, wordCounts)

# Run mapper
if __name__ == "__main__":
    mapper()
