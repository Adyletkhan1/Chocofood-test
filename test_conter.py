import pytest
import counter
from unittest import mock
import builtins


def test_merge():
    with mock.patch('builtins.input', side_effect=['HACK 2'] ):
        assert counter.counterer() == 'AC \
AH \
AK \
CA \
CH \
CK \
HA \
HC \
HK \
KA \
KC \
KH'