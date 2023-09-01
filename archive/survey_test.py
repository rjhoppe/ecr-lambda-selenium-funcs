"""
Test ran to see if the function could run headlessly and submit a single survey response
Test passed
"""

from selenium import webdriver
from tempfile import mkdtemp
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
import time


def handler(event=None, context=None):
    options = webdriver.ChromeOptions()
    service = webdriver.ChromeService("/opt/chromedriver")

    options.binary_location = '/opt/chrome/chrome'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-port=9222")

    chrome = webdriver.Chrome(options=options, service=service)
    chrome.get("https://tamearlyaccess.sjc1.qualtrics.com/jfe/form/SV_54nfTtytsta0KFw")
    time.sleep(1)

    pg1_actions = ActionChains(chrome)

    q1_pos_opt = ['mc-choice-input-QID16-1', 'mc-choice-input-QID16-2', 'mc-choice-input-QID16-3', 
                    'mc-choice-input-QID16-4', 'mc-choice-input-QID16-5', 'mc-choice-input-QID16-6',
                    'mc-choice-input-QID16-7']
    q1_choice = random.choice(q1_pos_opt)
    q1_button = chrome.find_element(By.ID, q1_choice)

    # Demographic question on education, can be reused, no logic applied
    q2_pos_opt = ['mc-choice-input-QID17-1', 'mc-choice-input-QID17-2', 'mc-choice-input-QID17-3',
                    'mc-choice-input-QID17-4', 'mc-choice-input-QID17-5', 'mc-choice-input-QID17-6',
                    'mc-choice-input-QID17-7']
    q2_choice = random.choice(q2_pos_opt)
    q2_button = chrome.find_element(By.ID, q2_choice)

    # Demographic question on income, can be reused, no logic applied
    q3_pos_opt = ['mc-choice-input-QID18-1', 'mc-choice-input-QID18-2', 'mc-choice-input-QID18-3',
                    'mc-choice-input-QID18-4', 'mc-choice-input-QID18-5', 'mc-choice-input-QID18-6',
                    'mc-choice-input-QID18-7']
    q3_choice = random.choice(q3_pos_opt)
    q3_button = chrome.find_element(By.ID, q3_choice)


    # Action Block
    pg1_submit = chrome.find_element(By.ID, 'next-button')
    pg1_actions.move_to_element(q1_button)
    pg1_actions.click(q1_button)
    pg1_actions.move_to_element(q2_button)
    pg1_actions.click(q2_button)
    pg1_actions.move_to_element(q3_button)
    pg1_actions.click(q3_button)
    pg1_actions.move_to_element(pg1_submit)
    pg1_actions.click(pg1_submit)
    pg1_actions.perform()
