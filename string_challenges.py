from collections import Counter

# Вывести последнюю букву в слове
word = 'Архангельск'
# ???

length = len(word)

print(word[length - 1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???

word_lower = word.lower()

count = Counter(word_lower)

print(count['а'])


# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???

def is_vowel_ru(letter):
    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я']
    if letter in vowels:
        return True
    else:
        return False
    
def vowels_cons_num_ru(word):
    letters = {'vowels': 0, 'consonants': 0}
    if not word.isalpha():
        raise ValueError('Данное значение не является словом')
    word = word.lower()
    for letter in word:
        if is_vowel_ru(letter) == True:
            letters['vowels'] += 1
        else:
            letters['consonants'] += 1
    return letters

print(vowels_cons_num_ru(word)['vowels'])



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???

sentence_words = sentence.split()

words_number = len(sentence_words) 

print(words_number)


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???

for word in sentence_words:
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???

letters_sum = 0

for word in sentence_words:
    letters_sum += len(word)

print(letters_sum / words_number)
