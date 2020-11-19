var scroll = window.requestAnimationFrame ||
  function (callback) { window.setTimeout(callback, 1000 / 60) };

var bounceElements = document.querySelectorAll('.bounce-on-scroll');

function isElementInViewport(el) {
  var viewport_offset = 2.25; // 2 - jumatatea superioara a ecranului (inceput de div, nu centrat), 1 - tot ecranul
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

function loop() {
  bounceElements.forEach(function (element) {
    if (isElementInViewport(element)) {
      // Scale promo up
      if (!element.classList.contains("animation-scale-up")) {
        element.classList.add('animation-scale-up');
        element.classList.remove('animation-scale-down');
      }
    } else {
      // Scale promo back down
      if (element.classList.contains("animation-scale-up")) {
        element.classList.remove('animation-scale-up');
        element.classList.add('animation-scale-down');
      }
    }
  });

  scroll(loop);
}

loop()