# Aouthor: Utku Türkbey
# Whatsapp Statistics V1.2
# This program is designed and implemented for parsing data and grouping information based on "message export" files of Whatsapp in .txt format.
# Most of the code in the version is focused on basic reading from a file, storing data in data structures and in general,
# pracitising basic Python programming skills and applying "Thinking Pythonically" as quoted by Prof. Charles Severance in his "Python for Everybody" book.
# In the following versions of the code, main concern will be centered of applying statistical operations on and visualizing the parsed data.
# For the time being most of this functionality is left out to be handled by Microsoft Excel Spreadsheets.
# Thank you for your interest and I hope this piece of simple coding project earns your, even partial, aprreciation.

#New in V1.2:
#Rather than manual initialization of month dictionaries in section 2.1, they are created in a loop and kept in a list
#In accordance with the updates in 2.1, section 2.5 is updated.
#Common printing operations defined before 3.1 as a python function for simplicity. Section 3 updated accordingly.

# !!!Program functionality is sensitive to data file format!!!
# !!!Restrcitions about file format:
    # *All message lines must start with a time stamp and then must be followed by the username, end with columns and a message body.
    # e.g. [6.12.2019 02:27:10] Utku Turkbey: <message body>
    # *Username might vary but time stamp format is strict
    # *Only English alphabet letters are allowed, otherwise statistical values might be incorrect

# Procedures mainly consist of:
    # 1)opening file,
    # 2)reading file and modifying necessary data structures wrt data,
    # 3)Printing results in a ordered and easy to read format

import string

#1) Opening file containing wapp text results

fname = input("Please enter a file name: ")
while True:
    try:
        fhand = open(fname,  encoding = "utf-8") #Data file is encoded in UTF-8(8-Bit Unicode) format
        break
    except:
        fname = input("Invalid file name!! Please enter a valid file name: ")


#2)reading file and modifying necessary data structures wrt data

#2.1)Creation of necessary data structures to hold info
#to keep record of number of messages sent by specific users
counts = dict()
#to keep record of count of used words
wordCounts = dict()
#to keep rocord of monthly message numbers
months = list()
for i in range(12):
    months.append(dict()) #Dictionary for each month data is stored in a list, in the order where index 0 is January and index 11 is December.

 #to keep records of number of messages sent by specific users within those time intervals
morning = dict() #5:00 - 19:00
evening = dict() #19:00 - 24:00
night = dict() #24:00 - 5:00
#to keep record of message body lengths(by wordcount) of messages sent by specific users
lengths = dict()

