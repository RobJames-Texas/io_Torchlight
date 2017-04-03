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

        print(root)

        ogreSkeleton = OgreSkeleton(root)

        self.assertTrue(len(ogreSkeleton.Bones) == 50)
        self.assertTrue(len(ogreSkeleton.BoneHierarchy) == 49)
        self.assertTrue('root' in ogreSkeleton.BoneDictionary)
        self.assertTrue('Bip01 Head' in ogreSkeleton.BoneDictionary)
        self.assertTrue('root' not in ogreSkeleton.BoneHierarchyDictionary)
        same = set(ogreSkeleton.BoneDictionary.keys()) & set(ogreSkeleton.BoneHierarchyDictionary.keys())
        self.assertTrue(len(same) == 49)
        diff = set(ogreSkeleton.BoneDictionary.keys()) - set(ogreSkeleton.BoneHierarchyDictionary.keys())
        self.assertTrue(len(diff) == 1)
        self.assertTrue('root' in diff)

        print('Vanquisher skeleton loaded properly.\n')


if __name__ == '__main__':
    unittest.main()
