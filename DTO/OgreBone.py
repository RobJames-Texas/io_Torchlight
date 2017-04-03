from OgrePosition import OgrePositionFromXml
from OgreRotation import OgreRotationFromXml

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
        self.Rotation = rotation

def OgreBoneFromXml(xml):
    id = int(xml.get('id'))
    name = str(xml.get('name'))
    position = OgrePositionFromXml(xml.find('position'))
    rotation = OgreRotationFromXml(xml.find('rotation'))

    return OgreBone(id, name, position, rotation)

