from model.Course import Course
from model.IlItemGroup import IlItemGroup
from model.Page import Page


class Ilias(Page):

    on_page_container_types = [IlItemGroup]
    downloadable_types = []
    tree_importance = 0

    @staticmethod
    def sub_page_types():
        return [Course]