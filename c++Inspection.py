import datetime


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date


def get_files(filename):
    info = filename.stat()
    print('{filename.name}\t Last Modified: {convert_date(info.st_mtime)}')


def inspectFile(filename):
    totalLoc = 0
    CommentedLoc = 0
    blankLoc = 0
    ActiveLoc = 0

    with open(filename, 'rb') as file:
        totalLoc = totalLoc + 1

        line = file.readline()
        li = languageDefn(line)
        if li == 1:
            ActiveLoc += 1

        elif li == 0:
            blankLoc += 1

        elif li == 3:
            CommentedLoc += 1


def languageDefn(line):
