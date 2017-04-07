from .OgreAxis import OgreAxisFromXml


class OgreRotation(object):
    """
    <rotation angle="3.141593">
        <axis x="0.707106" y="0.707107" z="0.000000"/>
    </rotation>
    """

    def __init__(self, angle, axis):
        self.Angle = angle
        self.Axis = axis


def OgreRotationFromXml(xml):
    angle = float(xml.get('angle'))
    axis = OgreAxisFromXml(xml.find('axis'))

    return OgreRotation(angle, axis)
