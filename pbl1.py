def split_lr():
    x = input()
    result = []
    countR = 0 
    countL = 0  
    LR = ""

# RRRLLLRRRLLL
# 3, 3, 
# [RRRLLL, RRRLLL]

    for i in x:
        if i == 'R':
            countR = countR + 1
        else:
            countL = countL + 1
        
        LR += i       
        if countR == countL:
            result.append(LR)
            LR = ""
            countL = 0
            countR = 0
    return result

how_many_child_do_you_have = split_lr()

print(len(how_many_child_do_you_have))
for LR in how_many_child_do_you_have:
    print(LR)
