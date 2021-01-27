countter=0
    summ=0
    for i in range(len(priceOfJeans)):
        
        summ1=priceOfJeans[i]
        if summ<budgeted:
            for j in range(len(priceOfShoes)):
                summ2=summ1+priceOfShoes[j]
                if summ2<budgeted:
                    for k in range(len(priceOfSkirts)):
                        summ3=summ2+priceOfSkirts[k]
                        if summ3<budgeted:
                            for l in range(len(priceOfTops)):
                                if summ3+priceOfTops[l]<=budgeted:
                                    countter+=1
    return countter
    
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getNumberOfOptions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY priceOfJeans
#  2. INTEGER_ARRAY priceOfShoes
#  3. INTEGER_ARRAY priceOfSkirts
#  4. INTEGER_ARRAY priceOfTops
#  5. INTEGER budgeted
#

def getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted):
    
    print(len(priceOfJeans),len(priceOfShoes),len(priceOfSkirts),len(priceOfTops))
    max_jeans=max(priceOfJeans)
    max_shoes=max(priceOfShoes)
    max_skirts=max(priceOfSkirts)
    max_tops=max(priceOfTops)
    
    min_jeans=min(priceOfJeans)
    min_shoes=min(priceOfShoes)
    min_skirts=min(priceOfSkirts)
    min_tops=min(priceOfTops)
    
    sum_min=min_shoes+min_skirts+min_tops
    sum_max=max_shoes+max_skirts+max_tops
    # Write your code here
    dict1={}
    dict2={}
    for i in range(len(priceOfJeans)):
        if priceOfJeans[i]<=budgeted-sum_min:
            if priceOfJeans[i]<=budgeted-sum_max:
                if 0 not in dict1:
                    dict1[0]=0
                dict1[0]+=1
            else:    
                if priceOfJeans[i] not in dict1:
                    
                    dict1[priceOfJeans[i]]=0
                dict1[priceOfJeans[i]]+=1
    
    sum_min=min_skirts+min_tops
    for key in dict1:
        
        for i in range(len(priceOfShoes)):
            summ=key+priceOfShoes[i]
            if summ<=budgeted-sum_min:
                
                if summ not in dict2:
                    dict2[summ]=0
                dict2[summ]+=dict1[key]
    dict1={}
    sum_min=min_tops
    for key in dict2:
        
        for i in range(len(priceOfSkirts)):
            summ=key+priceOfSkirts[i]
            if summ<=budgeted-sum_min:
                if summ not in dict1:
                    dict1[summ]=0
                dict1[summ]+=dict2[key]
    dict2={}
    for key in dict1:
        
        for i in range(len(priceOfTops)):
            summ=key+priceOfTops[i]
            if summ<=budgeted:
                if summ not in dict2:
                    dict2[summ]=0
                dict2[summ]+=dict1[key]
    return sum(dict2.values())
    
        
        

    dict1={}
    dict1[0]=0
    max_jeans=max(priceOfJeans)
    max_shoes=max(priceOfShoes)
    max_skirts=max(priceOfSkirts)
    max_tops=max(priceOfTops)
    
    min_jeans=min(priceOfJeans)
    min_shoes=min(priceOfShoes)
    min_skirts=min(priceOfSkirts)
    min_tops=min(priceOfTops)
    sum_min=min_shoes+min_skirts+min_tops
    sum_max=max_shoes+max_skirts+max_tops
    
    for i in range(len(priceOfJeans)):
        if priceOfJeans[i]<=budgeted-sum_max:
            dict1[0]+=1
        else:
            dict1[priceOfJeans[i]]=1
    keys=dict1.keys()
    add_list=[]
    for a in keys:
        for i in range(len(priceOfShoes)):
            summ=priceOfShoes[i]+a
            add_list.append(summ)
    for summ in add_list:      
        if summ not in dict1:
            dict1[summ]=1
        else:
            dict1[summ]+=1
                
                
    keys=dict1.keys()
    add_list=[]
    for a in keys:
        for i in range(len(priceOfSkirts)):
            summ=priceOfSkirts[i]+a
            add_list.append(summ)
    for summ in add_list:      
        if summ not in dict1:
            dict1[summ]=1
        else:
            dict1[summ]+=1
            
            
    keys=dict1.keys()
    add_list=[]
    for a in keys:
        for i in range(len(priceOfTops)):
            summ=priceOfTops[i]+a
            add_list.append(summ)
    for summ in add_list:      
        if summ not in dict1:
            dict1[summ]=1
        else:
            dict1[summ]+=1
    return sum(dict1.values())          
if __name__ == '__main__':