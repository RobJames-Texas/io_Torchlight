from OgreBone import OgreBone
from OgreBoneParent import OgreBoneParent

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

    def __init__(self, xml):
        #print 'OgreSkeleton init from xml\n'
        self.Bones = []
        self.BoneHierarchy = []

        for bone in xml.find('bones').findall('bone'):
            self.Bones.append(OgreBone(bone))
        
        for boneParent in xml.find('bonehierarchy').findall('boneparent'):
            self.BoneHierarchy.append(OgreBoneParent(boneParent))
