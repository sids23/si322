#solution2.py

#siddharth swarup & nick hogan

#first we will open the file
#then we make a dictionary reading the words into it
#everytime a word is seen it either adds to the dictionary or increments the count associtated with the value

wordlist = {

}

with open("words.txt", "r") as file:
    for line in file:
        list = line.strip().split()
        for raw_word in list:
            word = raw_word.lower()
            if word in wordlist:
                wordlist[word] += 1
            else:
                wordlist[word] = 1

#we searched up how to sort a dictionary by value and saw this command
#we got this from google AI search result
sortwordlist = dict(sorted(wordlist.items(), key = lambda item: item[1], reverse=True))

top5 = 0

#loop through the top 5 key value pairs and print them
for word, count in sortwordlist.items():
    if top5 > 4:
        break
    print(f"{word}: {count}")
    top5 += 1