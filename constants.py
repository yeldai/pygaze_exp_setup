import os



WORDS= ["dog","cat","gopher"]
NONWORDS= ["blorg","ghyt","blrub"]

LOGFILENAME=input("What is your participant code? ")
DIR =os.path.dirname(__file__)
DATADIR = os.path.join(DIR,"data")
if not os.path.isdir(DATADIR):
    os.mkdir(DATADIR)
LOGFILE=os.path.join(DATADIR,LOGFILENAME)


DISPSIZE=[1440,900]
BGC=(0,0,0)
FGC=(255,255,255)


TRACKERTYPE="eyelink"
DUMMYMODE=True