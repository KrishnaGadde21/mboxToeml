import mailbox,os
from email import generator
#from email.header import decode_header
#import base64


mbx = mailbox.mbox("sample.mbox")

saveEML_to = 'MboxToEmlAndAttch/EML/'
if not os.path.exists(saveEML_to):
    os.makedirs(saveEML_to)


saveAttch_to = 'MboxToEmlAndAttch/Attch/'
if not os.path.exists(saveAttch_to):
    os.makedirs(saveAttch_to)

for k,v in mbx.iteritems():
    with open(saveEML_to+str(k)+".eml",'w') as f:
        gen = generator.Generator(f)
        gen.flatten(v)
        
        

def extractattch(i):
    if i.get_content_maintype()=='multipart':
        for part in i.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            f=part.get_filename()
            print(f)


            if not os.path.exists(saveAttch_to):
                os.makedirs(saveAttch_to)


            fb = open( saveAttch_to+f,'wb')
            fb.write(part.get_payload(decode=True))
            fb.close()

            print()

for i in mbx:
    extractattch(i)        
