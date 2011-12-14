import xml.etree.ElementTree as ElementTree
import sys
import subprocess



if __name__ == "__main__":
    fname = sys.argv[1]
    txt = open(fname).read()
    tree = ElementTree.fromstring(txt)
    file_urls = [x.findtext('TRACKURL') for x in tree.find('TRACKLIST').findall('TRACK')]
    print 'grabbing the following urls'
    print file_urls
    for fu in file_urls:
        pipe = subprocess.Popen(["wget", fu],
                                stdout=subprocess.PIPE).stdout
        print pipe.read()
