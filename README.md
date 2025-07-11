# flask-aws-vpc-deploy
Flask AWS VPC Deployment

**📌 VPC Architecture Diagram**
vpc-diagram.png

**🚀 Deployment Steps**
Launch EC2 Instance in a public subnet of your custom VPC.

**Install dependencies:**
sudo apt update
sudo apt install python3-pip nginx -y
python3 -m venv venv
source venv/bin/activate
pip install flask

**Create Flask App (app.py):**
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Flask App running in AWS VPC!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

**Allow port 5000 in EC2 security group.**

**Edit Nginx config:**
sudo nano /etc/nginx/sites-available/default

Replace the server block with this:
server {
    listen 80;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

**sudo systemctl restart nginx**

**Run the App:**
python3 app.py

**Access it via:**
http://<EC2_PUBLIC_IP>:5000

**🌐 EC2 Public IP**
Example: http://13.53.214.123:5000
ec2-screenshot.png


**Note:**
🔓 Allow Port 5000 in Security Group
EC2 > Security Groups > [Your instance's SG]
Inbound Rules → Edit
Type: Custom TCP
Port: 5000
Source: 0.0.0.0/0 (or your IP)
