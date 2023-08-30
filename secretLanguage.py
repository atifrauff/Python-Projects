# First we'll encrypt our statements

# Function to replace each character with previous character in English alphabets
def longer_char(word):
    result = ""
    for char in word:
        if char.isalpha():
            prev_char = chr(ord(char)-1)
            # if the previous char is "a"
            result += prev_char if prev_char.isalpha() else "z"
        else:
            result += char
    return result

# decrypt longer words
def again_long(wording):
    result = ""
    for char in wording:
        if char.isalpha():
            prev_char = chr(ord(char)+1)
            result += prev_char if prev_char.isalpha() else "a"
        else:
            result += char
    return result
# taking input from user to encrypt the msg
msg = input("""Type your message down below
            
    --------->>>>   """)
print("\nDo you want to encode or decode any message?")
demand = input("Input 1 for encoding and 0 for decoding:  ")
coding = True if demand == "1" else False
if coding:
    word_list = msg.lower().split()
    # process words
    for i in range(len(word_list)):
        word = word_list[i]
        word_list[i] = longer_char(word)

    # join all the words back togethor
    translated_statement = " ".join(word_list).title()
    # display final statement
    print("\nEncrypted statement:")
    print(f"----->>>>  ",translated_statement)
else:
    # Now we'll Decrypt all of the statements
    word_list = msg.lower().split()
    for i in range(len(word_list)):
        word = word_list[i]
        word_list[i] = again_long(word)

    translated_statement = " ".join(word_list).title()
    print("\nDecrypted statement is:")
    print(f"----->>>>  ",translated_statement)
