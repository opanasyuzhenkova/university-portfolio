'''CREATE TABLE user
(id int, height real, name text, deleted bool,
created DATETIME)
'''
class User():
    def __init__(self, id: str, height: float ,name: str, deleted:bool, created):
        self.__id = id
        self.__name = name
        self.__height = height
        self.__deleted = deleted
        self.__created = created
      

    def __call__(self):
      arg_list = []
      for attr in self.__dict__.values():
        arg_list.append(attr)
      return(arg_list)
      
    @property
    def name(self):
        return self.__name

    @property
    def height(self):
        return self.__height

    @property
    def deleted(self):
        return self.__deleted

    @property
    def created(self):
        return self.__created


    @name.setter # проверка на то, чтобы ИМЯ не начиналось с цифры и не было пустым
    def name(self, name):
        test = name.isdigit()
        print('test', test)
        if (test != False):
            self.__name = name
        else:
            print('Name can not contain numbers!')

    @height.setter
    def height(self, height):
        self.__height = height

    @deleted.setter
    def deleted(self, deleted):
        self.__deleted = deleted

    @name.deleter
    def name(self):
        self.__name = None

    @height.deleter
    def height(self):
        self.__height = None

    @deleted.deleter
    def deleted(self):
        self.__deleted = None


if __name__ == '__main__':
    print(__doc__)


    #u1 = User(101,1.75,'Nick',0,'2022-03-02 14:51:21')
    #u1()
    # print(u1.name)
    # u1.name = ''
    # print(u1.name)
    # del u1.name
    # print(u1.name)