# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])#k should be key

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": 'd\'oh!', # needed an escape character for the inside quote mark 
                         "maggie": "(Pacifier Suck)"
                         }

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer']) # each key had to be placed in single array

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

