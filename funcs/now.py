
from webscrapper.scrapper import InspiroScrapper
from PIL import Image

def get_picture():
    """Get Motivational poster to present to user"""
    x = InspiroScrapper()
    title = x.inspiro_scrapper()

    try:
        with Image.open('motivate/{}'.format(title)) as img:
            img.show()

        return True

    except Exception as e:
        print("[!!] An error has occurred.. {}".format(e))
        return False
