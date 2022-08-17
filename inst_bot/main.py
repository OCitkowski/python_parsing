import time, random, os, json
from cr_graphy.crypt import write_key, load_key, encrypt, decrypt
from inst_bot.copy_auth import *

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.common.exceptions import NoSuchElementException


def crypt_auth(file_name):
    key_name = 'bot' + '.key'
    # file_name = 'test' + '.py'
    prefix = 're_'

    if os.path.isfile(key_name):
        # print('Key is exists')
        pass
    else:
        write_key(key_name)
        print(f'Creating the {key_name} full success')

    key = load_key(key_name)

    if os.path.isfile(prefix + file_name):

        decrypt(file_name, key, prefix)
        os.remove('re_' + file_name)

    else:
        encrypt(file_name, key, prefix)

def get_chrome_browser(headless:bool = False, start_maximized:bool = True, link_by_default:str = None):
    # https://peter.sh/experiments/chromium-command-line-switches/
    chrome_options = Options()

    if headless:
        chrome_options.add_argument('--headless')
    elif start_maximized:
        chrome_options.add_argument('--start-maximized')

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    chrome_options.add_argument('--data-path=/tmp/data-path')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--homedir=/tmp')
    chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

    # for ChromeDriver version 79.0.3945.16 or over
    # don`t show as web_drive
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    if not link_by_default == None:
        browser.get(link_by_default)
        time.sleep(random.randrange(2, 4))

    return browser

def set_cookies_by_user_id(browser, user_id:str = None)-> bool:
    result = False
    try:
        browser.delete_all_cookies()
        for cookie in json.load(open(f"{user_id}_cookies", "r")):
            browser.add_cookie(cookie)
        result = True
    except:
        browser.refresh()
        result = False
    finally:
        print(f'set cookies is {result}')
        return result

def save_cookies_by_user_id(browser, user_id: str = None) -> bool:
    result = False
    try:
        json.dump(browser.get_cookies(), open(f"{user_id}_cookies", "w"))
        result = True
    except:
        result = False
    finally:
        print(f'save cookies is {result}')
        return result

def login_in_instagram(browser, user_id: str = None, time_sleep:int = 3):

    result = False
    browser.get(site_path)
    time.sleep(random.randrange(time_sleep, time_sleep + 2))

    if not os.path.isfile(f"{user_id}_cookies"):
        try:
            browser.delete_all_cookies()
            username_input = browser.find_element('name', 'username')
            username_input.clear()
            username_input.send_keys(user_name)
            time.sleep(random.randrange(time_sleep, time_sleep + 2))
            password_input = browser.find_element('name', 'password')
            password_input.clear()
            password_input.send_keys(password)
            time.sleep(random.randrange(time_sleep, time_sleep + 2))
            password_input.send_keys(Keys.ENTER)
            time.sleep(random.randrange(time_sleep, time_sleep + 2))
            save_cookies_by_user_id(browser, user_id)

        except Exception as ex:
            print(ex)

    else:
        browser.delete_all_cookies()
        set_cookies_by_user_id(browser, user_id)
        time.sleep(random.randrange(time_sleep, time_sleep + 2))
        browser.refresh()
        time.sleep(random.randrange(time_sleep, time_sleep + 2))

        try:
            turn_on_button = browser.find_element(By.XPATH,
                                                  '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
            turn_on_button.click()
            result = True
        except NoSuchElementException:
            print('sorry? but do not found turn_on button`s')

    return result

def get_post_links_by_hashtag_in_instagram(browser, hashtag, quantity_lincs:int = 100, time_sleep:int = 3):
    posts_urls = []
    try:
        browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(random.randrange(time_sleep, time_sleep + 2))

        while len(posts_urls) < quantity_lincs:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randrange(time_sleep, time_sleep + 2))
            hrefs = browser.find_elements(By.TAG_NAME, "a")
            posts_urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]

    except Exception as ex:
        print(f' (sorry? but do not finded link`s ) /  {ex} ')
        return []

    finally:
        return posts_urls



