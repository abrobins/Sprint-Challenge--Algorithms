'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    if len(word) < 2:
        return 0
    # check for 'th' at beginning of word increment count and run fun again
    if word[0:2] == 'th':
        return 1 + count_th(word[2:])
    # otherwise run function and count 'th' from position 1 on
    else:
        return count_th(word[1:])
    # TBC


# print(count_th('this is the man that throws the thimble'))
