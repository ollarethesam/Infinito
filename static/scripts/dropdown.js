import { is_capitalized } from "./utils.js";

$(document).ready(function(){


    //dropdown fill


    $(document).on("click", ".dropdown", function(){
        $(".dropdown").not($(this)).children("span").removeClass("open")
        $(".dropdown").not($(this)).children(".dropdown-menu").removeClass("open")
        $(this).children("span").toggleClass("open")
        var dm = $(this).children(".dropdown-menu")
        dm.toggleClass("open")
        setTimeout(function() {
            if (!dm.hasClass('open')) {
                dm.empty();
            }
        }, 100);
        var url = $(this).parents('.drag-container').attr('id')
        var id = $(this).siblings(".form-control").attr("name")
        var model_name = $(this).siblings(".form-control").attr("class").split(' ')[1]
        $.ajax({
            url: url,
            type: 'GET',
            datatype: 'json',
            data: {
                id: id,
                model_name: model_name,
                offset: 0
            },
            success: function(response){
                dm.empty()
                dm.append(
                    `<li class="inline ">
                        <input type="text" class="dropdown-search-bar {0}-form" placeholder="Cerca">
                    </li>`.format(id)
                )
                $.each(response, function(i){
                    var li = '<li class="inline dropdown-menu-item item-{0}">'.format(i)
                    var cls_li ='</li>'
                    $.each(response[i], function(key, value){
                        li = li + "<div> {0} </div>".format(value)
                    })
                    li = li + cls_li
                    dm.append(li)
                })
                if(response.length == 0){
                    dm.append(
                        `<li class="inline dropdown-menu-item">
                            <div>
                                Nessun dato
                            </div>
                        </li>`);
                    }
            }
        })
        $(document).on("click", ".dropdown-menu .dropdown-search-bar", function(event) {
            event.stopPropagation()
        });
    })


    //searchbar


    $(document).on('keyup', '.dropdown-search-bar', function(){
        url = $(this).parents('.drag-container').attr('id')
        id = $(this).parents('.dropdown').siblings(".form-control").attr("name")
        chars = $(this).val()
        if(chars.length >= 0){
            $.ajax({
                url: url,
                type: 'GET',
                datatype: 'json',
                data: {
                    id: id,
                    chars: chars,
                    offset: 0
                },
                success: function(response){
                    var dm = $(".dropdown-menu")
                    $('.dropdown-menu-item').remove()
                    $.each(response, function(i){
                        var li = '<li class="inline dropdown-menu-item item-{0}">'.format(i)
                        var cls_li ='</li>'
                        $.each(response[i], function(key, value){
                            li = li + "<div> {0} </div>".format(value)
                        })
                        li = li + cls_li
                        dm.append(li)
                    })
                    if(response.length == 0){
                        dm.append(
                            `<li class="inline dropdown-menu-item">
                                <div>
                                    Nessun risultato
                                </div>
                            </li>`);
                        }
                }
            })
        }
    })

    var is_in = false
    $(document).on("mouseenter", ".dropdown",function(){
        is_in = true
    })
    $(document).on("mouseenter", ".dropdown-menu",function(){
        is_in = true
    })
    $(document).on("mouseleave", ".dropdown",function(){
        is_in = false
    })
    $(document).on("mouseleave", ".dropdown-menu",function(){
        is_in = false
    })
    $(document).on("click",function(){
        if(!is_in){
            $(".dropdown span").removeClass("open")
            $(".dropdown-menu").removeClass("open")
            setTimeout(function() {
                $(".dropdown-menu").empty();
            }, 100);
        }
    })
})

