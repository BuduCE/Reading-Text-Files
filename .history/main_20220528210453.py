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
    # text = None
    # [assignment] Add your code here
    try:
        d1 = dict()
        for line in text:
            words = line.split()
            for word in words:
                if word in d1:
                    d1[word] = d1[word] + 1
                else:
                    d1[word] = 1
        print(d1)
    except Exception as e:
        print("Errr")
    # return {"as": 10, "would": 20}
print(count_words())