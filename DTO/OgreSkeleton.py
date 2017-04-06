from . import OgreBone
from . import OgreBoneParent

class OgreSkeleton(object):
    """
    <skeleton>
      <bones>
        ...
      </bones>
      <bonehierarchy>
        <boneparent bone="Bip01" parent="root" />
        <boneparent bone="tag_zfishlureend" parent="root" />
        ...
      </bonehierarchy>
    </skeleton>
    """

    def __init__(self, bones, boneHierarchy):
        self.Bones = bones
        self.BoneHierarchy = boneHierarchy
        self.__BuildDictionaries()

    def __BuildDictionaries(self):
        self.BoneDictionary = {}
        self.BoneHierarchyDictionary = {}

        for bone in self.Bones:
            self.BoneDictionary[bone.Name] = bone

        for boneParent in self.BoneHierarchy:
            self.BoneHierarchyDictionary[boneParent.Bone] = boneParent

def OgreSkeletonFromXml(xml):
    #print 'OgreSkeleton init from xml\n'
    bones = []
    boneHierarchy = []

    for bone in xml.find('bones').findall('bone'):
        bones.append(OgreBone.OgreBoneFromXml(bone))
    
    for boneParent in xml.find('bonehierarchy').findall('boneparent'):
        boneHierarchy.append(OgreBoneParent.OgreBoneParentFromXml(boneParent))

    return OgreSkeleton(bones, boneHierarchy)
