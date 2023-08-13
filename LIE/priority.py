class priority:
    def __init__(self):
        self.__priority = 0

    @property
    def __priority__(self):
        return self.__priority

    def __lt__(self, other):
        try:
            return self.__priority__ < other.__priority__
        except:
            return self.__priority__ < other

    def __le__(self, other):
        try:
            return self.__priority__ <= other.__priority__
        except:
            return self.__priority__ <= other

    def __eq__(self, other):
        try:
            return self.__priority__ == other.__priority__
        except:
            return self.__priority__ == other

    def __ne__(self, other):
        try:
            return self.__priority__ != other.__priority__
        except:
            return self.__priority__ != other

    def __gt__(self, other):
        try:
            return self.__priority__ > other.__priority__
        except:
            return self.__priority__ > other

    def __ge__(self, other):
        try:
            return self.__priority__ >= other.__priority__
        except:
            return self.__priority__ >= other