def breakPalindrome(palindrome):
    def checkPalindrome(word):
        half_word_length = len(word) // 2
        if len(word) % 2 == 0:
            if word[0:half_word_length] == word[half_word_length:][::-1]:
                return True
        else:
            if word[0:half_word_length] == word[half_word_length + 1:][::-1]:
                return True
        return False

    for i in range(len(palindrome)):
        alpa_num = ord(palindrome[i])
        while alpa_num > 97:
            alpa_num -= 1
            alpa = chr(alpa_num)
            new_palindrome = ""
            for j in range(len(palindrome)):
                if j == i:
                    new_palindrome += alpa
                else:
                    new_palindrome += palindrome[j]
            if checkPalindrome(new_palindrome):
                return new_palindrome
    for i in range(len(palindrome) - 1, -1, -1):
        alpa_num = 96
        while alpa_num < 122:
            alpa_num += 1
            alpa = chr(alpa_num)
            new_palindrome = ""
            for j in range(len(palindrome)):
                if j == i:
                    new_palindrome += alpa
                else:
                    new_palindrome += palindrome[j]
            if checkPalindrome(new_palindrome) == False:
                return new_palindrome

    return ""
