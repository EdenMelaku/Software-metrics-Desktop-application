import argparse
import datetime
import os
import re


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date


def get_files( filename):

   info = filename.stat()
   print('{filename.name}\t Last Modified: {convert_date(info.st_mtime)}')


def inspectFile(filename):
    totalLoc = 0
    CommentedLoc = 0
    blankLoc = 0
    ActiveLoc = 0
    declaration =0

    extension = os.path.splitext(filename)[1]

    if (extension==".java"):

     print("THE FILE NAME IS  "+filename)

     with open(filename, 'r') as file:
        totalLoc=totalLoc+1


        line=file.readlines()
        for lii in line:
          li=languageDefn(lii)
          if li==1:
            ActiveLoc+=1

          elif li==0:
            blankLoc+=1

          elif li==3:
            CommentedLoc+=1

          else:
            declaration+=1

    sum=CommentedLoc+blankLoc+ActiveLoc+declaration
    print("toltal number of lines "+str(sum))
    print("commented lines "+str(CommentedLoc))
    print("blanck lines "+str(blankLoc))
    print("active lines "+str(ActiveLoc))
    print("import statements "+str(declaration))



    values=[ sum, CommentedLoc ,blankLoc ,ActiveLoc , declaration]

    return values





def languageDefn(line):


    #print("in method ")
    text=line;
    #print(text)


    if not text.strip():
       #print("empty")
       return 0

    elif (re.search("^// ",text.strip())):
        return 3
    elif (re.search("^//", text.strip())):
        return 3
        #print("commented")
    elif (re.search("^import ", text.strip())):
        return 2
        #print("import")

    else:
        #print("active")
        return 1




if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    print("program started execution")
    parser.add_argument('--filename', required=True, help='Full path to file name ')

    args = parser.parse_args()
    file = args.filename
    g="import eden"
    f=""
    k="dkfj"
    if(re.search("^\n",f)):
        print("matched")
    elif not f.strip():
        print("empty")
    else:
        print("not matched")



text="// comment  "

if not text.strip():
       print("empty")


elif (re.search("^// ",text)):

        print("commented")
elif (re.search("^//",text)):

        print("commented")
elif (re.search("^import ", text)):

        print("import")

else:
        print("active")

#inspectFile(file)




