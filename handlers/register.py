import tornado.escape
import methods.readdb as mrd
import methods.writedb as mwd
from handlers.base import BaseHandler

class RegisterHandler(BaseHandler): 
    def get(self):
        self.render("register.html", type_="register")

    def post(self):
        username = self.get_argument("rusername",default=None)
        password = self.get_argument("rpassword",default=None)
        repassword = self.get_argument("rrepassword",default=None)
        email = self.get_argument("remail",default=None)
        accept = self.get_argument("accept",default=None)
        dbinfo = mrd.select_dics("users","*")
        print(username,password)
        usrs,pwds,emails=zip(*map(lambda x: (x["username"],x["password"],x["email"]),dbinfo))
        if username=="" or password=="" or repassword=="" or email=="":
            self.write("do_not_full!")
        else:
            if username in usrs:
                self.write("user_is_exist!")
            else:
                if email in emails:
                    self.write("email_has_been_used!")
                else:
                    if repassword !=password:
                        self.write("repassword_is_false!")
                    else:
                        if accept=="true":
                            mwd.insertinfo("users",username,password,email)
                            self.write("success!")
                        else:
                            self.write("not_checked!")

