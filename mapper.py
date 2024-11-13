import sys
import os






def get_file():
    return os.environ.get("local_mr_file", "")

def ct_terms(line):
    words = line.strip().split()
    word_ct = {}
    for w in words:
        word = w.lower()
        if word in word_ct:
            word_ct[word] += 1
        else:
            word_ct[word] = 1
    return word_ct

def word_ct_output(filepath, word_ct):
    for word, ct in word_ct.items():
        print(f"{word}\t{filepath}\t{ct}")

def mapper():
    fp = get_file()
    for line in sys.stdin:
        word_ct = ct_terms(line)
        word_ct_output(fp, word_ct)

# Run mapper
if __name__ == "__main__":
    mapper()
