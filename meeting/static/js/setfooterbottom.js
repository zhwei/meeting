$(function () {
    if ($(window).height() > $("body").height()) {
        var cssfixedsupport = $.browser.msie && parseFloat($.browser.version) < 7;
        $(".footer").css(
                {
                    position: cssfixedsupport ? 'absolute' : 'fixed',
                    bottom: 0,
                    left: 0
                });
            } //if
   
});