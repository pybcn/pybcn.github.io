/*
 * Change Navbar color while scrolling
*/

$(window).on('scroll', function () {
      handleTopNavAnimation();
 });

$(window).on('load', function () {
      handleTopNavAnimation();
 });


function handleTopNavAnimation() {
    var top=$(window).scrollTop();

    if(top>10){
        $('#mainNav').addClass('navbar_small');
        $('.home_top_section').addClass('navbar_small');
    }
    else{
        $('#mainNav').removeClass('navbar_small');
        $('.home_top_section').removeClass('navbar_small');
    }
}



(function($) {

    $('a.nav-link.dropdown-toggle.open-submenu').click(function(e) {
        if ($(e.target).next( ".submenu" ).hasClass('hidden')) {
            $('.submenu').addClass('hidden');
            $(e.target).next( ".submenu" ).removeClass('hidden');
        }
        else {
            $(e.target).next( ".submenu" ).addClass('hidden');
        }
    });

})(jQuery); // End of use strict