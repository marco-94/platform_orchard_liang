// toast 弹窗
//调用方式
// toastr.error("错误");
// toastr.success('{{ result }}');
// toastr.warning("失败")
// toastr.info("你好")
toastr.options = {
    "closeButton": false, //是否显示关闭按钮
    "debug": false, //是否使用debug模式
    "progressBar": false, //是否显示进度条，当为false时候不显示；当为true时候，显示进度条，当进度条缩短到0时候，消息通知弹窗消失
    "positionClass": "toast-top-center",//显示的动画位置
    "showDuration": "400", //显示的动画时间
    "hideDuration": "400", //消失的动画时间
    "timeOut": "700", //展现时间
    // "extendedTimeOut": "1000", //加长展示时间
    "showEasing": "swing", //显示时的动画缓冲方式
    "hideEasing": "linear", //消失时的动画缓冲方式
    "showMethod": "fadeIn", //显示时的动画方式
    "hideMethod": "fadeOut" //消失时的动画方式
};