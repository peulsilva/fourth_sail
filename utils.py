def exists(char, array):
    for element in array:
        if element.char == char:
            element.addCounter()
            return True
    return False


def printArray(array):
    for element in array:
        print("Letter: "+ element.char+ " Count: ", element.count)