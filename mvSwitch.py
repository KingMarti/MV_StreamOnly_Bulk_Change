######################################################################################
###                                                                                ###
###                         ManyVids Bulk Stream Option Chnager                    ###
###                                     By KingMarti                               ###
###                                                                                ###
######################################################################################

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select

#############################################################################################
###                                                                                       ###
###         Enter your username and password in quotes after the equals sign below        ###
###                                                                                       ###  
#############################################################################################


manyvids_username =
manyvids_password =



links=[]
new_link_list=[]
video_list =[]

def getMV():
    options=Options()
    options.headless=True
    ###############################################################
    ###                                                         ###
    ###         To Run Without Opening A Browser Window         ###
    ###              Change webdriver.Firefox To:               ###
    ###           webdriver.Firefox(options=options)            ###
    ###                                                         ###
    ###############################################################
    bot = webdriver.Firefox()
    bot.get('https://manyvids.com/Login/')
    print('loading login page')
    time.sleep(3)
    bot.find_element_by_id('triggerUsername').send_keys(manyvids_username)
    bot.find_element_by_id('triggerPassword').send_keys(manyvids_password)
    bot.find_element_by_id('loginAccountSubmit').click()
    print('username and password entered')
    time.sleep(3)
    bot.get('https://manyvids.com/MV-Content-Manager/')
    print('loading content manager page')
    time.sleep(3)
    pages = bot.find_elements_by_class_name('page-link')
    print('Building Video Index, Please Wait')
    for page in pages:
        print('there are ',len(pages), 'pages of videos')
        drop_btn = bot.find_elements_by_xpath('//i[contains(@data-toggle,"dropdown")]')
        time.sleep(3)
        videos = bot.find_elements_by_class_name('manage-content__list-item')
        for vid in videos:
            video_links=bot.find_elements_by_xpath('//a[contains(@title,"Edit your content")]')
        for vid_link in video_links:
            links.append(vid_link.get_attribute('href'))
        print('Finished Indexing Videos')
        
        bot.find_element_by_class_name('next').click()
    for i in links:
        if i not in new_link_list:
            new_link_list.append(i)
    print('There are ', len(video_list), ' videos')
    for link in new_link_list:
        bot.get(link)
        time.sleep(3)
        stream_options = bot.find_element_by_xpath("//div[contains(@class,'js-edit-vid-stream-only')]")
        bot.execute_script('arguments[0].scrollIntoView();', stream_options)
        bot.execute_script('arguments[0].setAttribute("class","nice-select js-edit-vid-stream-only open")', stream_options)
        stream_options = bot.find_elements_by_xpath("//div[contains(@class,'js-edit-vid-stream-only')]/ul/li")
        ################################################################
        ###                                                          ###
        ###             To Chnage Stream Only To Yes Chnage          ###
        ###                    stream_options[1] to                  ###
        ###                     stream_options[0]                    ###
        ###                                                          ###
        ################################################################
        stream_options[1].click()
        print('option changed to no')
        time.sleep(3)
        print('Saving Chnages')
        bot.find_element_by_id('saveVideo').click()
        print('Video Updated, Moving to next video')
        time.sleep(5)
    print('all changes completed)
getMV()
