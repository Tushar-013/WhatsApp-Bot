import pywhatkit as kt
import getpass as gt


print("Lets Automate Whatsapp")

pnum=gt.getpass(prompt="Phonenumber: " ,stream=None)

msg ="hopw u will be fine"

kt.sendwhatmsg(pnum,msg,20,12)

