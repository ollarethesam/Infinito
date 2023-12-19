    
$(document).ready(function(){


    //formfill


    $(document).on('click', '.dropdown-menu-item', function(){
        $(this).parents(".dropdown").children("span").removeClass("open")
        $(this).parents(".dropdown-menu").removeClass("open")
        var form = $(this).closest('.drag-container')
        var dm = $(this).parents('.dropdown-menu')
        var url = form.attr('id')
        var key = $(this).children().first().text().trim()
        var key_id = $(this).parents('.dropdown').siblings(".form-control").attr("name")
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
                key: key,
                key_id: key_id,
                grid: wgrid
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
                    if(key == 'grid' && grid){
                        grid.find('.grid-row').remove()
                        $.each(value, function(index, obj){
                            row = '<tr class="grid-row {0}"></tr>'.format(index)
                            $(".grid").append(row)
                            $.each(obj, function(grid_key, grid_value){
                                $('.grid-row.{0}'.format(index)).append('<td class="grid-item">{0}</td>'.format(grid_value))
                            })
                        })
                    }
                })
                dm.removeClass('open')
                dm.siblings('span').removeClass('open')
            }
        })
    })


    //grid-form-fill


    $(document).on('click', '.grid-row', function(){
        var form = $(this).closest('.drag-container')
        var url = form.attr('id')
        var grid_pk_value = $(this).children().first().text().trim()
        var grid_pk_name = 'codart'
        var main_val = form.find('.main').val()
        $.ajax({
            url: url,
            type: 'GET',
            datatype: 'json',
            data: {
                grid_pk_value: grid_pk_value,
                grid_pk_name: grid_pk_name,
                main_val: main_val
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