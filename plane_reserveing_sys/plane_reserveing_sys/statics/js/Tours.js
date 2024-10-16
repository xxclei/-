$(document).ready(function(){
    // 当鼠标移动到侧边栏时显示
    var sidebartriger = 30; // 侧边栏宽度
    var sidebarWidth = 180; // 侧边栏宽度
    var sidebarVisible = false; // 侧边栏初始状态为不可见

    // 鼠标移动到屏幕左边一定区域自动展开侧边栏
    $(document).mousemove(function(e){
        if (e.pageX >sidebarWidth) {
            if (!sidebarVisible) {
                $('#sidebar').addClass('active');
                sidebarVisible = true;
                $('#toggleBtn').addClass('hidden');
            }
        } 
        
        if (e.pageX <=sidebartriger) {
            if (sidebarVisible) {
                $('#sidebar').removeClass('active');
                sidebarVisible = false;
                $('#toggleBtn').removeClass('hidden');
            }
        }
    });
    // 点击展开按钮时切换侧边栏状态
    $('#toggleBtn').click(function(){
        $('#sidebar').toggleClass('active');
        if ($('#sidebar').hasClass('active')) {
            $(this).addClass('hidden');
        } else {
            $(this).removeClass('hidden');
        }
    });

    // 侧边栏链接点击事件
    $('#sidebar a:not(.toggle-btn)').click(function(e){
        e.preventDefault();
        var target = $(this).data('target');
        $('div.content').removeClass('active');
        $(target).addClass('active');
    });

    // 侧边栏内部收起按钮
    $('#sidebar .toggle-btn').click(function(e){
        e.preventDefault();
        $('#sidebar').toggleClass('active');
        if ($('#sidebar').hasClass('active')) {
            $('#toggleBtn').addClass('hidden');
        } else {
            $('#toggleBtn').removeClass('hidden');
        }
    });
});
$(document).ready(function() {
    $('a').click(function(e) {
        e.preventDefault();
        var target = $(this).data('target');
        $('.content').hide(); // 隐藏所有内容区域
        $(target).show(); // 显示目标内容区域
        $('a').removeClass('active'); // 移除所有链接的active类
        $(this).addClass('active'); // 添加active类到当前点击的链接
    });
});
$(document).ready(function() {
    // 身份证号验证
    $('#id_number').on('input', function() {
        const idNumber = $(this).val();
        const regex = /^(^[1-9]\d{5}(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}([0-9Xx])$)$/; // 身份证号正则表达式
        if (!regex.test(idNumber)) {
            $('#id_error').text('身份证号码格式错误').show();
        } else {
            $('#id_error').hide();
            // 调用后端获取用户信息的函数
            fetchUserInfo(idNumber);
        }
    });

    // AJAX获取用户信息
    function fetchUserInfo(idNumber) {
        $.ajax({
            url: '/get_user_info/', // 后端处理请求的URL
            method: 'GET',
            data: { id_number: idNumber },
            success: function(response) {
                $('#user-info').empty();
                if (response.user_info.length > 0) {
                    response.user_info.forEach(user => {
                        $('#user-info').append(`<p>姓名: ${user.name}, 性别: ${user.gender}, 工作单位: ${user.work_unit}, 旅行时间: ${user.travel_date}, 目的地: ${user.destination}</p>`);
                    });
                } else {
                    $('#user-info').append('<p>未找到用户信息。</p>');
                }
            },
            error: function() {
                $('#user-info').append('<p>获取用户信息失败。</p>');
            }
        });
    }
});