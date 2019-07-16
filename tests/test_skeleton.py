# -*- coding: utf-8 -*-

import pytest
import os
from snapcraft_jsonnet.skeleton import find_snapcraft_file, parse_snapcraft_file

__author__ = "Daniel Llewellyn"
__copyright__ = "Daniel Llewellyn"
__license__ = "mit"


#def test_fib():
#    assert fib(1) == 1
#    assert fib(2) == 1
#    assert fib(7) == 13
#    with pytest.raises(AssertionError):
#        fib(-10)

def test_find_snapcraft():
    assert find_snapcraft_file(os.path.join(
        os.path.dirname(__file__),
        "test1"
    )) == os.path.join(
        os.path.dirname(__file__),
        "test1",
        "snap",
        "snapcraft.jsonnet"
    )

    assert find_snapcraft_file(os.path.join(
        os.path.dirname(__file__),
        "test2"
    )) == os.path.join(
        os.path.dirname(__file__),
        "test2",
        "snapcraft.jsonnet"
    )


def test_parse_snapcraft():
    yaml_file = os.path.join(
        os.path.dirname(__file__),
        "test1",
        "snap",
        "snapcraft.yaml"
    )
    with open(yaml_file, "r") as f:
        assert parse_snapcraft_file(find_snapcraft_file(os.path.join(
            os.path.dirname(__file__),
            "test1"
        ))) == f.read()
