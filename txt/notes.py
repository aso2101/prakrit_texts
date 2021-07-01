import re, os, string, sys
from pathlib import Path
from lxml import etree

inputfile  = sys.argv[1]
outputfile = inputfile.split(".")[0] + "-revised.xml"

def serialize(element,abbreviation,outfile):
    out = ""
    if element.tag == "{http://www.tei-c.org/ns/1.0}lg":
        chapterno = element.getparent().get("n")
        verseno = element.get("n")
        labels = element.findall("{http://www.tei-c.org/ns/1.0}label")
        lines = element.findall("{http://www.tei-c.org/ns/1.0}l")
        for label in labels:
            out += label.text + "\n"
        for number, line in enumerate(lines):
            caesuras = line.findall("{http://www.tei-c.org/ns/1.0}caesura")
            thisline = line.text
            if caesuras:
                for caesura in caesuras:
                    thisline += ", " + caesura.tail.strip()
            meter = ""
            if element.get("met") and number + 1 == len(lines):
                meter = " [" + element.get("met") + "]"
            thisline = re.sub("(॥|।)","",thisline.strip()) +  " // " + abbreviation + "." + chapterno + "." + verseno + labeldict[number] + meter + "\n"
            out += thisline
    print(out,file=outfile)
        

def recurse(elements,abbreviation,outfile):
    for element in elements:
        if element.tag in serializable:
            serialize(element,abbreviation,outfile)
        else:
            recurse(list(element),abbreviation,outfile)

initdig = re.compile("(^\d+)\. ")

if __name__ == "__main__":
    with open(inputfile,"r") as x:
        with open(outputfile,"w") as y:        
            for line in x:
                if re.match(initdig,line):
                    linenumber,entry = re.split(initdig,line)[-2:]
                    entries = entry.split(",")
                    readings = []
                    for entry in entries:
                        newentry = re.sub(r" *([^<]*) (<.*)",r'<rdg wit="\2">\1</rdg>',entry)
                        newentry = re.sub("<abbr>([^<]+?)\.</abbr>",r'#\1',newentry).strip()
                        readings.append(newentry)
                    line = linenumber + "<app>" + ''.join(readings) + """</app>
"""
                y.write(line)
