#!/usr/bin/env python
"""
Modelica parse Tree to AST tree.
"""
from __future__ import print_function, absolute_import, division, print_function, unicode_literals

import os
import sys
import unittest
import time

from pymola import parser
from pymola import tree
from pymola import gen_sympy

import jinja2

TEST_DIR = os.path.dirname(os.path.realpath(__file__))

class GenSympyTest(unittest.TestCase):
    "Testing"

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def flush(self):
        sys.stdout.flush()
        sys.stdout.flush()
        time.sleep(0.01)

    def test_estimator(self):
        with open(os.path.join(TEST_DIR, 'Estimator.mo'), 'r') as f:
            txt = f.read()
        ast_tree = parser.parse(txt)
        text = gen_sympy.generate(ast_tree, 'Estimator')
        with open(os.path.join(TEST_DIR, 'generated/Estimator.py'), 'w') as f:
           f.write(text)
        from generated.Estimator import Estimator as Estimator
        e = Estimator()
        res = e.simulate(x0=[1])
        self.flush()

    def test_spring(self):
        with open(os.path.join(TEST_DIR, 'Spring.mo'), 'r') as f:
            txt = f.read()
        ast_tree = parser.parse(txt)
        text = gen_sympy.generate(ast_tree, 'Spring')
        with open(os.path.join(TEST_DIR, 'generated/Spring.py'), 'w') as f:
           f.write(text)
        from generated.Spring import Spring as Spring
        e = Spring()
        res = e.simulate(x0=[1, 1])
        self.flush()

    def test_aircraft(self):
        with open(os.path.join(TEST_DIR, 'Aircraft.mo'), 'r') as f:
            txt = f.read()
        ast_tree = parser.parse(txt)
        text = gen_sympy.generate(ast_tree, 'Aircraft')
        with open(os.path.join(TEST_DIR, 'generated/Aircraft.py'), 'w') as f:
          f.write(text)
        # from generated.Aircraft import Aircraft as Aircraft
        #e = Aircraft()
        #res = e.simulate()
        self.flush()

    def test_connector(self):
        with open(os.path.join(TEST_DIR, 'Connector.mo'), 'r') as f:
            txt = f.read()
        ast_tree = parser.parse(txt)
        # print(ast_tree)

        flat_tree = tree.flatten(ast_tree, 'Aircraft')
        print(flat_tree)

        text = gen_sympy.generate(ast_tree, 'Aircraft')
        print(text)
        self.flush()

if __name__ == "__main__":
    unittest.main()
