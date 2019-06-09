import pytest
import polar
from unittest import mock
import builtins


def test_merge():
    with mock.patch('builtins.input', side_effect=['1+2j'] ):
        assert polar.polar() == (2.23606797749979, 1.1071487177940904)
        