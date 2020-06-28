# dsmc python module

dsmc (DontStealMyCode) is a python-based complete "framework" to encrypt and decrypt code or whatever file you want. Please the global repository for further details.  

## Installation

`pip install dsmc`

or

clone the repository via git `git clone https://github.com/Atepir/DontStealMyCode-DSMC-console-web-code-encrypter/dontstealmycode`

## I. Tests run
### 1. dsmc as a python file
##### a. Encrypting and decrypting the Haskell example
Encrypting
```shell script
python __init__.py -e 1 -c "tests/Haskell/example.hs" --f1 "factor1" --f2 "factor2" -o "../tests/Haskell/example_encrypted.hs"
```
Decrypting
```shell script
python __init__.py -d 1 -c "tests/Haskell/example_encrypted.hs" --f1 "factor1" --f2 "factor2" -o "../tests/Haskell/example_decrypted.hs"
```
##### b. Encrypting and decrypting general model
Encrypting
```shell script
python __init__.py -e 1 -c "path/to/the/file/to/encrypt" --f1 "<password-first-factor>" --f2 "<password-second-factor>" -o "path/then/name/to/the/output/encrypted/file"
```
Decrypting
```shell script
python __init__.py -d 1 -c "path/then/name/to/the/output/encrypted/file/to/decrypt" --f1 "<password-first-factor>" --f2 "<password-second-factor>" -o "path/then/name/to/the/output/decrypted/file"
```

##### c. For further details on the command line use of dsmc.py, please type
```shell script
python dsmc.py --help
```
or 
```shell script
python dsmc.py -h
```
### 2. dsmc as a python module
Please, see the example of use of dsmc as python module in the tests/ folder

<hr>
@author: Nongma Sorgho

@date: 06.28.2020