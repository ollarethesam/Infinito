import { popup_handler } from "./utils.js";
$(document).ready(function(){ 
    $(document).on('click', '.delete-btn', function(){
        var url = $(this).parents('.drag-container').attr('id')
        var delcode = {}
        var pk_list = $(this).parents('.container').find('.pk')
        if (pk_list.length > 1){
            $.each(pk_list, function(index, item){
                delcode[$(item).attr('class').split(' ')[0]] = $(item).val()
            })
            delcode = JSON.stringify(delcode)
        }
        else{
            delcode = pk_list.val()
        }
        console.log(delcode)
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