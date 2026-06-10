from typing import List

def contains_duplicate(words: List[str]) -> bool:
    len1 = len(words)
    my_set = set(words)
    len2 = len(my_set)
    if(len1 == len2):
        return False
    else:
        return True
            


# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
