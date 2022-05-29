import random
def RandomFloatNumberAsString(low, high):
    return random.uniform(low,high)

def RandomIntegerAsString(low, high):
    return random.randint(low,high)

def RandomAlphaNumericString(len):
    for i in range(0, len):
        clientID_prefix = clientID_prefix + str(random.randint(0, 99999))
        return len