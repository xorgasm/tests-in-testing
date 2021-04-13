# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 23:18:11 2021

@author: corey
"""
from random import randint
def repeats_positive_negative_mean(m,n):
    def positive_negative(x):
        ret=[]
        for i in range(1,x+1):
            ret.append(randint(-i,i))
        return ret
    vet=[]
    ratio_n_to_unique=[]
    for P in range(m):#test m times
        test=positive_negative(n)
        vet.append(len({element for element in test if -1*element in test and test.count(element)>1 }))
        ratio_n_to_unique.append(float(len(set(test)))/n)
    meanposneg=0
    meanset=0
    for i in vet:
        meanposneg +=i
    print("average probability of positive and negative appearing when there are repeats =", round(float(meanposneg/len(vet)),2))    
    for i in ratio_n_to_unique:
        meanset+=i
    print("average percentage of unique elements=",round(float(meanset)/len(ratio_n_to_unique),2))

def test_of_randomness(n):
    ret=[] 
    for x in range(1,n+1):
         ret.append(randint(-x,x))
    mean=0
    for x in ret:
        mean+=x
    mean=round(float(mean)/n,2)
    return mean

    
        
         
         