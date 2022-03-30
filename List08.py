def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    index=0
    if list1[index] == 1:
        list1[index] = True
    else:
        list1[index] = False
    index+=1

    if list1[index] == 1:
        list1[index] = True
    else:
        list1[index] = False
    index+=1

    if list1[index] == 1:
        list1[index] = True
    else:
        list1[index] = False
    index+=1

    if list1[index] == 1:
        list1[index] = True
    else:
        list1[index] = False
    index+=1

    if list1[index] == 1:
        list1[index] = True
    else:
        list1[index] = False
    index+=1
    return list1