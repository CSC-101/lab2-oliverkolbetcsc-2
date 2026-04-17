from typing import Optional


def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # What is the value of test on each call? test = False on the first call, test = True on the second call
    if test:                            # What is this check preventing? This check prevents trying to access an index out of range of L.
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # What is the value of first? None
second = checked_access([1, 0, 1], 2)    # What is the value of second? 1
print()