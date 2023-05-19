import json
from bs4 import BeautifulSoup


class Extractor:

    def __init__(self, jsonPath: str) -> None:
        self.model = json.load(open(jsonPath))

    @staticmethod
    def createMatchingFunc(locatorDict):
        tagName = locatorDict['name']
        attrName = locatorDict['attr']
        if 'equals' in locatorDict:
            attrValue = locatorDict['equals']
            return lambda tag: tag.name == tagName and attrValue == Extractor.getAttr(tag, attrName)
        else:
            attrValue = locatorDict['contains']
            return lambda tag: tag.name == tagName and attrValue in Extractor.getAttr(tag, attrName)

    @staticmethod
    def getAttr(tag, attrName, tagName: str = None):
        result = None
        if tagName:
            tag = tag.find(lambda tag: tag.name == tagName)
            if not tag:
                return None
        result = tag.get(attrName)
        if not result and hasattr(tag, attrName):
            result = getattr(tag, attrName)
        if isinstance(result, list):
            result = result[0]
        return result

    def start_extraction(self, soup):
        return self.extract_data(soup, 'start')

    def extract_data(self, tree: BeautifulSoup, type: str):
        result = []
        childTypes = self.model[type]['childTypes']
        for childType in childTypes:
            canidates = self.findCanidates(tree, childType)
            result.extend(self.encodeData(canidates, childType))
        return result

    def findCanidates(self, tree: BeautifulSoup, childType: str):
        locatorDict = self.model[childType]['locatorDict']
        matchingFunc = Extractor.createMatchingFunc(locatorDict)
        return tree.find_all(matchingFunc)

    def encodeData(self, tags, type):
        result = []
        baseDict = self.getBaseDict(type)
        attrsToFind = {attrName: locatorDict for attrName,
                       locatorDict in baseDict.items() if isinstance(locatorDict, dict)}
        for tag in tags:
            validCanidate = True
            tagDict = baseDict.copy()
            tagDict['type'] = type
            for dataAttrName, locatorDict in attrsToFind.items():
                tagName = None
                if 'name' in locatorDict:
                    tagName = locatorDict['name']
                attrName = locatorDict['attr']
                if attrValue := Extractor.getAttr(tag, attrName, tagName):
                    tagDict[dataAttrName] = attrValue
                else:
                    validCanidate = False
                    break
            if validCanidate:
                if not self.model[type]['leaf']:
                    tagDict['children'] = self.extract_data(
                        tag, type)
                result.append(tagDict)
        return result

    def getBaseDict(self, childType: str):
        result = self.model[childType].copy()
        result.pop('locatorDict')
        result.pop('leaf')
        result.pop('childTypes')
        return result
