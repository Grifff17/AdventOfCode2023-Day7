from collections import Counter

# dictionary of individual card values
cardValues = {
    "2":"02",
    "3":"03",
    "4":"04",
    "5":"05",
    "6":"06",
    "7":"07",
    "8":"08",
    "9":"09",
    "T":"10",
    "J":"11",
    "Q":"12",
    "K":"13",
    "A":"14"
}

cardValuesWild = {
    "2":"02",
    "3":"03",
    "4":"04",
    "5":"05",
    "6":"06",
    "7":"07",
    "8":"08",
    "9":"09",
    "T":"10",
    "J":"00",
    "Q":"12",
    "K":"13",
    "A":"14"
}

def solve():
    data = fileRead("input.txt")
    rounds = []
    for row in data:
        rounds.append(row.split(" "))
    
    sum = 0
    scores = []
    for round in rounds:
        score = float(scoreWildHand(round[0]))
        scores.append([score, int(round[1].strip())])
    scores.sort(key=lambda arr: arr[0])
    for i in range(len(scores)):
        sum = sum + ( (i+1) * scores[i][1] )
    print(sum)


# scores a hand and reurns a float representing how strong it is
def scoreHand(strHand):
    hand = list(strHand)
    score = ""
    uniqueCards = len(set(hand))
    if (uniqueCards == 1): #five of a kind
        score = "7"
    elif (uniqueCards == 2):
        if 1 in list(Counter(hand).values()): #four of a kind
            score = "6"
        else: #full house
            score = "5" 
    elif (uniqueCards == 3):
        if 3 in list(Counter(hand).values()): #three of a kind
            score = "4"
        else: # two pair
            score = "3"
    elif (uniqueCards == 4): #1 pair
        score = "2"
    else: #high card
        score = "1"
    score = score + "."
    for i in range(5):
        scoreFragment = cardValues.get(hand[i])
        score = score + scoreFragment
    return score

# scores a hand and reurns a float representing how strong it is, using wild jacks
def scoreWildHand(strHand):
    hand = list(strHand)
    score = ""

    replaceCard = "J"
    handCount = Counter(hand).most_common()
    mostCard = 0
    allMostCards = []
    for k,v in handCount:
        if ( v > mostCard and k != "J"):
            mostCard = v
            allMostCards = [k]
        elif ( v == mostCard and k !="J" ):
            allMostCards.append(k)
    print(hand)
    print(allMostCards)
    for card in allMostCards:
        if cardValuesWild.get(card) > cardValuesWild.get(replaceCard):
            replaceCard = card
    print(replaceCard)
    wildhand = list(strHand.replace("J", replaceCard))

    uniqueCards = len(set(wildhand))
    if (uniqueCards == 1): #five of a kind
        score = "7"
    elif (uniqueCards == 2):
        if 1 in list(Counter(wildhand).values()): #four of a kind
            score = "6"
        else: #full house
            score = "5" 
    elif (uniqueCards == 3):
        if 3 in list(Counter(wildhand).values()): #three of a kind
            score = "4"
        else: # two pair
            score = "3"
    elif (uniqueCards == 4): #1 pair
        score = "2"
    else: #high card
        score = "1"
    score = score + "."

    for i in range(5):
        scoreFragment = cardValuesWild.get(hand[i])
        score = score + scoreFragment

    return score

# read file input
def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

solve()