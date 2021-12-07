from model.Downloadable import Downloadable
import re
import model.Service as Service

pattern = re.compile(r"\.[a-z0-9]{1,4}")

class File(Downloadable):

    @staticmethod
    def create(element, parent):
        name = str(element.text)
        try:
            name = pattern.split(name)[0] + pattern.search(name)[0]
        except:
            try:
                extension = element.parent.parent.parent.find(class_="il_ItemProperty").text.replace(
                    "\n", "").replace("\t", "").replace("\xa0", "")
                name = f"{name}.{extension}"
            except:
                pass
        return File(name,
                    element['href'],
                    parent)

    @staticmethod
    def extract_from_page(content, parent):
        result = []
        raw_items = Service.get_items_where_href_contains_markers(
            content, '_file_')
        for element in Service.remove_duplicates_and_clear(raw_items):
            result.append(File.create(element, parent))
        return result

    def get_hash(self):
        return self.url.split("_file_")[1][:7]