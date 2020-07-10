# https://docs.python.org/3/tutorial/floatingpoint.htmlhttps://docs.python.org/3/tutorial/floatingpoint.html
for i in range(0, 10, 1):
    for j in range(0, 10, 1):
        if(((i/10 + j/10) * 10) != int((i/10 + j/10)*10)):
            print(str(i/10) + "+" + str(j/10) + "=" + str(i/10 + j/10))
print("Above is a list of additions 0.1 through 1 which will result in the issue.")
print("It seems to always result from interactions with .1, .2, and .3 because these numbers are not perfectly represented by the binary number system.")
