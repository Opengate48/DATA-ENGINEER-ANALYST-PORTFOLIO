import sys
import os


args = sys.argv
del args[0]
path = args[0]
repository = os.listdir(path)
users = dict()
resources = dict()
celebrity = ('', 0)
bestseller = ('', 0)
results = []
for file in repository:
    with open(str(path) + "/" + str(file), 'r+', encoding="ISO-8859-1") as f:
        while True:
            line = f.readline()
            line = tuple(str(j).strip() for j in line.split(","))
            ip = line[0]
            if len(line) >= 3:
                if ip in users:
                    users[ip] += 1                                                      #a specific ip and its frequency are associated in the dictionary
                else:
                    users[ip] = 1

                if users[ip] > celebrity[1]:
                    celebrity = (ip, users[ip])                                         #frequency is in the users[ip]
                link = line[-3]
                if link in resources:
                    resources[link] += 1                                                #specific url link and its frequency are associated in the dictionary
                else:
                    resources[link] = 1
                if resources[link] > bestseller[1]:
                    bestseller = (link, resources[link])                                #frequency is in the resources[link]
            if len(line)<4:
                break
    results.append((file, bestseller, celebrity))                                       #each pair of bestseller and celebrity is associated in tuple with its own file
    users = dict()
    resources = dict()
    celebrity = ('', 0)                                                                 #resetting the bestseller and celebrity to the default state before reading a new file
    bestseller = ('', 0)
for entry in results:
    print("Stat1: " + str(entry[1][0]) + " - " + str(entry[1][1]))
    print("Stat2: " + str(entry[2][0]) + " - " + str(entry[2][1]))



        
