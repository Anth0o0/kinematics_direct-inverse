import math

# Dimensions utilisées pour le robot PhantomX:
constL1 = 54,8
constL2 = 65,3
constL3 = 133
theta2Correction = 0 # Un complément
theta3Correction = 0 # Un complément

# Dimensions utilisées pour la simulation de bras simple
# bx = 0,07
# bz = 0,25
# constL1 = 0,085
# constL2 = 0,185
# constL3 = 0,250


def computeDK (theta1, theta2, theta3, l1 = constL1, l2 = constL2, l3 = constL3):       #direct kinematic, tp1
    # Un completer
    d12 = l2 * cos(theta2)
    d23 = l3 * cos(theta2 + theta3)
    P2z = sin(theta2) * L2
    P3x = (l1 + d12 + d23) * cos(theta1)
    P3y = (l1 + d12 + d23) * sin(theta1)
    P3z = P2z + L3 * sin(theta2 + theta3)

    retourne [x, y, z]


def computeIK (x, y, z, l1 = constL1, l2 = constL2, l3 = constL3):                      #inverse kinematic, tp2
    thêta1 = arctan(y/x)
    thêta2 = arcos((d²+ l2²-l3²)/(2*l2*l3))
    thêta3 = math.pi - arcos (l2² + l3² + sqrt(x²+y²+z²)(2*l2*l3))

    return [theta1, theta2, theta3]


def main ():
    print ("Test des fonctions cinématiques ...")                                       #we try to find out if it works 
    impression(
        "computeDK (x=287.7, y=0, z=0) = {}". format(
            computeDK(math.radian(0), 0, 0, l1=constL1, l2=constL2, l3=constL3)
        )
    )

    print(
        "computeDk(90, 0, 0) = {} . expected x=0, y=287.7, z=0".format(
            computeDK(math.radian(90), 0, 0, l1=constL1, l2=constL2, l3=constL3)
        )
    )

    print(
        "computeDk(0, 90, 0) = {} . expected x=0, y=287, z=156.7".format(
            computeDK(0, math.radian(90), 0, l1=constL1, l2=constL2, l3=constL3)
        )
    )


si __name__ == "__main__":
    principale()