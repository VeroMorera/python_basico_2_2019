import maya.cmds as mc
import maya.OpenMaya as om



class LimbsBuilder():

    def __init__(self, limbType):
        self.limbType = limbType

    def legGuides(self):


        def connect_limb_guides(hipRef, kneeRef, ankleRef, ballRef, toeRef, heel):
            # visualmente conecta huesos
            uplegLine = mc.annotate(kneeRef)
            mc.parent(uplegLine, hipRef, relative=True)
            mc.parent(kneeRef, hipRef)

            lolegLine = mc.annotate(ankleRef)
            mc.parent(lolegLine, kneeRef, relative=True)
            mc.parent(ankleRef, kneeRef)

            ankleLine = mc.annotate(ballRef)
            mc.parent(ankleLine, ankleRef, relative=True)
            mc.parent(ballRef, ankleRef)

            footLine = mc.annotate(toeRef)
            mc.parent(footLine, ballRef, relative=True)
            mc.parent(toeRef, ballRef)

            # referenciar lineas ref para que no se puedan modificar
            for line in [uplegLine, lolegLine, ankleLine, footLine]:
                mc.setAttr('{}.template'.format(line), 1)

                #for trs in ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz', '.sx', '.sy', '.sz', '.v']:
                   # mc.setAttr('{}{}'.format(line, trs), lock=True, keyable=False, channelBox=False)
            guides_grp = mc.group(hipRef, name='tempLegBuilder_grp')

        if self.limbType == 'human':

            #esto crea una referencia de la posicion de cada hueso
            hipRef = mc.sphere(n='hipRef', r=0.2)
            mc.move(0, 9, 0)
            kneeRef = mc.sphere(n='kneeRef', r=0.2)
            mc.move(0, 5, 0.3)
            ankleRef = mc.sphere(n='ankleRef', r=0.2)
            mc.move(0, 1, 0)
            ballRef = mc.sphere(n='ballRef', r=0.2)
            mc.move(0, 0.1, 0.7)
            toeRef = mc.sphere(n='toeRef', r=0.2)
            mc.move(0, 0, 1.5)
            temp_heel = mc.spaceLocator(n='temp_heel')
            mc.move(0, 0, -0.5)

            connect_limb_guides( hipRef, kneeRef, ankleRef, ballRef, toeRef, temp_heel)


        elif self.limbType == 'horse':

            hipRef = mc.sphere(n='hipRef', r=0.2)
            mc.move(0, 14, 0)
            kneeRef = mc.sphere(n='kneeRef', r=0.2)
            mc.move(0, 10, 1)
            ankleRef = mc.sphere(n='ankleRef', r=0.2)
            mc.move(0, 5.5, -0.8)
            ballRef = mc.sphere(n='ballRef', r=0.2)
            mc.move(0, 2, -0.2)
            toeRef = mc.sphere(n='toeRef', r=0.2)
            mc.move(0, 0, 0.6)
            temp_heel = mc.spaceLocator(n='temp_heel')
            mc.move(0, 0, -0.4)

            connect_limb_guides(hipRef, kneeRef, ankleRef, ballRef, toeRef, temp_heel)


        elif self.limbType == 'beetle':

            hipRef = mc.sphere(n='hipRef', r=0.2)
            mc.move(0, 5.5, 0)
            kneeRef = mc.sphere(n='kneeRef', r=0.2)
            mc.move(3, 6.5, 0)
            ankleRef = mc.sphere(n='ankleRef', r=0.2)
            mc.move(4, 1.5, 0)
            ballRef = mc.sphere(n='ballRef', r=0.2)
            mc.move(5.5, 0, 0)
            toeRef = mc.sphere(n='toeRef', r=0.2)
            mc.move(6.2, 0, 0)
            temp_heel = mc.spaceLocator(n='temp_heel')
            mc.move(4, 0, 0)

            connect_limb_guides(hipRef, kneeRef, ankleRef, ballRef, toeRef, temp_heel)

        else:
            om.MGlobal.displayError('Error, please choose between human, horse, or beetle...')


