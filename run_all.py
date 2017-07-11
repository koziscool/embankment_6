import glob

for f in glob.glob("e*.py"):
    execfile( f )