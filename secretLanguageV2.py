#             ______ENCODING FUNCTION______
# first we'll build a function for reversing the words of our statement
# and after reversing, its characters would be replaced by their previous alphabets
import random
def encode(words):
    final = ""
    words = words[::-1]
    for cha in words:
        if cha.isalpha():
            replace = chr(ord(cha)-1)
            final += replace if replace.isalpha() else "z"
        else:
            final += cha
    return final

#             ______DECODING FUNCTION______
# now we'll first reverse the coded statement
# then we'll replace its characters to upcoming alphabets
def decode(words):
    final = ""
    words = words[::-1]
    for cha in words:
        if cha.isalpha():
            replace = chr(ord(cha)+1)
            final += replace if replace.isalpha() else "a"
        else:
            final += cha
    return final

# building user interface
print("Welcome to Our Encoding and Decoding Program!")
message = input("""\nPlease Enter Your Message Down Below and Press ENTER to Start Process
    
    ------->>>>     """)
print("\nDo you want to Encode / Decode your message? ")
command = input("Press 1 to Encode and 0 to Decode:    ")
command = True if command == "1" else False
if command:
    wordsList = message.split()
    for i in range(len(wordsList)):
        word = wordsList[i]
        wordsList[i] = encode(word)
    encoded = " ".join(wordsList)
    # giving the encoded message
    print("\nYour Encoded Message is:\n")
    print(encoded)
else:
    wordList = message.split()
    for i in range(len(wordList)):
        word = wordList[i]
        wordList[i] = decode(word)
    decoded = " ".join(wordList).capitalize()
    # giving the decoded message
    print("\nYour Decoded Message is:\n")
    print(decoded)
