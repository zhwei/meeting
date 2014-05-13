function closeDialog() {

    $("#modalDialog").hide(400);
}

function showDialog(msg) {
    var w_parent = $("#modalDialog").parent().width();
    var w_self = $("#modalDialog").width();
    var position_x = ((w_parent) - (w_self) - (40)) / 2;
    $("#modalDialog").css({ left: position_x + "px" });

    $("#modalDialogText").html(msg)
    $("#modalDialog").show(400);
}
