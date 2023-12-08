$(document).ready(function(){
    $(document).on('click clean', '.clean-btn', function(){
        $(this).parents('.container').find('.form-control').val('')
        $(this).parents('.container').find(".form-control").prop('checked', false)
    })
})