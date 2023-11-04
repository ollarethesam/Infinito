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