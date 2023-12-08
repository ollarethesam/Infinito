import { popup_handler } from "./utils.js";
$(document).ready(function() {
    $(document).on('submit', 'form', function(event) {
        event.preventDefault();
        var formDataArray = $(this).serializeArray();
        $(this).find(':checkbox').each(function() {
            var index = formDataArray.findIndex(item => item.name === this.name);
            if (index !== -1) {
                formDataArray[index].value = this.checked ? 'on' : 'off';
            }
        });
        var formData = Array.from(formDataArray);
        var url = $(this).parents('.drag-container').attr('id')
        $.ajax({
            type: 'POST',
            url: url, 
            data: formData,
            success: function(response) {
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
