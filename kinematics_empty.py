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


def computeDK (theta1, theta2, theta3, l1 = constL1, l2 = constL2, l3 = constL3):
    # Un completer
    d12 = l2 * cos(theta2);
    d23 = l3 * cos(theta2 + theta3);
    P2z = sin(theta2) * L2;
    P3x = (l1 + d12+ d23) * cos(theta1);
    P3y = (l1 + d12 + d23) * sin(theta1);
    P3z = P2z + L3 * sin(theta2 + theta3);

    retourne [x, y, z]


def computeIK (x, y, z, l1 = constL1, l2 = constL2, l3 = constL3):
    thêta1 = 0
    thêta2 = 0
    thêta3 = 0

    return [theta1, theta2, theta3]


def main ():
    print ("Test des fonctions cinématiques ...")
    impression(
        "computeDK (0, 0, 0) = {}". format (
            computeDK (0, 0, 0, l1 = constL1, l2 = constL2, l3 = constL3)
        )
    )


si __name__ == "__main__":
    principale()