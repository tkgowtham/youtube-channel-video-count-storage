from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get('https://www.youtube.com/c/Freecodecamp/videos')
for i in range(1,982):
    driver.find_element_by_css_selector(f'ytd-grid-video-renderer.style-scope:nth-child({i}) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(2)').location_once_scrolled_into_view
    time.sleep(0.01)
with open('freecodecamp2.txt','a',encoding="utf-8") as file:
    for i in range(983,1238):#1238

        t = str(i)+' . '+driver.find_element_by_css_selector(f'ytd-grid-video-renderer.style-scope:nth-child({i}) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(2)').text
        driver.find_element_by_css_selector(f'ytd-grid-video-renderer.style-scope:nth-child({i}) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(2)').location_once_scrolled_into_view
        file.write(f'{t}\n')
        time.sleep(0.01)
        
driver.close()
                                                            
