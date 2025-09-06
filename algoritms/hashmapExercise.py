import csv
with open("nyc_weather.csv",mode='r') as csv_reader:
    f = csv.reader(csv_reader)
    weatherArray = []
    for line in f:
        try:
            temperature = int(line[1])
            weatherArray.append(temperature)
        except:
            print("Invalid temperature.Ignore the row")
    print(weatherArray)
    print(sum(weatherArray[0:7])/len(weatherArray[0:7]))
    print(max(weatherArray))
#The best data structure to use here was a list because all we wanted was access of temperature elements


    ## DICTIONARY WAY
with open("nyc_weather.csv",mode='r') as csv_reader:
    f = csv.reader(csv_reader)
    weatherDic = {}
    for line in f:
        print(line)
        day = line[0]
        try:
            temperature = int(line[1])
            weatherDic[day] = temperature
        except:
            print("Invalid temperature.Ignore the row")

    #imidiate access to the value
    print(weatherDic)
    print(weatherDic['9-Jan'])
    print(weatherDic['4-Jan'])

#The best data structure to use here was a dictionary (internally a hash table) because we wanted to know temperature for specific day, requiring key, value pair access where you can look up an element by day using O(1) complexity
word_count = {}
with open('poem.txt', 'r') as file:
    for line in file:
        tokens = line.split(" ")
        for token in tokens:
            token = token.replace('/n','')
            if token in word_count:
                word_count[token] += 1
            else:
                word_count[token] = 1

    print(word_count)
