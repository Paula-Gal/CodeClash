window.onload = function () {
    $('.btn-dashboard').addClass('scale-up-center');
    $('#loading').fadeIn(350);
}

onReady(function () {
    var page = $('.page');
    var loading = $('#loading');
    loading.fadeOut(350);
    setTimeout(function(){page.fadeIn(1000-350);}, 350);
    setTimeout(function(){
        setVisible('.page', true);
        setVisible('#loading', false);
    }, 500);
});

function onReady(callback) {
    var intervalId = window.setInterval(function () {
        if (document.getElementsByTagName('body')[0] !== undefined) {
            window.clearInterval(intervalId);
            callback.call(this);
        }
    }, 1000);
}


function setVisible(selector, visible) {
    document.querySelector(selector).style.display = visible ? 'block' : 'none';
}
