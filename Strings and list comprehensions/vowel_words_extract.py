
def extract_vowel_words(sentence):
    vowels = 'aeiouAEIOU'
    words = sentence.split()
    res = [word for word in words if word[0] in vowels]
    return ' '.join(res)

sentence = input()
print(extract_vowel_words(sentence))