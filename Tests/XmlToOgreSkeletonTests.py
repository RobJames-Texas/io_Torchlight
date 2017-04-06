import unittest
import xml.etree.ElementTree as ET
from DTO.OgreSkeleton import OgreSkeletonFromXml

class XmlToOgreSkeletonTests(unittest.TestCase):

    def test_CanFill(self):
        tree = ET.parse('Tests\Vanquisher.skeleton.xml')
        root = tree.getroot()

        ogreSkeleton = OgreSkeletonFromXml(root)

        self.assertEqual(50, len(ogreSkeleton.Bones), 'incorrect number of elements in Bones')
        self.assertEqual(49, len(ogreSkeleton.BoneHierarchy), 'incorrect number of elements in BoneHierarchy')
        self.assertTrue('root' in ogreSkeleton.BoneDictionary, 'BoneDictionary should contain ''root''')
        self.assertTrue('Bip01 Head' in ogreSkeleton.BoneDictionary, 'BoneDictionary should contain ''Bip01 Head''')
        self.assertTrue('root' not in ogreSkeleton.BoneHierarchyDictionary, 'BoneHierarchyDictionary should NOT contain ''root''')
        same = set(ogreSkeleton.BoneDictionary.keys()) & set(ogreSkeleton.BoneHierarchyDictionary.keys())
        self.assertEqual(49, len(same), 'incorrect number of keys are the same between BoneDictionary and BoneHierarchy')
        diff = set(ogreSkeleton.BoneDictionary.keys()) - set(ogreSkeleton.BoneHierarchyDictionary.keys())
        self.assertEqual(1, len(diff), 'incorrect number of keys are different between BoneDictionary and BoneHierarchy')
        self.assertTrue('root' in diff, 'the ''root'' bone should be in the difference between BoneDictionary and BoneHierarchy')

        print('\nPASS: OgreSkeleton load from xml')

if __name__ == '__main__':
    unittest.main()
