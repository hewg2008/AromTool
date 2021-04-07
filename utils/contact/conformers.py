'''任务描述：
输入两个芳香环.xyz文件（一个构象(conformer)， 输出多个构象（conformers）.xyz文件。
构象产生规则：1 每个单独的环内部相应位置不变，即环是刚性的。
             2 一个环保持不变，通过平移（translate), 旋转(rotate)另外一个环产生不同的构象。
'''


import os
import sys
import numpy as np
import math

MIN_RADIUS = 2.0
MAX_RADIUS = 4.0
RADIUS_STEP_SIZE = 0.1
PERIMETER_STEP_SIZE = 0.1


class RotationCoordinates():

    def Translation(self, ovector, pvector):
        return [ovector[0]-pvector[0], ovector[1]-pvector[1], ovector[2]-pvector[2]]

    def __RotateAroundx(self, iarray, theta):
        imatrix = np.array([[iarray[0]], [iarray[1]], [iarray[2]], [1]])
        rax = np.array([[1, 0, 0, 0],
                        [0, np.cos(theta), -np.sin(theta), 0],
                        [0, np.sin(theta), np.cos(theta), 0],
                        [0, 0, 0, 1]])
        ocoordinate = np.matmul(rax, imatrix)
        tmp = ocoordinate.tolist()
        result = [tmp[0][0], tmp[1][0], tmp[2][0]]
        return result

    def __RotateAroundy(self, iarray, theta):
        imatrix = np.array([[iarray[0]], [iarray[1]], [iarray[2]], [1]])
        ray = np.array([[np.cos(theta), 0, -np.sin(theta), 0],
                        [0, 1, 0, 0],
                        [np.sin(theta), 0, np.cos(theta), 0],
                        [0, 0, 0, 1]])
        ocoordinate = np.matmul(ray, imatrix)
        tmp = ocoordinate.tolist()
        result = [tmp[0][0], tmp[1][0], tmp[2][0]]
        return result

    def __RotateAroundz(self, iarray, theta):
        imatrix = np.array([[iarray[0]], [iarray[1]], [iarray[2]], [1]])
        raz = np.array([[np.cos(theta), -np.sin(theta), 0, 0],
                        [np.sin(theta), np.cos(theta), 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])
        ocoordinate = np.matmul(raz, imatrix)
        tmp = ocoordinate.tolist()
        result = [tmp[0][0], tmp[1][0], tmp[2][0]]
        return result

    def RotateAround(self, iarray, axix, theta):
        if axix.upper() == 'X':
            return self.__RotateAroundx(iarray, theta)
        elif axix.upper() == 'Y':
            return self.__RotateAroundy(iarray, theta)
        elif axix.upper() == 'Z':
            return self.__RotateAroundz(iarray, theta)

    def GetGeometricCenter(self, atomlist):
        result = [0, 0, 0]
        count = 0
        for atom in atomlist:
            if atom[0].upper() != 'H':
                result[0] = result[0]+atom[1]
                result[1] = result[1]+atom[2]
                result[2] = result[2]+atom[3]
                count = count+1
        return [float(result[0]/count), float(result[1]/count), float(result[2]/count)]

    def GenerateCenter(self, radius, xyz, xyangle, zxangle, density, filename):
        # radius:Distance range [r1,r2] (angstrom)
        # xyz:Distance range [xr1, xr2, yr1,yr2,zr1,zr2] (angstrom)
        # xyangle:theta1 [Starting angle, End angle] (angle)
        # zxangle:theta1 [Starting angle, End angle] (angle)
        # density:grid side length(angstrom)
        x = float(xyz[0])
        count = 0
        result = open(filename, 'w')
        while x <= radius[1]:
            if x >= xyz[0] and x <= xyz[1]:
                y = float(xyz[2])
                while y <= radius[1]:
                    if y >= xyz[2] and y <= xyz[3]:
                        z = float(xyz[4])
                        while z <= radius[1]:
                            if z >= xyz[4] and z <= xyz[5]:
                                r = np.sqrt(
                                    np.square(x)+np.square(y)+np.square(z))
                                r1 = np.sqrt(np.square(x)+np.square(y))
                                if r >= radius[0] and r <= radius[1]:
                                    zx_angle = np.arcsin(z/r)
                                    # print('zx_angle=%s'%zx_angle)
                                    if zx_angle >= (float(zxangle[0])/180*np.pi) and zx_angle <= (float(zxangle[1])/180*np.pi):
                                        if r1 == 0:
                                            count = count+1
                                            result.writelines(
                                                '%5i%10.2f%10.2f%10.2f\n' % (count, x, y, z))
                                        else:
                                            xy_angle = np.arccos(
                                                x/r1)
                                            # print('xy_angle=%s'%xy_angle)
                                            if xy_angle >= (float(xyangle[0])/180*np.pi) and xy_angle <= (float(xyangle[1])/180*np.pi):
                                                count = count+1
                                                result.writelines(
                                                    '%5i%10.2f%10.2f%10.2f\n' % (count, x, y, z))
                            z = z+density
                    y = y+density
            x = x+density
        result.close

    def __GenerateCenter(self, radius, xyz, xyangle, zxangle, density):
        # radius:Distance range [r1, r2, step size] (angstrom)
        # xyangle:theta1 [Starting angle, End angle] (angle)
        # zxangle:theta1 [Starting angle, End angle] (angle)
        # density:grid side length(angstrom)
        x = float(xyz[0])
        count = 0
        while x <= radius[1]:
            if x >= xyz[0] and x <= xyz[1]:
                y = float(xyz[2])
                while y <= radius[1]:
                    if y >= xyz[2] and y <= xyz[3]:
                        z = float(xyz[4])
                        while z <= radius[1]:
                            if z >= xyz[4] and z <= xyz[5]:
                                r = np.sqrt(
                                    np.square(x)+np.square(y)+np.square(z))
                                r1 = np.sqrt(np.square(x)+np.square(y))
                                if r >= radius[0] and r <= radius[1]:
                                    zx_angle = np.arcsin(z/r)
                                    # print('zx_angle=%s'%zx_angle)
                                    if zx_angle >= (float(zxangle[0])/180*np.pi) and zx_angle <= (float(zxangle[1])/180*np.pi):
                                        if r1 == 0:
                                            count = count+1
                                            yield([count, x, y, z])
                                        else:
                                            xy_angle = np.arccos(
                                                x/r1)
                                            # print('xy_angle=%s'%xy_angle)
                                            if xy_angle >= (float(xyangle[0])/180*np.pi) and xy_angle <= (float(xyangle[1])/180*np.pi):

                                                count = count+1
                                                yield([count, x, y, z])
                            z = z+density
                    y = y+density
            x = x+density

    def RotateAtom(self, atomlist, rx, ry, rz, filename):
        # atomlist[[atom1-type(string),atom1-x(float),atom1-y(float),atom1-z](float)]
        # rx,ry,rz [start_rad(float),stop_rad(float),step_size(float)]
        x = float(rx[0])
        count = 1
        outtxt = open(filename, 'w')
        while x <= rx[1]:
            y = float(ry[0])
            while y <= ry[1]:
                z = float(rz[0])
                while z <= rz[1]:
                    outtxt.writelines(
                        'Conformation-%s-%5.2s-%5.2s-%5.2s\n' % (count, x, y, z))
                    count = count+1
                    for atom in atomlist:
                        xyz = [atom[1], atom[2], atom[3]]
                        xyz = self.__RotateAroundz(xyz, z/180*np.pi)
                        xyz = self.__RotateAroundy(xyz, y/180*np.pi)
                        xyz = self.__RotateAroundx(xyz, x/180*np.pi)
                        outtxt.writelines('%-7s%18.12f%18.12f%18.12f\n' %
                                          (atom[0], xyz[0], xyz[1], xyz[2]))
                    z = z+rz[2]
                y = y+ry[2]
            x = x+rx[2]

    def __RotateAtom(self, atomlist, rx, ry, rz):
        # atomlist[[atom1-type(string),atom1-x(float),atom1-y(float),atom1-z](float)]
        # rx,ry,rz [start_rad(float),stop_rad(float),step_size(float)]
        x = float(rx[0])
        while x <= rx[1]:
            y = float(ry[0])
            while y <= ry[1]:
                z = float(rz[0])
                while z <= rz[1]:
                    result = []
                    for atom in atomlist:
                        xyz = [atom[1], atom[2], atom[3]]
                        xyz = self.__RotateAroundz(xyz, z/180*np.pi)
                        xyz = self.__RotateAroundy(xyz, y/180*np.pi)
                        xyz = self.__RotateAroundx(xyz, x/180*np.pi)
                        result.append([atom[0], xyz[0], xyz[1], xyz[2]])
                    yield([result, [x, y, z]])
                    z = z+rz[2]
                y = y+ry[2]
            x = x+rx[2]

    def TranslationAtom(self, atomlist, pan):
        length = len(atomlist)
        result = []
        for i in range(length):
            x = float(atomlist[i][1])-float(pan[0])
            y = float(atomlist[i][2])-float(pan[1])
            z = float(atomlist[i][3])-float(pan[2])
            result.append([atomlist[i][0], x, y, z])
        return result

    def GenerateFile(self, oatomlist, atomlist, name):
        xyz = open(name+'.xyz', 'w')
        xyz.writelines('%s\n\n' % (len(oatomlist)+len(atomlist)))
        qcin = open(name+'.qcin', 'w')
        head_xygjos = '$rem\njobtype sp\nexchange xygjos\nbasis 6-311++G**\nAUX_BASIS RIMP2-CC-PVTZ\nPURECART 1111\nTIME_MP2 TRUE\nINCDFT FALSE\n$end\n'
        qcin.writelines(head_xygjos)
        qcin.writelines('\n$comment\n%s\n$end\n\n$molecule\n   0 1\n' % name)
        for atom in oatomlist:
            xyz.writelines('%-7s%18.12f%18.12f%18.12f\n' %
                           (atom[0], atom[1], atom[2], atom[3]))
            qcin.writelines('%4s%15.5f%15.5f%15.5f\n' %
                            (atom[0], atom[1], atom[2], atom[3]))
        for atom in atomlist:
            xyz.writelines('%-7s%18.12f%18.12f%18.12f\n' %
                           (atom[0], atom[1], atom[2], atom[3]))
            qcin.writelines('%4s%15.5f%15.5f%15.5f\n' %
                            (atom[0], atom[1], atom[2], atom[3]))
        qcin.writelines('$end\n\n')
        xyz.close
        qcin.close


# class qmtoolbox():
#     def ExtractResult(self, software, method, filename):
#         log = open(filename, 'r')
#         energy = False
#         for line in log.readlines():
#             if software == 'qchem':
#                 if method == 'xygjos' or method == 'lxygjos':
#                     if 'Total XYGJ-OS energy' in line:
#                         line = line.split()
#                         energy = float(line[-1])
#                         break
#                 else:
#                     if 'Total energy in the final basis set =' in line:
#                         line = line.split()
#                         energy = float(line[-1])
#                         break
#         log.close()
#         return energy
#
#     def ResultList(self, software, ipath, method, filename):
#         rlist = open(filename, 'w')
#         tmp = -231.5986783899
#         for files in os.listdir(ipath):
#             if os.path.isfile(files) and ('.qcin' in files):
#                 name = files[:-5]
#                 log = name+'-'+method+'.log'
#                 result = self.ExtractResult(software, method, log)
#                 if result == False:
#                     rlist.writelines('%15s%20s\n' % (name, result))
#                 else:
#                     rlist.writelines('%15s%20.10f\n' %
#                                      (name, (result-2*tmp)*627.51))
#         rlist.close()
