import argparse
import os

from javaInspection import inspectFile

result=""


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
 global result
 result=result+"files  ="+str(len(files))+"   \n dir=  "+str(len(dir))
 print("files  ="+str(len(files))+"   \n dir=  "+str(len(dir)))
 result=result+"\nfile names are\n"
 print("file names are ")
 for f in files :
     result="\n"+f
     print (f)

 print("dir names are  ")
 result="\ndir names are \n"
 for x in dir :
     result="\n"+x
     print(x)

 return files,dir


totalLoc=0
CommentedLoc=0
blankLoc=0
ActiveLoc=0
DeclarationLoc=0




def inspectFiles(files,dir):
 TLOC = 0
 CLOC = 0
 BLOC = 0
 ALOC = 0
 DLOC = 0

 valls = []
 for m in files :
     values=inspectFile(m)
     valls.append(values)
    # TLOC.append(values[0])
     #CLOC.append(values[1])
     #BLOC.append(values[2])
     #ALOC.append(values[3])
     #DLOC.append(values[4])
     print(m)

     for num in values:
      print(num)

 global text
 i=0
 print("GENERATING TOTAL REPORT ")
 text=text+"GENERATING TOTAL REPORT "
 for k in valls:
     #print("name of file ----------  total number of line ----- commented------- blank--------active-----declaration")
    # print(str(k)+"-----"+str(TLOC[i])+"-----"+str(CLOC[i])+"-----"+str(BLOC[i])+"-----"+str(ALOC[i])+"-----"+str(DLOC[i]))
     sum=0
     TLOC=TLOC+k[0]
     CLOC=CLOC+k[1]
     BLOC=BLOC+k[2]
     ALOC=ALOC+k[3]
     DLOC=DLOC+k[4]

 text = text +"toltal number of lines "+str(TLOC)
 text=text+"commented lines "+str(CLOC)
 text=text+"blanck lines "+str(BLOC)
 text=text+"active lines "+str(ALOC)
 text=text+"import statements "+str(DLOC)

 print("toltal number of lines "+str(TLOC))
 print("commented lines "+str(CLOC))
 print("blanck lines "+str(BLOC))
 print("active lines "+str(ALOC))
 print("import statements "+str(DLOC))

def toPage(dir,files):
   inspectFiles(files,dir)
   global text
   return text

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    print("program started execution")
    parser.add_argument('--dataFolder', required=True, help='Full path to project')

    args = parser.parse_args()
    folder=args.dataFolder
    files, dir=returnFiles(folder)
    inspectFiles(files,dir)