class ControlShape():
    def __init__(self, joints, radius, side):
        self.joints = joints   #one or more joints
        self.radius = radius
        self.side = side

    def create_control(self):
        if self.joints == 0:
            om.MGlobal.displayError('Error, select al least one joint.')

        elif self.joints == 1:
            # Create controls for each joint
            ctrl = mc.circle(nr=(1, 0, 0), n=self.joints + '_', radius=self.radius)
            mc.makeIdentity(apply=True)

            # attach control to joint
            temp = mc.parentConstraint(self.joints, ctrl, mo=0)
            mc.delete(temp)

            # connect shapes to joint
            shapes = mc.listRelatives(ctrl, shapes=True)
            mc.parent(shapes, self.joints, relative=True, shape=1)
            mc.delete(ctrl)

            # make offset grp
            ctrl_off = mc.group(n=self.joints + '_offGrp', empty=True)
            mc.setAttr('{}.overrideEnabled'.format(ctrl_off), 1)
            mc.setAttr('{}.overrideColor'.format(ctrl_off), 6)
            temp = mc.parentConstraint(self.joints, ctrl_off, mo=0)
            mc.delete(temp)

            mc.parent(self.joints, ctrl_off)


        else:
            previous_sel = None

            for j in self.joints[:-1]:

                # Create controls for each joint
                ctrl = mc.circle(nr=(1, 0, 0), n= j + '_', radius=self.radius)
                mc.makeIdentity(apply=True)

                #attach control to joint
                temp= mc.parentConstraint(j, ctrl, mo=0)
                mc.delete(temp)

                #connect shapes to joint
                shapes = mc.listRelatives(ctrl, shapes=True)
                mc.parent(shapes, j, relative=True, shape=1)
                mc.delete(ctrl)

                #make offset grp
                ctrl_off = mc.group(n= j + '_offGrp', empty=True)
                mc.setAttr('{}.overrideEnabled'.format(ctrl_off), 1)
                mc.setAttr('{}.overrideColor'.format(ctrl_off), 6)
                temp = mc.parentConstraint(j, ctrl_off, mo=0)
                mc.delete(temp)

                mc.parent(j, ctrl_off)

                if previous_sel:
                    mc.parent(ctrl_off, previous_sel)
                previous_sel = j

                #lock_hide_attr
                for trs in ['.tx', '.ty', '.tz', '.sx', '.sy', '.sz', '.v', '.radius']:
                    mc.setAttr( '{}{}'.format(j, trs), lock=True, keyable=False, channelBox=False)



            om.MGlobal.displayInfo('FK ControlShape chain has been created with success!')

    def create_ikfk_switch(self):
        v1 = mc.curve(d=1, p=[(0.052, 4.96, 0), (0.061, 4.97, 0), (0.070, 4.98, 0), (0.164, 5.13, 0), (0.178, 5.14, 0),
                              (0.184, 5.14, 0), (0.196, 5.14, 0), (0.204, 5.14, 0), (0.346, 5.09, 0), (0.371, 5.08, 0),
                              (0.375, 5.07, 0), (0.373, 5.05, 0), (0.364, 4.88, 0), (0.365, 4.87, 0), (0.368, 4.86, 0),
                              (0.425, 4.82, 0), (0.438, 4.82, 0), (0.453, 4.82, 0), (0.606, 4.89, 0), (0.621, 4.90, 0),
                              (0.632, 4.90, 0), (0.644, 4.88, 0), (0.746, 4.76, 0), (0.759, 4.74, 0), (0.760, 4.73, 0),
                              (0.747, 4.72, 0), (0.650, 4.58, 0), (0.642, 4.57, 0), (0.639, 4.56, 0), (0.668, 4.49, 0),
                              (0.679, 4.48, 0), (0.694, 4.48, 0), (0.863, 4.46, 0), (0.877, 4.45, 0), (0.886, 4.45, 0),
                              (0.888, 4.43, 0), (0.910, 4.26, 0), (0.909, 4.26, 0), (0.909, 4.25, 0), (0.901, 4.25, 0),
                              (0.886, 4.24, 0), (0.733, 4.17, 0), (0.721, 4.17, 0), (0.712, 4.16, 0), (0.699, 4.08, 0),
                              (0.703, 4.07, 0), (0.717, 4.06, 0), (0.844, 3.94, 0), (0.853, 3.94, 0), (0.860, 3.93, 0),
                              (0.854, 3.91, 0), (0.783, 3.76, 0), (0.778, 3.75, 0), (0.770, 3.75, 0), (0.759, 3.75, 0),
                              (0.752, 3.75, 0), (0.588, 3.78, 0), (0.574, 3.78, 0), (0.561, 3.78, 0), (0.500, 3.71, 0),
                              (0.498, 3.70, 0), (0.503, 3.68, 0), (0.548, 3.52, 0), (0.554, 3.50, 0), (0.551, 3.50, 0),
                              (0.533, 3.48, 0), (0.410, 3.41, 0), (0.392, 3.39, 0), (0.385, 3.40, 0), (0.369, 3.41, 0),
                              (0.253, 3.52, 0), (0.241, 3.54, 0), (0.228, 3.54, 0), (0.127, 3.51, 0), (0.118, 3.50, 0),
                              (0.114, 3.48, 0), (0.065, 3.32, 0), (0.060, 3.31, 0), (0.053, 3.30, 0), (-0.123, 3.30, 0),
                              (-0.131, 3.31, 0), (-0.137, 3.32, 0), (-0.177, 3.49, 0), (-0.181, 3.50, 0),
                              (-0.188, 3.51, 0),(-0.296, 3.55, 0), (-0.308, 3.55, 0), (-0.320, 3.54, 0), (-0.448, 3.43, 0),
                              (-0.460, 3.42, 0),(-0.470, 3.41, 0), (-0.484, 3.42, 0), (-0.603, 3.51, 0), (-0.615, 3.52, 0),
                              (-0.615, 3.52, 0),(-0.621, 3.52, 0), (-0.615, 3.54, 0), (-0.558, 3.70, 0), (-0.555, 3.72, 0),
                              (-0.555, 3.73, 0),(-0.564, 3.74, 0), (-0.619, 3.81, 0), (-0.628, 3.81, 0), (-0.637, 3.82, 0),
                              (-0.651, 3.82, 0),(-0.819, 3.80, 0), (-0.834, 3.79, 0), (-0.844, 3.80, 0), (-0.851, 3.81, 0),
                              (-0.905, 3.95, 0),(-0.910, 3.96, 0), (-0.911, 3.97, 0), (-0.895, 3.98, 0), (-0.763, 4.09, 0),
                              (-0.752, 4.10, 0),(-0.745, 4.11, 0), (-0.747, 4.12, 0), (-0.755, 4.22, 0), (-0.762, 4.23, 0),
                              (-0.776, 4.23, 0),(-0.918, 4.30, 0), (-0.947, 4.31, 0), (-0.947, 4.32, 0), (-0.916, 4.48, 0),
                              (-0.909, 4.50, 0),(-0.885, 4.51, 0), (-0.715, 4.52, 0), (-0.702, 4.52, 0), (-0.692, 4.53, 0),
                              (-0.646, 4.62, 0),(-0.648, 4.63, 0), (-0.657, 4.64, 0), (-0.744, 4.78, 0), (-0.755, 4.80, 0),
                              (-0.754, 4.81, 0),(-0.740, 4.82, 0), (-0.635, 4.93, 0), (-0.621, 4.94, 0), (-0.613, 4.95, 0),
                              (-0.594, 4.94, 0),(-0.447, 4.86, 0), (-0.432, 4.85, 0), (-0.417, 4.85, 0), (-0.345, 4.89, 0),
                              (-0.339, 4.91, 0),(-0.339, 4.93, 0), (-0.338, 5.09, 0), (-0.338, 5.10, 0), (-0.333, 5.11, 0),
                              (-0.316, 5.11, 0),(-0.162, 5.15, 0), (-0.142, 5.16, 0), (-0.135, 5.15, 0), (-0.124, 5.14, 0),
                              (-0.040, 4.99, 0),(-0.032, 4.98, 0), (-0.023, 4.97, 0), (0.052, 4.96, 0)])
        v2 = mc.curve(d=1, p=[(0, -0.027, 0), (-0.03, 3.3, 0)])

        mc.select(v1, v2)
        mc.ls(sl=True)
        shps = mc.listRelatives(shapes=True)
        mc.parent(shps, v1, relative=True, shape=True)
        mc.delete(v2)
        sel = mc.rename(v1, self.side + 'IkFkSwitch_ctrl')

        ikfk_off = mc.group(name= self.side + 'IkFkSwitch_ctrl_offGrp', empty=1)
        temp = mc.pointConstraint(sel, ikfk_off, mo=0)
        mc.delete(temp)
        mc.parent(sel, ikfk_off)

        #
        mc.addAttr(sel, longName='IK_FK', defaultValue=0, minValue=0, maxValue=1, keyable=True)

        # lock_hide_attr
        for trs in ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz', '.sx', '.sy', '.sz', '.v']:
            mc.setAttr('{}{}'.format(sel, trs), lock=True, keyable=False, channelBox=False)


