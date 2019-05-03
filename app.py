import argparse
import os

from javaInspection import inspectFile

#tasks to do 











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
DeclarationLoc=0

TLOC=[]
CLOC=[]
BLOC=[]
ALOC=[]
DLOC=[]


def inspectFiles(files,dir):

 for m in files :
     t,c,b,a,d=inspectFile(m)
     TLOC.append(t)
     CLOC.append(c)
     BLOC.append(b)
     ALOC.append(a)
     DLOC.append(d)
 i=0
 print("GENERATING TOTAL REPORT ")
 for k in files:
     print("name of file ----------  total number of line ----- commented------- blank--------active-----declaration")
     print(str(k)+"-----"+str(TLOC[i])+"-----"+str(CLOC[i])+"-----"+str(BLOC[i])+"-----"+str(ALOC[i])+"-----"+str(DLOC[i]))


     i+=1



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    print("program started execution")
    parser.add_argument('--dataFolder', required=True, help='Full path to project')

    args = parser.parse_args()
    folder=args.dataFolder
    files, dir=returnFiles(folder)
    inspectFiles(files,dir)




