
import requests
import time

class InspiroScrapper():
    """This module takes care of making requests, obtaining images and
       saving them for usage from inspirobot through web requests"""

    def __init__(self):
        self.url = "http://inspirobot.me/api?generate=true"

    def _web_scrapper(self):
        """function to perform actual request to and from inspirobot"""
        r = requests.get(self.url)
        image_url = r.text
        r = requests.get(image_url)
        image = r.content

        return(image)


    def inspiro_scrapper(self):
        """callable function hopefully abstracting further functions called"""
        try:
            x = int(time.time())     
            image = self._web_scrapper()
            title = "motivation{}".format(x)
            with open("motivate/{}".format(title), "wb") as f:
                f.write(image)

            return(title)

        except TypeError:
            print("Something wrong with web_scrapper!!")
            return(False)