class Leg():
    def __init__(self, side):
        self.side = side

        #estos son solo los nombres de los huesos que se van a usar en el codigo.
        self.legJnts = [self.side + "hip_ctrl", self.side + "knee_ctrl", self.side + "ankle_ctrl",
                   self.side + "ball_ctrl", self.side + "toe_jntEnd"]

    def create_bones(self):

        #limpiar escena
        mc.select(clear=True)
        bonesOnLimb = 5
        limbBones = []

        for i in range(bonesOnLimb):
            jnt = mc.joint()
            limbBones.append(jnt)


        #reposition and rename bones
        temp = mc.pointConstraint('hipRef', limbBones[0], mo=0)
        mc.rename(limbBones[0], self.side + "hip_ctrl")
        mc.delete(temp)

        temp = mc.pointConstraint('kneeRef', limbBones[1], mo=0)
        mc.rename(limbBones[1], self.side + "knee_ctrl")
        mc.delete(temp)

        temp = mc.pointConstraint('ankleRef', limbBones[2], mo=0)
        mc.rename(limbBones[2], self.side + "ankle_ctrl")
        mc.delete(temp)

        temp = mc.pointConstraint('ballRef', limbBones[3], mo=0)
        mc.rename(limbBones[3], self.side + "ball_ctrl")
        mc.delete(temp)

        temp = mc.pointConstraint('toeRef', limbBones[4], mo=0)
        mc.rename(limbBones[4], self.side + "toe_jntEnd")
        mc.delete(temp)

        #delete guides
        mc.delete('tempLegBuilder_grp')

    def orient_bones(self):

        # make helper joint to orient end joint
        temp = mc.duplicate(self.legJnts[4], renameChildren=1)
        mc.parent(temp, self.legJnts[4])


        if self.side == 'L_' or  'l_':

            for jnt in self.legJnts:
                mc.joint(jnt, e=True, oj='xyz', sao='zdown', zso=True, ch=1)

            # delete helper joint
            mc.delete(temp)

        '''
        elif self.side == 'R_' or  'r_': #AQUI NECESITO X APUNTANDO HACIA ARRIBA

            for jnt in self.legJnts:
                mc.joint(jnt, e=True, oj='xyz', sao='zup', zso=True, ch=1)

            # delete helper joint
            mc.delete(temp)
        '''

    def make_ik(self):

        # Create the Iksolvers:
        upperleg = mc.ls(self.legJnts[0], self.legJnts[2])
        mc.select(upperleg)
        ikrp = mc.ikHandle(name = self.side + 'ankle_IkRp', solver='ikRPsolver')

        loLegBall = mc.ls(self.legJnts[2:4])
        mc.select(loLegBall)
        iksc1 = mc.ikHandle(name = self.side  + 'ball_IkSc', solver='ikSCsolver')

        loLegToe = mc.ls(self.legJnts[3:5])
        mc.select(loLegToe)
        iksc2 = mc.ikHandle(name = self.side  + 'toe_IkSc', solver='ikSCsolver')


        #create main control
        ik_ctrl = mc.circle(n= self.side + 'LegIK_ctrl', radius=2, nr=(0, 1, 0))
        mc.makeIdentity()
        temp= mc.pointConstraint(self.legJnts[2], ik_ctrl, mo=0)
        mc.delete(temp)

        # make offset grp
        ctrl_off = mc.group(n=ik_ctrl[0] + '_offGrp', empty=True)
        temp = mc.parentConstraint(ik_ctrl, ctrl_off, mo=0)
        mc.delete(temp)
        mc.parent(ik_ctrl, ctrl_off)

        for trs in ['.sx', '.sy', '.sz', '.v']:
            mc.setAttr(ik_ctrl[0] + trs, lock=True, keyable=False, channelBox=False)

        mc.parent(ikrp[0], iksc1[0], iksc2[0], ik_ctrl)
        mc.hide(ikrp[0], iksc1[0], iksc2[0])

        #create PV
        ikpv = mc.curve(d=1, n=self.side + 'leg_PV', p=[(-4.37114e-08, -1, -1), (0, 0, 1), (1, 0, -1), (1.31134e-07, 1, -1),
                                                   (0, 0, 1), (-1, 8.74228e-08, -1), (-4.37114e-08, -1, -1), (1, 0, -1),
                                                   (1.31134e-07, 1, -1), (-1, 8.74228e-08, -1)])

        temp_constraint = mc.pointConstraint(self.legJnts[1], ikpv, maintainOffset=0)
        mc.delete(temp_constraint)
        mc.poleVectorConstraint(ikpv, ikrp[0], weight=1 )

        # Offset pv
        ikpv_off = mc.group(ikpv, n=ikpv + '_offGrp')
        mc.move(0, 0, 10, ikpv_off, r=True)

        for trs in ['.rx', '.ry', '.rz', '.sx', '.sy', '.sz', '.v']:
            mc.setAttr(ikpv + trs, lock=True, keyable=False, channelBox=False)

        #color
        if self.side == 'L_' or  'l_':
            for ctrl in [ctrl_off, ikpv_off]:
                mc.setAttr('{}.overrideEnabled'.format(ctrl), 1)
                mc.setAttr('{}.overrideColor'.format(ctrl), 6)

        elif self.side == 'R_' or 'r_':
            for ctrl in [ctrl_off, ikpv_off]:
                mc.setAttr('{}.overrideEnabled'.format(ctrl), 1)
                mc.setAttr('{}.overrideColor'.format(ctrl), 13)

    def make_fk(self):
        fk = ControlShape(self.legJnts, 1, self.side)
        fk.create_control()

    def switch_ikfk(self):

        ikfk_switch =  self.side + 'IkFkSwitch_ctrl'
        ikfk_switchOff = self.side + 'IkFkSwitch_ctrl_offGrp'

        # Create IK FK control
        switch = ControlShape(self.legJnts, 1, self.side)
        switch.create_ikfk_switch()

        #connect fk
        mc.connectAttr(ikfk_switch + '.IK_FK', self.side + 'hip_ctrl_offGrp.v')

        #connect ik
        revFk = mc.shadingNode('reverse', asUtility=True, name= self.side + 'leg_REV')

        mc.connectAttr( ikfk_switch + '.IK_FK', '{}{}'.format(revFk, '.inputX'))
        mc.connectAttr('{}{}'.format(revFk, '.outputX'), self.side + 'LegIK_ctrl_offGrp.v' )
        mc.connectAttr('{}{}'.format(revFk, '.outputX'), self.side + 'leg_PV_offGrp.v')
        for iks in ['L_ankle_IkRp', 'L_ball_IkSc', 'L_toe_IkSc']:
            mc.connectAttr('{}{}'.format(revFk, '.outputX'), '{}{}'.format(iks, '.ikBlend'))

        # color
        if self.side == 'L_' or 'l_':
            mc.setAttr('{}.overrideEnabled'.format(ikfk_switchOff), 1)
            mc.setAttr('{}.overrideColor'.format(ikfk_switchOff), 18)

        elif self.side == 'R_' or 'r_':
            mc.setAttr('{}.overrideEnabled'.format(ikfk_switchOff), 1)
            mc.setAttr('{}.overrideColor'.format(ikfk_switchOff), 20)


        #fix switch pos
        mc.pointConstraint(self.legJnts[2], ikfk_switchOff, mo=0)
        mc.setAttr('{}{}'.format(ikfk_switchOff, '.rx'), -90)
        mc.setAttr('{}{}'.format(ikfk_switchOff, '.rz'), 90)

        #create ik_grp
        ikgrp = mc.group(n='IK_grp', empty=True)
        mc.parent(self.side + 'LegIK_ctrl_offGrp', self.side + 'leg_PV_offGrp', ikfk_switchOff, ikgrp)


