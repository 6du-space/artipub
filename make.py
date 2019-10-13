#!/usr/bin/env python3

from os.path import dirname,abspath,join
from os import walk
from config import CONFIG
from mako.template import Template
from pathlib import Path

CONFIG = dict((k,v) for k,v in CONFIG.__dict__.items() if not k.startswith("_"))

ROOT = dirname(abspath(__file__))
TEMPLATE = "template"
LEN = len(ROOT)+1+len(TEMPLATE)+1


def make(file):

    with open(file) as f:
        txt = f.read()
        outfile = join( ROOT, "dist", file[LEN:])
        Path(
            dirname(
                outfile
            )
        ).mkdir(parents=True, exist_ok=True)
        with open(outfile, "w") as out:
            out.write(Template(txt).render(**CONFIG))


def main():
    for root, dirs, files in walk(join(ROOT, TEMPLATE)):
        for i in files:
           make(join(root,i))


if __name__ == "__main__":
  main()
