import re, os, string, sys, pathlib, subprocess
from lxml import etree
from itertools import chain

inputfile  = sys.argv[1]

if __name__ == "__main__":
    inputfilename = str(pathlib.Path(inputfile).resolve())
    xsl = os.path.abspath(str(pathlib.Path(sys.argv[0]).parent) + "/tei2text.xsl")
    outputfilename = inputfilename.replace('/tei/','/txt/').replace('.xml','.txt')
    source = "-s:'"+inputfilename+"'"
    stylesheet = "-xsl:'"+os.path.abspath(xsl)+"'"
    output = "-o:'"+outputfilename+"'"
    javacall = "java -cp /usr/share/java/*:/usr/share/java/ant-1.9.6.jar net.sf.saxon.Transform "+source+ " "+stylesheet+" "+output
    try:
        txt = subprocess.Popen(javacall,stdout=subprocess.PIPE,shell=True)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
