export function popup_handler(type, url, response){
    if($('#{0}'.format(url)).find('.popup').length){
        $('#{0}'.format(url)).find('.popup').remove()
    }
    var cont = '<ul class="{0}-container"> <i class="bx bx-x" ></i></ul>'.format(type)
    var size = 0
    $('#{0}'.format(url)).append(cont)
    $.each(response['{0}'.format(type)], function(key, value){
        $(document).find('#{0}'.format(url)).children('.{0}-container'.format(type)).append('<li class="{0}">{1}</<li>'.format(type, value))
        size++
    })
    var height = $('#{0}'.format(url)).find('.{0}-container'.format(type)).outerHeight(true)
    $('#{0}'.format(url)).find('.{0}-container'.format(type)).css('top', -(height) +'px')
    $('#{0}'.format(url)).find('.{0}-container'.format(type)).addClass('popup')
    $(document).on('click', '.{0}-container i'.format(type), function(){
        var cont = $(this).parents('.{0}-container'.format(type))
        cont.removeClass('popup')
        setTimeout(function() {
            cont.remove()
        }, 400)
    })
    var cont = $('#{0}'.format(url)).find('.popup')
    var disappear_time = 2000
    for (let i = 0; i < size; i++) {
        let increment = disappear_time / 5; // Calculate half of y
        disappear_time += increment; // Increment y by the calculated value
    }
    setTimeout(function() {
        cont.removeClass('popup')
        setTimeout(function() {
            cont.remove()
        }, 400)
    }, disappear_time)
}

export function filler(response, form, grid){
    console.log(response)
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
        if(key == 'grid' && grid){
            grid.find('.grid-row').remove()
            $.each(value, function(index, obj){
                var row = '<tr class="grid-row {0}"></tr>'.format(index)
                $(".grid").append(row)
                $.each(obj, function(grid_key, grid_value){
                    $('.grid-row.{0}'.format(index)).append('<td class="grid-item">{0}</td>'.format(grid_value))
                })
            })
        }
    })
}
export function is_capitalized(string){
    fl = string[0]
    return fl == fl.toUpperCase
}