class Colors:
    def __init__(self):
        self.rgb = ['red', 'green', 'blue']

    # on définit d'autres méthodes pour Color ...

    def __iter__(self):
        return self.ColorIterator(self)

    class ColorIterator:
        def __init__(self, colors):
            self.__colors = colors
            self.__index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.__index >= len(self.__colors):
                raise StopIteration

            color = self.__colors[self.__index]
            self.__index += 1
            return color
