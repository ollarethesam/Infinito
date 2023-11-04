$(document).ready(function(){
    $(document).on('click', '.arrows-btn', function(){
        url = $(this).parents('.container').siblings('.drag-header').children('.drag-name').text().split(' ').join("-").replace("à", "a").replace("ò", "o").replace("è", "e")
        direction = $(this).attr('id')
        start_value = $(this).parents('.container').find('.pk').val()
        field = $(this).parents('.container').find('.pk').attr('id').split("_").pop()
        $.ajax({
            url: url,
            type: 'GET',
            datatype: 'json',
            data: {
                direction: direction,
                start_value: start_value,
                field: field,
                offset: 0
            },
            success: function(response){
                $.each(response, function(key, value){
                    $('#id_{0}'.format(key)).val(value)
                })
            }
        })
    })
})