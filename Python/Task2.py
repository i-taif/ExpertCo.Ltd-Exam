from datetime import datetime 
import re


def timeDifference(date1:str , date2:str) -> str:
    '''
    this func to calculate the amount of time between tow date,
    I use datetime library for date and abs() func to avoid negative values 
    '''
    dateTime1=datetime.strptime(date1,"%d/%m/%Y")
    dateTime2=datetime.strptime(date2,"%d/%m/%Y") 
    years= abs(dateTime2.year - dateTime1.year) 
    months= abs(dateTime2.month - dateTime1.month) 
    days= abs(dateTime2.day - dateTime1.day) 
    return f'{years} Years, {months} Months, {days} Days'
    
# print(timeDifference('22/2/1970','22/2/1980')) #output : 10 Years, 0 Months, 0 Days

try:
    datePattern = "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}" 
    input = input('Please Enter tow Dates: ') 
    dateTime = re.findall(datePattern, input) #return list contain date with dd/mm/yyyy formating
    if not dateTime: raise IOError('please follow the format dd/mm/yyyy')
    print(f'Output: {timeDifference(dateTime[1], dateTime[0])}')

except IOError as e:
    print(e)
except IndexError as e:
    print('you must enter two dates')



