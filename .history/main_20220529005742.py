# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from fileinput import filename
from typing import Counter

##Alternative
# def read_file_content(filename):
#     # [assignment] Add your code here 
#     filename = 'story.txt'
#     with open(filename) as st:
#         return Counter(st.read().split())
    
# print(read_file_content(filename))

def read_file_content(filename):
    # [assignment] Add your code here 
    filename = 'story.txt'
    # with open(filename) as st:
    with open(filename, 'r') as st:
        st_content = st.read()
        st_content = st_content.split()
        # return Counter(st.read().split())
        return(st_content)
    return(read_file_content(filename))

def count_words():
    text = read_file_content(filename)
    # [assignment] Add your code here
    for line in text:
        return Counter(line) 
    # return {"as": 10, "would": 20}
print(count_words())