var html = document.documentElement;
var body = document.body;

var scroller = {
    target: document.querySelector("#scroll-container"),
    ease: 0.05,
    endY: 0,
    y: 0,
    resizeRequest: 1,
    scrollRequest: 0,
};

var requestId = null;

// TweenLite.set(scroller.target, {
//     rotation: 0.01,
//     force3D: true
// });

window.addEventListener("load", onLoad);

function onLoad() {
    // updateScroller();
    window.focus();
    window.addEventListener("resize", onResize);
    document.addEventListener("scroll", onScroll);
}



function onScroll() {
    scroller.scrollRequest++;
    // if (!requestId) {
    //     requestId = requestAnimationFrame(updateScroller);
    // }
}

function onResize() {
    scroller.resizeRequest++;
    // if (!requestId) {
    //     requestId = requestAnimationFrame(updateScroller);
    // }
}


// side scroll


// jQuery(function () {
    jQuery( document ).ready(function() {
      jQuery('ul#navi li').on('click', function () {
        jQuery(this).parent().find('li.active').removeClass('active');
        jQuery(this).addClass('active');
    });  
    })
// });


// hamburgermenu

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    // document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.body.style.backgroundColor = "white";
}

document.addEventListener("click", function () {
    if (parseInt(jQuery('#mySidenav').css('width')) > 0) {
        document.getElementById("mySidenav").style.width = "0";
    }
});

function myFunction() {
    var dots = document.getElementById("dots");
    var moreText = document.getElementById("more");
    var btnText = document.getElementById("myBtn");

    if (dots.style.display === "none") {
        dots.style.display = "inline";
        btnText.innerHTML = "Read more";
        moreText.style.display = "none";
    } else {
        dots.style.display = "none";
        btnText.innerHTML = "Read less";
        moreText.style.display = "inline";
    }
}


