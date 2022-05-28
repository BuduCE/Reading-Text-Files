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
    
print(read_file_content('filename'))

# def count_words():
#     text = read_file_content
#     # ("story.txt")
#     # [assignment] Add your code here
#     count = 0
#     for a in text:
#         count = count+1
#     print(count)
#     # return {"as": 10, "would": 20}
# print(count_words())