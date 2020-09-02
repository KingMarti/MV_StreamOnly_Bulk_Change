# MV_StreamOnly_Bulk_Change
A Quick Hacked Together Script For Changing the Stream Only Option On All Videos On ManyVids

Requirements: 
Selenium framework
Firefox web driver 

Install Selenium: 

Open Terminal/Cmd and Write Command as written Below
  python -m pip install selenium

Install The FireFox Web Driver Windows(64 bit) install instructions. 

Download the file from the link below: 
https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-win64.zip

You now need to add the GeckoDriver to the Enviormant variables. To do this follow the instructions in the link below: 
https://www.qafox.com/webdriverio-setup-environment-variable-for-gecko-driver/

With everything set up you now need to open the script to add in your log in information. 
The script can be opened with notepad if you dont have a text editor like visual studio code, atom or notepad++. 
Just make sure it's notepad and not wordpad. Wordprcessors will not work for editing this file. 

The script has comment boxes containing important information and a secondery option for a command depending on the result you want.
once you have added the username and password, and any editied any of the options you want to change it's time to run the script. 

open a comand prompt (windows key +r and then type cmd and press enter) 
With windows exploer open ( the default folder viewer ) locate where you saved the sctipt, click the address bar and copy the 
address to the file
in the command prompt window, type cd and then paste in the address to the script and press enter
type python mvSwitch.py 

If you didnt turn off the browser window in the settings then a browser window will open and navigate to ManyVids
If you did turn that off, there will be output to explain what is happening in the command prompt.

