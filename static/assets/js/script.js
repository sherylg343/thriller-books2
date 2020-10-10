$(document).ready(function(){
    $(".dropdown-trigger").dropdown();
    $('.sidenav').sidenav();
    $('body').scrollspy({ target: '#nav-parent' })
    $('#rateMe2').mdbRate();
  });

  $('select').formSelect();

  //code from https://jsfiddle.net/8cn2mekf/8/ for star rating
  $('.controls.rating')
    .addClass('starRating') //in case js is turned off, it fals back to standard radio button
    .on('mouseenter', 'label', function(){
            DisplayRating($(this)); // when we hover into a label, show the ratings
        }
    )
    .on('mouseleave', function() {
        // when we leave the rating div, figure out which one is selected and show the correct rating level
        var $this = $(this),
            $selectedRating = $this.find('input:checked');
        if ($selectedRating.length == 1) {
            DisplayRating($selectedRating); // a rating has been selected, show the stars
        } else {
            $this.find('label').removeClass('on'); // nothing clicked, remove the stars
        };
    }
);

var DisplayRating = function($el){
    // for the passed in element, add the 'on' class to this and all prev labels
    // and remove the 'on' class from all next labels. This stops the flicker of removing then adding back
    $el.addClass('on');
    $el.parent('label').addClass('on');
    $el.closest('td').prevAll().find('label').addClass('on');
    $el.closest('td').nextAll().find('label').removeClass('on');
};