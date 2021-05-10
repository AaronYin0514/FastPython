PI = 3.14
_MY_PI = 3.14

def sayHello():
    print('Hello,Python')

def _mySayHello():
    print('Hello,Python')

class Person(object):
    def __str__(self):
        return '我是Person对象'

class _Person(object):
    def __str__(self):
        return '我是_Person对象'



