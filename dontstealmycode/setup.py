import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dsmc", # Replace with your own username
    version="0.0.3",
    author="Nongma SORGHO",
    author_email="sorghocharles8@gmail.com",
    description="[Dont Steal My Code : Console & web code encrypter & decrypter]",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atepir/DontStealMyCode-DSMC-console-web-code-encrypter/tree/master/dontstealmycode",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)