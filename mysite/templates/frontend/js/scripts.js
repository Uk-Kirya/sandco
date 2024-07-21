$(".phonee").mask("+7 (999) 999 - 99 - 99");

(function () {
    'use strict'
    var forms = document.querySelectorAll('.needs-validation')

    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }

                form.classList.add('was-validated')
            }, false)
        })
})()


$(document).ready(function () {
    var owl = $('.slider');
    owl.owlCarousel({
        margin: 0,
        nav: true,
        dots: false,
        autoHeight: true,
        loop: true,
        items: 1
    });
})

$(document).ready(function () {
    var owl = $('.about_slider');
    owl.owlCarousel({
        margin: 0,
        nav: true,
        dots: false,
        autoHeight: true,
        loop: true,
        items: 1
    });
})

$(document).ready(function () {
    var owl = $('.carousel_1');
    owl.owlCarousel({
        margin: 24,
        nav: true,
        dots: false,
        autoHeight: true,
        loop: true,
        responsive: {
            0: {
              items: 1
            },
            576: {
              items: 1
            },
            768: {
              items: 2
            },
            1200: {
              items: 3
            }
          }
    });
})

$(document).ready(function () {
    var owl = $('.carousel_2');
    owl.owlCarousel({
        margin: 24,
        nav: true,
        dots: false,
        autoHeight: true,
        loop: false,
        responsive: {
            0: {
              items: 1
            },
            576: {
              items: 1
            },
            768: {
              items: 2
            },
            1200: {
              items: 3
            }
          }
    });
})

$(document).ready(function () {
    var owl = $('.carousel_3');
    owl.owlCarousel({
        margin: 24,
        nav: true,
        dots: false,
        autoHeight: true,
        loop: true,
        responsive: {
            0: {
              items: 1
            },
            576: {
              items: 2
            },
            768: {
              items: 3
            },
            1200: {
              items: 4
            }
          }
    });
})

$(document).ready(function () {
    var owl = $('.years');
    owl.owlCarousel({
        margin: 0,
        nav: true,
        dots: false,
        autoHeight: true,
        loop: false,
        responsive: {
            0: {
              items: 1
            },
            576: {
              items: 2
            },
            768: {
              items: 3
            },
            1200: {
              items: 4
            }
          }
    });
})


$(document).ready(function () {
    $("a.topLink").click(function () {
        $("html, body").animate({
            scrollTop: $($(this).attr("href")).offset().top + "px"
        }, {
            duration: 0,
            easing: "swing"
        });
        return false;
    });
});


$(function () {
    $(window).scroll(function () {
        var top = $(document).scrollTop();
        if (top > 40) $('.head').addClass('head_fixed');
        else $('.head').removeClass('head_fixed');
    });
});


// Hide Header on on scroll down
var didScroll;
var lastScrollTop = 0;
var delta = 5;
var navbarHeight = $('header').outerHeight();

$(window).scroll(function(event) {
    didScroll = true;
});

setInterval(function() {
    if (didScroll) {
        hasScrolled();
        didScroll = false;
    }
}, 250);

function hasScrolled() {
    var st = $(this).scrollTop();

    if (Math.abs(lastScrollTop - st) <= delta)
        return;
    if (st > lastScrollTop && st > navbarHeight) {
        $('header').removeClass('nav-down').addClass('nav-up');
    } else {
        if (st + $(window).height() < $(document).height()) {
            $('header').removeClass('nav-up').addClass('nav-down');
        }
    }

    lastScrollTop = st;
}