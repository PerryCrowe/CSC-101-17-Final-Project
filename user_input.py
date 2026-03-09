from dataset import *
import sys

def gather_data ():
    user_input = []
    print("Would you like to compare two reports or look at one report?")
    ans = input("Please input 'One' or 'Two'")
    if ans.lower() == 'one':
        user_input.append(input("Enter Desired Year:"))
        user_input.append(input("Enter Statistic from list:"))
    return user_input

print(gather_data())