class HumanLeg(Leg):

    def RFL(self):
        # RFL
        mc.select(self.legJnts)
        mc.duplicate(self.legJnts[2:5])
        mc.parent(world=True)
        dup = mc.ls(sl=True)
        mc.select(cl=True)
        mc.rename(dup[0], 'RFL_' + self.side + 'ankle_JC')
        mc.rename(dup[1], 'RFL_' + self.side + 'ball_JC')
        mc.rename(dup[2], 'RFL_' + self.side + 'toe_JC')
        heel = mc.duplicate('RFL_' + self.side + 'toe_JC', n='RFL_' + self.side + 'heel_JC')[0]
        temp = mc.pointConstraint('temp_heel', heel)
        mc.delete(temp, 'temp_heel')
        toetap = mc.duplicate('RFL_' + self.side + 'toe_JC', n='RFL_' + self.side + 'toeTap_JC')[0]
        tempPoint = mc.pointConstraint('RFL_' + self.side + 'ball_JC', toetap)
        mc.delete(tempPoint)
        mc.parent('RFL_' + self.side + 'ankle_JC', 'RFL_' + self.side + 'ball_JC')
        mc.parent('RFL_' + self.side + 'ball_JC', 'RFL_' + self.side + 'toe_JC')
        mc.parent('RFL_' + self.side + 'toe_JC', 'RFL_' + self.side + 'heel_JC')
        mc.parent('RFL_' + self.side + 'toeTap_JC', 'RFL_' + self.side + 'toe_JC')


        # Create attributes for the RFL

        ikcc = self.side + 'LegIK_ctrl'

        mc.parent(heel, ikcc)
        mc.addAttr(ikcc, ln='______________', attributeType='enum', enumName='RFL', k=True, h=False)
        mc.setAttr('{}.______________'.format(ikcc), lock=True)
        mc.addAttr(ikcc, ln='RollHeel', attributeType='double', dv=0, k=True, h=False)
        mc.addAttr(ikcc, ln='TwistHeel', attributeType='double', dv=0, k=True, h=False)
        mc.addAttr(ikcc, ln='RollBall', attributeType='double', dv=0, k=True, h=False)
        mc.addAttr(ikcc, ln='RollToe', attributeType='double', dv=0, k=True, h=False)
        mc.addAttr(ikcc, ln='TwistToe', attributeType='double', dv=0, k=True, h=False)
        mc.addAttr(ikcc, ln='ToeTap', attributeType='double', dv=0, k=True, h=False)
        # mc.addAttr(ikcc, ln='SideToSide', attributeType='double', min=-10, max=10, dv=0, k=True, h=False)


        # Connect attributes for the RFL
        mc.connectAttr(('{}.RollHeel'.format(ikcc)), '{}.rz'.format(heel))
        mc.connectAttr(('{}.TwistHeel'.format(ikcc)), '{}.ry'.format(heel))
        mc.connectAttr(('{}.RollBall'.format(ikcc)), '{}.rz'.format('RFL_' + self.side + 'ball_JC'))
        mc.connectAttr(('{}.RollToe'.format(ikcc)), '{}.rz'.format('RFL_' + self.side + 'toe_JC'))
        mc.connectAttr(('{}.TwistToe'.format(ikcc)), '{}.ry'.format('RFL_' + self.side + 'toe_JC'))
        mc.connectAttr(('{}.ToeTap'.format(ikcc)), '{}.rz'.format('RFL_' + self.side + 'toeTap_JC'))

        #re-parent ik handles
        mc.parent(self.side + 'ankle_IkRp', 'RFL_' + self.side + 'ankle_JC')
        mc.parent(self.side + 'ball_IkSc', 'RFL_' + self.side + 'ball_JC')
        mc.parent(self.side + 'toe_IkSc', 'RFL_' + self.side + 'toeTap_JC')

        mc.hide(heel)


