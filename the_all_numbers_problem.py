#Write a function which will read the input until terminated by -1 and create two lists, one to hold the odd numbers and one to hold the even numbers. The function should return both these lists as a tuple, the odd list followed by the even list.
def get_evenodd_list():
    odds = []
    evens = []
    num = int(input()) 
    while num != -1:
        if num % 2 != 0:
            odds.append(num)
        elif num % 2 == 0:
            evens.append(num)
        num = int(input())
        
    both = odds, evens    
    return both
