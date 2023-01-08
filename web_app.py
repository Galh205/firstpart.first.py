from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("C:\\Users\\galh\\OneDrive - Mobileye\\Documents\\DevOps\\chromedriver.exe"))


def get_user_name_from_db(user_id):
    pass

@app.route("/get_user_name")
def get_user_name(user_id):
    get_user_name_from_db(user_id)
    return "<H1 id='user'>" + user_name + "</H1>"

@app.route("/get_user_name")
def get_user_name(user_id):
 user_name = get_user_name_from_db(user_id)
 if user_name == None:
 return "<H1 id='error'>" no such user: + user_id + "</H1>"