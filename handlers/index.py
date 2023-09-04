import tornado.escape
import methods.readdb as mrd
from handlers.base import BaseHandler

class IndexHandler(BaseHandler):    #继承base.py中的类BaseHandler
    def get(self):
        usernames = mrd.select_columns(table="users",column="username")
        self.render("index.html")

    def post(self):
        username = self.get_argument("username",default=None)
        password = self.get_argument("password",default=None)
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.set_current_user(username)    #将当前用户名写入cookie，方法见下面
                self.write(username)
                self.redirect('/user')

            else:
                self.write("passworderror")
        else:
            self.write("user_not_exist")

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', tornado.escape.json_encode(user))    #注意这里使用了tornado.escape.json_encode()方法
        else:
            self.clear_cookie("user")