def login(time_sleep: int = 3, close_browser: bool = False):
    user_phone = '555777'

    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    # chrome_options.add_argument('--single-process')
    # chrome_options.add_argument('--data-path=/tmp/data-path')
    # chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--homedir=/tmp')
    chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    # for ChromeDriver version 79.0.3945.16 or over
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    browser.get("https://www.whatismyip.com/my-ip-information/")
    time.sleep(random.randrange(2, 4))
    browser.get(site_path)
    time.sleep(random.randrange(2, 4))

    # cookies
    if not os.path.isfile(f"{user_phone}_cookies"):

        try:
            browser.delete_all_cookies()

            username_input = browser.find_element('name', 'username')
            username_input.clear()
            username_input.send_keys(user_name)

            time.sleep(random.randrange(3, 5))

            password_input = browser.find_element('name', 'password')
            password_input.clear()
            password_input.send_keys(password)

            time.sleep(random.randrange(3, 5))

            password_input.send_keys(Keys.ENTER)
            time.sleep(random.randrange(50, 60))

            json.dump(browser.get_cookies(), open(f"{user_phone}_cookies", "w"))

            time.sleep(random.randrange(3, 5))
            browser.close()
            browser.quit()

        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()
    else:
        browser.delete_all_cookies()

        for cookie in json.load(open(f"{user_phone}_cookies", "r")):
            browser.add_cookie(cookie)

        time.sleep(random.randrange(3, 5))
        browser.refresh()
        time.sleep(random.randrange(3, 5))

        try:
            turn_on_button = browser.find_element(By.XPATH,
                                                  '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
            turn_on_button.click()

        except NoSuchElementException:
            print('sorry? but do not finded button`s')

        finally:
            time.sleep(time_sleep)

            if close_browser:
                browser.close()
                browser.quit()
            else:
                return browser

def hashtag_search(browser, hashtag, close_browser: bool = False, Unlike: bool = False):
    try:
        browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(3)

        for i in range(1, 4):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randrange(3, 5))

            hrefs = browser.find_elements(By.TAG_NAME, "a")
            posts_urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]

        print(posts_urls)

        for url in posts_urls:
            try:
                time_sleep = 5
                browser.get(url)
                time.sleep(time_sleep)

                # like_button
                like_button = browser.find_element(By.XPATH,
                                                   '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button')

                print(f'accessible_name - {like_button.accessible_name}')
                if like_button.accessible_name == 'Like' and not Unlike:
                    like_button.click()
                    print(f'like')
                elif like_button.accessible_name != 'Like' and Unlike:
                    like_button.click()
                    print(f'Unlike')

                # follow_button
                follow_button = browser.find_element(By.XPATH,
                                                     '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div')
                print(follow_button.text)
                follow_button.click()

                if follow_button.text == 'Following':
                    unfollow_button = browser.find_element(By.XPATH,
                                                           '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]')
                    unfollow_button.click()

                time.sleep(random.randrange(time_sleep, time_sleep + 2))
                print(follow_button.text)

                browser.refresh()
                time.sleep(random.randrange(time_sleep, time_sleep + 2))
   
            except NoSuchElementException as ex:
                print(ex)

    except Exception as ex:
        print(f' (sorry? but do not finded link`s ) /  {ex} ')
        browser.close()
        browser.quit()

    finally:
        if close_browser:
            browser.close()
            browser.quit()


if __name__ == '__main__':

    # if os.path.isfile('re_auth_data.py'):
    #     crypt_auth('auth_data.py')
    # browser = login(5, False)
    # hashtag_search(browser, 'vinnytsia', False, True)
    # crypt_auth('auth_data.py')
    # browser.get('https://bot.sannysoft.com/')
    user_id = '66665'
    time_sleep = 5
    hashtag = 'vinnytsia'
    browser = get_chrome_browser()
    print(login_in_instagram(browser, user_id, time_sleep))
    time.sleep(random.randrange(time_sleep + 20, time_sleep + 22))
    print(save_cookies_by_user_id(browser, user_id))
    print(get_links_by_hashtag_in_instagram(browser, hashtag, 10, 3))
    browser.close()
