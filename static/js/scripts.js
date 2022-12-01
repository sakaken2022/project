/*!
* Start Bootstrap - Clean Blog v6.0.8 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})

var send_post = new XMLHttpRequest();
var send_get2 = new XMLHttpRequest();
var res_post, timerID, res_get2;

function setSrc_Java() {
	document.form1.fmout.value = ' ';
	document.form1.fmerr.value = ' ';
	document.form1.fmlan.value = "java";
}


function postPaiza() {
	var src = document.form1.fmsrc.value;
	var lan = document.form1.fmlan.value;
	var inp = document.form1.fminp.value;
	var para = "source_code=" + src + "&language=" + lan + "&api_key=guest";
	console.log(src);
	
    send_post.open('POST', 'http://api.paiza.io/runners/create', true);
    send_post.responseType = 'json';
	send_post.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=Shift-JIS');
	send_post.setRequestHeader('Access-Control-Allow-Origin', 'http://api.paiza.io/');
    send_post.send(para);
}

send_post.onload = function () {
	res_post = this.response;
	console.log(res_post["id"]);
	timerID = setInterval("getPaiza2()", 2000);
}

function getPaiza2() {
	clearInterval(timerID);
	var url2 = "http://api.paiza.io:80/runners/get_details?id=" + res_post["id"] + "&api_key=guest";
    send_get2.open('GET', url2, true);
    send_get2.responseType = 'json';
    send_get2.send();
}

send_get2.onload = function () {
	res_get2 = this.response;
	console.log(res_get2["stdout"]);
	console.log(res_get2["build_stderr"]);
	document.form1.fmout.value = res_get2["stdout"];
	document.form1.fmerr.value = res_get2["build_stderr"];
}
