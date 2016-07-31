# Practice with palindromes
# Python 2.7
# J. Plasmeier | jplasmeier@gmail.com
# MIT License


def find_longest_palindromic_substring(string):
    longest = ''
    for index, char in enumerate(string):
        first = index
        second = index+1
        while(second < len(string) and string[first] == string[second]):
            first = first - 1
            second = second + 1
        candidate = string[first+1:second]
        if len(candidate) > len(longest):
            longest = candidate

        first = index
        second = index+2
        while(second < len(string) and string[first] == string[second]):
            first = first - 1
            second = second + 1
        candidate = string[first+1:second]
        if len(candidate) > len(longest):
            longest = candidate
    return longest

string = 'rgrgwtacocatat'
print find_longest_palindromic_substring(string)

