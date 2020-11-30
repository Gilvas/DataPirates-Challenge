# DataPirates-Challenge
Python scraping code to gather data from website and export the results to JSONL file

## Description
With this program, you can gather all the table information from the brazilian postal codes, and export it to a JSONL file. You can check the website [BuscaCep.Correios](http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm) before we get into the code.

## Installation
Make sure you have installed [Python 3](https://www.python.org/downloads/) in your machine.
I have provided the third-party modules necessary to run the code. Please, download [requirements.txt](https://github.com/Gilvas/DataPirates-Challenge/blob/main/Pirates%20Chalenge/requirements.txt) and install each one of them. Those modules can be installed as follows:
- in Windows, open the Command Prompt (cmd), type '**pip install /path/to/requirements.txt**'
- in other terminals, please go to [Installing Python Modules](https://docs.python.org/3/installing/index.html) for further instructions

If you have any troubles installing those third-party modules, install them one by one as follows:
- in Windows, open the Command Prompt (cmd), type '**pip install third-party module name**'
- example of the above situation: **pip install webdriver-manager**
- in other terminals, please go to [Installing Python Modules](https://docs.python.org/3/installing/index.html) for further instructions

The **.py** code can be compiled by the program of your preference. For instance, I use [Visual Studio Code](https://code.visualstudio.com/) to run my codes, but make sure that you add the [python extension](https://code.visualstudio.com/docs/languages/python).

## Usage
There are two files in the [project](https://github.com/Gilvas/DataPirates-Challenge/tree/main/Pirates%20Chalenge). Let's explain them individually.

#### postalCodeSearcher.py
1. download the file
1. run the code
1. the code will loop over all of the UFs found in the website
1. when it terminates, the results will be written to a **out.json** file in the same path directory in which you have the postalCodeSearcher.py

#### shouldExpect.py
1. download the file
1. run the code
1. when the website opens, return to the code and type the UF that you want to get the information about
1. if the UF provided is found, then the code executes and the results will be written to a **expected.json** file in the same path directory in which you have the shouldExpect.py
1. if the UF is not there, all the UF found in the website will be printed and then you try again
1. in the case that you type again a UF which is not there, the code exits

## Note
I wrote the code in Windows. Therefore, the shebang line (first line of the code) tells my computer run Python 3 in my operating system Windows. If you use another OS, Linux or OS X, please change that first line to the one which fits you. Please visit [Automate the Boring Stuff with Python Programming](https://automatetheboringstuff.com/appendixb/) for further explanation.
