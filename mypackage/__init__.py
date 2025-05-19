
__all__ = ['Fruits', 'get_fruit', '_Fruits1']

class Fruits:
    one = 'banana'
    two = 'apple'

class Fruits1:
    one = 'coconut'
    two = 'orange'

class _Fruits1:
    one = 'coconut'
    two = 'orange'

def get_fruit():
    return [Fruits.one, Fruits.two]


