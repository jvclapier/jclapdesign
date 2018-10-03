(function ($) {
  $(document).ready(function(){

    // hide .navbar first
    $(".navbar").hide();

    // fade in .navbar
    $(function () {
        $(window).scroll(function () {

            // set distance user needs to scroll before we start fadeIn
            if ($(this).scrollTop() > 400) {
                $('.navbar').fadeIn();
                console.log("reached 400 px scroll");
            } else {
                $('.navbar').fadeOut();
                console.log("back to the top scroll");
            }
        });
    });

});
  }(jQuery));
