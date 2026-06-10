def concatenate(s1: str, s2: str) -> str:
    newstr = s1 + s2
    i = len(newstr)
    if (i>10):
        return ("Too long!")
    else:
        return(newstr)    





# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
