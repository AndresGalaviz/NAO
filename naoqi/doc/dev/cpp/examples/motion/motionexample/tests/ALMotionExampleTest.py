"""
  This is a simple python script to test the autogenerated module

"""
print '        START TESTING ALMotionExample MODULE'

from naoqi import ALProxy

IP = "127.0.0.1"
PORT = 9559

#________________________________
# Generic Proxy creation
#________________________________

try:
  ALMotionExample_Proxy = ALProxy("ALMotionExample",IP,PORT)
except Exception,e:
  print "Error when creating ALMotionExample_Proxy proxy:"
  print str(e)
  exit(1)

# Uncomment lines to call examples

### Cartesian ###

## Cartesian arm 1.
## Moves the left arm with Cartesian Control, to one position then back again.
ALMotionExample_Proxy.cartesianArm1()

## Cartesian arm 2.
## Moves the left arm with Cartesian Control, along a trajectory then back to the start.
#ALMotionExample_Proxy.cartesianArm2()

## Cartesian foot.
## Lowers the Torso and moves to the side, then moves the Left Leg left.
#ALMotionExample_Proxy.cartesianFoot()

## Cartesian torso 1.
## Belly dancing: makes the torso follow a near circular path.
#ALMotionExample_Proxy.cartesianTorso1()

## Cartesain torso 2
## Controls the position and orientation of the torso along a path.
#ALMotionExample_Proxy.cartesianTorso2()

## Cartesian torso arm 1.
## Simultaneously controls three effectors:
## the Torso, the Left Arm and the Right Arm
#ALMotionExample_Proxy.cartesianTorsoArm1()

## Cartesian torso arm 2
## Moves the torso while keeping the arms fixed in nao space
#ALMotionExample_Proxy.cartesianTorsoArm2()

### Various ###

## Collision detection
## Nao bump on his torso and head with his arm
#ALMotionExample_Proxy.collisionDetection("LArm") # "LArm" or "RArm"

## Move hand.
#ALMotionExample_Proxy.moveHand()

## Moves Nao to the init pose.
#ALMotionExample_Proxy.poseInit()

## Moves Nao to the zero pose, where all joints are at angle zero
#ALMotionExample_Proxy.poseZero()

## Sets the stiffness to the minimum value.
#ALMotionExample_Proxy.stiffnessOff()

## Sets the stiffness to the maximum value.
#ALMotionExample_Proxy.stiffnessOn()

### Walk ###

## Small example to make Nao execute
## The Cha Cha Basic Steps for Men
## Using setFootStep API
## http://www.dancing4beginners.com/cha-cha-steps.htm
#ALMotionExample_Proxy.setFootStepDance()

## Moves using the moveToward command and shows control of the arms.
# ALMotionExample_Proxy.move()

## Move: Small example to make Nao walk
##       with gait customization
## NAO is Keyser Soze
#ALMotionExample_Proxy.moveCustomization()

## Move: Small example to make Nao walk
##       Faster (Step of 6 cm)
#ALMotionExample_Proxy.moveFaster()

## Nao walks using the moveTo command and shows odometry.
#ALMotionExample_Proxy.moveTo()

## Move To: Small example to make Nao Walk To an Objective
##          With customization
#ALMotionExample_Proxy.moveToCustomization()

## Move To: Small example to make Nao Walk follow
##          a Dubins Curve
#ALMotionExample_Proxy.moveToDubinsCurve()

### Whole Body ###

## Whole Body effector control head.
## Example of a whole body head orientation control
#ALMotionExample_Proxy.wbEffectorControlHead()

## Whole Body effector control Left arm.
#ALMotionExample_Proxy.wbEffectorControlLArm()

## Whole Body effector control Right arm.
#ALMotionExample_Proxy.wbEffectorControlRArm()

## Whole Body effector control constraint.
## Balance Constraints
#ALMotionExample_Proxy.wbEffectorControlConstraint()

## Whole body constraints to keep the feet on the plane,
## despite conflicting commands.
#ALMotionExample_Proxy.wbFootState()

## Example of a whole body kick
#ALMotionExample_Proxy.wbKick()

## Example of a whole body multiple effectors control "LArm", "RArm" and "Torso"
#ALMotionExample_Proxy.wbMultipleEffectors()
