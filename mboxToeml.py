
import mailbox

mbx = mailbox.mbox("sample.mbox")

for k,v in mbx.iteritems():
    f=open("test"+str(k)+".eml",'w')
    f.write(str(v))
           
