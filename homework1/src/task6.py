'''
Arguments: A file
Reads a given file and counts the amount of words.
Return: Returns the total amount of words in the file.
'''
def read_file(file):
    # Opens a file as read and closes file at the end
    with open(file, mode='r') as f:
        counter = 0
        # Each line in the file
        for line in f:           
            # Each word in the line
            for w in line.split():   
                # Only counts read words, not punctuation.
                if w != ',' and w != '.':
                    counter += 1

    return counter