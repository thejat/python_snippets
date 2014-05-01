import PyPDF2
import os

pdf = PyPDF2.PdfFileReader(open('ProgramMSOMwithlinks_021.pdf','rb'))
pgs = pdf.getNumPages()
key = '/Annots'
uri = '/URI'
ank = '/A'

links = []

for pg in range(pgs):
    p = pdf.getPage(pg)
    o = p.getObject()
    if o.has_key(key):
        ann = o[key]
        for a in ann:
            u = a.getObject()
            if u[ank].has_key(uri):
                links.append(u[ank][uri])
links = [x for x in set(links)]
for x in links:
	os.system('wget ' + x)
