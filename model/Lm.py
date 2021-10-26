import Folder

class Lm(Folder):

    def __init__(self, name, url, parent, content, number):
        super().__init__(name, url, parent, content)
        self.number = number

    @staticmethod
    def create(element, parent, number):
        url = element['href']
        content = BeautifulSoup(session.get(url).text, 'lxml')
        if number == 0:
            return Lm(str(element.text),
                      element['href'],
                      parent,
                      content,
                      number)
        else:
            return Lm(str(number) + str(element.text),
                      element['href'],
                      parent,
                      content,
                      number)

    def get_new_pages(self):
        result = []
        # try:
        #     element = driver.find_element_by_xpath("//*[@class='ilc_page_tnav_TopNavigation']//*[@class='ilc_page_rnavlink_RightNavigationLink']")
        #     if self.number == 0:
        #         result.append(Lm.create(element, self, self.number + 1))
        #     else:
        #         result.append(Lm.create(element, self.parent, self.number + 1))
        # except:
        #     pass
        return result
