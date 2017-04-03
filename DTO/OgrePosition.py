class OgrePosition(object):

    """
    <position x="-0.000000" y="0.000284" z="-0.000000"/>
    """

    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z

def OgrePositionFromXml(xml):
    x = float(xml.get('x'))
    y = float(xml.get('y'))
    z = float(xml.get('z'))
    
    return OgrePosition(x, y, z)

