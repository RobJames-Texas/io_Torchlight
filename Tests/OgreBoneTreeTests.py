import unittest
import xml.etree.ElementTree as ET
from io_Torchlight.Components.OgreBoneTreeProvider import OgreBoneTreeProvider
from io_Torchlight.DTO.OgreSkeleton import OgreSkeletonFromXml


class OgreBoneTreeTests(unittest.TestCase):
    def setUp(self):
        testFile = 'io_Torchlight\Tests\Vanquisher.skeleton.xml'
        xml = ET.parse(testFile)
        self.XmlRoot = xml.getroot()

    def test_CanCreate(self):
        ogreSkeleton = OgreSkeletonFromXml(self.XmlRoot)
        provider = OgreBoneTreeProvider(ogreSkeleton)
        tree = provider.Fetch()

        self.assertEqual(
            'root', tree.OgreBone.Name,
            'first bone should be root')
        self.assertNotEqual(
            0, len(tree.Children),
            'root bone should have children.')
        self.assertEqual(
            'Bip01',
            tree.Children[0].OgreBone.Name)

        print('\nPASS: OgreBoneTree.Create')

if __name__ == '__main__':
    unittest.main()
