import { popup_handler } from "./utils.js";
$(document).ready(function() {
    $(document).on('submit', 'form', function(event) {
        event.preventDefault();
        var formData = new FormData(this);
        $(this).find(':checkbox').each(function() {
            formData.set($(this).attr('name'), this.checked);
        });
        var url = $(this).attr('action')
        if (!(url.startsWith('/Login'))){
            url = url.split('/').pop()
        }
        if ($('.content').css('background-size') == 'cover' && url.startsWith('/Login')) {
            formData.append('resize', true)
        }
        $.ajax({
            type: 'POST',
            url: url, 
            data: formData,
            contentType: false,
            processData: false,
            cache: false,
            success: function(response) {
                console.log(response)
                if(response['errors']){
                    popup_handler('errors', url, response)
                }
                else if(response['success']){
                    popup_handler('success', url, response)
                    $(document).find('#{0} .clean-btn'.format(url)).trigger('click')
                }
            },
            errors: function(errors) {
            }
        });
        formData = null
    });
});
