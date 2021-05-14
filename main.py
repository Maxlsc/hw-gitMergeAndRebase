# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2021 zhangt2333. All Rights Reserved.
# Author-Github: github.com/zhangt2333

import sys
import requests
import re
import os
from bs4 import BeautifulSoup

username = os.environ["USERNAME"]
hw_index = int(re.findall(r'homework([0-9]+)', os.environ["ISSUE_TITLE"])[0])

def hw1():
    s = ""
    sys.exit(0 if '1+1=2' in s else -1)


def hw2():
    s = ""
    sys.exit(0 if '1+1=2' in s and '1+2=3' in s and '1+3=4' in s else -1)


def hw3():
    s = ""
    sys.exit(0 if '1+1=2' in s and '1+2=3' in s and '1+3=4' in s else -1)


def hw4():
    s = ""
    sys.exit(0 if '1+1=2' in s and '1+2=3' in s and '1+3=4' in s else -1)


methods = [hw1, hw2, hw3, hw4]
if __name__ == '__main__':
    methods[hw_index - 1]()