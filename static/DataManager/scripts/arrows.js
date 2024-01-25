import { filler } from "./utils.js";
$(document).ready(function(){
    $(document).on('click', '.arrows-btn', function(){
        var form = $(this).closest('.drag-container')
        var url = form.attr('id')
        var direction = $(this).attr('class').split(' ').pop()
        var start_value = form.find('.pk').val()
        var field = form.find('.pk').attr('class').split(' ')[0]
        var grid = form.find('.grid')
        var wgrid = false
        if(grid){
            wgrid = true
        }
        $.ajax({
            url: url,
            type: 'GET',
            datatype: 'json',
            data: {
                direction: direction,
                start_value: start_value,
                field: field,
                offset: 0,
                grid: wgrid
            },
            success: function(response){
                filler(response, form, grid)
                form.find('.form-control').each(function () {
                    var lc = $(this).attr('class').split(' ')[0]
                    if (!(lc in response)){
                        form.find('.{0}'.format(lc)).val('')
                        form.find('.{0}'.format(lc)).prop('checked', false)
                    }
                })
            }
        })
    })
})