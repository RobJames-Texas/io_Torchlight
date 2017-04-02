class OgreBoneParent(object):
    """
    <boneparent bone="Bip01" parent="root" />
    """

    def __init__(self, bone, parent):
        self.Bone = bone
        self.Parent = parent

    def __init__(self, xml):
        self.Bone = str(xml.get('bone'))
        self.Parent = str(xml.get('parent'))
