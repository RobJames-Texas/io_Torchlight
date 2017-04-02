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
