try:
    first = int(input())
    second = int(input())
    if first > second:
        print("The first one wins")
    elif second > first:
        print("The second one wins")
    else:
        print("Draw")
except ValueError:
    print("Please enter 2 integers.")
