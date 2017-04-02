from OgreAxis import OgreAxis

class OgreRotation(object):
    """
    <rotation angle="3.141593">
        <axis x="0.707106" y="0.707107" z="0.000000"/>
    </rotation>
    """

    def __init__(self, angle, axis):
        self.Angle = angle
        self.Axis = axis

    def __init__(self, xml):
        self.Angle = float(xml.get('angle'))
        self.Axis = OgreAxis(xml.find('axis'))
