# read sums.txt
with open("sums.txt", "r") as file:
    for line in file:
        nums = line.split()
        num1 = int(nums[0])
        num2 = int(nums[1])
        print(num1 + num2)
