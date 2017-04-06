import unittest
import xml.etree.ElementTree as ET
from Components import OgreBoneTreeProvider
from DTO import OgreSkeleton

class OgreBoneTreeTests(unittest.TestCase):
    def setUp(self):
        xml = ET.parse('Tests\Vanquisher.skeleton.xml')
        self.XmlRoot = xml.getroot()

    def test_CanCreate(self):
        ogreSkeleton = OgreSkeleton.OgreSkeletonFromXml(self.XmlRoot)
        provider = OgreBoneTreeProvider.OgreBoneTreeProvider(ogreSkeleton)
        tree = provider.Fetch()

        self.assertEqual('root', tree.OgreBone.Name, 'first bone should be root')
        self.assertNotEqual(0, len(tree.Children), 'root bone should have children.')
        self.assertEqual('Bip01', tree.Children[0].OgreBone.Name)

        print('\nPASS: OgreBoneTree.Create')

if __name__ == '__main__':
    unittest.main()
