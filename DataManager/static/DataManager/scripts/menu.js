$(document).ready(function(){
    var timeout
    $(document).on("mouseenter",".nav .nav-item",function(){
        $(this).siblings(".nav-item").find(".menu").removeClass("open")
        $(this).siblings(".nav-item").find(".sub-menu").removeClass("open")
        $(this).children(".menu").addClass("open")
        $(this).children(".nav-label").addClass("open")
    });
    $(document).on("mouseenter", ".nav",function(){
        clearTimeout(timeout)
    });
    $(document).on("mouseleave", ".nav",function(){
        timeout = setTimeout(() => {
            $(".open").removeClass("open")
        }, 1000);
    });
    $(document).on("mouseleave", ".nav-item",function(){
        $(this).children(".nav-label").removeClass("open")
    });
    $(document).on("mouseenter",".menu-item",function(){
        $(this).siblings(".menu-item").find(".sub-menu").removeClass("open")
        $(this).children(".sub-menu").addClass("open")
        $(this).children(".label").children("i").css({"transform":"rotate(360deg)"})
    });
    $(document).on("mouseleave",".menu-item",function(){
        $(this).children(".label").children("i").css({"transform":"rotate(270deg)"})
    });
});