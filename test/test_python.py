import json
import unittest
import os.path as path
import subprocess as sp

class PythonTest(unittest.TestCase):

    # execute the lamp to specify package.json
    def __init__(self, *args, **kwargs):
        super(PythonTest, self).__init__(*args, **kwargs)

        # execute the lampy and resolve the package.json
        sp.call(['python3', path.join('..', 'lamp.py'), 'package.json'])

        self.package = json.load(open('package.json'))
        self.msg     = 'The resolved version of {}'

    '''
    n, m and o represents a constants
    x represents a range
    '''

    # test for the range ^n.m.o
    def test_express(self):
        # Arrange
        version = self.package['dependencies']['express']
        # Act
        resolved = '4.13.0'
        # Assert
        self.assertEqual(version, resolved, self.msg.format('express'))

    # test for the range ~n.m.o
    def test_lodash(self):
        # Arrange
        version = self.package['dependencies']['lodash']
        # Act
        resolved = '3.9.3'
        # Assert
        self.assertEqual(version, resolved, self.msg.format('lodash'))

    # test for a specify range n.m.o
    def test_mocha(self):
        # Arrange
        version = self.package['devDependencies']['mocha']
        # Act
        resolved = '2.2.0'
        # Assert
        self.assertEqual(version, resolved, self.msg.format('mocha'))

    # test for a unexisted range in specify date
    def test_mongoose(self):
        # Arrange
        version = self.package['devDependencies']['mongoose']
        # Act
        resolved = '^4.5.9'
        # Assert
        self.assertEqual(version, resolved, self.msg.format('mongoose'))

    # test for the range ^n.x
    def test_socket_io(self):
        # Arange
        version = self.package['peerDependencies']['socket.io']
        # Act
        resolved = '1.3.5'
        # Assert
        self.assertEqual(version, resolved, self.msg.format('socket.io'))

    # test for the range n.x
    def test_jsdom(self):
        # Arange
        version = self.package['peerDependencies']['jsdom']
        # Act
        resolved = '4.5.2'
        # Assert
        self.assertEqual(version, resolved, self.msg.format('jsdom'))

    # test for the range *
    def test_react(self):
        # Arange
        version = self.package['optionalDependencies']['react']
        # Act
        resolved = '0.14.0-alpha3'
        # Assert
        self.assertEqual(version, resolved, self.msg.format('react'))

    # test for the range latest
    def test_validate_npm_pn(self):
        # Arange
        version = self.package['optionalDependencies']['validate-npm-package-name']
        # Act
        resolved = '2.2.1'
        # Assert
        self.assertEqual(version, resolved, self.msg.format('validate-npm-package-name'))

    # test for the range >= n.m
    def test_mongodb(self):
        # Arange
        version = self.package['optionalDependencies']['mongodb']
        # Act
        resolved = '2.1.0-alpha'
        # Assert
        self.assertEqual(version, resolved, self.msg.format('mongodb'))

    # test for the range ^n.x || ^n
    def test_jsdom_other(self):
        # Arange
        version = self.package['optionalDependencies']['jsdom']
        # Act
        resolved = '5.5.0'
        # Assert
        self.assertEqual(version, resolved, self.msg.format('jsdom'))

if __name__ == '__main__':
    unittest.main()