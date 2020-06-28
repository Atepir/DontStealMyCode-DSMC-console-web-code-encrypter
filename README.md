# Don't Steal My Code !

This is the name of a python-based module, program, website and console app written for the 2020 Macrohacks Hackathon.

## I. What it does ?

It encrypts or decrypts code from any language you want to an unreadable and very securized file using a kind of double factor authentification and an math function to translate pseudo-randomly all the characters of your code, each character having his own encryption deduced by the precedently described math function given by the user when settings the two factors of his code.

## II. Why do that ?

Sometimes, for a reason or for another, we need to keep some code secret or we just don't want someone steals it.

For instance, using a private github repository may be due to this attitude to keep some code in a kind of circle.

## III. Don't Steal My Code Features

### 1.The web driven application
#### Installation
`pip install dsmc-web`
#### Examples
Please see `dsmc_website/` folder for more informations.

I have deployed an Heroku app at [dsmc.herokuapp.com](https://dsmc.herokuapp.com).

### 2.The python console launcher
#### Examples
##### a. Encrypting and decrypting the Haskell example
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
python __init__.py --help
```
or 
```shell script
python __init__.py -h
```

### 3. The python module
#### Installation

`pip install dsmc`
#### Examples
Please, see the example of use of dsmc as python module in the tests/ folder

### 4. Differences between dsmc and dsmc-web
dsmc works with argparse parameters when dsmc-web doens't

### 5. Application current limitations
According to what it does, the application can encrypt or decrypt non-utf8 programs, programs non-readable in python and particularly (for development purposes) programs which contains one or more of the following characters :
<ul>
    <li>指</li>
    <li>会</li>
    <li>字</li>
    <li>上</li>
    <li>下</li>
</ul>

### 6. Notice
This software is not Turing-complete, he can't encrypt and decrypt himself, it's not a Turing machine !

### 7. Technologies
<ul>
    <li>Python</li>
    <li>Bash</li>
    <li>Flask</li>
    <li>Heroku</li>
    <li>Html</li>
    <li>Css</li>
    <li>Javascript</li>
    <li>FontsAwesome</li>
    <li>GoogleFonts</li>
</ul>

## IV. Licence and author
### 1. Licence
Copyright (c) 2020 Sorgho Nongma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### 2. Author
SORGHO Nongma Charles Gérard, student at the University of Strasbourg.
