bag = {"r":12, "g":13, "b":14}
file = open("input.txt","r")
sum = 0
lines = file.readlines()
for line in lines:
    start = line.find(":")
    Line = line[start:].strip() ; print(Line)
    R = [] ; B = [] ; G = []
    colors = {"r":[], "g":[], "b":[]}
    i = 0
    while i in range(len(Line)):
        if Line[i].isdigit():
            digit = Line[i]

            i += 1
            while Line[i].isdigit():
                digit += Line[i]
                i += 1

            curr = colors.get(Line[i+1])
            curr.append(int(digit))
        i += 1
    print(colors) 
    maxRed = max(colors.get("r"))
    maxGreen = max(colors.get("g"))
    maxBlue = max(colors.get("b"))
    if maxRed <= bag.get("r") and maxGreen <= bag.get("g") and maxBlue <= bag.get("b"):
        gameID = line[5:start]
        sum += int(gameID)
print(sum)
