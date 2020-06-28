"""
    This example using DontStealMyCode as a python deletes the original code and only keep the encrypted one

    In this way, you have only encrypted codes you can decrypt when you want to use them via another program we can write ...
"""

from dontstealmycode.dsmc import Code
import os

code_file = str(input("[INPUT] Path to the code file to encrypt : "))
first_factor = input("[INPUT] Password First Factor : ")
second_factor = input("[INPUT] Password Second Factor : ")
output = input("[INPUT] Path then name of the Output encrypted file to be created : ")

myCodeObject = Code(code_file, first_factor, second_factor)
myCodeObject.encrypt(output)
deletion_command = "rm " + code_file
os.system(deletion_command)

