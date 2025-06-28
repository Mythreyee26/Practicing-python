# n = "abcdefghijk"
# print(n[::3])

def returns_every_third_character(s):
    return s[::3]

s = input("Enter a string: ")
print("returns every third character:", returns_every_third_character(s))