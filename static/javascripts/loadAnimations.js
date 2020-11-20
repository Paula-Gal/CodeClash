var scroll = window.requestAnimationFrame ||
  function (callback) { window.setTimeout(callback, 1000 / 60) };

window.onscroll = function() {scrollEvent()};

var bounceElements = document.querySelectorAll('.bounce-on-scroll');
var floatElements = document.querySelectorAll('.float-on-scroll');
var promo = document.getElementById('promo');
var float_speeds = ['animation-float-slow', 'animation-float-medium', 'animation-float-fast'];

function isElementInViewport(el, viewport_offset = 1) {
  //viewport_offset ex 2 - jumatatea superioara a ecranului (inceput de div, nu centrat), 1 - tot ecranul
  if (typeof jQuery === "function" && el instanceof jQuery) {
    el = el[0];
  }
  var rect = el.getBoundingClientRect();
  return (
    (rect.top <= 0
      && rect.bottom >= 0)
    ||
    (rect.bottom >= (window.innerHeight || document.documentElement.clientHeight) / viewport_offset &&
      rect.top <= (window.innerHeight || document.documentElement.clientHeight) / viewport_offset)
    ||
    (rect.top >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) / viewport_offset)
  );
}

function scrollEvent(){
  if (document.body.scrollTop > 150 || document.documentElement.scrollTop > 150) {
    document.getElementById("promo").style.padding = "3rem";
    bounceElements.forEach(function (element) {
      if (isElementInViewport(element, 1.2)){
        element.classList.add('animation-scale-up');
        element.classList.remove('animation-scale-down');
      }
    }); 
    
  } else {
    bounceElements.forEach(function (element) {
      if (isElementInViewport(element, 1.2) && element.classList.contains('animation-scale-up')){
        element.classList.remove('animation-scale-up');
        element.classList.add('animation-scale-down');
        document.getElementById("promo").style.padding = "1rem";
      }
    }); 
  }
}


function loop() {

  floatElements.forEach(function (element) {
    if (isElementInViewport(element)) {
      if (!element.classList.contains("nu_mai_adauga_animation")) {
        // fa cumva sa nu se mai repete functia asta
        // si la un interval
        element.classList.add("nu_mai_adauga_animation");
        var timeout = Math.floor(Math.random() * 1500);
        var random_index = Math.floor(Math.random() * 3);
        setTimeout(function(){element.classList.add(float_speeds[random_index]);}, timeout);
      }
    }
    else {
      // dont float this bitch
      if (element.classList.contains("nu_mai_adauga_animation")){
        element.classList.remove('nu_mai_adauga_animation');
        float_speeds.forEach(function (speed){element.classList.remove(speed);});
      }
    }
  });

  scroll(loop);
}

loop()