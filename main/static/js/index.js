var qy;
var i;
i = 0;
$(document).ready(function() {
    $("#zzd").on("click",main);						
});
function main() { 
    $.getJSON(zzd_url,function(data) {
		if (data.login==true) {
			if (i !== 0) {
		        $.Toast('不可重复点击','请按下方按钮完成测试','warning',{
                    stack: true,
                    has_icon:false,
                    has_close_btn:true,
                    fullscreen:false,
                    timeout:3000,
                    sticky:false,
                    has_progress:true,
                    rtl:false
		        });
				return;
			}
		    $('#ss').text('你的智障度是：' + data.zzd);
	        var $two_choice = $('<br /> <button type="button" class="btn btn-primary btn-lg" id="kx">本测试科学</button> <button type="button" class="btn btn-primary btn-lg" id="bkx">本测试不科学</button>');
			$('div.d').append($two_choice);
			i += 1;
		    $('#kx').click(function() {
			if (data.zzd >= 50) {
			    qy = "low";
				zzd();
			}
			else {
				qy = "high";
				zzd();
			}
			});
		    $('#bkx').click(function() {
			if (data.zzd >= 50) {
				qy = "high";
				zzd();
			}
			else {
				qy = "low";
				zzd();
			}
			});
		}
		else {
		    $('#ss').text('你的智障度是：' + data.zzd);
			$.Toast('请登录','登录可享受精准测试与更多功能','warning',{
                stack: true,
                has_icon:false,
                has_close_btn:true,
                fullscreen:false,
                timeout:2000,
                sticky:false,
                has_progress:true,
                rtl:false
			});
		}
	});	
}
function zzd() {
	$.ajax({
		type:"POST",
		url:zzd_url,
		data:JSON.stringify({'qy':qy}),
		contentType:"application/json;charset=UTF-8",
		success: function(data) {
		$('div.d').text('');
		$('#ss').text('你的智障度实际是：' + data.zzd);
	    }
	});	
	i -= 1;
}