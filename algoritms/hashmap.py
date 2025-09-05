## BAD way
stock_prices = []
with open("stock_prices.csv","r") as f:
for line in f:
    tokens = line.split(',')
    day = tokens[0]
    price = float(tokens[1])
    stock_prices.append([day,price])

for element in stock_prices:
    if element[0] == 'march 9':
        print(element[1])

## DICTIONARY WAY
stock_prices = {}
for line in f:
    tokens = line.split(',')
    day = tokens[0]
    price = float(tokens[1])
    stock_prices.append[day] = price

#imidiate access to the value
stock_prices['march 9']


def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100 

get_hash('march') #68

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self,key,val):
        h = self.get_hash(key):
        self.arr[h] = val

    def __getitem__(self,key):
        h = self.get_hash(key):
        return self.arr[h]
    
    def add(self,key,val):
        h = self.get_hash(key):
        self.arr[h] = val


t = HashTable()
t.get_hash(9)