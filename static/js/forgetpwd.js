
$(document).ready(function(){
    $("#toforgetpwd").click(function(){
        window.location.href="/forgetpwd"
    });


    $("#forgetpwd").click(function(){
        var user = $("#username").val();
        var email = $("#email").val();
        var domain = document.domain;
        var pd = {"username":user, "email":email,"domain":domain};
        $.ajax({
            type:"post",
            url:"/forgetpwd",
            data:pd,
            cache:false,
            success:function(evt){
                alert("邮件可能发送较慢，点击按钮后请稍等半分钟！")
				if(evt=="no_email_exist"){
                    alert("输入的邮箱没有注册，请检查是否输错！");
				}
				else if(evt=="success_send_email"){
                    alert("找回密码邮件已发送，请查收，如果没收到提示请检查邮箱垃圾箱！");
                    window.location.href="/"                    
                }
                else{
                    alert("如需找回密码，请输入您的邮箱！")
                }
            },
            error:function(){
                alert("error!");
            },
        });
    });
});
