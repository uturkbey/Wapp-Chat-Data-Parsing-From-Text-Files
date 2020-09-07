# Aouthor: Utku Türkbey
# Whatsapp Statistics V1.0
# This program is designed and implemented for parsing data and grouping information based on "message export" files of Whatsapp in .txt format.
# Most of the code in the version V1.0 is focused on basic reading from a file, storing data in data structures and in general,
# pracitising basic Python programming skills and applying "Thinking Pythonically" as quoted by Prof. Charles Severance in his "Python for Everybody" book.
# In the following versions of the code, main concern will be centered of applying statistical operations on and visualizing the parsed data.
# For the time being most of this functionality is left out to be handled by Microsoft Excel Spreadsheets.
# Thank you for your interest and I hope this piece of simple coding project earns your, even partial, aprreciation.


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
#to keep rocord of monthly message numbers
jan = dict()
feb = dict()
march = dict()
apr = dict()
may = dict()
june = dict()
july = dict()
aug = dict()
sept = dict()
oct = dict()
nov = dict()
dec = dict()
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
                jan[words[2]] = jan.get(words[2], 0) + 1
            elif int(dateStamp[1]) == 2 :
                feb[words[2]] = feb.get(words[2], 0) + 1
            elif int(dateStamp[1]) == 3 :
                march[words[2]] = march.get(words[2], 0) + 1
            elif int(dateStamp[1]) == 4 :
                apr[words[2]] = apr.get(words[2], 0) + 1
            elif int(dateStamp[1]) == 5 :
                may[words[2]] = may.get(words[2], 0) + 1
            elif int(dateStamp[1]) == 6 :
                june[words[2]] = june.get(words[2], 0) + 1
            elif int(dateStamp[1]) == 7 :
                july[words[2]] = july.get(words[2], 0) + 1
            elif int(dateStamp[1]) == 8 :
                aug[words[2]] = aug.get(words[2], 0) + 1
            elif int(dateStamp[1]) == 9 :
                sept[words[2]] = sept.get(words[2], 0) + 1
            elif int(dateStamp[1]) == 10 :
                oct[words[2]] = oct.get(words[2], 0) + 1
            elif int(dateStamp[1]) == 11 :
                nov[words[2]] = nov.get(words[2], 0) + 1
            else :
                dec[words[2]] = dec.get(words[2], 0) + 1
            #2.6)Message body length calculation(by number of words)
            wordCount = len( ( line[msgStart+2:] ).split() ) #after ":" there is always a " ", thus +2 occures
            lengths[words[2]] = lengths.get(words[2], 0) + wordCount

#3)Printing the calculated values
#!!!(Once Again) Most of the data visualization and statsitical values calculations such as averages or standart deviations are handled in Microsoft Excel Spreadsheets.
#!!!Follownig versions of this program will be mostly focused on visualization and analysis of the data

#3.1)Printing total message counts
print("Total messages: ")
#create a list and fill with tupples
c = list()
for key, val in list(counts.items()):
    c.append((val, key))
#sort list of tuppless and print it
c.sort(reverse=True)
for key, val in c:
    print(val, key)
print()

#3.2)Printing total morning message counts
print("Total messages (5:00 - 19:00): ")
#create a list and fill with tupples
m = list()
for key, val in list(morning.items()):
    m.append((val, key))
#sort list of tuppless and print it
m.sort(reverse=True)
for key, val in m:
    print(val, key)
print()

#3.3)Printing total evening message counts
print("Total messages (19:00 - 24:00): ")
#create a list and fill with tupples
e = list()
for key, val in list(evening.items()):
    e.append((val, key))
#sort list of tuppless and print it
e.sort(reverse=True)
for key, val in e:
    print(val, key)
print()

#3.4)Printing total night message counts
print("Total messages (24:00 - 5:00): ")
#create a list and fill with tupples
n = list()
for key, val in list(night.items()):
    n.append((val, key))
#sort list of tuppless and print it
n.sort(reverse=True)
for key, val in n:
    print(val, key)
print()

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


print(jan)
print(feb)
print(march)
print(apr)
print(may)
print(june)
print(july)
print(aug)
print(sept)
print(oct)
print(nov)
print(dec)

#This is the end:)
