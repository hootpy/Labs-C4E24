import datetime
from gmail import *
import random

now = datetime.datetime.now()
email = GMail('<c4e24pythonhien@gmail.com>','Hienhunter96')

sickness_list = ["thuong han","kiet li","tieu chay"]
sickness = random.choice(sickness_list)

html_content= f'''
<p>Ch&agrave;o sếp!</p>
<p>S&aacute;ng nay em bị {sickness} nặng, tinh thần kh&ocirc;ng được tốt, long thể bất an&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
<p>Sếp cho em nghỉ ốm nh&eacute;,&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-tongue-out.gif" alt="tongue-out" /></p>
<p>Nh&acirc;n vi&ecirc;n</p>
'''
while True:
    if now.hour >= 7:
        msg = Message('Don xin nghi om',to='Huy<hienftu0511@gmail.com>',html=html_content)

        email.send(msg)
        break
    else:
        print("Wait to 7AM")
