def singleton(class_):
    """
    Create singleton class by decorating their class definition.
    :param class_:
    :return: A singleton instance
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance
