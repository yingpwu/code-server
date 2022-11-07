from pprint import pprint as print


class User:
    def __new__(cls, *args):
        print("in new")
        return super().__new__(cls)

    def __init__(self, name) -> None:
        print("in init")
        self.name = name
# user=User("wangwu")


class ModelMeta(type):
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)

        return super().__new__(cls, *args, **kwargs)


class Next(metaclass=ModelMeta):
    name = "name1"
    age = "age1"

    def __init__(cls):
        field = []
        for name in dir(cls):
            unbound_field = getattr(cls, name)
            field.append(unbound_field)

            if hasattr(unbound_field, "_formfield"):
                print("this is an undoun_field attribute")
        print(field)


model = Next()
