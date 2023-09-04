function getCookie(name){
    var x = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return x ? x[1]:undefined;
}

$(document).ready(function(){
    $("#login").click(function(){
        var user = $("#username").val();
        var pwd = $("#password").val();
        var pd = {"username":user, "password":pwd, "_xsrf":getCookie("_xsrf")};
        $.ajax({
            type:"post",
            url:"/",
            data:pd,
            cache:false,
            success:function(evt){
				if(evt=="passworderror"){
                    alert("密码错误，请重新输入");
				}
				else if(evt=="user_not_exist"){
                    alert("该用户不存在，请注册！")
                    
				}
				else{
					window.location.href = "/user";
				}
            },
            error:function(){
                alert("error!");
            },
        });
    });
});
