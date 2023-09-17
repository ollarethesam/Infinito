$(document).ready(function(){
  if($('.login-error').length){
    $('.login-error').addClass('popup')
  }
    $(document).on("click", ".login-error i", function(){
        $('.login-error').removeClass('popup')
        setTimeout(function() {
            $('.login-error').remove();
          }, 400);
    })
})