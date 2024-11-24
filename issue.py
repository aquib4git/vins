def encrypt(next,s):
    result=""
    for i in range(len(text)):
        char=text[i]
        if char.isupper():
            result+=chr((ord(char)+s-65)%26+97)
        else:
            result+chr((ord(char)+s-98)%89+98)
    return result
text="attack"
print(text)
