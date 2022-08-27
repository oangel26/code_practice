#!/usr/bin/env python3
"""
Group Anagrams
"""
def group_anagrams(list):
    """
    Metodo que retorna grupacion de anagramas
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    def check_anagram(str1, str2):
        """ checks if two strings are anagrams """
        for i in str1:
            if i in str2:
                anagram = True
            else:
                anagram = False
                break
        return anagram

    
    for i, word in enumerate(list):
        swich = 1
        if i == 0:
            ana_groups =[[word]]
        else:
            for group in ana_groups:
                if check_anagram(group[0], word):
                    group.append(word)
                    swich = 0
                    break
            if swich == 1:
                ana_groups.append([word])

    return ana_groups



if __name__ == "__main__":
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    strs2 = [""]
    strs3 = ["a"]

    print(group_anagrams(strs1))
    print(group_anagrams(strs2))
    print(group_anagrams(strs3))
