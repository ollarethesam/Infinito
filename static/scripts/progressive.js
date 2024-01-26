$(document).ready(function(){
    $(document).on('click', '.clean-btn', function(){
        var form = $(this).closest('.drag-container')
        var url = form.attr('id')
        var numpro_request = true
        $.ajax({
            url: url,
            type: 'GET',
            datatype: 'json',
            data: {
                nr: numpro_request
            },
            success: function(response){
               form.find('.numpro').val(response['nr'])
            }
        })
    })
})