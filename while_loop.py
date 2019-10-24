#!/usr/bin/env python3

# Created by:Euel Yirga
# Created on:October 2019
# This program is a while loop



def main():
    # this function uses a while loop
    loop_counter = 1
    # input
    positive_integer = int(input("Enter amount of times to repeat: "))
    print("")

    # process & output
    while loop_counter < (positive_integer + 1):
        loop_counter = loop_counter + 1
        loop_sum = loop_counter * (loop_counter+1)/2

    print(loop_sum - loop_counter)
    
if __name__ == "__main__":
    main()