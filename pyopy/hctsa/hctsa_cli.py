# coding=utf-8
"""Command-line access to some tools to manage HCTSA."""
import argh

from pyopy.hctsa.hctsa_bindings_gen import gen_bindings
from pyopy.hctsa.hctsa_install import install
from pyopy.hctsa.hctsa_catalog import summary


if __name__ == '__main__':
    parser = argh.ArghParser()
    parser.add_commands([
        # matlab world installation
        install,
        # python-land binding generation
        gen_bindings,
        # catalog summary
        summary,
    ])
    parser.dispatch()
