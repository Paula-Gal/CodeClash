window.onload = function () {
    $('.btn-dashboard').addClass('scale-up-center');
    document.getElementById("loading").style.display = "none";
    $('#loading').fadeIn();
}

onReady(function () {
    var page = $('.page');
    var loading = $('#loading');
    loading.fadeOut();
    setTimeout(function(){page.fadeIn();}, 300);
    setTimeout(function(){
        setVisible('.page', true);
        setVisible('#loading', false);
    }, 1000);
});

function onReady(callback) {
    var intervalId = window.setInterval(function () {
        if (document.getElementsByTagName('body')[0] !== undefined) {
            window.clearInterval(intervalId);
            callback.call(this);
        }
    }, 1000);
}

function fade(element) {
    var op = 1;  // initial opacity
    var timer = setInterval(function () {
        if (op <= 0.1){
            clearInterval(timer);
            element.style.display = 'none';
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op -= op * 0.1;
    }, 50);
}

function setVisible(selector, visible) {
    document.querySelector(selector).style.display = visible ? 'block' : 'none';
}
