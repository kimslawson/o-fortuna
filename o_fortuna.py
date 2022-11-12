from googletrans import Translator
import subprocess
w=0
while w<50000:
    f=subprocess.check_output(['fortune']).decode('utf-8')
    t=Translator()
    r=t.translate(f, dest='la')
    print(r.text, end='\n\n')
    w+=len(r.text.split())
