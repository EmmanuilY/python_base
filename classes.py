class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

# Создание нескольких "экземпляров"
a = Singleton()
b = Singleton()

# Проверка того, что a и b являются одним и тем же объектом
print(a is b)  # Выведет: True


"""
Регистрация подклассов: Метаклассы можно использовать для автоматической регистрации подклассов при их создании. 
Это может быть полезно, например, в фреймворках, которые используют подклассы для определения расширений или плагинов:
"""
class PluginMeta(type):
    plugins = []

    def __init__(cls, name, bases, attrs):
        if not attrs.get('abstract', False):
            PluginMeta.plugins.append(cls)
        super().__init__(name, bases, attrs)

class Plugin(metaclass=PluginMeta):
    abstract = True

class MyPlugin(Plugin):
    pass

print(PluginMeta.plugins)  # [<class '__main__.MyPlugin'>]


class MyClass:
    __slots__ = ('name', 'age')

obj = MyClass()
obj.name = "John"  # это ок
obj.age = 20  # это тоже ок

obj.height = 180  # это приведет к ошибке AttributeError
"""
Специальный атрибут класса __slots__ в Python используется для ограничения количества атрибутов, которые объекты данного класса могут иметь. 
Это также может помочь улучшить производительность и уменьшить использование памяти, ограничивая внутреннее представление объектов.
"""