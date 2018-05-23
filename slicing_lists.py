#Write a function called get_sliced_lists which will take a list parameter and return the following lists which should be created using slices:

#A list including all but the last element
#A list including all but the first and last elements
#A reversed list (created using slicing)

def get_sliced_lists(a):
    first = []
    second = []
    third = []
    
    i = 0 
    b = len(a)-2
    while i <= b:
        first.append(a[i])
        i = i + 1
        
    i = 1
    while i <= b:
        second.append(a[i])
        i = i + 1
        
    i = (len(a))-1
    while i >= 0:
        third.append(a[i])
        i = i - 1
        
    lsts = first, second, third
    return lsts
