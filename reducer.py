import sys
from collections import defaultdict





def parse(line):
    word, fp, ct = line.strip().split("\t")
    return word, fp, int(ct)

def update_word_dict(word_dict, word, fp, ct):
    word_dict[word][fp] += ct

def format(postings):
    return ' '.join([f"{doc}:{freq}" for doc, freq in postings.items()])

def invert_idx_output(word_dict):
    for word, postings in word_dict.items():
        postings_list = format(postings)
        print(f"{word}\t{{{postings_list}}}")

def reducer():
    word_dict = defaultdict(lambda: defaultdict(int))
    for line in sys.stdin:
        word, fp, ct = parse(line)
        update_word_dict(word_dict, word, fp, ct)
    invert_idx_output(word_dict)

# Run reducer
if __name__ == "__main__":
    reducer()
