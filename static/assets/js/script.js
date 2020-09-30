$(document).ready(function(){
    $(".dropdown-trigger").dropdown();
    $('.sidenav').sidenav();
    $('body').scrollspy({ target: '#nav-parent' })
     $('select').formSelect();
  });