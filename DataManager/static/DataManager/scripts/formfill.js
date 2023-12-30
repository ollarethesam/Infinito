import { filler } from "./utils.js";
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
        if(grid.length != 0){
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
                filler(response, form, grid)
                if(dm){
                    dm.removeClass('open')
                    dm.siblings('span').removeClass('open')
                }
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
        var grid = form.find('.grid')
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
                    filler(response, form, grid)
                })
            }
        })
    })
})


//input form fill


$(document).on('input change', '.form-control', function(){
    var form = $(this).closest('.drag-container')
    var url = form.attr('id')
    var key = $(this).val()
    var key_id = $(this).attr("name")
    var grid = form.find('.grid')
    var wgrid = false
    if(grid.length != 0){
        wgrid = true
    }
    if($(this).siblings('.dropdown').length > 0){
        $.ajax({
            url: url,
            type: 'GET',
            datatype: 'json',
            data: {
                key: key,
                key_id: key_id,
                grid: wgrid,
                from_input: true
            },
            success: function(response){
                filler(response, form, grid)

            }
        })
    }
})