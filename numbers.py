#Write a function called get_odd_list which returns a list of odd numbers. The function should read numbers from standard input until one of the numbers is -1. The function should only add odd numbers to the list. Put your function in a file called numbers.py.
def get_odd_list():
    odds = []
    num = int(input()) 
    while num != -1:
        if num % 2 != 0:
           odds.append(num)
        num = int(input())
    return odds
    
    