class HorseLeg(HumanLeg):

    def RFL(self):

        HumanLeg.RFL(self)

        # fix hierarchy and pivots
        mc.parent('RFL_' + self.side + 'heel_JC', world=1)
        temp = mc.pointConstraint(self.legJnts[3], self.side + 'LegIK_ctrl_offGrp')
        mc.delete(temp)
        mc.parent('RFL_' + self.side + 'heel_JC', self.side + 'LegIK_ctrl')

        # create secondary control
        ik_ctrl2 = mc.circle(n=self.side + 'AnkleIK_ctrl', radius=1, nr=(1, 0, 0))
        mc.makeIdentity()

        temp = mc.parentConstraint(self.legJnts[2], ik_ctrl2, mo=0)
        mc.delete(temp)

        for trs in ['.rx', '.ry', '.rz', '.sx', '.sy', '.sz', '.v']:
            mc.setAttr('{}{}'.format(ik_ctrl2[0], trs), lock=True, keyable=False, channelBox=False)

        # make offset grp
        ctrl_off = mc.group(n=ik_ctrl2[0] + '_offGrp', empty=True)
        temp = mc.pointConstraint(ik_ctrl2, ctrl_off, mo=0)
        mc.delete(temp)

        mc.parent(ik_ctrl2[0], ctrl_off)

        #hierarch and dependences
        mc.pointConstraint(self.side + 'LegIK_ctrl', ctrl_off, mo=1)
        mc.pointConstraint(ik_ctrl2, 'RFL_' + self.side + 'ankle_JC', mo=1)

    def switch_ikfk(self):

        Leg.switch_ikfk(self)
        mc.parent(self.side + 'AnkleIK_ctrl_offGrp', 'IK_grp')

        # color
        if self.side == 'L_' or 'l_':
            for ctrl in [self.side + 'AnkleIK_ctrl_offGrp']:
                mc.setAttr('{}.overrideEnabled'.format(ctrl), 1)
                mc.setAttr('{}.overrideColor'.format(ctrl), 6)

        elif self.side == 'R_' or 'r_':
            for ctrl in [self.side + 'AnkleIK_ctrl_offGrp']:
                mc.setAttr('{}.overrideEnabled'.format(ctrl), 1)
                mc.setAttr('{}.overrideColor'.format(ctrl), 13)


