# -*- coding: utf-8 -*-
"""
Created on Sat May 15 20:02:17 2021

@author: Bravo
"""


def convertFahrtoCelsius(fahr_val):
    """
    Convert a temperature value in Fahrenheit to degree Celsius.
    
    returns a number to four decimal place
    returns an error message if the input isn't a number
    """
    try:
        fahr_val_type = type(fahr_val).__name__
        
        fahr_val = int(fahr_val)
        
        celsius_val = (fahr_val - 32) * (5/9)
        celsius_val = round(celsius_val, 4)
        
        return celsius_val
    except:
        return (fahr_val, 'is not a valid number but a/an', fahr_val_type)
    
print(convertFahrtoCelsius(0))



#%%

def checkYuGiOh(list_end):
    """
    Check and replace all multiples of 2,3,5.
    
    in a list with 'yu', 'gi', 'oh', respectively
    the list ranges from 1 to list_end
    """ 
    try:
        list_end = int(list_end)
        num_list = list(range(1 , list_end + 1))
        # print(num_list)
        
        num_list_clone = num_list[:]
        
        divisor_dict = {
            2: 'yu',
            3: 'gi',
            5: 'oh'
        }
        
        for num in num_list:
            for key in divisor_dict.keys():                
                if num % key == 0: # checks if the number is a multiple
                    num_index = num_list.index(num)
                    # print(num, ':', num_index)
                    
                    if type(num_list_clone[num_index]) == str: # if the number has already been switched with one out of the three words, add the next word to it instead of replacing it
                        # print(num_list_clone[num_index])
                        
                        another_suffix = '-' + divisor_dict[key]
                        num_list_clone[num_index] += another_suffix
                        
                        # print(num_list_clone[num_index])
                    
                    else:
                        num_list_clone[num_index] = divisor_dict[key]
        
        return num_list_clone
    
    except:
        return 'Invalid Parameter:', list_end
    
print(checkYuGiOh(10))