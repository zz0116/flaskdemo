from flask import Flask

app = Flask(__name__)

# 为什么放在上面会导致views.py页面ImportError: cannot import name 'app'？
# 因为这一句相当于把views代码粘到这，而app是在上面定义的，views里面用到了app
from app import views
from app.controller import post
