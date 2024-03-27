from IliasCrawler.models.extractor.Locator import Locator
import IliasCrawler.models.extractor.service as service


class DynamicAttribute:

    def __init__(self, name, instructions) -> None:
        self.name = name
        self.attr_name = instructions['attrName']
        self.locator = None
        if 'locator' in instructions:
            self.locator: Locator = Locator(instructions['locator'])

    def get_value(self, canidate):
        tag_containing_attr = canidate
        if self.locator:
            tag_containing_attr = self.locator.find_elements(canidate)
            if not tag_containing_attr:
                return None
            else:
                tag_containing_attr = tag_containing_attr[0]
        return service.get_attr(tag_containing_attr, self.attr_name)