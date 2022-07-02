import manager.Pixoo as p


class Manager:
    __modules = []
    __device = None

    def __init__(self):
        self.__device = p.Pixoo(host="11:75:58:BD:0C:34")
        self.__device.connect()

    def register_module(self, module):
        self.__modules.append(module)

    def get_modules(self):
        return self.__modules

    def get_device(self):
        return self.__device
