# Python Basics Practice assignment 1
# By Gabriel Smith


def reverse(word):
    newWord = ''
    for i in range(len(word), 0, -1):
        newWord += word[i-1]
    return newWord


name = input('Please enter your first and last name separated by a space: ')
if(' ' in name):
    name = name.split(' ', 2)
    print(reverse(name[0]) + ' ' + reverse(name[1]))
else:
    print("That's not the proper format, goodbye")
