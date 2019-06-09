import pytest
import Capitalize
from unittest import mock
import builtins


def test_merge():
    with mock.patch('builtins.input', side_effect=[' 1 w 2 r 3 g'] ):
        assert Capitalize.solve() == ' 1 W 2 R 3 G'
        

    #1 w 2 r 3 g

    #1 W 2 R 3 g

    #132 456 Wq m e

    #132 456 Wq M E

    #hello world lol

    #Hello World Lol