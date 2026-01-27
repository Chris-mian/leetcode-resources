from typing import Any

def binary_search(lst: list[tuple[int, Any]], key: int) -> Any:
    l = 0
    r = len(lst)
    while (r > l):
        m = (r+l) // 2
        curKey = lst[m][0]
        if curKey == key:
            return lst[m][1]
        elif curKey < key:
            l = m + 1
        else:
            r = m 
    return None
    
    
TEST_LIST_1 = [(2*i+3, i+5) for i in range(100)]
assert(binary_search(TEST_LIST_1, 22) == None)
assert(binary_search(TEST_LIST_1, 23) == 15)
print("SUßß")