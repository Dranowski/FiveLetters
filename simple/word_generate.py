# f = open('russian_nouns.txt', 'r', encoding='utf-8')
# vocabulary = open('five_letters_nouns.txt', 'w', encoding='utf-8')
# for line in f:
#     if len(line)-1 == 5:
#         vocabulary.write(line)
# f.close()

import random
import linecache
def generate():
    f = open('five_letters_nouns.txt', 'r', encoding='utf-8')
    line = random.randint(1, 3483)
    ans = linecache.getline('five_letters_nouns.txt', line)
    f.close()
    return ans