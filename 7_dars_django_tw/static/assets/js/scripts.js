var getTimestamp = function (context_url, signature_hex, callback, fail) {
    $.ajax({
        url: context_url + '/dsvs/gettimestamp',
        method: 'POST',
        data: {
            signatureHex: signature_hex
        },
        success: function (data) {
            if (data.Success) {
                callback(data.Data);
            } else {
                fail(data.Reason);
            }
        },
        error: function (response) {
            fail(response);
        }
    });
}

var activateMenu = function (module) {
    var element = $("#menu-" + module);
    if (element.length) {
        element.addClass("active");
    }
}

var showNotification = function ($notification, html) {
    if (html) {
        $notification.html(html);
        $notification.show();
    }
};

var hideNotification = function ($notification) {
    $notification.html("");
    $notification.hide();
};

var enableElements = function () {
    for (var i = 0; i < arguments.length; i++) {
        $.each(arguments[i], function (i, item) {
            $(item).removeAttr("disable").removeAttr("disabled");

            if ($(item).getType() === "select" && typeof $(item).selectpicker === "function") {
                $(item).selectpicker("refresh");
            }
        });
    }
};

var disableElements = function () {
    for (var i = 0; i < arguments.length; i++) {
        $.each(arguments[i], function (i, item) {
            $(item).attr("disable", true).attr("disabled", true);

            if ($(item).getType() === "select" && typeof $(item).selectpicker === "function") {
                $(item).selectpicker("refresh");
            }
        });
    }
};

$.fn.getType = function () {
    if (this[0]) {
        return this[0].tagName === "INPUT" ? this[0].type.toLowerCase() : this[0].tagName.toLowerCase();
    }
};

$.fn.isEnable = function () {
    var $me = $(this[0]);
    if (!$me.attr("disabled")) {
        return true;
    }
    return false;
};
$.fn.isDisable = function () {
    var $me = $(this[0]);
    if (!$me.attr("disabled")) {
        return true;
    }
    return false;
};

// Button loader 
$.fn.startLoader = function () {
    var $me = $(this[0]);;
    if ($me.getType() == "button") {
        $me.attr("originHtml", $me.html());
        $me.html("<div class=\"loader center-block\"></div>");
    }
};
$.fn.stopLoader = function () {
    var $me = $(this[0]);
    if ($me.getType() == "button") {
        if ($me.attr("originHtml")) {
            $me.html($me.attr("originHtml"));
            $me.removeAttr("originHtml");
        }
    }
};

$.fn.enterKey = function(fnc) {
    return this.each(function() {
        $(this).keypress(function(ev) {
            var keycode = (ev.keyCode ? ev.keyCode : ev.which);
            if (keycode == '13') {
                fnc.call(this, ev);
            }
        });
    });
};

var rsubmitterTypes = /^(?:submit|button|image|reset|file)$/i;
var rsubmittable = /^(?:input|select|textarea|keygen)/i;
var rcheckableType = (/^(?:checkbox|radio)$/i);
var rCRLF = /\r?\n/g;

// String format
String.format = function () {
    var s = arguments[0];
    for (var i = 0; i < arguments.length - 1; i++) {
        var reg = new RegExp("\\{" + i + "\\}", "gm");
        s = s.replace(reg, arguments[i + 1]);
    }
    return s;
};

jQuery.fn.extend({
    serialize: function () {
        return jQuery.param(this.serializeArray());
    },
    serializeArray: function () {
        return this.map(function () {
            // Can add propHook for "elements" to filter or add form elements
            var elements = jQuery.prop(this, "elements");
            return elements ? jQuery.makeArray(elements) : this;
        })
            .filter(function () {
                var type = this.type;

                // Use .is( ":disabled" ) so that fieldset[disabled] works
                return this.name && !jQuery(this).is(":disabled") &&
                    rsubmittable.test(this.nodeName) && !rsubmitterTypes.test(type) &&
                    (this.checked || !rcheckableType.test(type));
            })
            .map(function (i, elem) {
                var val = jQuery(this).val();

                return val == null ?
                    null :
                    jQuery.isArray(val) ?
                        jQuery.map(val, function (val) {
                            return { name: elem.name, value: val.replace(rCRLF, "\r\n") };
                        }) :
                        { name: elem.name, value: val.replace(rCRLF, "\r\n") };
            }).get();
    },
    serializeAll: function () {
        return this.map(function () {
            // Can add propHook for "elements" to filter or add form elements
            var elements = jQuery.prop(this, "elements");
            return elements ? jQuery.makeArray(elements) : this;
        })
            .filter(function () {
                var type = this.type;

                // Use .is( ":disabled" ) so that fieldset[disabled] works
                return this.name && /*!jQuery( this ).is( ":disabled" ) &&*/
                    rsubmittable.test(this.nodeName) && !rsubmitterTypes.test(type) &&
                    (this.checked || !rcheckableType.test(type));
            })
            .map(function (i, elem) {
                var val = jQuery(this).val();

                return val == null ?
                    null :
                    jQuery.isArray(val) ?
                        jQuery.map(val, function (val) {
                            return { name: elem.name, value: val.replace(rCRLF, "\r\n") };
                        }) :
                        { name: elem.name, value: val.replace(rCRLF, "\r\n") };
            }).get();
    },
    serializeAllAsJson: function () {
        var json = {};
        var serialize = this.serializeAll();
        if (jQuery.isArray(serialize)) {
            jQuery.each(serialize, function (i, item) {
                json[item.name] = item.value;
            });
        }
        return json;
    }
});

var entityMap = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;',
    '/': '&#x2F;',
    '`': '&#x60;',
    '=': '&#x3D;'
};

var escapeHtml = function (string) {
    return String(string).replace(/[&<>"'`=\/]/g, function (s) {
        return entityMap[s];
    });
}

if (typeof Inputmask !== 'undefined') {
    Inputmask.extendAliases({
        facturaNumeric: {
            alias: "numeric",
            groupSeparator: " ",
            autoGroup: true,
            digits: 2,
//          digitsOptional: false
            placeholder: '',
            rightAlign: false,
            allowPlus: true,
            allowMinus: true
        }
    });

    Inputmask.extendAliases({
        facturaNumericRate: {
            alias: "numeric",
            groupSeparator: " ",
            autoGroup: true,
            digits: 4,
            placeholder: '',
            rightAlign: false,
            allowPlus: true,
            allowMinus: true
        }
    });

    if (typeof Inputmask !== 'undefined') {
        Inputmask.extendAliases({
            facturaDate: {
                alias: "dd.mm.yyyy",
                placeholder: "__.__.____",
                clearIncomplete: true
            }
        });
    }
}
