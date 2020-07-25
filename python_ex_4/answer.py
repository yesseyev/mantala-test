import os
from urllib.parse import urlparse

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TwitterParser:
    """
    Parser for twitter profile page

    Manipulates the ChromeDriver to parse
    """

    def __init__(self, chrome_driver_path=os.getenv('CHROME_DRIVER_PATH', 'chromedriver'), timeout_delay=5):
        # Adding chrome options to avoid loading images
        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.images": 2})

        self.__browser = webdriver.Chrome(chrome_driver_path, options=options)
        self.timeout_delay = timeout_delay

    def set_network_conditions(self, **conditions):
        """ Chrome driver network conditions configuration """
        self.__browser.set_network_conditions(**conditions)

    def quit_browser(self):
        """ Closing web driver window """
        self.__browser.quit()

    def get_followers_count(self, url: str) -> int:
        """
        Finds number of followers in twitter profile page

        :param url: URL string in [https://twitter.com/{username}] format
        :return: number of followers or -1 if account blocked/does not exists
        """
        if not self.__is_valid_profile_url(url):
            raise ValueError('URL string is not in https://twitter.com/{username}')
        self.__browser.get(url)

        followers = -1
        try:
            el = WebDriverWait(self.__browser, self.timeout_delay).until(
                EC.presence_of_element_located((By.XPATH, '//a[contains(@href, \'/followers\')]')))

            followers = el.get_attribute('title')  # Executed after element is present
        except TimeoutException:
            print("Loading took too much time!")

        return self.__to_integer(followers)

    @staticmethod
    def __to_integer(followers):
        """ Converts result to integer """
        if isinstance(followers, str):
            followers = followers.replace(',', '')

        return int(followers)

    @staticmethod
    def __is_valid_profile_url(url):
        if not isinstance(url, str):
            return False

        o = urlparse(url)
        is_twitter = o.scheme == 'https' and o.netloc == 'twitter.com'
        is_profile_page = len(o.path.split('/')) == 2 and len(o.path) > 0

        return is_twitter and is_profile_page


if __name__ == '__main__':
    URL = 'https://twitter.com/KMbappe'

    twitter = TwitterParser()
    # twitter.set_network_conditions(
    #         offline=False,
    #         latency=5,  # additional latency (ms)
    #         download_throughput=10 * 1024,  # maximal throughput
    #         upload_throughput=10 * 1024)  # maximal throughput
    print(twitter.get_followers_count(URL))
    twitter.quit_browser()
