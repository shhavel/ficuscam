#!/usr/bin/python3
import subprocess
from datetime import datetime

time = datetime.now()
outdir = "/home/pi/ficuscam/%04d-%02d-%02d" % (time.year, time.month, time.day)
filename = "%s/%02d%02d.jpg" % (outdir, time.hour, time.minute)
subprocess.run("mkdir -p %s && LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libv4l/v4l1compat.so fswebcam -r 640x480 --jpeg 100 -D 3 -S 13 %s" % (outdir, filename), shell=True)
print("Captured %s" % filename)
