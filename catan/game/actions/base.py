from catan.shared.object import GameObject 

class Action(GameObject):
    def __init__(self, actor_id):
        self.actor_id = actor_id
        self.executed = False

    def execute(self, shared_state, actor_collection, board):
        if self.executed:
            raise RuntimeError("Action was already executed.")
        raise NotImplementedError()

    def undo(self, shared_state, actor_collection, board):
        if not self.executed:
            raise RuntimeError("Action has not been executed yet.")