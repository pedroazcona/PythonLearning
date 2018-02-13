# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 11:38:17 2018

@author: poaa
"""
import logging
import mylib

def main():
    logging.basicConfig(filename=r'C:\Users\poaa\Documents\Python Scripts\Learning2\log\example.log',filemode='w', level=logging.INFO, format='%(asctime)s : %(levelname)s :%(message)s', datefmt='%m/%d/%Y %H:%M:%S')

    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()