class BeetleLeg(Leg):

    # in this case orientation has variation because of leg position.
    def orient_bones(self):
        legJnts = [self.side + "hip_ctrl", self.side + "knee_ctrl", self.side + "ankle_ctrl",
                   self.side + "ball_ctrl", self.side + "toe_jntEnd"]

        for j in legJnts[:-1]:

            mc.joint(j, e=True, oj='xyz', sao='ydown', zso=True, ch=1)

        # orient end joint (dup, orient and remove duplicated)
        temp = mc.duplicate(legJnts[4], renameChildren=1)
        mc.parent(temp, legJnts[4])
        mc.joint(legJnts[4], e=True, oj='xyz', sao='ydown', zso=True, ch=1)
        mc.delete(temp)

    def make_ik(self):
        # heritate all commands from leg
        Leg.make_ik(self)

        # create secondary control
        ik_ctrl2 = mc.circle(n=self.side + 'FootIK_ctrl', radius=1)
        mc.makeIdentity()

        temp = mc.pointConstraint(self.legJnts[3], ik_ctrl2, mo=0)
        mc.delete(temp)

        # make offset grp
        ctrl_off = mc.group(n=ik_ctrl2[0] + '_offGrp', empty=True)
        temp = mc.pointConstraint(ik_ctrl2, ctrl_off, mo=0)
        mc.delete(temp)

        mc.parent(ik_ctrl2, ctrl_off)
        mc.parent(self.side + 'ball_IkSc', self.side + 'toe_IkSc', ik_ctrl2)

        mc.parent(ik_ctrl2, self.side + 'LegIK_ctrl')
        mc.delete('temp_heel')

        # fix pv pos
        mc.select(self.side + 'leg_PV_offGrp')
        mc.move(8, 0, 0)
        mc.rotate(0, 90, 0)

        # color
        if self.side == 'L_' or 'l_':
            mc.setAttr('{}.overrideEnabled'.format(ctrl_off), 1)
            mc.setAttr('{}.overrideColor'.format(ctrl_off), 6)

        elif self.side == 'R_' or 'r_':
            mc.setAttr('{}.overrideEnabled'.format(ctrl_off), 1)
            mc.setAttr('{}.overrideColor'.format(ctrl_off), 13)


