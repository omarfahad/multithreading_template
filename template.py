import os, requests, time
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
import threading
import sys
from colorama import Fore, Style
import json


bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
res = Style.RESET_ALL
yl = Fore.YELLOW

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}


def filter(nn):
    try:
      print("this function will run")
      # code here vmro :}
    except:
       pass


def main():
    print(f'''    
    
    
    your tool banner here
                                                                    
 
    ''')
    list = input(f"{gr}Give Me Your List.txt > {gr}{res} ")
    star = open(list, 'r').readlines()
    try:
       ThreadPool = Pool(500)
       ThreadPool.map(filter, star)
       ThreadPool.close()
       ThreadPool.join()
    except:
       pass
       
if __name__ == '__main__':
    main()
