function setHomepage() { // 设为首页
    if (document.all) {
        document.body.style.behavior = 'url(#default#homepage)';
        document.body.setHomePage(window.location);
    }
    //    else if (window.sidebar) {
    //        if (window.netscape) {
    //            try {
    //                netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
    //            }
    //            catch (e) {
    //                alert("您的浏览器不支持自动设为首页，请手动设置！", "提示信息");
    //            }
    //        }
    //        var prefs = Components.classes['@mozilla.org/preferences-service;1'].getService(Components.interfaces.nsIPrefBranch);
    //        prefs.setCharPref('browser.startup.homepage', window.location);
    //    } 
    else {
        alert("您的浏览器不支持自动设为首页，请手动设置！", "提示信息");
    }
} 
