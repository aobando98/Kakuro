'''
Python class to get the solution of a kakuro puzzle
'''

def posCombinations(spaces):
    result = 1
    currentMultiplier = 9

    for x in range(0, spaces):
        result = result * currentMultiplier
        currentMultiplier -= 1

    return result

'''
Numbers: must be [1,2,3,4,5,6,7,8,9]
Target: The desired sum we want to reach
finalResult: must start as []
'''
def subset_sum(numbers, target, partial, finalResult, allowedSpaces):
    # We have to make sure we don't use the target number
    if target in numbers:
        numbers.remove(target)
    
    # We check the amount of numbers we have used isn't out of range
    if len(partial) <= allowedSpaces:
        
        s = sum(partial)

        # check if the partial sum is equals to target and uses the right amount of numbers
        if s == target and len(partial) == allowedSpaces:
            # We add the partial result to the final result
            finalResult.append(partial)
            
        if s >= target:
            return # if we reach the number we stop

        for i in range(len(numbers)):
            n = numbers[i]
            remaining = numbers[i+1:]
            subset_sum(remaining, target, partial + [n], finalResult, allowedSpaces)

        return finalResult


        

