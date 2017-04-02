class OgreAxis(object):

    """
    <axis x="0.707106" y="0.707107" z="0.000000"/>    
    """

    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z

    def __init__(self, xml):
        self.X = float(xml.get('x'))
        self.Y = float(xml.get('y'))
        self.Z = float(xml.get('z'))
