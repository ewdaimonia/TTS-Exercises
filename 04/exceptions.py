tests = int(input())
for i in range(0, tests, 1):
    nums = input()
    nums.split(" ")
    try:
        result = int(nums[0]) / int(nums[2])
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)
    else:
        print(int(result))
