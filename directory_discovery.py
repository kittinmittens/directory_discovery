#!/usr/bin/python3
##me@danielpeluso.com
###Print all directories recursively taking in 1 argument
####lists depth of each directory from listed argument
import sys
import os
###
##
#
tt = sys.argv[1]
def ls(path):

    if hasattr(ls, "depth"):
     ls.depth += 1
    else:
     ls.depth = 0

    debug=1
    if debug:
       print
       print ('listed___path arg [' + path + ']')
       print ('listed______depth arg [' + str(ls.depth) + ']')


    list=os.listdir(path)
    for fn in list:
      if os.path.isdir(path + '/' + fn):
         ls(path + '/' + fn)
         print ('listed_________fn=[' + path + '/' + fn +'] ' + '[' + str(ls.depth) + ']')
         ls.depth-=1
      else:
         pass
#
##
#
def main():
   ls(tt)
   sys.exit(0)
#
##
#
if __name__== '__main__':
    main()
