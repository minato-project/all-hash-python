from unittest import TestCase
import urlparse
import skein_hash
import weakref
import binascii
import StringIO

from binascii import unhexlify


class Test(TestCase):

    def test_powhash(self):
        teststart = '700000005d385ba114d079970b29a9418fd0549e7d68a95c7f168621a314201000000000578586d149fd07b22f3a8a347c516de7052f034d2b76ff68e0d6ecff9b77a45489e3fd511732011df0731000';
        testbin = unhexlify(teststart)
        hash_bin = skein_hash.getPoWHash(testbin)
        self.assertEqual(hash_bin, unhexlify('c5286459ea4716b77ab979a1bc0198c996adb57d15fb848d99f7a85e83c7eee4'))
