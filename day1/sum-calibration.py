file = open("input.txt", "r")
lines = file.readlines()
sum = 0
#  one, two, three, four, five, six, seven, eight, and nine also count as valid "digits" : 
invletterDigits = {"eno": "1", "owt":"2", "eerht":"3", "ruof":"4", "evif":"5", "xis":"6", "neves":"7", "thgie":"8", "enin":"9"}
letterDigits = {"nine":"9", "eight":"8", "seven":"7", "six":"6", "five":"5", "four":"4", "three":"3", "two":"2", "one":"1"}
for line in lines:

    for i in range(len(line)):
        if line[i:i+3] in ["one", "two", "six"]:
            first = letterDigits[line[i:i+3]]
            break
        if line[i:i+4] in ["four", "five", "nine"]:
            first = letterDigits[line[i:i+4]]
            break
        if line[i:i+5] in ["three", "eight", "seven"]:
            first = letterDigits[line[i:i+5]]
            break
        if line[i].isdigit():
            first = line[i]
            break

    invLine = line[::-1]
    for j in range(len(invLine)):
        if invLine[j:j+3] in ["eno", "owt", "xis"]:
            last = invletterDigits[invLine[j:j+3]]
            break
        if invLine[j:j+4] in ["ruof", "evif", "enin"]:
            last = invletterDigits[invLine[j:j+4]]
            break
        if invLine[j:j+5] in ["eerht", "thgie", "neves"]:
            last = invletterDigits[invLine[j:j+5]]
            break
        if invLine[j].isdigit():
            last = invLine[j]
            break

    value = first + last
    print("digit: "+value)
    sum += int(value)
    print("line: "+line)


print("Sum: "+str(sum))

