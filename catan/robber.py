from catan.shared import GameObject, FieldType


class Robber(GameObject):
    def __init__(self):
        super().__init__()
        self.position = None