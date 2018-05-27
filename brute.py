#!/usr/bin/python3

import requests
import time


def sub_checker(sub):
    url = "https://" + sub + domain
    #sleep for variable amount if connection refused
    timeout = 1
    r = ''
    while r == '':
        try:
            r = requests.get(url)
            break
        except:
            time.sleep(timeout)
            timeout = timeout + 1
            continue
        if(r.status_code != 404):
            print(url,end=" ")
            print(r.status_code)
            return


if __name__ == "__main__":
    domain = ".ns.agency"

    letters = 'abcdefghijklmnopqrstuvwxyz'
    words_list = []
    
    #create a words list to test out
    #only goes up to 5 letter words 
    for length in range (5):
        a = [i for i in letters]
        for y in range(length):
            a = [x+i for i in letters for x in a]
        words_list = words_list + a


    #actually test domain
    for word in words_list:
        sub_checker(word)
