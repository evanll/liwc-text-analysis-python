# -*- coding: utf-8 -*-
"""
Written by Evan Lalopoulos <evan.lalopoulos.2017@my.bristol.ac.uk>
University of Bristol, May 2018
Copyright (C) - All Rights Reserved
"""

import os

from liwc import Liwc

# Replace with the path of a liwc (.dic) file
LIWC_FILEPATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'LIWC2007_English.dic'))

if __name__ == "__main__":
    liwc = Liwc(LIWC_FILEPATH)

    print(liwc.search('happy'))
    print(liwc.parse('I love ice cream.'.split(' ')))



