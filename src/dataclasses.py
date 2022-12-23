"""
Define the JSON schemas of the REST API input/output data
"""

import logging
from dataclasses import field
from enum import Enum

from pydantic.dataclasses import dataclass

logger = logging.getLogger(__name__)


class MyEnum(Enum):
    """ Some enumeration """
    CHOICE1 = 'Good choice'
    CHOICE2 = 'Hum'
    CHOICE3 = 'Bad choice !'


@dataclass
class MyCustomData:
    """ Some custom dataclass. """

    my_first_field: int = field(metadata=dict(title='My first field'))
    my_second_field: str = field(metadata=dict(title='My second field'))

    @property
    def my_property(self) -> MyEnum:
        """ Returns some enumeration member based on object's field. """
        return MyEnum(self.my_second_field)


@dataclass
class InputData:
    """ Input data of the REST API. """

    some_input_field: int = field(metadata=dict(
        title='Some input field',
        description='A field of type "integer"'
    ))
    some_other_input_field: list[MyCustomData] = field(metadata=dict(
        title='Another input field',
        description='A field with contains a list of some custom objects.'
    ))

    @classmethod
    def parse_file(cls, path) -> 'InputData':
        """ Parse input data from a .json file. """
        return cls.__pydantic_model__.parse_file(path=path)


@dataclass
class OutputData:
    """ Output data of the REST API. """

    some_output_field: MyCustomData = field(metadata=dict(
        title='Some output field',
        description='Some description'
    ))
    some_other_output_field: float = field(metadata=dict(
        title='Some other output field',
        description='Some description'
    ))
    some_last_output_field: str = field(metadata=dict(
        title='Some last output field',
        description='Some description'
    ))
