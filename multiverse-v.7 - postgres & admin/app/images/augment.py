import os
import glob
files1 = [f for f in glob.glob("train/*")]
for i in range (0,len(files1)):
		os.system("python augmentation.py -folder="+str(files1[i])+" -limit=5000")
