def title_case(sentence):
    words = sentence.split()
    res = []
    for word in words:
        if word:
            first = word[0].upper()
            rest = word[1:].lower()
            res.append(first + rest)
    return ' '.join(res)

n = input("enter a String: ")
print(title_case(n))