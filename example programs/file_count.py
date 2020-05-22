# This exercise 6 can give two points at maximum!
# Part 1.
# Create a function file_count that gets a filename as parameter and returns a triple of numbers.
# The function should read the file, count the number of lines, words, and characters in the file,
# and return a triple with these count in this order. You get division into words by splitting at whitespace.
#  You don't have to remove punctuation.
# Part 2.
# Create a main function that in a loop calls file_count using each filename in the list of
# command line parameters sys.argv[1:] as a parameter, in turn. For call python3 src/file_count file1 file2 ... the output should be
# ?      ?       ?       file1
# ?      ?       ?       file2
# ...
# The fields are separated by tabs (\t). The fields are in order: linecount, wordcount, charactercount, filename.
import sys
import os


def file_count(preFile, index):
    # print(preFile)
    file = open(os.path.join(sys.path[0], str(preFile)), "r")
    #print(os.path.join(sys.path[0], str(preFile[0])))
    data = file.read()
    lineFile = data.split("\n")
    count = 0
    for i in lineFile:
        if i:
            count += 1
    result = (str(count), "\t", str(len(data.split())),
              "\t", str(len(data)), "\t", str(preFile)[:-3])
    file.close()
    return result


def main(*args):
    #    print(args)
    for i, value in enumerate(args[0]):
        print(''.join(file_count(value, i)))


if __name__ == "__main__":
    main(sys.argv[1:])
