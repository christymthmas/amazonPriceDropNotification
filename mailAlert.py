import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def mailing(brand,DESIRED_PRICE,url,fromaddr,password,toaddr,yourname,productTitle,amazonPrice,youSave,youSavePercentage):    
   
    # instance of MIMEMultipart
    msg = MIMEMultipart()
    
    # storing the senders email address  
    msg['From'] = fromaddr
    
    # storing the receivers email address 
    msg['To'] = toaddr
    
    # storing the subject 
    msg['Subject'] = "Price drop detected!"

    if len(productTitle)>80:
        tail = "..."
    else:
        tail =""
    productTitle = productTitle[:80]
    # string to store the body of the mail
    if youSave==-1:
        body = """\
<span style=""font-family:Arial,Helvetica,Sans-Serif;">
Hey {},<br><br>

Price dropped on <a href = {}>{}{} <b>!!</b></a><br>
<span style="font-size:12px;font-weight:normal;font-style:normal;text-decoration:none;color:#333;text-align:left;margin:0;">by <b>{}</b><br></span>

Desired Price&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size:12px;font-weight:normal;color:#cc0000">₹ {:,}</span><br>
Current Price&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size:13px;font-weight:bold;color:#cc0000">₹ {:,}</span><br>
<br>
Grab your deal <b>NOW!</b>
</span>
""".format(yourname,url,productTitle,tail,brand,DESIRED_PRICE,amazonPrice)

    else:
        body = """\
<span style=""font-family:Arial,Helvetica,Sans-Serif;">
Hey {},<br><br>

Price dropped on <a href = {}>{}{} <b>!!</b></a><br>
<span style="font-size:12px;font-weight:normal;font-style:normal;text-decoration:none;color:#333;text-align:left;margin:0;">by <b>{}</b><br></span>

Desired Price&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size:12px;font-weight:normal;color:#cc0000">₹ {:,}</span><br>
Current Price&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size:13px;font-weight:bold;color:#cc0000">₹ {:,}</span><br>

<span style="font-size:12px;color:#333;">-----You'll save ₹ {:,} ({}%)-----</span>
<br><br>
Grab your deal <b>NOW!</b>
</span>
""".format(yourname,url,productTitle,tail,brand,DESIRED_PRICE,amazonPrice,youSave,youSavePercentage)
    
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'html'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.ehlo()

    # start TLS for security
    s.starttls()

    s.ehlo()

    # Authentication
    try:
        s.login(fromaddr, password)
    except:
        print("\n\n--------login error---------\n\n")
        return
    # Converts the Multipart msg into a string
    text = msg.as_string()
    
    # sending the mail
    try:
        s.sendmail(fromaddr, toaddr, text)
        print("\n\n--------notification has been sent to '{}'----------\n\n".format(toaddr))
    except:
        print("\n\n--------unexpecter error happened while senting mail---------\n\n")
    # terminating the session
    s.quit()

if __name__=="__main__":

    #this is only for testing the mail
    url = "https://www.amazon.in/dp/B09576CYNP?pf_rd_r=1D7A788Z4MRSM1RFY8XG&pf_rd_p=ebc78bad-a4b8-486c-821a-3075becda16e&pd_rd_r=b576cc25-f9bb-43f6-b322-94ac37bc0be5&pd_rd_w=2nHhJ&pd_rd_wg=PVkje&ref_=pd_gw_unk"
    amazonPrice = 24999
    brand="One Plus"
    productTitle = "OnePlus Nord CE 5G (Charcoal Ink, 8GB RAM, 128GB Storage)"
    email="something@gmail.com"
    password = "password"
    rec_email= "something@gmail.com"
    name = "Your Name"
    
    mailing(brand,25000,url,email, password, rec_email, Name ,productTitle, amazonPrice,-1,-1)
