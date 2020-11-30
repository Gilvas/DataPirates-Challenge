#! python3

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd
from bs4 import BeautifulSoup
import html5lib
import aiohttp, asyncio
import requests, json, os
from tabulate import tabulate

# Launch URL
url = "http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm"

# Check the behaviour of the website
async def main():
    async with aiohttp.ClientSession() as session:
        async with await session.get(url, max_redirects= -1) as response:
            response

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
  
# Create a Firefox session
browser = webdriver.Firefox(executable_path = GeckoDriverManager().install())
browser.implicitly_wait(3)
browser.get(url)

# Get all of the UF values
buttonUF = browser.find_element_by_name("UF")
optionsUF = [x for x in buttonUF.find_elements_by_tag_name("option")]
print("Get all UF...")
allUFs = []
for elements in optionsUF:
    allUFs.append(elements.get_attribute("value"))
allUFs.pop(0) # delete the empty value
dataList = [] # it will store the table information about the UFs

# Function that verifies next page 
def isNextPage1():
    if not browser.find_elements_by_css_selector(".ctrlcontent > div:nth-child(11) > a:nth-child(1)"): 
        return False
    else:
        return True

def isNextPage2():
    if not browser.find_elements_by_css_selector(".ctrlcontent > div:nth-child(9) > a:nth-child(1)"):  
        return False
    else:
        return True

# Select all UFs and click the Search button for each UF
print("\nLoop over all UF")
for UF in allUFs:
    print("\nGetting the information of: " + UF)
    choice = Select(browser.find_element_by_name("UF"))
    chooseUF = choice.select_by_value(UF)
    clickSearch = browser.find_element_by_css_selector(".btn2").click()

    # Get the new URL information
    newUrl = BeautifulSoup(browser.page_source, "lxml")
    table = newUrl.find_all("table")[1] # second table in the page contains the information

    # Give the information to pandas to put it in a dataframe object
    dataFrame = pd.read_html(str(table), header=0)
    dataFrame[0].columns = ["Localidade","Faixa de CEP","Situação", "Tipo de Faixa"]
    dataList.append(dataFrame[0][1:])

    # Verify next page of the same UF
    checker1 = isNextPage1()
    checker2 = isNextPage2()
  
    while (checker1 == True or checker2 == True):
        if (checker1 == True):
            browser.find_element_by_css_selector(".ctrlcontent > div:nth-child(11) > a:nth-child(1)").click()
            newUrl = BeautifulSoup(browser.page_source, "lxml")
            table = newUrl.find_all("table")[0] # first table in the page contains the information
            dataFrame = pd.read_html(str(table), header=0)
            dataList.append(dataFrame[0][1:])
        else: # checker2 == True
            browser.find_element_by_css_selector(".ctrlcontent > div:nth-child(9) > a:nth-child(1)").click()
            newUrl = BeautifulSoup(browser.page_source, "lxml")
            table = newUrl.find_all("table")[0] # first table in the page contains the information
            dataFrame = pd.read_html(str(table), header=0)
            dataList.append(dataFrame[0][1:])
            
        checker1 = isNextPage1()
        checker2 = isNextPage2()

    # Check next UF
    browser.find_element_by_css_selector(".ctrlcontent > div:nth-child(4) > a:nth-child(1)").click()

# Close the Firefox session
browser.close()
browser.quit()

# Concatenate the tables into a result variable
print("\nThe results are in\n")
result = pd.concat([pd.DataFrame(dataList[i]) for i in range(len(dataList))],ignore_index=True)

# Name the columns
result.columns = ["Localidade","Faixa de CEP","Situação", "Tipo de Faixa"]

# Generate an Id index and order the columns
result["id"] = result.index + 1
result = result[["id","Localidade","Faixa de CEP","Situação", "Tipo de Faixa"]]

# Convert the pandas dataframe to JSON
json_records = result.to_json(orient='records', lines=True, force_ascii=False)

# Converts to an ascii table
print(tabulate(result,tablefmt='psql'))

# Get current working directory
path = os.getcwd()

# Open, write, and close the file
f = open(path + "\\out.json","w") 
f.write(json_records)
f.close()
