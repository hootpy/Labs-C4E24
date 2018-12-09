from gmail import *
from random import randint


sickness_list = ["thuong han","kiet li","tieu chay"]
i = randint(0,len(sickness_list)-1)
sickness = sickness_list[i]

#1. Select a sickness
html_template= '''
<p>Ch&agrave;o sếp!</p>
<p>S&aacute;ng nay em bị {{sickness}} nặng, tinh thần kh&ocirc;ng được tốt, long thể bất an&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
<p>Sếp cho em nghỉ ốm nh&eacute;,&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-tongue-out.gif" alt="tongue-out" /></p>
<p>Nh&acirc;n vi&ecirc;n</p>
'''

html_content = html_template.replace("{{sickness}}",sickness)

email = GMail('Hien.<c4e24pythonhien@gmail.com>','Hienhunter96')

msg = Message('Test message',to='Huy<c4e.techkidsvn@gmail.com>',html=html_content)

email.send(msg)