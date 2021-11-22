from catan.shared import GameObject, FieldType


class Road(GameObject):
    def __init__(self, position):
        super().__init__()
        self.position = position