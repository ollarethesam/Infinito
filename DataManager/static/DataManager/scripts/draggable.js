$(document).ready(function(){

    function handle_mousedown(e){
        if (!$(e.target).closest('.container').length) {
            window.my_dragging = {};
            my_dragging.pageX0 = e.pageX;
            my_dragging.pageY0 = e.pageY;
            my_dragging.elem = this;
            my_dragging.offset0 = $(this).offset();
            function handle_dragging(e){
                var left = my_dragging.offset0.left + (e.pageX - my_dragging.pageX0);
                var top = my_dragging.offset0.top + (e.pageY - my_dragging.pageY0);
                $(my_dragging.elem)
                .offset({top: top, left: left});
            }
            function handle_mouseup(e){
                $(document)
                .off('mousemove', handle_dragging)
                .off('mouseup', handle_mouseup);
            }
            $(document)
            .on('mouseup', handle_mouseup)
            .on('mousemove', handle_dragging);
        }
    }
    $(document).on("mousedown", '.content > .drag-container', handle_mousedown);
    
    $(document).on("click", ".draggable-opener, .inside-opener", function(){
        $('.drag-container').removeClass('focus')
        var url = $(this).text().split(" ").join("-").replace("à", "a").replace("ò", "o").replace("è", "e")
        var name = $(this).text()
        if(url == '+'){
            url = $(this).attr('class').split(' ').pop()
            name = url.split('-').join(' ')
        }
        console.log(url)
        
        var newDiv = `<div class="drag-container visible focus" id={0}>
                        <div class="drag-header">
                        <span class="drag-name">{1}</span>
                            <div class="drag-close">
                                <i class='bx bx-minus minimize'></i>
                                <i class='bx bx-x close'></i>
                            </div>
                        </div> 
                    </div>`.format(url, name)
        if(!$('.content').find('#{0}'.format(url)).length){
            $(".content").append(newDiv);
            $.ajax({
                type: "GET",
                url: url,
                success: function (data) {
                    $("#{0}".format(url)).append(data);
                },
                error: function () {
                    $("#{0}".format(url)).append("Failed to load content.");
                }
            });
        }
        // Use AJAX to fetch content from a Django view and insert it into the new <div>
        
    })
    $(document).on("click", ".close", function(){
        $(this).parents(".drag-container").remove()
    })
    $(document).on("click", ".content > .drag-container .minimize", function(){
        $(".minimized-container").append($(this).parents(".drag-container"))
        var dHeaderWidth = $(this).parents(".drag-header").width()
        $(this).parents(".drag-container").css({"width": dHeaderWidth})
    })
    $(document).on("click", ".minimized-container > .drag-container .minimize", function(){
        $(".content").append($(this).parents(".drag-container"))
        $(this).parents(".drag-container").css({"width": "fit-content"})
    })
})

$(document).on('mousedown', '.drag-container', function(){
    $(this).addClass('focus')
    $('.drag-container').not(this).removeClass('focus');
})
