import os
import subprocess as sp
from unittest import TestCase

class TestreadGFF(TestCase):
    def setUp(self):
        from urllib import request
        import gzip

        gff = 'ftp://ftp.flybase.net/releases/FB2016_04/dmel_r6.12/gff/dmel-all-r6.12.gff.gz'
        self.gffname = '/tmp/dmel-all-r6.12.gff.gz'

        gtf = 'ftp://ftp.flybase.net/releases/FB2016_04/dmel_r6.12/gtf/dmel-all-r6.12.gtf.gz'
        self.gtfname = '/tmp/dmel-all-r6.12.gtf.gz'
    
        # Download URLs unless I already have a copy
        if not os.path.exists(self.gffname):
            request.urlretrieve(gff, filename=self.gffname)

        if not os.path.exists(self.gtfname):
            request.urlretrieve(gtf, filename=self.gtfname)

        # Extract gz's
        if not os.path.exists(self.gffname.strip('.gz')):
            proc1 = sp.check_call('gunzip -c {0} > {1}'.format(self.gffname, self.gffname.strip('.gz')), shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

        if not os.path.exists(self.gtfname.strip('.gz')):
            proc2 = sp.check_call('gunzip -c {0} > {1}'.format(self.gtfname, self.gtfname.strip('.gz')), shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    def tearDown(self):
        pass
        # Delete the extracted files
        #os.unlink(self.gffname.strip('.gz'))
        #os.unlink(self.gtfname.strip('.gz'))

        # Delete created databases
        #os.unlink(self.gffname.strip('.gz') + '.db')
        #os.unlink(self.gtfname.strip('.gz') + '.db')

    def test_readGFF_zipped_gff(self):
        from gtf2IntronBed import readGFF
        readGFF(self.gffname)
        




if __name__ == '__main__':
    import unittest


    unittest.main()
