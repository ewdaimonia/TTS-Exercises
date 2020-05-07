# Python Basics Practice assignment 5
# By Gabriel Smith

for i in range(1, 11, 1):
    for j in range(1, 11, 1):
        print(str(j*i).rjust(4), end=" ")
    print()
