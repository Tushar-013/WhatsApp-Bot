import pywhatkit as kt
import getpass as gt





phonenumber=gt.getpass(prompt="Phone number: " ,stream=None)

msg ="Hello I'm a Whatsapp bot"
# 20,12 is time format ,it takes 24 hrs time format
kt.sendwhatmsg(phonenumber,msg,20,12)

