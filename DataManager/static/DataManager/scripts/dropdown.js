$(document).ready(function(){
    var is_in = false
    //dropdown fill
    $(document).on("click", ".dropdown", function(){
        $(".dropdown").not($(this)).children("span").removeClass("open")
        $(".dropdown").not($(this)).children(".dropdown-menu").removeClass("open")
        $(this).children("span").toggleClass("open")
        $(this).children(".dropdown-menu").toggleClass("open")

        url = $(this).parents('.container').siblings('.drag-header').children('.drag-name').text().split(' ').join("-").replace("à", "a").replace("ò", "o").replace("è", "e")
        id = $(this).siblings(".form-control").attr("name")
        $.ajax({
            url: url,
            type: 'GET',
            datatype: 'json',
            data: {
                id: id,
                offset: 0
            },
            success: function(response){
                var dm = $(".dropdown-menu")
                dm.empty()
                dm.append(
                    `<li class="inline ">
                        <input type="text" class="dropdown-search-bar {0}-form" placeholder="Cerca">
                    </li>`.format(id)
                )
                $.each(response, function(i){
                    var li = '<li class="inline dropdown-menu-item">'
                    var cls_li ='</li>'
                    $.each(response[i], function(key, value){
                        li = li + "<div> {0} </div>".format(value)
                    })
                    li = li + cls_li
                    dm.append(li)
                })
            }
        })
        $(document).on("click", ".dropdown-menu", function(event) {
            event.stopPropagation()
        });
    })
    //searchbar
    $(document).on('keyup', '.dropdown-search-bar', function(){
        url = $(this).parents('.container').siblings('.drag-header').children('.drag-name').text().split(' ').join("-").replace("à", "a").replace("ò", "o").replace("è", "e")
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
                        var li = '<li class="inline dropdown-menu-item">'
                        var cls_li ='</li>'
                        $.each(response[i], function(key, value){
                            li = li + "<div> {0} </div>".format(value)
                        })
                        li = li + cls_li
                        dm.append(li)
                    })
                }
            })
        }
    })
    //formfill
    $(document).on('click', '.dropdown-menu-item', function(){
        $(this).parents(".dropdown").children("span").removeClass("open")
        $(this).parents(".dropdown-menu").removeClass("open")
        url = $(this).parents('.container').siblings('.drag-header').children('.drag-name').text().split(' ').join("-").replace("à", "a").replace("ò", "o").replace("è", "e")
        key = $(this).children().first().text().trim()
        $.ajax({
            url: url,
            type: 'GET',
            datatype: 'json',
            data: {
                key: key,
                offset: 0
            },
            success: function(response){
                $.each(response, function(key, value){
                    $('#id_{0}'.format(key)).val(value)
                })
            }
        })
    })


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
        }
    })
})