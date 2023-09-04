$(document).ready(function(){
    //点击获得用户名，并跳转到大厅地址，用户名作为网址的参数传递

    $("tofaceinput").click(function(){
        alert("aaaaa")
        window.location.href="/workattendance.html"
    });
//     $("#webchatlogin").click(function(){
//         var user = $("#uname").val();
//         var pd = {"uname":user};
//         $.ajax({
//             type:"post",
//             url:"/webchatindex",
//             data:pd,
//             cache:false,
//             success:function(data){
//                 window.location.href = "/basic?u="+user;
//             },
//             error:function(){
//                 alert("error!");
//             },
//         });
//     });
 })