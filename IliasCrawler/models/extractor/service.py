def get_attr(tag, attrName):
    result = tag.get(attrName)
    if not result and hasattr(tag, attrName):
        result = getattr(tag, attrName)
    if isinstance(result, list):
        result = result[0]
    return result