# Dev_Trial_Task
Consist of 3 python scripts:

1. download_html.py
    - This script is hardcoded to download HTML files from classcentral(.)com
    - This script allows you to download the HTML file of a website and its first-level subpages.
    
    Note: 
      - You have to change the URL encoded in this script to the website you are trying to download.
        - eg: driver.get("mywebsite.com")
      - Also, set-up the 'FILE_PATH', 'download_path' and the 'chrome_driver_path'
      - Edit the 'all_links' values to suit your needs.
      

2. html_lookup.py
    - This script lookups for all html file in a specified directory.
    - This script calls translate.py to translate each HTML file it may find.
    
    Note: 
      - Update the 'root_dir' to your preference.
      
3. translate.py
    - This script srape to the html file and for all possible text it can translate.
    - List of the HTML elements and/or attributes that may contain text that can be translated:
      - <a>	<h2>	<h5>	<button>
      - <p>	<h3>	<h6>	<placeholder>
      - <title>	<h4>	<span>	
      - <h1>	<h5>	<strong>	
