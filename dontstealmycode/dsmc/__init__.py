# coding: utf-8

from os import system
import argparse

parser = argparse.ArgumentParser(description="[DontStealMyCode (DSMC) - console & web code encrypter & decrypter]"
                                             "Encrypts and Decrypts code via the command line interface or on the Heroku server."
                                             "Can also be used as a module in python to perform some encryption-decryption tasks."
                                             "Developed in one day by Nongma SORGHO in the MacroHacks Hackathon!")

parser.add_argument("-e", metavar="e", help="[HELP] Use this option to encrypt a code, set its value to 1 to do that", default=0)
parser.add_argument("-d", metavar="d", help="[HELP] Use this option to decrypt an encrypted code, set its value to  to do that", default=0)

parser.add_argument("-c", metavar="c", help="[HELP] Relative or Absolute path to the Code you want to encrypt or of the encrypted code you want to decrypt")
parser.add_argument("--f1", metavar="f1", help="[HELP] First factor of your code, this can be a number, a string, a text, whatever you want, essential is to remind it because you will need it to decrypt your code when need")
parser.add_argument("--f2", metavar="f2", help="[HELP] Second factor of your code, this can be a number, a string, a text, whatever you want, essential is to remind it because you will need it to decrypt your code when need")
parser.add_argument("-o", metavar="o", help="[HELP] Relative or Absolute path of the output of you command", default="dsmc.txt")

args = parser.parse_args()

class Code():
    def __init__(self, code_file, first_factor, second_factor):
        """
        :param code_file: the file which contains the code to encrypt
        """
        print("[DontStealMyCode (DSMC) - console & web code encrypter & decrypter]")
        self.__code_file = code_file
        first_factor, second_factor = str(first_factor), str(second_factor)
        self.__code_key = (int(ord(first_factor)) if len(first_factor) == 1 else int(sum(ord(i) for i in first_factor)), int(ord(second_factor)) if len(second_factor) == 1 else int(sum(ord(j) for j in second_factor)))
        with open(self.__code_file) as code_file_loaded:
            try:
                self.__code = code_file_loaded.readlines()
                self.__entire_code = code_file_loaded.read()
                print("[INFO] Code Object initialized")
            except:
                print("[ERROR] File error")


    def encrypt(self, output="encrypted_code.txt"):
        encrypted_code = ""
        crypting_math_function = self.__code_key[0]
        for line in self.__code:
            line = line.replace("\r\n", "🧑🏻🧑🏻‍💼指‍")
            line = line.replace("\t", "会")
            line = line.replace(" ", "字")
            line = line.replace("'", "上")
            for x in range(len(line)):

                if line[x] != "指" and line[x] != "会" and line[x] != "字" and 97<=ord(line[x])<=122:
                    crypting_math_function += self.__code_key[1]
                    try:
                        encrypted_code += chr((ord(line[x]) + crypting_math_function)%26 + 97)
                    except:
                        print("[ERROR] An Unknown error occured while processing")
                        break
                elif line[x] != "指" and line[x] != "会" and line[x] != "字" and 65<=ord(line[x])<=90:
                    try:
                        encrypted_code += chr((ord(line[x]) + crypting_math_function) % 26 + 65)
                    except:
                        print("[ERROR] An Unknown error occured while processing")
                        break

                else:
                    encrypted_code += line[x]
        encrypted_code = encrypted_code.replace("\n", "下")
        command = "echo '" + encrypted_code + "' > " + output
        system(command)
        print("[INFO] Process Ended Correctly")

    def decrypt(self, output="decrypted_code.txt"):
        decrypted_code = ""
        decrypting_math_function = self.__code_key[0]
        for line in self.__code:
            line = line.replace("下", "\n")
            for x in range(len(line)):

                if line[x] != "指" and line[x] != "会" and line[x] != "字" and 97<=ord(line[x])<=122:
                    decrypting_math_function += self.__code_key[1]
                    try:

                        decrypted_code += chr((ord(line[x]) - decrypting_math_function + 14)%26 + 97)
                    except:
                        print("[ERROR] An Unknown error occured while processing")
                        break
                elif line[x] != "指" and line[x] != "会" and line[x] != "字" and 65<=ord(line[x])<=90:
                    try:
                        decrypted_code += chr((ord(line[x]) - decrypting_math_function)%26 + 65)
                    except:
                        print("[ERROR] An Unknown error occured while processing")
                        break
                else:
                    decrypted_code += line[x]
        decrypted_code = decrypted_code.replace("会", "\t")
        decrypted_code = decrypted_code.replace("字", " ")
        decrypted_code = decrypted_code.replace("上", "'")
        decrypted_code = decrypted_code.split("指")
        with open(output, "w") as file:
            for i in decrypted_code:
                file.write(i + '\n')
            file.close()
        print("[INFO] Process Ended Correctly")

if args.e == '1':
    pyEncrypt = Code(args.c, args.f1, args.f2)
    pyEncrypt.encrypt(args.o)

if args.d == '1':
    pyTestCodeObject = Code(args.c, args.f1, args.f2)
    pyTestCodeObject.decrypt(args.o)