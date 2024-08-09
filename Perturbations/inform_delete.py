import random
import re
import nltk
import numpy as np

def is_the_same(list1, list2):
    for s1, s2 in zip(list1, list2):
        if s1 != s2:
            return False
    return True


def attack_informative_delete_last(text):
    original_sentences = nltk.sent_tokenize(text)
    perturbed_sentences = original_sentences[:-1]
 
    return ' '.join(perturbed_sentences)


if __name__ == '__main__':
    text = """Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Josh will call Brian after work to talk about it."""
    perturbed_text = attack_informative_delete_last(text)
    print('Original: {}'.format(text))
    print('Perturbed: {}'.format(perturbed_text))

