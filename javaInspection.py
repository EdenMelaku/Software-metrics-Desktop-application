import argparse
import datetime
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
javaComment= "(?://.*)|(/\\*(?:.|[\\n\\r])*?\\*/)"

javaImport="[import ][a-zA-Z\.\*\;]*"
def languageDefn(line):


   # print(line)
    #print()
    text=str(line)
    print(text)


    if not text.strip():
       return 0
    elif (re.search("^//",text)):
        return 3
    elif (re.search("^import", text)):
        return 2
    else:
        return 1



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    print("program started execution")
    parser.add_argument('--filename', required=True, help='Full path to file name ')

    args = parser.parse_args()
    file = args.filename
    g="impo eden"
    if(re.search("^import",g)):
        print("matched")
    else:
        print("not matched")


    inspectFile(file)




