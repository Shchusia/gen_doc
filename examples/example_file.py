"""
Example file on how to document a file
"""
from abc import ABC, abstractmethod
from typing import List, Dict

CONST_VAL = 'first_test_const_value'
CONST_VAL_SECOND = {
    'value': 1
}


def decorator_factory(arg1, arg2, arg3) -> List[Dict]:
    def decorator(function):
        def wrapper(*args, **kwargs):
            if arg1:
                result = function(arg2, *args, **kwargs)
            else:
                result = function(arg3, *args, **kwargs)
            return result

        return wrapper

    return decorator


@decorator_factory(True, 2, arg3=3)
def test_func(arg, *args, **kwargs) -> List[Dict]:
    """
    Test function with decorator with parameters
    :param arg:
    :param args:
    :param kwargs:
    :return:
    """
    pass


class ExampleClass(ABC):
    _value = 'example'

    @property
    def value(self):
        """

        :return:
        """
        return self._value

    @value.setter
    def value(self, value) -> None:
        """
        setter
        :param value:
        :return:
        """
        self._value = value

    @abstractmethod
    def test_func(self):
        """
        class test function
        :return:
        """
        raise NotImplementedError

    @staticmethod
    def test_static(value: int, arg_1: Dict, arg_2: List[Dict]) -> Dict[str, str]:
        """
        test staticmethod
        :return:
        """
        pass

    async def run(self, arg) -> int:
        """
        async function
        :param arg:
        :return:
        """
        pass
