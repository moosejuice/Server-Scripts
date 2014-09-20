import os, shutil, stat, time

"""
python script to move files in downloaded directory out of folders into the root. Then delete the folders.
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
June 19, 2014   - delete .html files

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
            if (srcFile.upper().endswith(".TXT")):
             print "Deleting %s" %srcFile
             log.write("Deleting %s\n" %srcFile)
             os.remove(srcFile)
            elif (srcFile.upper().endswith(".GIF")):
             print "Deleting %s" %srcFile
             log.write("Deleting %s\n" %srcFile)
             os.remove(srcFile)          
            elif (srcFile.upper().endswith(".NFO")):
             print "Deleting %s" %srcFile
             log.write("Deleting %s\n" %srcFile)
             os.remove(srcFile)
            elif (srcFile.upper().endswith(".PNG")):
             print "Deleting %s" %srcFile
             log.write("Deleting %s\n" %srcFile)
             os.remove(srcFile)
            elif (srcFile.upper().endswith(".JPG")):
             print "Deleting %s" %srcFile
             log.write("Deleting %s\n" %srcFile)
             os.remove(srcFile)
            elif (srcFile.upper().endswith(".JPEG")):
             print "Deleting %s" %srcFile
             log.write("Deleting %s\n" %srcFile)
             os.remove(srcFile)
            elif (srcFile.upper().endswith(".MP3")):
             log.write("Moving to iTunes add Folder %s\n" % srcFile)
             shutil.move(srcFile, addToiTunes)
            elif (srcFile.upper().endswith(".SRT")):
             print "Deleting %s" %srcFile
             log.write("Deleting %s\n" %srcFile)
             os.remove(srcFile)
            elif (srcFile.upper().endswith(".M3U")):
             print "Deleting %s" %srcFile
             log.write("Deleting %s\n" %srcFile)
             os.remove(srcFile)
            elif (srcFile.upper().endswith(".BMP")):
             print "Deleting %s" % srcFile
             log.write("Deleting %s\n" % srcFile)
             os.remove(srcFile)
            elif (srcFile.upper().endswith(".HTML")):
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
        except Exception as e:
            errors.write("Error Processing %s\n" % srcFile)
            errors.write("\t%s" % e)
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
