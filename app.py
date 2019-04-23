import argparse
import os

from javaInspection import inspectFile


def returnFiles(baseDir):
 # List all subdirectories using os.listdir
 i=0
 j=0
 files=[]
 dir=[]


 basepath = baseDir
 for entry in os.listdir(basepath):

    if os.path.isdir(os.path.join(basepath, entry)):
        dir.append(os.path.join(basepath,entry))
        dir1=os.path.join(basepath,entry)

        j+=1
        for x in os.listdir(dir1):
            if os.path.isdir(os.path.join(dir1, x)):

                dir.append(os.path.join(dir1, x))
                dir2=os.path.join(dir1,x)
                j+=1
                for y in os.listdir(dir2):
                    if os.path.isdir(os.path.join(dir2, y)):
                        dir.append(os.path.join(dir2, y))
                        dir3=os.path.join(dir2,y)
                        j += 1
                        for z in os.listdir(dir3):
                            if os.path.isdir(os.path.join(dir3, z)):
                                dir.append(os.path.join(dir3, z))
                                j += 1
                            else:
                                files.append(os.path.join(dir3, z))
                                i += 1
                    else:
                        files.append(os.path.join(dir2, y))
                        i += 1

            else:
                files.append(os.path.join(dir1,x))
                i+=1


    else:
      files.append(os.path.join(basepath,entry))
      i+=1

 print("files  ="+str(len(files))+"   \n dir=  "+str(len(dir)))
 print("file names are ")
 for f in files :
     print (f)

 print("dir names are  ")

 for x in dir :
        print(x)

 return files,dir


totalLoc=0
CommentedLoc=0
blankLoc=0
ActiveLoc=0
def inspectFies(files,dir):

 for m in files :
     inspectFile(m)



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    print("program started execution")
    parser.add_argument('--dataFolder', required=True, help='Full path to project')

    args = parser.parse_args()
    folder=args.dataFolder
    files, dir=returnFiles(folder)




