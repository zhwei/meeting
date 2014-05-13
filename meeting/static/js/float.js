jQuery.fn.float = function (settings) {
    if (typeof settings == "object") {
        settings = jQuery.extend({
            delay: 600,
            offset: {
                left: 0,
                right: 0,
                top: 0,
                bottom: 220
            },
            style: null, //
            width: 220,  //
            height: 400, //
            position: "rm" //
        }, settings || {});
        var winW = 1000; // $(window).width();
        var winH = $(window).height(); // $(window).height();

        function getPosition($applyTo, position) {
            var _pos = null;
            $applyTo.data("offset", "left");
            $applyTo.data("offsetPostion", settings.offset.left);
            _pos = { left: settings.offset.left, top: settings.offset.top };
            return _pos;
        } //function getPosition

        function setPosition($applyTo, position, isUseAnimate) {
            var scrollTop = $(window).scrollTop();
            var scrollLeft = $(window).scrollLeft();
            var _pos = getPosition($applyTo, position);
            _pos.top += scrollTop;
            //            if (_pos.top > settings.offset.top + 230) {
            //                _pos.top -= 80;

            //                var ie7 = $.browser.msie && parseFloat($.browser.version) >= 7;
            //                if (ie7) {
            //                    _pos.top -= 150;
            //                }
            //            }

            var nums = $("#floatMenu ul li").size();

            var footerH = $(".footer").height();
            //360 is top, 50 is from h3 title
            var nH = 50 + nums * 25 + footerH;
            if (_pos.top + nH > winH) 
            {
                _pos.top -= nH;
            }


            isUseAnimate && $applyTo.stop().animate(_pos, settings.delay) || $applyTo.css(_pos);
        } // function setPosition
        return this.each(function () {
            var $this = $(this);
            $(".leftPart").css("position", "relative");
            $this.css("position", "absolute");
            settings.style && $this.css(settings.style);
            setPosition($this, settings.position);
            $(this).data("isAllowScroll", true);
            $(window).scroll(function () {
                $this.data("isAllowScroll") && setPosition($this, settings.position, true);
            });
        })
    } else {
        var speed = arguments.length > 1 && arguments[1] || "fast";
        this.each(function () {
            if (settings == "clearOffset") {
                var _c = {};
                if ($(this).data("offset")) {
                    _c[$(this).data("offset")] = 0;
                    $(this).data("isAllowScroll", false);
                    $(this).stop().animate(_c, speed);
                }
            } else if (settings == "addOffset") {
                var _c = {};
                if ($(this).data("offset") && $(this).data("offsetPostion")) {
                    _c[$(this).data("offset")] = $(this).data("offsetPostion");
                    $(this).stop().animate(_c, speed);
                    $(this).data("isAllowScroll", true);
                }

            } else if (settings == "setScrollDisable") {
                $(this).data("isAllowScroll", false);
            } else if (settings == "setScrollUsable") {
                $(this).data("isAllowScroll", true);
            }
        })
    }
}		  
