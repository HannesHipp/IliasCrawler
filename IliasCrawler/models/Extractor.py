import json
from bs4 import BeautifulSoup, Tag


class Extractor:

    def __init__(self, jsonPath: str) -> None:
        self.model = json.load(open(jsonPath))

    def startExtraction(self, soup):
        return self.extractData(soup, 'start')

    def extractData(self, tree: BeautifulSoup, type: str):
        result = []
        childTypes = self.model[type]['childTypes']
        for childType in childTypes:
            typeDescription = self.model[childType].copy()
            typeDescription.pop('childTypes')
            locatorDict = typeDescription.pop('locator')
            elements = self.findElements(tree, locatorDict)
            endpoint = typeDescription.pop('endpoint')
            attrsDict = typeDescription
            attrsDict['type'] = childType
            result.extend(self.encodeElements(elements, attrsDict, endpoint))
        return result

    def findElements(self, tree: BeautifulSoup, locatorDict: dict) -> list[Tag]:
        locatorDict = locatorDict.copy()
        if not locatorDict:
            return [tree]
        containsDict = locatorDict.pop('contains', None)
        name = locatorDict.pop('name', None)
        exactDict = locatorDict
        if exactDict:
            matches = tree.find_all(attrs=exactDict)
            if name:
                matches = [tag for tag in matches if tag.name == name]
        else:
            if name:
                matches = tree.find_all(name)
            else:
                matches = tree.find_all(
                    attrs={key: True for key in containsDict})
        if containsDict:
            matches = [tag for tag in matches if all(value in Extractor.getAttr(
                tag, attr) for attr, value in containsDict.items())]
        return matches

    def encodeElements(self, tags, attrsDict: dict, endpoint: bool):
        result = []
        attrsToFind = {attrName: locatorDict for attrName,
                       locatorDict in attrsDict.items() if isinstance(locatorDict, dict)}
        for tag in tags:
            validCanidate = True
            concreteDict = attrsDict.copy()
            for attrName, locatorDict in attrsToFind.items():
                subElementAttr = list(locatorDict.keys())[0]
                locatorDict = locatorDict[subElementAttr]
                subElement = self.findElements(tag, locatorDict)
                if not subElement:
                    validCanidate = False
                    break
                subElement = subElement[0]
                attrValue = Extractor.getAttr(subElement, subElementAttr)
                if not attrValue:
                    validCanidate = False
                    break
                concreteDict[attrName] = attrValue
            if validCanidate:
                if not endpoint:
                    concreteDict['children'] = self.extractData(
                        tag, attrsDict['type'])
                result.append(concreteDict)
        return result

    @staticmethod
    def parseLocatorDict(locatorDict):

        return (locatorDict, containsDict, name)

    @staticmethod
    def getAttr(tag, attrName):
        result = tag.get(attrName)
        if not result and hasattr(tag, attrName):
            result = getattr(tag, attrName)
        if isinstance(result, list):
            result = result[0]
        return result
