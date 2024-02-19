import webview
from api import getcity_name
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(BASE_DIR,'ui','index.html')

class Api:
    def hellworld(self,pinter):
        print("Hello world"," ", pinter)

    def writter(self):
        return "comming in here"

    def city_getter(self,city_name):
        js = getcity_name(city_name)
        # print(js)
        return js

if __name__ == '__main__':
    ap = Api()
    window = webview.create_window('Weather Forcast', HTML_FILE,js_api=ap)

    webview.start()
