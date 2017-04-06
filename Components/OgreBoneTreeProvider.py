from DTO import OgreBoneTree

class OgreBoneTreeProvider:

    def __init__(self, ogreSkeleton):
        root = set(ogreSkeleton.BoneDictionary.keys()) - \
            set(ogreSkeleton.BoneHierarchyDictionary.keys())

        if (len(root) > 1):
            raise "More than one bone without a parent!"

        self.RootBoneName = root.pop()
        self.OgreSkeleton = ogreSkeleton
        self.__InverseHierarchy()

    def Fetch(self):
        return OgreBoneTree.OgreBoneTree(self.OgreSkeleton.BoneDictionary[self.RootBoneName], self.__FetchChildrenRecursively(self.RootBoneName))

    def __FetchChildrenRecursively(self, branchName):
        children = []
        if branchName in self.InverseHierarchy.keys():
            for boneName in self.InverseHierarchy[branchName]:
                children.append(OgreBoneTree.OgreBoneTree(self.OgreSkeleton.BoneDictionary[boneName], self.__FetchChildrenRecursively(boneName)))

        return children

    def __InverseHierarchy(self):
        self.InverseHierarchy = {}
        for boneParent in self.OgreSkeleton.BoneHierarchy:
            if (boneParent.Parent not in self.InverseHierarchy):
                self.InverseHierarchy[boneParent.Parent] = []

            self.InverseHierarchy[boneParent.Parent].append(boneParent.Bone)
