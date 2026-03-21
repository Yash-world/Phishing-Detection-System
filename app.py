from flask import Flask  , render_template , request
import re 
import pandas as pd
import tldextract 
import language_tool_python
tool = language_tool_python.LanguageTool('en-US')
import pytesseract

from PIL import Image




app=Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')


#url logic
phish_words = ['login', 'verify', 'update', 'bank', 'secure', 'account']
@app.route('/url', methods=["GET", "POST"])

def form():
    result = None
    max_score = 90 + (len(phish_words) * 10)
    risk_percentage = 0
    

    if request.method == "POST":
        url = request.form['url']
        score = 0
        

        if "@"in url:
            score += 10
        

        if url.startswith("http://"):
            score += 10
           

        if url.count('.') > 3:
            score += 10
       

        if len(url) > 60:
            score += 10
           
     
        if any(word in url.lower() for word in phish_words):
            score += sum(10 for word in phish_words if word in url.lower())
         

        ext = tldextract.extract(url)
        domain = ext.domain
        subdomain = ext.subdomain

        if '-' in domain:
            score += 10
           

        if subdomain.count('.') >= 2:
            score += 10
          

        if re.search(r'(\d{1,3}\.){3}\d{1,3}', url):
            score += 10
       

        if url.count('/') > 5:
            score += 10
        

        if re.search(r'http[s]?://[^/]+//', url):
            score += 10
        

        risk_percentage = round((score / max_score) * 100)

        if risk_percentage >= 60:
            result = "High Risk 🚨"
        elif risk_percentage >= 30:
            result = "Medium Risk ⚠"
        else:
            result = "Low Risk ✅"

        return render_template("dashboard.html",
                               result=result,
                               risk_percentage=risk_percentage)

    return render_template("url.html")

#email logic 


@app.route('/email', methods=["GET", "POST"])
def email_check():

    result = None
    matches = []
    email_risk_percentage = 0
  
    words = ['urgent', 'verify', 'login', 'password','bank', 'account', 
             'click', 'update','confirm', 'suspend', 'security alert']

    urgent_words = ['immediately', 'act now', 'limited time',
                    'within 24 hours', 'suspended']

    info_words = ['enter password', 'send otp','credit card',
                  'debit card','cvv']

    if request.method == "POST":

        email_text = request.form.get('email', '')
        screenshot = request.files.get('screenshot')

        if screenshot and screenshot.filename != "":
            image = Image.open(screenshot)
            extracted_text = pytesseract.image_to_string(image)
            email_text += " " + extracted_text.lower()

        email_text = email_text.lower()

     

        email_score = 0
        max_score = 30 + (len(words)*10) + (len(urgent_words)*10) + (len(info_words)*10)

    
        email_score += sum(10 for word in words if word in email_text)

     
        if email_text.count("http") >= 2:
            email_score += 10

      
        if re.search(r'\.(xyz|top|tk|gq)', email_text):
            email_score += 10

       
        email_score += sum(10 for word in urgent_words if word in email_text)

     
        email_score += sum(10 for word in info_words if word in email_text)

        
        matches = tool.check(email_text)
        error_count = len(matches)

        if error_count >= 10:
            email_score += 30
        elif error_count >= 5:
            email_score += 20
        elif error_count >= 2:
            email_score += 10

        email_risk_percentage = round((email_score / max_score) * 100)

        if email_risk_percentage >= 70:
            result = "High Risk 🚨"
        elif email_risk_percentage >= 40:
            result = "Medium Risk ⚠"
        else:
            result = "Low Risk ✅"

        return render_template("email.html",
                               email_text=email_text,
                               result=result,
                               email_risk_percentage=email_risk_percentage)

    return render_template('email.html')





#sms logic
keywords = ["urgent", "verify", "update", "click","login", "bank", "account", "suspended","winner", "free", "prize", "otp"] 
short_links = ["bit.ly", "tinyurl", "goo.gl", "t.co"]
urgent_words = ["immediately", "now", "within 24 hours", "act fast"]
fake_words = ["secure-login", "verify-account", "update-info"]



@app.route('/sms', methods=["GET", "POST"])
def sms_check():

    result = None


    if request.method == "POST":
        sms = request.form['sms']
        screenshot = request.files.get('screenshot')

        screenshot = request.files.get("screenshot")
        if screenshot and screenshot.filename != "":
            image = Image.open(screenshot.stream)
            extracted_text = pytesseract.image_to_string(image)
            sms = (sms or "") + "\n" + extracted_text



        sms_lower = sms.lower()
        score = 0
        risk_percentage = 0
        max_score =40 + (len(keywords)*10) + (len(short_links)*10) + (len(urgent_words)*10) + (len(fake_words)*10)




    


    
       
        if any(word in sms.lower() for word in keywords):
                score += sum(10 for word in keywords if word in sms.lower())

        
        if re.search(r"http[s]?://|www\.", sms_lower):
            score += 10

        
        if any(word in sms.lower() for word in short_links):
                score += sum(10 for word in short_links if word in sms.lower())

        
        digits = sum(c.isdigit() for c in sms)
        if digits > 6:
            score += 10

        
        if sms.isupper() and len(sms) > 15:
            score += 10

        
        if any(word in sms.lower() for word in urgent_words):
                score +=  sum(10 for word in urgent_words if word in sms.lower())

        if any(word in sms.lower() for word in fake_words):
                score +=  sum(10 for word in fake_words if word in sms.lower())


        risk_percentage = round((score / max_score) * 100)

        if risk_percentage >= 60:
            result = "High Risk 🚨"
        elif risk_percentage >= 30:
            result = "Medium Risk ⚠"
        else:
            result = "Low Risk ✅"

        

        return render_template("sms.html",
                               sms = sms ,
                               result=result,
                               risk_percentage=risk_percentage)

    return render_template("sms.html")






@app.route('/recovery', methods=["GET", "POST"])
def recovery():

    recovery_type = None
    steps = []

    if request.method == "POST":
        recovery_type = request.form.get("type")

        if recovery_type == "password":
            steps = [
                "Immediately change your password on the real website",
                "Enable 2FA (Two Factor Authentication)",
                "Logout from all devices",
                "Check login activity and remove unknown sessions"
            ]

        elif recovery_type == "bank":
            steps = [
                "Call your bank helpline immediately",
                "Block your debit/credit card",
                "Freeze online banking temporarily",
                "Immediately call Cyber Crime Helpline: 1930"
            ]

        elif recovery_type == "otp":
            steps = [
                "Immediately contact your bank",
                "Block your account temporarily",
                "Monitor transactions carefully"
            ]

        elif recovery_type == "device":
            steps = [
                "Disconnect from internet",
                "Run full antivirus scan",
                "Uninstall unknown applications",
                "Change passwords from another safe device"
            ]

    return render_template("recovery.html", steps=steps)



if __name__ == "__main__":
    app.run(debug=True)







    



        
