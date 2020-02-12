# -*- coding: utf-8 -*-
"""
This is the main sc-jsonnet file.
"""

import argparse
import errno
import os
import sys
import logging
import urllib.request
import json
import yaml

import _jsonnet

from sc_jsonnet import __version__

__author__ = "Daniel Llewellyn"
__copyright__ = "Daniel Llewellyn"
__license__ = "mit"

_logger = logging.getLogger(__name__)

warning_header = """
## DO NOT EDIT THIS FILE ##
# This file is automatically generated by sc-jsonnet. To modify,
# edit snapcraft.jsonnet and run sc-jsonnet (from the snap store).
"""


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Snapcraft Jsonnet parser")
    parser.add_argument(
        "--version",
        action="version",
        version="sc-jsonnet {ver}".format(ver=__version__))
    parser.add_argument(
        "-o",
        "--output-file",
        dest="outfile",
        help="set the output file. Should be set to 'snap/snapcraft.yaml' " +
        "for compatibility.",
        type=str,
        metavar="STR",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO)
    parser.add_argument(
       "-vv",
       "--very-verbose",
       dest="loglevel",
       help="set loglevel to DEBUG",
       action="store_const",
       const=logging.DEBUG)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def try_path(dir, rel):
    if not rel:
        raise RuntimeError('Got invalid filename (empty string).')

    isUrl = False

    if rel[0:7] == 'http://' or rel[0:8] == 'https://':
        full_path = rel
        isUrl = True
    elif rel[0] == '/':
        full_path = rel
    else:
        full_path = dir + rel

    if isUrl:
        with urllib.request.urlopen(full_path) as f:
            if (f.getcode() == 200):
                return full_path, f.read().decode('utf-8')
            else:
                _logger.error("Error receiving remote {url}".format(
                    url=full_path), f.getcode())
                return full_path, None

    if not os.path.isfile(full_path):
        lib_path = os.path.join(os.path.dirname(__file__), "lib", full_path)
        snap_path = os.path.join("snap", full_path)
        snap_local_path = os.path.join("snap", "local", full_path)
        if os.path.isfile(snap_path):
            full_path = snap_path
        elif os.path.isfile(snap_local_path):
            full_path = snap_local_path
        elif os.path.isfile(lib_path):
            full_path = lib_path
        else:
            _logger.error(
                "Error opening {path}: is not a file (also tried"
                " [{snappath}, {snaplocalpath}, {libpath}])".format(
                    path=full_path, snappath=snap_path, libpath=lib_path,
                    snaplocalpath=snap_local_path))
            return full_path, None

    with open(full_path) as f:
        return full_path, f.read()


def import_callback(dir, rel):
    full_path, content = try_path(dir, rel)
    if content:
        return full_path, content
    raise FileNotFoundError(
        errno.ENOENT, os.strerror(errno.ENOENT), full_path)


def parse_snapcraft_file(path):
    with open(path, "r") as f:
        return _jsonnet.evaluate_snippet(
            "snippet",
            f.read(),
            import_callback=import_callback
        )


def find_snapcraft_file(dir):
    paths = [
        "snap/local/snapcraft.jsonnet",
        "snap/snapcraft.jsonnet",
        "snapcraft.jsonnet"
    ]
    for path in paths:
        p = os.path.join(dir, path)
        if os.path.isfile(p):
            return p

    raise FileNotFoundError(
        errno.ENOENT, os.strerror(errno.ENOENT), "snapcraft.jsonnet")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    try:
        json_string = parse_snapcraft_file(find_snapcraft_file(os.getcwd()))
        json_doc = json.loads(json_string)
        yaml_string = yaml.dump(json_doc)
        if args.outfile is not None:
            with open(args.outfile, "w") as f:
                f.write(warning_header)
                f.write(yaml_string)
        else:
            print(warning_header)
            print(yaml_string)
    except FileNotFoundError as e:
        print(e)
        print("""
Make sure you are executing sc-jsonnet within your project folder.

Your 'snapcraft.jsonnet' file should be located at:
    ./snap/snapcraft.jsonnet
""")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
