import subprocess

cmd = ["rpm", "-qa"]
plist = subprocess.Popen(cmd)
for line in plist:
   print(line)
