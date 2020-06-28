# coding: utf-8

from os import system

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
