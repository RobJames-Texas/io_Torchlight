import unittest
import xml.etree.ElementTree as ET
import sys
import os
sys.path.append(os.path.abspath("../DTO"))
from OgreSkeleton import OgreSkeleton

class XmlToOgreSkeletonTest(unittest.TestCase):

    def test_CanFill(self):
        tree = ET.parse('Vanquisher.skeleton.xml')
        root = tree.getroot()

        print root

        ogreSkeleton = OgreSkeleton(root)

        self.assertTrue(len(ogreSkeleton.Bones) == 50)
        self.assertTrue(len(ogreSkeleton.BoneHierarchy) == 49)
        
        print 'Vanquisher skeleton loaded properly.\n'

if __name__ == '__main__':
    unittest.main()
