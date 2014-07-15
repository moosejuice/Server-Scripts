'''
import_mp4(filepath)
        Takes file in filepath and movies it into the movie library in the following format:
                base/Movie Title/Movie Title.mp4
        Some error checking included for file transfers into directory
'''
import os
import time
from shutil import move
			
def import_mp4(filepath):
        basedir = "D:\Library\Automatically Add to iTunes"
	librarybase="D:\Library\Movies"
        errordir=os.path.join(basedir,"Errors")
	name=os.path.basename(filepath)
	foldername=name[:-4].replace("_","")
	foldername=foldername.split("(")[0].rstrip()
	newpath=os.path.join(librarybase,foldername)
	
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	
	for x in range(0,5):
		try:
                        os.rename(filepath, os.path.join(newpath,name))
			print "\tMoved ", filepath, " To ", os.path.join(newpath,name)
			return
		except Exception as e:
			if 32 == e.args[0]:       
                                print "\tFile in use. Trying again in 5 seconds"
                                time.sleep(5)
                        elif 183 == e.args[0]:
                                print "\tFile already exists in library."
                                if not os.path.exists(errordir):
                                        os.makedirs(errordir)
                                move(filepath, os.path.join(errordir,name))
                                print "\tMoved file to ", errordir
                                return
		if x == 4:
                        print "\tProcess timed out. Moving to ", errordir
                        if not os.path.exists(errordir):
                                os.makedirs(errordir)
                        move(filepath, os.path.join(errordir,name))
