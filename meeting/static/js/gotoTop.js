(function ($) {
    var goToTopTime;
    $.fn.goToTop = function (options) {
        var opts = $.extend({}, $.fn.goToTop.def, options);
        var $window = $(window);
        $body = (window.opera) ? (document.compatMode == "CSS1Compat" ? $('html') : $('body')) : $('html,body');
        // opera fix
        //$(this).hide();
        var $this = $(this);
        clearTimeout(goToTopTime);
        goToTopTime = setTimeout(function () {
            //var controlLeft;
            //if ($window.width() > opts.pageHeightJg * 2 + opts.pageWidth) {
            //    controlLeft = ($window.width() - opts.pageWidth) / 2 + opts.pageWidth + opts.pageWidthJg;
            //} else {
            //    controlLeft = $window.width() - opts.pageWidthJg - $this.width();
            //}



            //判断是否ie6
            var cssfixedsupport = $.browser.msie && parseFloat($.browser.version) < 7;

            //左侧
            //ie6:直接containerX
            //非ie6:container的左侧+containerX,而左侧的计算应该用(window.width-continaer.width)/2
            //var controlLeft = cssfixedsupport ? opts.containerX : ($window.width() - $(opts.containerObj).width()) / 2 + opts.containerX;
            var controlLeft =  ($window.width() - $(opts.containerObj).width()) / 2 + opts.containerX;
            


            //ie6 ".container" releative
            //if (cssfixedsupport) {
            //    $(opts.containerObj).css({
            //        position: 'relative'
            //    });
            //}



            var controlTop = $window.height() - $this.height() - opts.containerBtn;
            controlTop = cssfixedsupport ? $window.scrollTop() + controlTop : controlTop;


            var shouldvisible = ($window.scrollTop() >= opts.startline) ? true : false;
            if (shouldvisible) {
                $this.stop().show();
            } else {
                $this.stop().hide();
            }

            $this.css({
                position: cssfixedsupport ? 'absolute' : 'fixed',
                top: controlTop,
                //left: controlLeft
                right:0 //空白最右边
            });
        }, 30);

        $(this).click(function (event) {
            $body.stop().animate({ scrollTop: $(opts.targetObg).offset().top }, opts.duration);
            $(this).blur();
            event.preventDefault();
            event.stopPropagation();
        });
    };

    $.fn.goToTop.def = {
        //pageWidth: 910,
        //页面宽度
        //pageWidthJg: 2,
        //按钮和页面的间隔距离
        //pageHeightJg: 171,
        //按钮和页面底部的间隔距离
        startline: 30,
        //出现回到顶部按钮的滚动条scrollTop距离
        duration: 200,
        //回到顶部的速度时间
        targetObg: "body",
        //目标位置 linzh--modify
        //containerObj: ".container",
        containerObj: "body",
        containerX: 958,
        containerBtn: 171
        //距离Container的X坐标为958
        //不管是不是ie6,都是直接添加到body中去，
        //而位置总是要固定在Container内的X坐标为958的地方
        //所以Left是相对body的，距离要计算Container的左侧空白+ Container的X坐标
    };
})(jQuery);
$(function () {
    $('<a href="javascript:;" class="backToTop" title="返回顶部">&nbsp;</a>').appendTo("body");
});