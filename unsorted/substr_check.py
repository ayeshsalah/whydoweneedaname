def check_substr(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    start_index = 0
    end_index = -1
    substr = []
    for index1, char1 in enumerate(str1):
#         print(char1)
        for char2 in str2[start_index:]:
            if char1 == char2:
                substr.append(char2)
                start_index = index1
            else:
                break      
    if len(substr) == len(str2):
        return "substring"
    else:
        return "not substring"


print(check_substr("ayesh", "yes"))
print(check_substr("ayesh", "123"))
print(check_substr("ayesh", "ysh"))