# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word):
    anagram = {}
    for x in word:
        if x in anagram:
            anagram[x] += 1
        else:
            anagram[x] = 1
    return anagram

a_word ='elvis'
b_word ='lives'
if (len(a_word) != len(b_word)):
    print('false')
else:
    if (find_anagram(a_word) == find_anagram(b_word)):
        print('True')
    else:
        print('False')
    # [assignment] Add your code here

    #return True
