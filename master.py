# Author: Perry

from function_file import new_data
from function_file import read_data
from user_input import gather_data

def master() -> None:
    while True:
        ans = input("Would you like to read or write data? ")
        if ans.lower() == "read":
            reports_by_year = read_data()
            gather_data()
            return None
        elif ans.lower() == "write":
            new_data()
            return None
        else:
            print("Invalid input.")