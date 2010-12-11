# file: util.py
# -*- coding: utf-8 -*-
import uuid
import md5

def convert_e2b(number):
    n = str(number)
    bengali_number = u''
    for char in n:
        if char == '0':
            bengali_number = bengali_number + u'০'
        elif char == '1':
            bengali_number = bengali_number + u'১'
        elif char == '2':
            bengali_number = bengali_number + u'২'
        elif char == '3':
            bengali_number = bengali_number + u'৩'
        elif char == '4':
            bengali_number = bengali_number + u'৪'
        elif char == '5':
            bengali_number = bengali_number + u'৫'
        elif char == '6':
            bengali_number = bengali_number + u'৬'
        elif char == '7':
            bengali_number = bengali_number + u'৭'
        elif char == '8':
            bengali_number = bengali_number + u'৮'
        elif char == '9':
            bengali_number = bengali_number + u'৯'
        elif char == '.':
            bengali_number = bengali_number + u'.'   
    return bengali_number

def get_uuid():
    return md5.new(str(uuid.uuid1())).hexdigest()