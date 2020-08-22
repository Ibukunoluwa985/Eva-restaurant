// navar color change on scroll
var navbar = document.getElementById('custom_navbar2');
window.onscroll = function () { 
    "use strict";
    if (document.body.scrollTop >= 200 || document.documentElement.scrollTop >= 200) {
        navbar.classList.add("nav-colored");
        navbar.classList.remove("nav-transparent");
    } 
    else {
        navbar.classList.add("nav-transparent");
        navbar.classList.remove("nav-colored");
    }
};

// hide after 2 sec
$(function() {
    setTimeout(function() { 
        $("#hideDiv").fadeOut(1500); 
    }, 2000)
  });