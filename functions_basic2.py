# #countdown-Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(input):
    num=[]
    for x in range(input,-1,-1):
        num.append(x)
    return num
print(countdown(10))

# #print and return-Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return():
    x=[1,2,3,4,5]
    print(x[0])
    return(x[1])
print(print_and_return())

# #First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first_plus_length():
    x=[1,2,3,4,5]
    return(x[0]+len(x))
print(first_plus_length())

#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are 
# greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def greather_than(arr):
    arrToReturn=[]
    for num in arr:
        if num > arr[1]:
            arrToReturn.append(num)
    return arrToReturn
print(greather_than([5,2,1,9,6]))

#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a 
# list whose length is equal to the given size, and whose values are all the given value.
def length_and_value(a,b):
    num=a*str(b)
    return num
print(length_and_value(4,7))
print(length_and_value(6,2))