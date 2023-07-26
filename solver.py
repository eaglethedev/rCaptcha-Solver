import speech_recognition as sr
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
import undetected_chromedriver.v2 as uc
from time import sleep
import urllib.request
from selenium import webdriver   
import warnings

from pydub import AudioSegment

from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException  
from selenium.webdriver.chrome.options import Options
import os
#warnings  
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(chrome_options=options)
browser.get("https://store.steampowered.com/join/?redir=%3Fl%3Dturkish&snr=1_60_4__62")
r = sr.Recognizer()
sleep(3)
qframe = browser.find_element_by_css_selector("iframe").get_attribute("name")
iframe = browser.find_element_by_name(qframe).click()
sleep(1)
qframe = browser.find_elements_by_css_selector("iframe")[2].get_attribute("name")
browser.switch_to.frame(qframe)
browser.find_element(By.CSS_SELECTOR, '#recaptcha-audio-button').click()
sleep(1)
wavlink = browser.find_element(By.CSS_SELECTOR, 'body > div > div > div.rc-audiochallenge-tdownload > a').get_attribute("href")
m5 = wavlink
sleep(1)
def mp(url):
    fullname = "audio"+".mp3"
    urllib.request.urlretrieve(url,fullname)     
mp(m5)
# files                                                                       
src = "audio.mp3"
dst = "audio.wav"

# convert wav to mp3                                                            
audSeg = AudioSegment.from_mp3("audio.mp3")
audSeg.export(dst, format="wav")


with sr.AudioFile(r"audio.wav") as source:
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
        browser.find_element_by_css_selector("#audio-response").send_keys(text)
        browser.find_element_by_css_selector("#recaptcha-verify-button").click()
    except:
        print("sa")
        
os.remove(r"audio.wav")
os.remove(r"audio.mp3")