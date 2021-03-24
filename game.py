block = []

def findBlock(list, target):
    length=len(list)
    sum = 0
    for i in range(length):
        print(block)
        print("sum:", sum)
        sum+=list[i]
        block.append(list[i])
        if sum>target:
            condition1=abs(target-(sum-block[0]))
            condition2=abs(target-(sum-list[i]))
            print(condition1, condition2)
            if condition1<condition2:
                print("condition1", block[0])
                del block[0]
            else:
                print("condition2", block[i])
                del block[i]
    return block

print(findBlock([1,2,3,4,5,6,7], 5))