import consts
import requests


source_url = [df="KXResearch/Dynamic/"，"公告通知":"Survey/Notice/","asd":"Survey/Lecture/","StudentsWork/Dynamic/"}
# the sources will init at runtime!

class Source:
    level1 = str()
    level2 = str()
    name = str()
    def __init__(self, str1, str2, str3):
        self.level1 = str1
        self.level2 = str2
        self.name = str3
    def url(self):
        '''Return the url of the base page of the news source as a string.'''
        return consts.base_url + self.level1 + "/" + self.level2 + "/"

class Page(Source):
    ID = int()
    text = str()
    def url(self):
        '''Return the url of the page as a string.'''
        return consts.base_url + self.level1 + "/" + self.level2 + "/" + "?PageID=" + self.ID

    def __str__(self):
        return self.name + " " + self.ID

    def get(self):
        try:
            r = requests.get(self.url)
        except Exception:
            return Exception
        self.text = r.content()

    def next_page(self):
        new_page = self
        new_page.ID = new_page.ID + 1
        if new_page.empty():
