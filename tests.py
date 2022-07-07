import sys
import os
import random
import cv2
import subprocess
from spectreye import Spectreye

# helper tests for running Spectreye on different image batches
# TODO match angle snaps with encoder data for full dataset testing

ds = "datasets/HallC_SHMS_HMS_2018/HallC_SpectrometerAngles2018.dat"

lowqual = ["COIN_HMS_angle_03322.jpg", "COIN_HMS_angle_03814.jpg", "HMS_angle_01870.jpg"]

# choose randomly from preselected test images
def gtest(sae):
    while True:
        path = random.choice(os.listdir("images/"))
        if len(path) > 4 and path[-4:] == ".jpg":
            path = "images/" + path
            print(path)
            sae.from_frame(cv2.imread(path))

# choose randomly from all angle snaps
def rtest(sae):
    while True:
        path = random.choice(os.listdir("images/angle_snaps/"))
        if len(path) > 4 and path[-4:] == ".jpg":
            path = "images/angle_snaps/" + path
            print("\n" + path)

            datetime = subprocess.getoutput("strings " + path + " | grep \"201\"").splitlines()[0]
            datetime = datetime.replace(":", "-", 2)
            print(datetime)

            #line = subprocess.getoutput("strings " + ds + " | grep \"" + datetime + "\"")
            #print(line)

            res = sae.from_frame(cv2.imread(path))



# choose randomly from selected problem images
def prob_test(sae):
    while True:
        path = "images/angle_snaps/" + random.choice(lowqual)
        print(path)
        sae.from_frame(cv2.imread(path))

# choose randomly from SHMS snaps
def shms_test(sae):
    while True:
        path = random.choice(os.listdir("images/angle_snaps/"))
        if len(path) > 4 and path[-4:] == ".jpg" and "_SHMS" in path:
            path = "images/angle_snaps/" + path
            print(path)
            sae.from_frame(cv2.imread(path))

# choose randomly from HMS snaps
def hms_test(sae):
    while True:
        path = random.choice(os.listdir("images/angle_snaps/"))
        if len(path) > 4 and path[-4:] == ".jpg" and "_HMS" in path:
            path = "images/angle_snaps/" + path
            print(path)
            sae.from_frame(cv2.imread(path))


if __name__ == "__main__":
    sae = Spectreye(True)
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "g" or sys.argv[1] == "-g":
            gtest(sae)
        elif sys.argv[1] == "r" or sys.argv[1] == "-r":
            rtest(sae)
        elif sys.argv[1] == "p" or sys.argv[1] == "-p":
            prob_test(sae)
        elif sys.argv[1] == "s" or sys.argv[1] == "-s":
            shms_test(sae)
        elif sys.argv[1] == "h" or sys.argv[1] == "-h":
            hms_test(sae)