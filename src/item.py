class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        def on_take():
            pass
        def on_drop():
            pass


class LightSource(Item):
    def __init__(self, name, description, lightUsed=False):
        super().__init__(name, description)
        self.lightUsed = lightUsed