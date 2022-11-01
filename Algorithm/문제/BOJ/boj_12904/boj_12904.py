import sys
sys.stdin = open("input.txt", "r")

start_word = input()
end_word = input()

is_answer = 0
def make_word(word):
    global start_word, is_answer
    if len(word) == len(start_word):
        if word == start_word:
            is_answer =1
        return
    else:
        if word.endswith("A"):
            make_word(word[:-1])
        else:
            make_word(word[:-1][::-1])

make_word(end_word)
print(is_answer)