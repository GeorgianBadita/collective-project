from app.repository.IRepository import IRepository


class AbstractRepository(IRepository):

    def __init__(self, validator, db_instance, db_table):
        super().__init__(validator, db_instance, db_table)

    def add(self, entity):
        if not self.find_one(entity.get_id()):
            self._validator.validate(entity)
            self._db_instance.session.add(entity)
            self._db_instance.session.commit()
            return entity
        return None

    def find_one(self, entity_id):
        return self._db_table.query.get(entity_id)

    def update(self, entity):
        if not self.find_one(entity.get_id()):
            return None
        self.delete(entity.get_id())
        self.add(entity)
        return entity

    def delete(self, entity_id):
        if not self.find_one(entity_id):
            return None
        entity = self.find_one(entity_id)
        self._db_instance.session.delete(entity)
        self._db_instance.session.commit()
        return entity

    def find_all(self):
        return self._db_table.query.all()
