def printgreen(text):
    print(f"\033[92m{text}\033[0m")
def printred(text):
    print(f"\033[91m{text}\033[0m")
def printyellow(text):
    print(f"\033[93m{text}\033[0m")
def printblue(text):
    print(f"\033[94m{text}\033[0m")

def textgreen(text):
    return f"\033[92m{text}\033[0m"
def textred(text):
    return f"\033[91m{text}\033[0m"
def textyellow(text):
    return f"\033[93m{text}\033[0m"
def textblue(text):
    return f"\033[94m{text}\033[0m"

if __name__ == "__main__":
    printgreen("This is green text.")
    printred("This is red text.")
    printyellow("This is yellow text.")
    printblue("This is blue text.")