
$(document).ready(function(){
    
    $("#resetpassword").click(function(){
        var user = $("#username").val();
        var pwd = $("#password").val();
        var rpwd = $("#repassword").val();
        var email = $("#email").val();
        var pd = {"username":user, "password":pwd, "repassword":rpwd,"email":email};
        $.ajax({
            type:"post",
            url:"/modify",
            data:pd,
            cache:false,
            success:function(data){
				if(data=="repassword_is_false!"){
                    alert("确认密码错误，请重新输入");
                }
                else if(data=="do_not_full!"){
                    alert("请补充好信息！")
                }
                else if(data=="username_email_unfit!"){
                    alert("用户名与邮箱不匹配！请重新输入！")
                }
                else if(data=="username_not_exist!"){
                    alert("用户不存在，请返回注册！")
                }
				else if(data=="success!"){
                    alert("修改成功，请登录！")
					window.location.href = "/";
				}
            },
            error:function(){
                alert("error!");
            },
        });
    });
});