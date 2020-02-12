# -*- coding: utf-8 -*-

import json
import yaml
import os
from sc_jsonnet.cli import find_snapcraft_file, parse_snapcraft_file

__author__ = "Daniel Llewellyn"
__copyright__ = "Daniel Llewellyn"
__license__ = "mit"


def test_find_snapcraft():
    assert find_snapcraft_file(os.path.join(
        os.path.dirname(__file__),
        "test1"
    )) == os.path.join(
        os.path.dirname(__file__),
        "test1",
        "snap",
        "local",
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
    def jsonstr(v):
        return json.dumps(v, sort_keys=True, indent=4, separators=(',', ': '))

    yaml_file = os.path.join(
        os.path.dirname(__file__),
        "test1",
        "snap",
        "snapcraft.yaml"
    )
    with open(yaml_file, "r") as f:
        yaml_doc = yaml.load(f, Loader=yaml.FullLoader)

        jsonnet_doc = json.loads(parse_snapcraft_file(
            find_snapcraft_file(os.path.join(
                os.path.dirname(__file__),
                "test1"
            ))))

        assert jsonstr(yaml_doc) == jsonstr(jsonnet_doc)
