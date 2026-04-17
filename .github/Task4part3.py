def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # What is the value of words at this point? ["this","is","confusing","code","AVOID","SUCH."]
         # What are the values of first and second at this point? ["this","is","confusing","code","AVOID","SUCH."]
         # What happened? Since surprising returns L, which is always words, both and first and second become bound to the list words, and as words (or L) is changed, both lists change with it.
print()