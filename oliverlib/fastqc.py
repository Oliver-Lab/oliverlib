#!/usr/bin/env python
""" Quick and dirty Fastqc parser """
import os
import pandas as pd
from io import StringIO

class FastQC(object):
    def __init__(self, id, filename):
        """ Parse a FastQC data file """
        self.filename = filename
        self.id = id
        self.blocks = {}

    def _parser(self)
        with open(self.filename, 'r') as fh:
            currBlock = None
            for row in fh:
                if row:
                    if row.startswith('##FastQC'):
                        self.version = row.split()[1]
                    elif row == '>>END_MODULE':
                        self.blocks.update(FastQCBlock(currBlock))
                        currBlock = None
                    elif (row.startswith('>>'):
                        currBlock = [row.lstrip('>>').rstip()]
                    else:
                        currBlock.append(row.rstip())



class FastQCBlock(object):
    def __init__(self, block):
    self.id = block[0].split()[0]
    self.status = block[0].split('\t')[1]
    block[1] = block[1].lstrip('#')
    block_str = '\n'.join(block[1:])
    self.df = pd.read_csv(StringIO(block_str), sep='\t')
