def divisible(num:int) -> str:
    '''
    this func to determine if a number is divisible by all its numbers 
    '''
    try :
           # I use sum() to check if summation the list is 0
        return 'Yes' if sum([num % int(i) for i in str(num)]) == 0 else 'No' 
    except: # for divided by Zero
        return 'No'
# print(divisible(130)) # output: No
number = int(input('Input: ')) 
print(f'Output: {divisible(number)}')