# teaching-selenium-to-a-pleb
Some code teaching a pleb how to use selenium


## Setting up a selenium project

1. You will need a webdriver (that is on the system path) for whatever browser you want to use (must match versions in most cases). To do this put it in a folder and include that folder in a `manifest.ini` file (and relatively path to it using `__file__`), or put it on your system path. If you go the `manifest.ini` route (requires project to be a full python package with a `setup.py` file also) check out [check-manifest](https://pypi.org/project/check-manifest/) which is a great tool to automate this process. Chrome's webdriver can be found [here](https://chromedriver.chromium.org/downloads), also keep in mind different OS's use different drivers. The included `chromedriver.exe` is the windows chrome webdriver for version 94

2. Install selenium [see here](#install-dependencies)

3. Add boilerplate code:

   ```python
   from selenium import webdriver # Step 1 import
   import os
   
   # Step 2 instantiate webdriver instance
   
   ## Get the path to the webdriver
   if os.name == "nt": # windows
       webdriver_path = os.path.join(os.path.dirname(__file__), "chromedriver.exe")
   else:
       webdriver_path = "" # Add in binaries and paths for linux/mac
   
   driver = webdriver.Chrome(webdriver_path) # This will be used to access everything on the web
   
   # Step 3 get a webpage
   driver.get("https://google.com") 
   
   # Step 4 write the rest of your script
   while True:
       ...
   ```


## Selenium alternative

There is a new project called `pylenium` which is a `selenium` "alternative", that handles some of the complications for you. If possible you can also try using that, the details for usage can be found [here](https://docs.pylenium.io/).


### Install dependencies

Run `pip install -r requirements.txt` to grab pylenium and selenium
