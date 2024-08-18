import pandas
df = pandas.read_csv("fpnames.csv")

x=0

innerList=[]

newList = df["Names"].tolist()

newerList = []

container = []

list2 = []
spoonerList = []

vowels = "aieou"

for plant in newList: 
    if " " in plant:
        newPlant = plant.split(" ")
        if plant[0] not in vowels and newPlant[1][0] not in vowels:
            if len(newPlant) == 2:
                if newPlant[0][0] != newPlant[1][0]:
                    newerList.append(plant)



for choice in newerList:
    splitChoice = choice.split(" ")
    list2.append(splitChoice)
    spoonerLetters = []
    for word in splitChoice:
        spoonerLetters.append("'")
        for letter in list(word):
            if letter in vowels:
                break
            else:
                spoonerLetters.append(letter)
    stringSpooner = "".join(spoonerLetters)
    spooner = stringSpooner.split("'")
    del spooner[0]
    spoonerList.append(spooner)
    
for words,spoon in zip(list2,spoonerList):
    if len(spoon[0]) == 1:
        new = list(words[0])
        new[0] = spoon[1]
        newWord = "".join(new)
    else:
        newWord = words[0].replace(words[0][:len(spoon[0])], spoon[1])
    innerList.append(newWord)
    innerList.append(" ")
    if len(spoon[1]) == 1:
        new = list(words[1])
        new[0] = spoon[0]
        newWord = "".join(new)
    else:
        newWord = words[1].replace(words[1][:len(spoon[1])], spoon[0])
    innerList.append(newWord)
    finalString = "".join(innerList)
    container.append(finalString)
    innerList=[]
    #print(newWord)
    
output = open("TheAnswer.txt", "w")

for plant_name, spooner in zip(newerList, container):
    output.write("Plant Name: " + plant_name + "\n" +
                 "Spoonerism: " + spooner + "\n\n")
    
output.close()
            
        
            
    
            