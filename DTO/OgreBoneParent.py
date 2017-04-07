class OgreBoneParent(object):
    """
    <boneparent bone="Bip01" parent="root" />
    """

    def __init__(self, bone, parent):
        self.Bone = bone
        self.Parent = parent


def OgreBoneParentFromXml(xml):
    bone = str(xml.get('bone'))
    parent = str(xml.get('parent'))

    return OgreBoneParent(bone, parent)
