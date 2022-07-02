class TemplateModule:
    def __init__(self, name):
        self.__name = name

    def render(self, device):
        raise NotImplementedError

    def get_name(self):
        """
        Return the name of the module
        """
        return self.__name
