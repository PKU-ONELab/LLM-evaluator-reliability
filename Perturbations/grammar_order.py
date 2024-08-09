import random
import re
import nltk
import numpy as np

def contains_non_alpha(word):
    # Regular expression for characters not in a-z
    return bool(re.search('[^a-z]', word))


def introduce_swap(sentence):
    """Swap two adjacent words in the sentence"""
    words = sentence.split()
    
    if len(words) > 5:
        if len(words) < 10:
            
            position = [i for i in range(1, len(words) - 1) if not contains_non_alpha(words[i]) and not contains_non_alpha(words[i+1])]

            if position:
                word_index = random.choice(position) 
                words[word_index], words[word_index+1] = words[word_index+1], words[word_index]
        else:
        
            position1 = [i for i in range(1, len(words)//2 - 1) if not contains_non_alpha(words[i]) and not contains_non_alpha(words[i+1])]

            if position1:
                word_index1 = random.choice(position1)
                words[word_index1], words[word_index1+1] = words[word_index1+1], words[word_index1]

            position2 = [i for i in range(len(words)//2, len(words) - 1) if not contains_non_alpha(words[i]) and not contains_non_alpha(words[i+1])]

            if position2:
                word_index2 = random.choice(position2)
                words[word_index2], words[word_index2+1] = words[word_index2+1], words[word_index2]
        
    return " ".join(words)


def attack_grammar_word_order(text):
    original_sentences = nltk.sent_tokenize(text)
    perturbed_sentences = []
    for sentence in original_sentences:
        perturbed_sentence = introduce_swap(sentence)
        perturbed_sentences.append(perturbed_sentence)
    return ' '.join(perturbed_sentences)


if __name__ == '__main__':
    text = """Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Josh will call Brian after work to talk about it."""
    perturbed_text = attack_grammar_word_order(text)
    print('Original: {}'.format(text))
    print('Perturbed: {}'.format(perturbed_text))
