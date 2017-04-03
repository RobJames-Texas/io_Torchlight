import unittest
import xml.etree.ElementTree as ET
import sys
import os
sys.path.append(os.path.abspath("../DTO"))
sys.path.append(os.path.abspath("../Providers"))
from OgreSkeleton import OgreSkeletonFromXml
from OgreBoneTreeProvider import OgreBoneTreeProvider

class OgreBoneTreeTests(unittest.TestCase):
    def setUp(self):
        xml = ET.parse('Vanquisher.skeleton.xml')
        self.XmlRoot = xml.getroot()

    def test_CanCreate(self):
        ogreSkeleton = OgreSkeletonFromXml(self.XmlRoot)
        tree = OgreBoneTreeProvider(ogreSkeleton).Fetch()

        self.assertEqual('root', tree.OgreBone.Name, 'first bone should be root')
        self.assertNotEqual(0, len(tree.Children), 'root bone should have children.')
        self.assertEqual('Bip01', tree.Children[0].OgreBone.Name)

        print('\nPASS: OgreBoneTree.Create')

if __name__ == '__main__':
    unittest.main()
