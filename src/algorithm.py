from src.interfaces import CITIES

def erratic_search(word: str) -> str:
    instances = {}

    word = word.lower()
    word_instances = {}
    for letter in word:
        word_instances[letter] = word_instances.get(letter, 0) + 1

    for city in CITIES:
        copy_instances = word_instances.copy()
        equal_count = 0
        for letter in city:
            if copy_instances.get(letter, 0) > 0:
                equal_count += 1
                copy_instances[letter] -= 1
        instances[city] = equal_count
    
    words = [key for key, value in instances.items() if value == max(instances.values())]

    if len(words) == 1:

        return [words[0]]
    
    else:
        equal_letters = {}
        for max_city in words:
            min_length = min(len(word), len(max_city))
            count = 0
            for i in range(min_length):
                if word[i] == max_city[i]:
                    count += 1
            equal_letters[max_city] = count
    
        words2 = [key for key, value in equal_letters.items() if value == max(equal_letters.values())]

        if len(words2) == 1:

            return [words2[0]]

        else:

            return words2