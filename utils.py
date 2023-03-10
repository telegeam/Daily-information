import pprint
import os
import cachetools
from colorama import Fore
from shelved_cache import PersistentCache
from cachetools import LRUCache

# 指定缓存路径为脚本所在目录
basePath = os.path.dirname(os.path.abspath(__file__))
filename = basePath + os.sep + "mycache.pc"
pc = PersistentCache(LRUCache, filename, maxsize=10)

class Cache:
    @staticmethod
    def check_first(x):
        """
        检查是否首次调用
        """
        if pc.__contains__(x):
            return False
        pc[x] = 1
        return True

    @staticmethod
    def close():
        """
        关闭缓存文件
        """
        pc.close()

class Color:
    @staticmethod
    def print_focus(data: str):
        print(Fore.YELLOW+data+Fore.RESET)

    @staticmethod
    def print_success(data: str):
        print(Fore.LIGHTGREEN_EX+data+Fore.RESET)

    @staticmethod
    def print_failed(data: str):
        print(Fore.LIGHTRED_EX+data+Fore.RESET)

    @staticmethod
    def print(data):
        pprint.pprint(data)


class Pattern:
    @staticmethod
    def create(length: int=8192):
        pattern = ''
        parts = ['A', 'a', '0']
        while len(pattern) != length:
            pattern += parts[len(pattern) % 3]
            if len(pattern) % 3 == 0:
                parts[2] = chr(ord(parts[2]) + 1)
                if parts[2] > '9':
                    parts[2] = '0'
                    parts[1] = chr(ord(parts[1]) + 1)
                    if parts[1] > 'z':
                        parts[1] = 'a'
                        parts[0] = chr(ord(parts[0]) + 1)
                        if parts[0] > 'Z':
                            parts[0] = 'A'
        return pattern

    @staticmethod
    def offset(value: str, length: int=8192):
        return Pattern.create(length).index(value)
