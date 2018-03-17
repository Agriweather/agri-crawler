function ClearIfDefaultText(defaultText, e) {
    var input = GetElementTriggerEvent(e);
    if (input.value == defaultText) {
        input.value = "";
    }
}

function GetElementTriggerEvent(e) {
    var targ;
    if (!e) {
        e = window.event;
    }
    if (e.target) {
        targ = e.target;
    }
    else if (e.srcElement) {
        targ = e.srcElement;
    }
    if (targ.nodeType == 3) // defeat Safari bug
    {
        targ = targ.parentNode;
    }
    return targ;
}

//=============================================================================
//=   功能說明: 編審身份證字號是否正確
//=   傳入參數: pUserID : 要編審的號碼(身份證字號:10位文數字)
//=   傳回參數: 物件    : eErr           表編審成功/失敗
//=                       eErrDesc       編審失敗錯誤訊息
//=============================================================================
function gfcChkIdCard(pUserID) {
    var tobjRtn = new Object();  //-傳回Object
    var ixI;
    var tAreaNo;
    var tSum;
    var tAreaCode;
    var tSecondID;         //身份證第二碼

    if (pUserID == "" || pUserID == null) {
        tobjRtn.eErr = false;
        return tobjRtn;
    }
    tobjRtn.eErr = true;
    pUserID = pUserID.toUpperCase();
    if (pUserID.length != 10)//確定身份證字號有10碼
    {
        tobjRtn.eErrDesc = "輸入無效的身份證字號 (ex:資料長度錯誤) !";
        return tobjRtn;
    }
    tAreaCode = pUserID.substr(0, 1);
    if (tAreaCode.valueOf() < "A" || tAreaCode.valueOf() > "Z")//確定首碼在A-Z之間
    {
        tobjRtn.eErrDesc = "輸入無效的身份證字號 (ex:首碼應介於A-Z之間) !";
        return tobjRtn;
    }
    if (isNaN(parseInt(pUserID.substring(1, 10), 10)) == true) //確定2-10碼是數字
    {
        tobjRtn.eErrDesc = "輸入無效的身份證字號 (ex:第2-10碼須是數字) !";
        return tobjRtn;
    }
    //身份證號碼第 2 碼必須為 1 或 2
    tSecondID = pUserID.substr(1, 1);
    if (tSecondID != "1" && tSecondID != "2") {
        tobjRtn.eErrDesc = "輸入無效的身份證字號 !";
        return tobjRtn;
    }
    //取得首碼對應的區域碼，A ->10, B->11, ..H->17,I->34, J->18...
    tAreaNo = "ABCDEFGHJKLMNPQRSTUVXYWZIO".search(tAreaCode) + 10;
    pUserID = tAreaNo.toString(10) + pUserID.substring(1, 10);

    //  取得CheckSum的值
    //  核對身份證號碼是否正確
    //  A  = 身份證號碼區域碼第 1碼
    //  A0 = 身份證號碼區域碼第 2碼 * (10 - 1)
    //  A1 = 身份證號碼第 2碼 * (10 - 2)
    //  A2 = 身份證號碼第 3碼 * (10 - 3)
    //  A3 = 身份證號碼第 4碼 * (10 - 4)
    //  A4 = 身份證號碼第 5碼 * (10 - 5)
    //  A5 = 身份證號碼第 6碼 * (10 - 6)
    //  A6 = 身份證號碼第 7碼 * (10 - 7)
    //  A7 = 身份證號碼第 8碼 * (10 - 8)
    //  A8 = 身份證號碼第 9碼 * (10 - 9)
    //  CheckSum = A + A0 + A1 + A2 + ........ + A7 + A8

    tSum = parseInt(pUserID.substr(0, 1), 10) + parseInt(pUserID.substr(10, 1), 10);

    for (ixI = 1; ixI <= 9; ixI++) {

        tSum = tSum + parseInt(pUserID.substr(ixI, 1), 10) * (10 - ixI);

    }

    if ((tSum % 10) != 0) {
        tobjRtn.eErrDesc = "輸入無效的身份證字號 !";
        return tobjRtn;
    }
    tobjRtn.eErr = false;
    return tobjRtn;
}

function MM_swapImgRestore() { //v3.0
    var i, x, a = document.MM_sr; for (i = 0; a && i < a.length && (x = a[i]) && x.oSrc; i++) x.src = x.oSrc;
}

function MM_preloadImages() { //v3.0
    var d = document; if (d.images) {
        if (!d.MM_p) d.MM_p = new Array();
        var i, j = d.MM_p.length, a = MM_preloadImages.arguments; for (i = 0; i < a.length; i++)
            if (a[i].indexOf("#") != 0) { d.MM_p[j] = new Image; d.MM_p[j++].src = a[i]; }
    }
}

function MM_findObj(n, d) { //v4.01
    var p, i, x; if (!d) d = document; if ((p = n.indexOf("?")) > 0 && parent.frames.length) {
        d = parent.frames[n.substring(p + 1)].document; n = n.substring(0, p);
    }
    if (!(x = d[n]) && d.all) x = d.all[n]; for (i = 0; !x && i < d.forms.length; i++) x = d.forms[i][n];
    for (i = 0; !x && d.layers && i < d.layers.length; i++) x = MM_findObj(n, d.layers[i].document);
    if (!x && d.getElementById) x = d.getElementById(n); return x;
}

function MM_swapImage() { //v3.0
    var i, j = 0, x, a = MM_swapImage.arguments; document.MM_sr = new Array; for (i = 0; i < (a.length - 2); i += 3)
        if ((x = MM_findObj(a[i])) != null) { document.MM_sr[j++] = x; if (!x.oSrc) x.oSrc = x.src; x.src = a[i + 2]; }
}


