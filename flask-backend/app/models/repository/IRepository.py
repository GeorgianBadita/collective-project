
class IRepository:
    def __init__(self, validator, db_instance):
        self._validator = validator
        self._db_instance = db_instance

    def add(self, entity):
        raise NotImplementedError("Add function not implemented")

    def find_one(self, entity_id):
        raise NotImplementedError("Find function not implemented")

    def update(self, entity):
        raise NotImplementedError("Update function not implemented")

    def delete(self, entity_id):
        raise NotImplementedError("Delete function not implemented")

    def find_all(self, entity):
        raise NotImplementedError("Find All function not implemented")