#2.2)Reading from file line by line
for line in fhand : #Pase data line by line
    if line[0] == '[' or line[0] == 'â' : #All message lines starts with a time stamp such as [6.12.2019 02:27:10], other lines are simply ignored
        msgStart = line.find(":",20) #First ":" after the time stamp, hence the username, indicates the (starting index - 1) of the message body within the line
        if msgStart != -1 : #If ":" is not found then this line is not a message but a notofication
            words = line.split() #Obtain each word in line as a list
            #2.3)Message Count(Although this value could be calculated as the sum of time of the day or month intervals, it is calculated individually for clearity )
            counts[words[2]] = counts.get(words[2], 0) + 1 #Third word in every message line is the first word of username, related message count is incremented in every occurance of username
            #2.4)Message count wrt time intervals
            timeStamp = words[1].split(":") #Second word in every message line is always the time data subsection of the time Stamp in the format such as 02:27:10]
            if int(timeStamp[0]) >= 5 and  int(timeStamp[0]) < 19 : #Hour section of the time stamp shows message is sent in the morning
                morning[words[2]] = morning.get(words[2], 0) + 1
            elif int(timeStamp[0]) >= 19 and  int(timeStamp[0]) < 24 : #Hour section of the time stamp shows message is sent in the evening
                evening[words[2]] = evening.get(words[2], 0) + 1
            else :
                night[words[2]] = night.get(words[2], 0) + 1
            #2.5)message count wrt months
            dateStamp = words[0].split(".") #First word in every message line is always the date data subsction of the time stamp in the format such as [6.12.2019
            if int(dateStamp[1]) == 1 : #Month section of the date stamp shows in which month the message is sent
                months[0][words[2]] = months[0].get(words[2], 0) + 1
            elif int(dateStamp[1]) == 2 :
                months[1][words[2]] = months[1].get(words[2], 0) + 1
            elif int(dateStamp[1]) == 3 :
                months[2][words[2]] = months[2].get(words[2], 0) + 1
            elif int(dateStamp[1]) == 4 :
                months[3][words[2]] = months[3].get(words[2], 0) + 1
            elif int(dateStamp[1]) == 5 :
                months[4][words[2]] = months[4].get(words[2], 0) + 1
            elif int(dateStamp[1]) == 6 :
                months[5][words[2]] = months[5].get(words[2], 0) + 1
            elif int(dateStamp[1]) == 7 :
                months[6][words[2]] = months[6].get(words[2], 0) + 1
            elif int(dateStamp[1]) == 8 :
                months[7][words[2]] = months[7].get(words[2], 0) + 1
            elif int(dateStamp[1]) == 9 :
                months[8][words[2]] = months[8].get(words[2], 0) + 1
            elif int(dateStamp[1]) == 10 :
                months[9][words[2]] = months[9].get(words[2], 0) + 1
            elif int(dateStamp[1]) == 11 :
                months[10][words[2]] = months[10].get(words[2], 0) + 1
            else :
                months[11][words[2]] = months[11].get(words[2], 0) + 1
            #2.6)Message body length calculation(by number of words)
            wordCount = len( ( line[msgStart+2:] ).split() ) #after ":" there is always a " ", thus +2 occures
            lengths[words[2]] = lengths.get(words[2], 0) + wordCount
            #2.7)Number of times words are used
            body = line[msgStart+2:] #hold body seperatel
            body = body.translate(str.maketrans('', '', string.punctuation))
            body = body.lower()
            bodyWords = body.split()
            for w in bodyWords :
                wordCounts[w] = wordCounts.get(w, 0) + 1

#3)Printing the calculated values
#!!!(Once Again) Most of the data visualization and statsitical values calculations such as averages or standart deviations are handled in Microsoft Excel Spreadsheets.
#!!!Follownig versions of this program will be mostly focused on visualization and analysis of the data


def printData(data, size=0): #A function defined for handling common printing operations
    #create a list and fill with tupples
    lst = list()
    for key, val in list(data.items()):
        lst.append((val, key))
    #sort list of tuppless and print it
    lst.sort(reverse=True)
    if size == 0:
        for key, val in lst:
            print(val, key)
    elif size > 0:
        for key, val in lst[:int(size)]:
            print(val, key)
    else:
        print("INVALID SIZE")
    print()

#3.1)Printing total message counts
print("Total messages: ")
printData(counts)

#3.2)Printing total morning message counts
print("Total messages (5:00 - 19:00): ")
printData(morning)

#3.3)Printing total evening message counts
print("Total messages (19:00 - 24:00): ")
printData(evening)

#3.4)Printing total night message counts
print("Total messages (24:00 - 5:00): ")
printData(night)

#3.5)Printing total message lengths
print("Total/Average message lengths(by word count): ")
#create a list and fill with tupples
l = list()
for key, val in list(lengths.items()):
    l.append((val, key))
#sort list of tuppless and print it
l.sort(reverse=True)
for key, val in l:
    print(val, key, key/counts[val])
print()

#3.6)Printing 100 most common words
print("Number of occurance of words: ")
print("Total word count: " , len(wordCounts))
printData(wordCounts, 100)

#3.7)Printing monthly message count of users
for i in range(len(months)) :
    print("Month :", i + 1)
    printData(months[i])

#This is the end:)
