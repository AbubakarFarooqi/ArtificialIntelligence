def edit_distance_recursive(str1, str2, memo={}):
    if (str1, str2) in memo:
        return memo[(str1, str2)]

    if len(str1) == 0:
        result = len(str2)
    elif len(str2) == 0:
        result = len(str1)
    elif str1[-1] == str2[-1]:
        result = edit_distance_recursive(str1[:-1], str2[:-1], memo)
    else:
        insertion = edit_distance_recursive(str1, str2[:-1], memo) + 1
        deletion = edit_distance_recursive(str1[:-1], str2, memo) + 1
        substitution = edit_distance_recursive(str1[:-1], str2[:-1], memo) + 1
        result = min(insertion, deletion, substitution)

    memo[(str1, str2)] = result
    return result

print(edit_distance_recursive("kitten","sitten"))