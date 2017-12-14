#opt3 Jack Wu
def groupSum( start, list1, target):
    if  target == 0:
        return True
    if start == len(list1):
        return False
    return groupSum(start+1, list1, target= target- list1[start]) or groupSum(start+1, list1, target)
