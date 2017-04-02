from OgrePosition import OgrePosition
from OgreRotation import OgreRotation

class OgreBone(object):
    """
    <bone id="42" name="root">
        <position x="-0.000000" y="0.000284" z="-0.000000"/>
        <rotation angle="3.141593">
            <axis x="0.707106" y="0.707107" z="0.000000"/>
        </rotation>
    </bone>
    """
    def __init__(self, id, name, position, rotation):
        self.Id = id
        self.Name = name
        self.Position = position
        self.Rotation = Rotation

    def __init__(self, xml):
        self.Id = int(xml.get('id'))
        self.Name = str(xml.get('name'))
        self.Position = OgrePosition(xml.find('position'))
        self.Rotation = OgreRotation(xml.find('rotation'))

