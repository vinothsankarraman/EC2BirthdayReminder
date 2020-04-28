import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
birthdayFile = '/home/ec2-user/birthdayreminder'

def checkTodaysBirthdays():
    fileName = open(birthdayFile, 'r')    
    today = time.strftime('%m%d')    
    flag = 0    
    for line in fileName:
        if today in line:
            line = line.split(' ')            
            firstname = line[1]           
            secondname = line[2]            
            flag = 1            
            emailcontent = 'Todays Birthday ' + firstname + ' ' + secondname
            fromaddr = "vinothemailbox@gmail.com"
            toaddr = "vinothemailbox@gmail.com"
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Birthday Today"
            body = emailcontent
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login("vinothemailbox@gmail.com", "sarojini_58")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()          
    if flag == 0:
    	    server = smtplib.SMTP('smtp.gmail.com', 587)
    	    server.ehlo()
    	    server.starttls()
    	    server.login("vinothemailbox@gmail.com", "sarojini_58")
    	    nmsg = 'No Birthdays Today'
    	    fromaddr = "vinothemailbox@gmail.com"
    	    toaddr = "vinothemailbox@gmail.com"
    	    msg = MIMEMultipart()
    	    msg['From'] = fromaddr
    	    msg['To'] = toaddr
    	    msg['Subject'] = "Birthday Today"
    	    body = nmsg
    	    msg.attach(MIMEText(body, 'plain'))
    	    text = msg.as_string()
    	    server.sendmail(fromaddr, toaddr, text)
    	    server.quit()
        

if __name__ == '__main__':
    checkTodaysBirthdays()