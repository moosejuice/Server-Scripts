import os, shutil, stat, time

"""
python script to move files in downloaded directory out of folders into the root. Then delete the folders.
ie: flattens a specified directory.
Also removes non video files. ie: txt files, .nfo
Aug 7, 2013     - delete .jpg files
                - move .mp3 files directly into iTunes library.
Aug 20, 2013    - delete .png files
Oct 3, 2013     - delete .srt files
Oct 25, 2013    - delete .m3u playlist files
Feb 23, 2014    - add error output file
Add try catch on file operatoins.
April 16, 2014  - turn to function, add recursive calls to properly flatten more than depth of 1 folder
April 27, 2014  - delete files containing 'sample' that are less than 30MB. Have no use for sample files.
May 27, 2014    - delete .bmp files
Need to convert .m4a to mp3 before adding to iTunes
"""
root = 'E:\Torrents\Completed'
destDir = destPath = srcPathInit = root
addToiTunes = 'D:\Library\Automatically Add to iTunes'
errors = open("D:/Logs/errors.txt", "a")
log = open("D:/Logs/log.txt", "a")
errors.write("Error Log for %s\n" % time.strftime("%d/%m/%Y"))
log.write("Activity Log for %s\n" % time.strftime("%d/%m/%Y"))

def flatten(srcPath):
    for srcDir, dirs, files in os.walk(srcPath):
     print srcDir
     if not os.path.exists(destDir):
      os.mkdir(destDir)
     for file in files:
      if(srcDir == root):
       print 'File is already in %s' %root
       log.write('%s is already in %s\n' % (file, root))
      else:
       srcFile = os.path.join(srcDir, file)
       destFile = os.path.join(destDir, file)
       print 'Processing %s' %srcFile
       if os.path.exists(destFile):
        print "Dest File exists already %s" %destFile
        log.write("Dest File exists already %s\n" %destFile)
       else:
        try:
            if (srcFile.endswith(".txt")):
             print "Deleting %s" %srcFile
             log.write("Deleting %s\n" %srcFile)
             os.remove(srcFile)
            elif (srcFile.endswith(".gif")):
             print "Deleting %s" %srcFile
             log.write("Deleting %s\n" %srcFile)
             os.remove(srcFile)          
            elif (srcFile.endswith(".nfo")):
             print "Deleting %s" %srcFile
             log.write("Deleting %s\n" %srcFile)
             os.remove(srcFile)
            elif (srcFile.endswith(".png")):
             print "Deleting %s" %srcFilelog.write()
             log.write("Deleting %s\n" %srcFile)
             os.remove(srcFile)
            elif (srcFile.endswith(".jpg")):
             print "Deleting %s" %srcFile
             log.write("Deleting %s\n" %srcFile)
             os.remove(srcFile)
            elif (srcFile.endswith(".mp3")):
             log.write("Moving to iTunes add Folder %s\n" % srcFile)
             shutil.move(srcFile, addToiTunes)
            elif (srcFile.endswith(".srt")):
             print "Deleting %s" %srcFile
             log.write("Deleting %s\n" %srcFile)
             os.remove(srcFile)
            elif (srcFile.endswith(".m3u")):
             print "Deleting %s" %srcFile
             log.write("Deleting %s\n" %srcFile)
             os.remove(srcFile)
            elif (srcFile.endswith(".bmp")):
             print "Deleting %s" % srcFile
             log.write("Deleting %s\n" % srcFile)
             os.remove(srcFile)
            elif "SAMPLE" in srcFile.upper():
                if os.path.getsize(srcFile) < 31457280:
                    print "Deleting %s" % srcFile
                    log.write("Deleting sample file %s\n" % srcFile)
                    os.remove(srcFile)
            else:
             shutil.move(srcFile, destDir)
             log.write("Moving %s to %s\n" %(srcFile, destDir))
        except:
            errors.write("Error Processing %s\n" % srcFile)
     for dir in dirs:
         newdir = os.path.join(srcDir, dir)
         log.write("\nFlattening %s\n" % newdir)
         flatten(newdir)
         
     if (srcDir == root):
      print 'Will not delete %s' %root
      log.write('Will not delete %s\n' %root)
     else:
      log.write('Deleting folder %s\n' % srcDir)
      shutil.rmtree(srcDir)
      

flatten(srcPathInit)
print 'Flattening Complete'
log.write('Flattening Complete\n')
