# you can use this to sort strings too
def bubble_sort(elements, key):
    size = len(elements)

    for i in range(size-1):
        swapped = False

        for j in range(size-1-i):
            print("init",elements[j][key],j, elements[j+1][key],j+1)
            if elements[j][key] > elements[j+1][key]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                print("swapped",elements[j],j, elements[j+1],j+1)
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    elements1 = [1,2,3,4,2]
    elements2 = ["mona", "dhaval", "aamir", "tina", "chang"]
    elementsE = [
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    ]

    bubble_sort(elementsE, "name")
    print(elementsE)
    #print(elementsE[2]['transaction_amount'])