# Imagine we have a long list of codewords and each codeword triggers a specific function to be called.
# For example, the codeword 'go' which calls the function handleGo, and 
# another codeword 'ok' which calls the function handleOk.
# We can use a dictionary to encode this.

def handleGo(x):
    return "Handling a go! " + x


def handleOk(x):
    return "Handling an ok! " + x


# Dictionary that pairs STRINGS (codewords) to FUNCTIONS.       
codewords = { 
  'go': handleGo,   # The KEY here is 'go' and the VALUE it maps to is handleGo (Which is a function!).
  'ok': handleOk,   
}

# Now, we see a codeword given to us:
codeword = "go"

# We can handle it as follows:
if codeword in codewords:
        answer = codewords[codeword]("Argument")
        print(answer)
else:
        print("I don't know that codeword.")
