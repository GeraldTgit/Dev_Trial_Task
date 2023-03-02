import os
from bs4 import BeautifulSoup
from selenium import webdriver

# path to the downloaded chromedriver executable
chrome_driver_path = "C:\Program Files\Python311\chromedriver.exe"

# define a constant variable for the file path
FILE_PATH = 'C:\PythonFiles\Developer Trial Task\index.html'

# create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# navigate to the website
driver.get("https://www.classcentral.com")

# get the HTML source code of the website
html = driver.page_source

# save the HTML code to a file
with open(FILE_PATH, 'w', encoding='utf-8') as file:
    file.write(html)
print("index.html downloaded.. .")

# set the download directory to the specified path
download_path = 'C:\PythonFiles\Developer Trial Task'
prefs = {"download.default_directory": download_path}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", prefs)

# open the saved HTML file and read its contents
with open(FILE_PATH, 'r', encoding='utf-8') as file:
    html = file.read()

# create a BeautifulSoup object from the HTML code
soup = BeautifulSoup(html, 'html.parser')

# find all 'a' tags with 'href' attribute
links = soup.find_all('a', href=True)

#Create list for important links
importantlinks = ["https://www.classcentral.com/subjects","https://www.classcentral.com/login","https://www.classcentral.com/signup","https://www.classcentral.com/help/moocs","https://www.classcentral.com/universities"]

# create a list of href values that do not have a dot in them
no_dot_links = [link.get('href') for link in links if '.' not in link.get('href')]

# create a list of href values that start with '/subject'
subject_links = [link for link in no_dot_links if link.startswith('/')]

# add 'https://www.classcentral.com' before '/subject' links
subject_links = [f'https://www.classcentral.com{link}' for link in subject_links]

# create a list of href values that start with '/subject'
university_links = [link.get('href') for link in links if link.get('href').startswith('/university')]

# add 'https://www.classcentral.com' before '/subject' links
university_links = [f'https://www.classcentral.com{link}' for link in university_links]

# create a list of href values that start with '/subject'
classcentral_links = [link.get('href') for link in links if link.get('href').startswith('https://www.classcentral.com')]

# combine the two lists
all_links = importantlinks + university_links + classcentral_links + subject_links 

# create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# download the HTML files of the first 200 links
for i, link in enumerate(all_links[:200]):
    # navigate to the website
    driver.get(link)
    
    # get the HTML source code of the website
    html = driver.page_source
    
    #testlink name
    testlink = link
    testlink = testlink.replace("https://www.classcentral.com/", "")
    testlink = testlink.replace("/", "-")

    # save the HTML code to a file
    file_name = f'-{testlink}.html'
    file_path = os.path.join(download_path, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html)

    # update href in index.html for links with https://www.classcentral.com/
    for a_tag in soup.find_all('a', href=link):
        a_tag['href'] = file_name
        print(f'Updated href in index.html for {link} to {file_name}')

    # update href in index.html for links WITHOUT https://www.classcentral.com/
    testlink = link.replace("https://www.classcentral.com", "")
    for a_tag in soup.find_all('a', href=testlink):
        a_tag['href'] = file_name
        print(f'Updated href in index.html for {testlink} to {file_name}')

    # print the name of the downloaded file
    print(f'Downloaded: {file_name} : {i+1} out of 200')

# save the updated HTML code to the index.html file
with open(FILE_PATH, 'w', encoding='utf-8') as file:
    file.write(str(soup))

# close the browser
driver.quit()
print("Done!")
