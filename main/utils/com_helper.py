import string, random

def getRandomNo(keylength=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=keylength))
