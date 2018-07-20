$(document).ready(function() {
    // Check if element is scrolled into view

    $('.navbar-nav .nav-item').hover(
      function(){
        $(this).addClass('rubberBand');
      },
      function(){
        $(this).removeClass('rubberBand');
      }
    );


    function isScrolledIntoView(elem) {
      var docViewTop = $(window).scrollTop();
      var docViewBottom = docViewTop + $(window).height();
  
      var elemTop = $(elem).offset().top;
      var elemBottom = elemTop + $(elem).height();
  
      return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
    }
    // If element is scrolled into view, flip it in
    $(window).scroll(function() {
      $('.scroll-animations .animated').each(function() {
        if (isScrolledIntoView(this) === true) {
          $(this).addClass('flipInY');
        }
      });
      $('.scroll-animas .animated').each(function() {
        if (isScrolledIntoView(this) === true) {
          $(this).addClass('zoomIn');
        }
      });
      $('.scroll-anime .animated').each(function() {
        if (isScrolledIntoView(this) === true) {
          $(this).addClass('fadeInUp');
        }
      });
      $('.scrollinus .animated').each(function() {
        if (isScrolledIntoView(this) === true) {
          $(this).addClass('fadeInRight');
        }
      });
    });
  });



