def get_val(collection, key=None, default='git'):
    if key:
        if key in collection:
            return collection[key]
        return default
    return default
