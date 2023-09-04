


$(document).ready(function(){
    $("#toregister").click(function(){
        window.location.href = "/register";
    })
    $("#tologin").click(function(){
        window.location.href = "/";
    })
    $("#register").click(function(){
        var user = $("#rusername").val();
        var pwd = $("#rpassword").val();
        var rpwd = $("#rrepassword").val();
        var email = $("#remail").val();
        var accept = $("#accept-terms").is(":checked");
        var pd = {"rusername":user, "rpassword":pwd, "rrepassword":rpwd,"remail":email,"accept":accept,};
        $.ajax({
            type:"post",
            url:"/register",
            data:pd,
            cache:false,
            success:function(data){
				if(data=="repassword_is_false!"){
                    alert("确认密码错误，请重新输入");
                }
                else if(data=="do_not_full!"){
                    alert("请补充好信息！");
                }
				else if(data=="user_is_exist!"){
                    alert("该用户已存在，请登录！")
                }
                else if(data=="email_has_been_used!"){
                    alert("邮箱已被注册，请更换邮箱！")
                }
                else if(data=="not_checked!"){
                    alert("请同意用户协议！")
                }
				else if(data=="success!"){
                    alert("注册成功，请登录！")
					window.location.href = "/";
				}
            },
            error:function(){
                alert("error!");
            },
        });
    });
    $("#useragree").click(function(){
        var agreementtext = "《用户协议》\n"+
                            "不传播非法信息，宣传正能量。\n"+
                            "保护自己及他人的隐私。\n"+
                            "尊重自己及他人。\n"+
                            "祝您心情愉快。\n";
        alert(agreementtext);
    });
});
