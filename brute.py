#!/usr/bin/python3

import multiprocessing
import requests
import time
import sys
from multiprocessing.dummy import Pool as ThreadPool 

def argument_check():
    if(len(sys.argv) != 2):
        print("Please enter a domain to check")
        exit(1)
    else:
        return sys.argv[1]

def sub_checker(sub,domain):
    url = "https://" + sub + domain
    #sleep for variable amount if connection refused
    try:
        r = requests.head(url)
    except requests.exceptions.RequestException as e:
        return

    if(r.status_code != 404):
        print(url,end=" ")
        print(r.status_code)
        return

if __name__ == "__main__":

    domain = argument_check()
    domain = "." + domain

    letters = 'abcdefghijklmnopqrstuvwxyz'
    words_list = []
    
    #create a words list to test out
    #only goes up to 5 letter words 
    for length in range (5):
        a = [i for i in letters]
        for y in range(length):
            a = [x+i for i in letters for x in a]
        words_list = words_list + a

    for word in words_list:
        sub_checker(word,domain)
