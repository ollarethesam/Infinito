$(document).ready(function(){
  if($('.login-error').length){
    $('.login-error').addClass('popup')
  }
    $(document).on("click", ".login-error i", function(){
      let popup = $(this).parents('.login-error')
        popup.removeClass('popup')
        setTimeout(function() {
            popup.remove();
          }, 400);
    })
})