import random
import re
import nltk
import numpy as np

def contains_non_alpha(word):
    # Regular expression for characters not in a-z
    return bool(re.search('[^a-z]', word))


def introduce_typo(sentence):
    """Insert two typos into the sentence"""
    words = sentence.split()
    
    
    indexes = [i for i, word in enumerate(words) if len(word) >= 4 and not contains_non_alpha(word) ]
    
    if len(indexes) <= 3:
        typo_word_indexes = indexes
    else:
        typo_word_indexes = np.random.choice(indexes, size=3, replace=False).tolist()

    for typo_word_index in typo_word_indexes:
        word = words[typo_word_index]

        # Randomly choose to repeat, delete, or swap characters
        typo_choice = random.choice(["repeat", "delete", "swap"])
        
        if typo_choice == "repeat" and len(word) > 2:
            # Repeat a random character
            char_index = random.randint(0, len(word) - 1)
            word = word[:char_index] + word[char_index] + word[char_index:]
        elif typo_choice == "delete" and len(word) > 2:
            # Delete a random character
            char_index = random.randint(1, len(word) - 1)
            word = word[:char_index] + word[char_index + 1:]
        elif typo_choice == "swap" and len(word) > 2:
            # Swap two adjacent characters
            char_index = random.randint(0, len(word) - 2)
            word = word[:char_index] + word[char_index + 1] + word[char_index] + word[char_index + 2:]

        words[typo_word_index] = word
    return ' '.join(words)


def attack_grammar_typos(text):
    original_sentences = nltk.sent_tokenize(text)
    perturbed_sentences = []
    for sentence in original_sentences:
        perturbed_sentence = introduce_typo(sentence)
        perturbed_sentences.append(perturbed_sentence)
    return ' '.join(perturbed_sentences)


if __name__ == '__main__':
    text = """Josh wants to buy a tablet and doesn't know which brand he should choose. According to Brian, other brands are better than Apple and he can get a Samsung tablet cheaper. Josh will call Brian after work to talk about it."""
    perturbed_text = attack_grammar_typos(text)
    print('Original: {}'.format(text))
    print('Perturbed: {}'.format(perturbed_text))
