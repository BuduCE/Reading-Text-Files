# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from fileinput import filename


def read_file_content(filename):
    # [assignment] Add your code here 
    filename = 'story.txt'
    with open(filename, 'r') as rstory:
        rstory_content = rstory.read()
        print(rstory_content)
    
    # return "Hello World"

#Initiate the function
print(read_file_content('filename'))

def count_words():
    text = read_file_content(filename)
    dl = dict()
    # "./story.txt"
    # [assignment] Add your code here
    for line in text:
        words = line.split()
        for word in words:
            if word in dl:
                dl[word] = dl[word] + 1
            else:
                dl[word] = dl[word] = 1
            prin
    # return {"as": 10, "would": 20}
print(count_words())