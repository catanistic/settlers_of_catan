from catan.shared.schema import Schema


def id_generator():
    id = 0
    while True:
        yield id
        id += 1


class GameObject():
    id_generator = id_generator()

    def __init__(self):
        self.schema = Schema()
        self.object_id = next(self.id_generator)

    @property
    def id(self):
        """Returns unique id of the game object.
        """
        return self.object_id

    def observation(self, spectator_id=None):
        """Returns observation that is pertinent to the object.

        Args:
            spectator_id: The id for the spectator of the game Object.
                          This can affect the observation in cases with hidden information.
        """
        raise NotImplementedError()