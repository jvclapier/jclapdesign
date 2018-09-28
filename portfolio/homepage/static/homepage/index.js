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

  $( document ).ready(function() {

    // Open navbarSide when button is clicked
    $('#navbarSideButton').on('click', function() {
      $('#navbarSide').addClass('reveal');
      $('.overlay').show();
    });

    // Close navbarSide when the outside of menu is clicked
    $('.overlay').on('click', function(){
      $('#navbarSide').removeClass('reveal');
      $('.overlay').hide();
    });

  });
