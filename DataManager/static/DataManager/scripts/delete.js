import { popup_handler } from "./utils.js";
$(document).ready(function(){ 
    $(document).on('click', '.delete-btn', function(){
        var url = $(this).parents('.container').siblings('.drag-header').children('.drag-name').text().split(' ').join("-").replace("à", "a").replace("ò", "o").replace("è", "e")
        console.log($(this).parents('.container').find('.pk').val())
        var delcode = $(this).parents('.container').find('.pk').val()
        if(delcode){
            if(confirm('vuoi eliminare il record {0}?'.format(delcode))){
                $.ajax({
                    url: url,
                    type: 'GET',
                    datatype: 'json',
                    data: {
                        delcode: delcode,
                    },
                    success: function(response) {
                        if(response['errors']){
                            popup_handler('errors', url, response)
                        }
                        else if(response['success']){
                            popup_handler('success', url, response)
                            $(document).find('#{0} .clean-btn'.format(url)).trigger('click')
                        }
                    }
                })
            }
        }
    })
})