# Initial commit

I will try to perform a python-based console & web service which allow to encrypt and decrypt code to avoid code stealing of all kinds.

I go on the base of a pseudo "two factors authentification" which will encrypt each character of the uploaded code in another character with an apparent randomly generated password but really chosen by the user.

Let's go on the backend !

[INFO] Backend done ! Second commit !
[INFO] Taking test in Examples folder

## I. [COMMANDS] Tests run
### 1. dsmc as a python file
##### a. Encrypting and decrypting the Haskell example
Encrypting
```shell script
python dsmc.py -e 1 -c "tests/Haskell/example.hs" --f1 "factor1" --f2 "factor2" -o "Examples/Haskell/example_encrypted.hs"
```
Decrypting
```shell script
python dsmc.py -d 1 -c "tests/Haskell/example_encrypted.hs" --f1 "factor1" --f2 "factor2" -o "Examples/Haskell/example_decrypted.hs"
```
##### b. Encrypting and decrypting general model
Encrypting
```shell script
python dsmc.py -e 1 -c "path/to/the/file/to/encrypt" --f1 "<password-first-factor>" --f2 "<password-second-factor>" -o "path/then/name/to/the/output/encrypted/file"
```
Decrypting
```shell script
python dsmc.py -d 1 -c "path/then/name/to/the/output/encrypted/file/to/decrypt" --f1 "<password-first-factor>" --f2 "<password-second-factor>" -o "path/then/name/to/the/output/decrypted/file"
```

##### c. For further details on the command line use of dsmc.py, please type
```shell script
python dsmc.py --help
```
or 
```shell script
python dsmc.py -h
```
### 1. dsmc as a python module
Please, see the example of use of dsmc as python module in the Examples/ folder