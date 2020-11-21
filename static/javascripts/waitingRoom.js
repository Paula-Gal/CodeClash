var blobs = document.querySelectorAll('.blob');

window.onload = function () {
    findGame();
    setVisible('.page', false);
    $('.page').fadeIn(500);
}

onReady(function () {
    var pulse_speeds = ["animation-pulse-slow", "animation-pulse-medium", "animation-pulse-fast"];
    blobs.forEach(function (blob){
        var random_nr = Math.floor(Math.random()*1000);
        setTimeout(function(){
            random_0_2 = Math.floor(Math.random() * 2);
            blob.classList.add(pulse_speeds[random_0_2]);
        }, random_nr);
        console.log(random_nr);
    });
    setVisible('.page', true);
});

function onReady(callback) {
    var intervalId = window.setInterval(function () {
        if (document.getElementsByTagName('body')[0] !== undefined) {
            window.clearInterval(intervalId);
            callback.call(this);
        }
    }, 200);
}

function setVisible(selector, visible) {
    document.querySelector(selector).style.display = visible ? 'block' : 'none';
}