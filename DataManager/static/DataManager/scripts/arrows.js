$(document).ready(function(){
    $(document).on('click', '.arrows-btn', function(){
        var form = $(this).closest('.drag-container')
        var url = form.attr('id')
        var direction = $(this).attr('class').split(' ').pop()
        var start_value = form.find('.pk').val()
        var field = form.find('.pk').attr('class').split(' ')[0]
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
                    var input = form.find(".{0}".format(key))
                    if(input.is('input[type="checkbox"]')){
                        if (value == true){
                            input.prop('checked', true)
                        }
                        else{
                            input.prop('checked', false)
                        }
                    }
                    else{
                        input.val(value)
                    }
                })
            }
        })
    })
})