import itertools


def findsubsets(n, k):
    return list(itertools.combinations(range(n), k))

def switch_string(str, positions):
    s = list(str)
    for i in positions:
        if s[i] == "0":
            s[i] = "1"
        else:
            s[i] = "0"
    return "".join(s)

def count_difference(str1, str2):
    s1 = list(str1)
    s2 = list(str2)
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count

def kmistakes(s, k):
    n = len(s)
    mistakes_positions = findsubsets(n, k)
    all_strings =[]
    for position in mistakes_positions:
        all_strings.append(switch_string(s, position))
    return all_strings

def find_matches(string, k):
    string_mistakes = kmistakes(string, k)
    s = string_mistakes[0]
    possible_strings = kmistakes(s, k)
    string_to_loop = possible_strings.copy()
    for string_i in string_to_loop:
        b = True
        for string_j in string_mistakes:
            if count_difference(string_i, string_j) != k:
                b = False
        if b == False:
            possible_strings.remove(string_i)

    return string_mistakes, string_to_loop

def imo(n, k):
    vec = n*["0"]
    s = "".join(vec)
    return n, k, find_matches(s, k)

for n in range(1, 5):
    for k in range(n):
        print(imo(n, k))