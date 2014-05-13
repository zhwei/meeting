function AddFavorite() {



    try {
        //IE
        var sURL = window.location;
        var sTitle = document.title;
        window.external.addFavorite(sURL, sTitle); 
    } catch (e) { 
        try {
            //Firefox
            var sURL = window.location;
            var sTitle = document.title;
            window.sidebar.addPanel(sTitle, sURL, ""); 
        } catch (e) { 
            alert("您的浏览器不支持自动加入收藏，请手动设置！", "提示信息");   
        } 
    } 
}