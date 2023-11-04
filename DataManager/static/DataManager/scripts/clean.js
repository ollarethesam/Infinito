$(document).ready(function(){
    $(document).on('click clean', '.clean-btn', function(){
        $(this).parents('.container').find('.form-control').val('')
    })
})