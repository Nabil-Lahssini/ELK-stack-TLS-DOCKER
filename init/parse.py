import os
path = "./login.txt"

def parse(text):
    phrases = text.split("\n")
    stopwords = ["Changed", "password","for","=", "PASSWORD",""]
    finalList = []
    for phrase in list(phrases):
        if phrase != "":
            if phrase[0] == "P":
                words = phrase.split(" ")
                for word in words:
                    if word in stopwords:
                        words.remove(word)
                finalList.append(words)
    return finalList

def save(data):
    f = open(path, 'a')
    myList = parse(data)
    for login in myList:
        f.write(login[0].upper()+"_USERNAME" + "="+login[0]+"\n")
        f.write(login[0].upper() +"_PASSWORD" + "="+login[1]+"\n")
    f.close()