# this program will let you convert large numbers into their desired names or vice versa

def convert_less_than_thousand(num):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Ninteen"]

    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninty"]

    if num < 20:
        return ones[num]
    elif num < 100:
        return tens[ num // 10 ] + " " + ones[ num % 10 ] if num % 10 != 0 else ""
    else:
        hundred_part = ones[num // 100] + " Hundred" if num // 100 != 0 else " "
        tens_part = convert_less_than_thousand(num % 100)
        
        if tens_part:
            return hundred_part + " and " + tens_part
        else:
            return hundred_part

def convert_to_words(num):
    if num == 0:
        return "Zero"
    
    groups = ["", "Thousand", "Million", "Billion"]
    result = ""
    group_idx = 0

    while num > 0:
        if num % 1000 != 0:
            result =  convert_less_than_thousand(num % 1000) + " " + groups[group_idx] + " " + result

        num = num // 1000
        group_idx += 1

    return result


if __name__ == "__main__":
    num = int(input("Enter a number:    "))
    print(convert_to_words(num))
