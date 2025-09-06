## BAD way
"""
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
"""

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
    
    #this override allow us to set the value for index t["march 7"] = 420
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    #this override allow us to get the value for index has t["dec 30"]
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None        


t = HashTable()
t.get_hash(9)
t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t.arr
t["dec 30"] = 88
t["dec 30"]
del t["march 6"]
t.arr