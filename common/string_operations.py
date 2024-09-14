#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    string_operations.py 
   Description :
   Author : chenqiyue
   CreateDate：2023/12/07  用例id:
-------------------------------------------------
"""
def has_invalid_values(input_str):
    fields = input_str.split('\n')
    for field in fields:
        key_value = field.split('=')
        if len(key_value) == 2:
            _, value = key_value
            if value in ["null", ""]:
                return True
    return False
