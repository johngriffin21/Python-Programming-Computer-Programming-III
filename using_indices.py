#Write a function called get_counts which will take as a parameter a list of words and return a list of integers which will be a count of the lengths of those words. No word will have more than 9 letters.
def get_counts(lst):
    i = 0
    j = 0
    nlst = [0 ,0, 0, 0, 0, 0 ,0 ,0 ,0 ,0]
    while i < len(lst):
        t = 0
        while t <= 9:
           if len(lst[i]) == t:
              nlst[t] += 1 
           t = t + 1 
        i = i + 1
    
    return nlst
