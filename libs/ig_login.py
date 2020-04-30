# coding=utf-8
#!/usr/bin/env python3

from instagram_private_api import Client
from libs.helpers import error, info, ask, success, report_account, clear_screen

def login_to_account(username, password):
    try:
        Client(username, password)
        return True
    except Exception as e:
        if (str(e) == "checkpoint_challange_required"):
            return True
        return False
    