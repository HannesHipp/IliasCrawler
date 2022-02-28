from controller.Frame import Frame
from model.Ilias import Ilias
from service.BusinessModel import BusinessModel
from tests import clean_tree


class CrawlingController(Frame):

    def __new__(cls, container):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CrawlingController, cls).__new__(cls)
        return cls.instance

    def __init__(self, container):
        self.ui_file_location = 'C:\\Users\\Hannes\\Code Projekte\\IliasCrawler\\IliasCrawler\\resources\\CrawlingView.ui'
        super().__init__(container)
        # connections

    def show(self):
        super().show()
        data = CrawlingController.crawl()
        BusinessModel.instance.downloadable_data = data
        
    @staticmethod
    def crawl():
        result = []
        for course in [course for course in BusinessModel.instance.fresh_courses if course.should_be_downloaded]:
            result += course.crawl()
        return result

    @staticmethod
    def postprocess_data(data):
        data = CrawlingController.clean_tree(data)
        data = CrawlingController.shorten_long_item_paths(data)
        return data

    @staticmethod
    def clean_tree(downloadables):
        for downloadable in downloadables:
            current = downloadable.parent
            while current.parent is not None:
                if len(current.children) == 1:
                    item_to_delete = CrawlingController.decide_which_item_to_delete(current)
                    CrawlingController.delete_item_from_tree(item_to_delete)
                current = current.parent
        return downloadables

    @staticmethod
    def decide_which_item_to_delete(current):
        if type(current).tree_importance < type(current.children[0]).tree_importance:
            return current.children[0]
        else:
            return current

    @staticmethod
    def delete_item_from_tree(item):
        # tree_importance
        # 0 = necessary, don't delete
        # 1, 2, 3, ... = not necessary, delete if appropriate
        if type(item).tree_importance != 0:
            for child in item.children:
                child.parent = item.parent
                item.parent.children.append(child)
            item.parent.children.remove(item)

    @staticmethod
    def shorten_long_item_paths(data):
        windows_max_path_length = 248
        for item in data:
            item_path = f"{item.get_path()}\\{item.name}.{item.file_extension}"
            if len(item_path) > windows_max_path_length:
                component_dict = CrawlingController.get_component_dict(item)
                number_of_components = len(component_dict)
                number_of_separators = number_of_components - 1
                file_extension_length = len(item.file_extension) + 1
                userpath_plus_ilias_length = len(item_path.split('\\Ilias\\')[0] + "\\Ilias\\")
                available_string_length = windows_max_path_length - file_extension_length - userpath_plus_ilias_length - number_of_separators
                for component_name in component_dict:
                    allowed_component_length = int(available_string_length/number_of_components)
                    if (len(component_name) - allowed_component_length) > 0:
                        number = int(allowed_component_length / 2) - 1
                        name = f"{component_name[:number]}_{component_name[-number:]}"
                        component_dict[component_name].name = name
                    else:
                        name = component_name
                    available_string_length = available_string_length - len(name)
                    number_of_components = number_of_components - 1
        return data

    @staticmethod
    def get_component_dict(item):
        d = {}
        while type(item) is not Ilias:
            d[item.name] = item
            item = item.parent
        result = {}
        for k in sorted(d, key=len, reverse=False):
            result[k] = d[k]
        return result

        