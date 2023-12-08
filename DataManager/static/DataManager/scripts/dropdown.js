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
        
        $.ajax({
            url: url,
            type: 'GET',
            datatype: 'json',
            data: {
                id: id,
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
                            Nessun dato
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
                                Nessun risultato
                            </li>`);
                        }
                }
            })
        }
    })


    //formfill


    $(document).on('click', '.dropdown-menu-item', function(){
        $(this).parents(".dropdown").children("span").removeClass("open")
        $(this).parents(".dropdown-menu").removeClass("open")
        var form = $(this).closest('.drag-container')
        var dm = $(this).parents('.dropdown-menu')
        var url = form.attr('id')
        var key = $(this).children().first().text().trim()
        var key_id = $(this).parents('.dropdown').siblings(".form-control").attr("name")
        $.ajax({
            url: url,
            type: 'GET',
            datatype: 'json',
            data: {
                key: key,
                key_id: key_id
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
                dm.removeClass('open')
                dm.siblings('span').removeClass('open')
            }
        })
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

