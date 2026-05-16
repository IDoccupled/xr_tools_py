def textgreen(text: any)-> str:
    return f"\033[92m{text}\033[0m"

def textred(text: any)-> str:
    return f"\033[91m{text}\033[0m"

def textyellow(text: any)-> str:
    return f"\033[93m{text}\033[0m"

def textblue(text: any)-> str:
    return f"\033[94m{text}\033[0m"

def printgreen(text: any):
    print(textgreen(text))

def printred(text: any):
    print(textred(text))

def printyellow(text: any):
    print(textyellow(text))

def printblue(text: any):
    print(textblue(text))

if __name__ == "__main__":
    import numpy as np
    printgreen(np.array([[1, 2], [3, 4]]))
    printgreen("This is green text.")
    printred("This is red text.")
    printyellow("This is yellow text.")
    printblue("This is blue text.")