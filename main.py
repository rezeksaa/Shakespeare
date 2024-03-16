import random
import re

def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    return text

def preprocess_dataset(text):
    words = re.findall(r'\w+', text.lower())
    return words

def build_markov_chain(words, order):
    markov_chain = {}
    for i in range(order, len(words)):
        key = tuple(words[i - order:i])
        value = words[i]

        if key not in markov_chain:
            markov_chain[key] = []

        markov_chain[key].append(value)

    return markov_chain

def generate_phrase(markov_chain, start_key, length):
    phrase = [start_key[random.randint(0,1)]]
    current_key = start_key

    for _ in range(length - 1):
        next_word = random.choice(markov_chain[current_key])
        phrase.append(next_word)
        current_key = current_key[1:] + (next_word,)

    return ' '.join(phrase)

def main():
    file_path = 'shakespeare.txt'
    dataset = load_dataset(file_path)
    words = preprocess_dataset(dataset)

    markov_chain = build_markov_chain(words, 2)
    start_key = ('the', 'best')
    length = 10

    generated_phrase = generate_phrase(markov_chain, start_key, length)
    print("Generated Phrase :")
    print(generated_phrase)

if __name__ == '__main__':
    main()