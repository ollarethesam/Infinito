import { popup_handler } from "./utils.js";
$(document).ready(function() {
    $(document).on('submit', 'form', function(event) {
        event.preventDefault(); // Prevent the default form submission behavior
        // Collect form data
        var formData = $(this).serialize();
        url = $(this).siblings('.drag-header').children('.drag-name').text().split(' ').join("-").replace("à", "a").replace("ò", "o").replace("è", "e")
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
    });
});
