class consoles:
    """Родительский класс игровых консолей"""

    def __init__(self, name: str, cost: int):
        self.name = name
        self.cost = cost

    def __str__(self):
        return f"Название:{self.name}. Цена:{self.cost}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, topic={self.cost!r})"


class sony(consoles):
    """Дочерний класс игровых консолей sony"""

    def __init__(self, name: str, cost: int, model: int):
        super().__init__(name, cost)
        if isinstance(model, int):
            if model > 0:
                self.model = model
            else:
                raise AttributeError("error number of model")
        else:
            raise AttributeError("error number of model")

    def __str__(self):
        return f"Марка консоли - {self.name}. Цена-{self.cost}. Номер модели-{self.model}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, topic={self.cost!r}, model={self.model!r})"


consoles1 = consoles('nintendo switch', 38000)
print(consoles1)
consoles2 = sony('play station', 51000, 5)
print(consoles2)
