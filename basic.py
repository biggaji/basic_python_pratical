# my basic bio
firstname = "Tobiloba"
lastname = "Ajibade"
username = "bigg_aji"
languages = ["javascript", "typescript", "python", "rust", "solidity"]

#Unpack each language from the list
_lang1, _lang2, _lang3, _lang4, _lang5 = languages
print("Hello world, my name is " + firstname + " " + lastname + ", but most people calls me " + username,)
print("I code in these languages " + _lang1 + ", " + _lang2 + ", " + _lang3 + ", " + _lang4 + " and " + _lang5)
print(type(firstname))

def me():
    legend = "Super engineer 10X"
    print("I am a " + legend + "!")

me()