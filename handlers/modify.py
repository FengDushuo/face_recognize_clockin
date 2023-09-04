import tornado.web
import tornado.escape
import methods.readdb as mrd
import methods.writedb as mwd
from handlers.base import BaseHandler
from handlers.forgetpwd import *

class ModifyHandler(BaseHandler):
    def get(self):
        # token = self.get_argument("token",default=None)
        # for user in USER_INFO.values():
        #     if User_Info["token"] == token:
        self.render("modify.html")

    def post(self):
        username = self.get_argument("username",default=None)
        password = self.get_argument("password",default=None)
        repassword = self.get_argument("repassword",default=None)
        email = self.get_argument("email",default=None)
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
        if username=="" or email=="" or password=="" or repassword=="":
            self.write("do_not_full!")
        else:
            if username:
                if email !=user_infos[0][3]:
                    self.write("username_email_unfit!")
                else: 
                    if repassword !=password:
                        self.write("repassword_is_false!")
                    else:
                        mwd.updateinfo("users",username,password,email)
                        self.write("success!")
            else:
                self.write("username_not_exist!")
                   