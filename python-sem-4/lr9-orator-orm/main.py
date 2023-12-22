import orator


config = {
    'sqlite': {
        'driver': 'sqlite',
        'database': ':memory:',
    }
}


class User(orator.Model):
    __timestamps__ = False
    __table__ = 'user'
    __guarded__ = ['id']
    __fillable__ = ['name', 'height', 'deleted1', 'created1']

    @property
    def data(self):
        return (self.id, self.name, self.height, self.deleted1, self.created1)

def allUsers():
    for i in User.all():
        print(i.data)


if __name__ == '__main__':
    db = orator.DatabaseManager(config)
    orator.Model.set_connection_resolver(db)
    schema = orator.Schema(db)
    try:
        with schema.create('user') as table:
            table.increments('id')
            table.string('name')
            table.decimal('height', 3, 2).nullable()
            table.boolean('deleted1').nullable()
            table.date('created1').nullable()
    except orator.exceptions.query.QueryException:
        pass



    u1 = User.first_or_create(name='Mary', height=1.55, deleted1=0, created1='2022-06-11 17:55:35')
    allUsers()

    u1.name = 'Nick'
    u1.save()
    allUsers()