function getToday(format) {
    var today = new Date();
    var year = today.getFullYear(); ;
    var month = today.getMonth() + 1;
    var day = today.getDate();
    if (format.indexOf('/') == 3) year = year - 1911;
    if (year < 100) year = '0' + year;
    if (month < 10) month = '0' + month;
    if (day < 10) day = '0' + day;
    return year + '/' + month + '/' + day;
}

function ajaxStart() {
    $.blockUI({ message: "程式執行中，請稍候...", fadeIn: 1500});
    //$.blockUI({ message: "<img src='/images/images/ajax-loader.gif' />" });
}
function ajaxStop() {
    $.unblockUI();
}

function CheckEndDateValueSeq(source, args) {
    args.IsValid = true; 
    var ControlToCompare = $("#" + source.controltovalidate).attr("ControlToCompare");
    if (!ControlToCompare) {        
        return;
    }

    var EndDate = $("#" + source.controltovalidate).val();
    var StartDate = $('[id$=' + ControlToCompare + ']').val();

    if (StartDate != "" && EndDate != "") {
        if (StartDate > EndDate) {            
            args.IsValid = false;
        }
    }
}

function CheckYearMonthValueSeq(source, args) {
    args.IsValid = true;
    var StartYear = $("#" + source.controltovalidate).attr("StartYear");
    var StartMonth = $("#" + source.controltovalidate).attr("StartMonth");
    var EndYear = $("#" + source.controltovalidate).attr("EndYear");

    if (!StartYear || !StartMonth || !EndYear) {
        return;
    }
    
    var sEndMonth = $("#" + source.controltovalidate).val();
    var sStartYear = $('[id$=' + StartYear + ']').val();
    var sStartMonth = $('[id$=' + StartMonth + ']').val();
    var sEndYear = $('[id$=' + EndYear + ']').val();

    if (sStartYear != "" && sStartMonth != "" && sEndYear != "" && sEndMonth != "") {
        if (sStartYear + sStartMonth > sEndYear + sEndMonth) {
            args.IsValid = false;
        }
    }
}

function InitCalendar() {
    //民國年
    $(".Wdate").prop('title', '日期格式為：' + getToday('yyy/MM/dd'));
    $(".Wdate").on("click", function () {
        WdatePicker({ dateFmt: 'yyy/MM/dd', realDateFmt: 'yyyy/MM/dd' });
    });
    //西元年
    $(".Fdate").prop('title', '日期格式為：' + getToday('yyyy/MM/dd'));
    $(".Fdate").on("click", function () {
        WdatePicker({ dateFmt: 'yyyy/MM/dd', realDateFmt: 'yyyy/MM/dd' });
    });
}

function RecoverDisabledWebControl() {
    $("select:disabled").each(function (i, v) {
        $(v).prop("disabled", false).css("background-color", "lightgray");
        $(v).find("option").each(function (j, opt) {
            if (!$(opt).prop("selected")) {
                $(opt).remove();
            }
        });
    });

    $("input[type=text]:disabled, textarea:disabled").each(function (i, v) {
        $(v).prop("disabled", false).prop("readOnly", true).css("background-color", "lightgray");
        $(v).off();
    });

    
}


function moveCenter(uri, winName, features, w, h) {
    var maxWidth = window.screen.width;
    var maxHeight = window.screen.height;
    var top = (maxHeight - h) / 2;
    var left = (maxWidth - w) / 2;
    var winObj = window.open(uri, winName, features + ",top=" + top + ",left=" + left);
    winObj.focus();
}

function ShowDialogMessage(divId, msg, InputOKClickStript) {
    var selDivId = "#" + divId;

    if ($(selDivId).length == 0) {
        alert(msg);
        eval(InputOKClickStript);
        return;
    }

    $(selDivId).html(msg);
    $(selDivId).dialog({
        title: '提示訊息',
        width: 550,
        position: [$(window).width() / 2 - 200, window.screen.height / 2 - 200],
        modal: true,
        buttons: {
            確定: function () {
                eval(InputOKClickStript);
                $(this).dialog('close');
            }
        }
    });
}

function OpenPicker(url, title) {
    var w = "800";
    var h = "600";
    var left = (screen.width / 2) - (w / 2);
    var top = (screen.height / 2) - (h / 2);
    return window.open(url, title, 'toolbar=no, location=no, directories=no, status=no, menubar=yes, scrollbars=yes, resizable=no, copyhistory=no'
        + ', width=' + w + ', height=' + h + ', top=' + top + ', left=' + left).focus();
}

function CallAjax(url, data, success) {
    ajaxStart();
    $.ajax({
        type: "POST",
        url: url,
        data: data,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        cache: false,
        success: function (response) {
            success(response);
        },
        error: function (response) {
            ShowCallBackErrorMessage(response);
        },
        complete: function () {
            ajaxStop();
        }
    });
}

function ShowCallBackErrorMessage(response) {
    var responseText = $.trim(response.responseText);
    if (responseText != "") {
        alert(responseText);
    }
}

function SetValidatorEnable(controlId, enabled) {
    if (typeof Page_Validators != 'undefined') {
        for (i = 0; i <= Page_Validators.length; i++) {
            var vldGrp = null;
            if (Page_Validators[i] != null) {
                if (Page_Validators[i].controltovalidate == controlId) {
                    ValidatorEnable(Page_Validators[i], enabled);
                }
            }
        }
    }
}