class OgreAxis(object):

    """
    <axis x="0.707106" y="0.707107" z="0.000000"/>
    """

    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z


def OgreAxisFromXml(xml):
    x = float(xml.get('x'))
    y = float(xml.get('y'))
    z = float(xml.get('z'))

    return OgreAxis(x, y, z)
