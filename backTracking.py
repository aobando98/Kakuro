'''
Python class to get the solution of a kakuro puzzle
'''

###############################################################
'''
Function to get the posible combinations using x given spaces
'''
def posCombinations(spaces):
    result = 1
    currentMultiplier = 9

    for x in range(0, spaces):
        result = result * currentMultiplier
        currentMultiplier -= 1

    return result
###############################################################

'''
Function to get the minimum number using x given spaces
spaces: amount of spaces to be used
'''
def minNumber(spaces):
    result = 0
    for x in range(1, spaces + 1):
        result += x
    return result
###############################################################

'''
Function to get the maximum number using x given spaces
spaces: amount of spaces to be used 
'''
def maxNumber(spaces):
    result = 0
    for x in range(10 - spaces, 10):
        result += x
    return result
###############################################################

'''
Function to check if a number is in a given vector
number: number to check if it's in the vector
vector: vector we want to check the presence of the number
'''
def checkPresence(number, vector):
    if number in vector:
        return True
    else:
        return False
###############################################################

'''
Function to get the valid(s) vectors that sum up a given number
numbers: must be [1,2,3,4,5,6,7,8,9]
target: The desired sum we want to reach
allowedSpaces: the amount of numbers you can use to reach the desired number
finalResult: must start as []
partial: must start as []
'''
def subset_sum(numbers, target, allowedSpaces, finalResult, partial):
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
            subset_sum(remaining, target, allowedSpaces, finalResult, partial + [n])

        return finalResult
#################################################################################################

'''
Function to check if a vectors numbers are in another vector
vector_1: the vector we want to check if the numbers are in vector_2, must be a list
vector_2: where we check if the number are in
returns: True if we can delete the given vector, False if we can't
'''
def checkPosRemove(vector_1, vector_2):
    print(vector_1, vector_2)
    for x in range(0, len(vector_1)):
        if vector_1[x] in vector_2:
            return False
    return True
###############################################################

'''
Function to delete certain elements from a vector
returns: the vector with the desired indexes deleted
'''
def removeVector(indexes, vector):
    indexCorrector = 0
    for x in range(0, len(indexes)):
        del vector[x - indexCorrector]
        indexCorrector += 1
    return vector
###############################################################

'''
Function to delete posible uses of vectors
returns: Both vectors without the comb. of numbers they can't use
'''
def removePosSolutionPre(vector_1, vector_2):
    if len(vector_1) == 1 and len(vector_2) > 1:

        indexCorrector = 0
        for index in range(0, len(vector_2)):
            if checkPosRemove(vector_2[index - indexCorrector], vector_1[0]):
                del vector_2[index - indexCorrector]
                indexCorrector += 1
        return [vector_1, vector_2]

    elif len(vector_2) == 1 and len(vector_1) > 1:

        indexCorrector = 0
        for index in range(0, len(vector_1)):
            if checkPosRemove(vector_1[index - indexCorrector], vector_2[0]):
                del vector_1[index - indexCorrector]
                indexCorrector += 1
        return [vector_1, vector_2]
###############################################################################
                
            
        
    

