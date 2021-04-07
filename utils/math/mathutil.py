import numpy as np


# 基础的数学工具类
class MathUtil:

    @staticmethod
    def isContact(verctor1, verctor2, threshold=8.0):
        x = (verctor1.x - verctor2.x) ** 2
        y = (verctor1.y - verctor2.y) ** 2
        z = (verctor1.z - verctor2.z) ** 2
        distance = np.sqrt(x + y + z)
        result = True if (distance <= threshold) else False
        return distance, result

    @staticmethod
    def getAngle(vector1, vector2):
        """Return the angle between two vectors in degrees."""
        v1 = vector1.to_points()
        v2 = vector2.to_points()
        vector_dot = np.dot(v1, v2)
        v1norm = np.sqrt(vector1.x ** 2 + vector1.y ** 2 + vector1.z ** 2)
        v2norm = np.sqrt(vector2.x ** 2 + vector2.y ** 2 + vector2.z ** 2)
        angle = np.arccos(vector_dot / (v1norm * v2norm)) * 180 / np.pi
        return angle
