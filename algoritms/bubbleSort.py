# you can use this to sort strings too
def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        print("init")
        for j in range(size-1-i):
            print("init",elements[j],j, elements[j+1],j+1)
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                print("swapped",elements[j],j, elements[j+1],j+1)
                swapped = True
        print("finish")
        if not swapped:
            break


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    elements1 = [1,2,3,4,2]
    elements2 = ["mona", "dhaval", "aamir", "tina", "chang"]

    bubble_sort(elements)
    print(elements)