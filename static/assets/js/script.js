$(document).ready(function(){
    $(".dropdown-trigger").dropdown();
    $('.sidenav').sidenav();
    $('body').scrollspy({ target: '#nav-parent' })
    $('#rateMe2').mdbRate();
  });

  $('select').formSelect();

  /**code from https://jsfiddle.net/8cn2mekf/8/ for star rating*/
  $('.controls.rating')
    .addClass('starRating') 
    .on('mouseenter', 'label', function() {
            DisplayRating($(this));
        }
    )
    .on('mouseleave', function() {
/** when we leave the rating div, figure out which one is selected and show the correct rating level */
        var $this = $(this),
            $selectedRating = $this.find('input:checked');
        if ($selectedRating.length == 1) {
            DisplayRating($selectedRating); 
        } else {
            $this.find('label').removeClass('on'); 
        };
    }
);

var DisplayRating = function($el){
/**for the passed in element, add the 'on' class to this and all prev labels
and remove the 'on' class from all next labels. This stops the flicker of removing then adding back */
    $el.addClass('on');
    $el.parent('label').addClass('on');
    $el.closest('td').prevAll().find('label').addClass('on');
    $el.closest('td').nextAll().find('label').removeClass('on');
};

/** from mentor Brian Macharia, allow user cancel or confirm delete of
book review before deleting */
/**function confirmDelete(reviewID) {
    deleteUrl = '/delete_review' + reviewID
    let deleteConfirmed = confirm('Are you certain you want to delete this review?')
    if (deleteConfirmed) {
        location.href = deleteURL
    }
}*/