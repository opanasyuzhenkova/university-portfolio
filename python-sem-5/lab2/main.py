import re
import requests
import sys
from urllib.request import urlopen
from importlib.abc import PathEntryFinder
from importlib.util import spec_from_loader


def url_hook(some_str):
    '''Получает строку URL, возвращает URL и множество имен, которое мы извлекли (точка входа, которая запускает все остальное)'''
    try:
        page = requests.get(some_str)
        filenames = re.findall("[a-zA-Z_][a-zA-Z0-0_]*.py", page.text)
        modnames = {name[:-3] for name in filenames}
        return URLFinder(some_str, modnames)
    except:
        raise ImportError


sys.path_hooks.append(url_hook)
print(sys.path_hooks)


class URLFinder(PathEntryFinder):
    def __init__(self, url, available):
        self.url = url
        self.available = available

    def find_spec(self, name, target=None):
        '''Поиск содержимого модуля'''
        if name in self.available:
            origin = "{}/{}.py".format(self.url, name)
            loader = URLLoader()
            return spec_from_loader(name, loader, origin=origin)

        else:
            return None


class URLLoader:
    '''Выполнение импортируемого модуля'''
    def create_module(self, target):
        return None

    def exec_module(self, module):
        with urlopen(module.__spec__.origin) as page:
            source = page.read()
        code = compile(source, module.__spec__.origin, mode="exec")
        exec(code, module.__dict__)
