#!/usr/bin/env python
import unittest
from oliverlib import fastqc

BLOCK = """>>Per base sequence quality	pass
#Base	Mean	Median	Lower Quartile	Upper Quartile	10th Percentile	90th Percentile
1	33.325882537780295	34.0	34.0	34.0	31.0	34.0
2	33.44737950739895	34.0	34.0	34.0	31.0	34.0
3	33.446659779075645	34.0	34.0	34.0	31.0	34.0
4	36.67489445866323	37.0	37.0	37.0	37.0	37.0
5	36.658260994356844	37.0	37.0	37.0	35.0	37.0
6	36.65553688182567	37.0	37.0	37.0	35.0	37.0
7	36.65730974503444	37.0	37.0	37.0	35.0	37.0
8	36.62655009906297	37.0	37.0	37.0	35.0	37.0
9	38.53114508354548	39.0	39.0	39.0	38.0	39.0
10	38.47594460091534	39.0	39.0	39.0	37.0	39.0
"""

class TestFastqc(unittest.TestCase):
    def setUp(self):
        self.filename = 'tests/data/fastqc_data.txt'
        self.id = 'test'

    def tearDown(self):
        pass

    def test_FastQCBlock(self)
        fq = fastqc.FastQCBlock(BLOCK.split('\n'))
        print(fq.df)


if __name__ == '__main__':
    unittest.main()

