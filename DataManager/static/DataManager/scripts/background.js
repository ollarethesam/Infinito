$(document).ready(function() {
    $("#colorPicker").on("input", function() {
        var selectedColor = $(this).val();
        $(".content").css("background-color", selectedColor);
    });
    $('.image-picker-button').on('click', function(){
      $("#imagePicker").attr('type', 'file');
    })
    $("#imagePicker").on("change", function(e) {
        var file = e.target.files[0];
        var reader = new FileReader();
        reader.onload = function(e) {
        var imageUrl = e.target.result;
        $(".content").css("background-image", "url(" + imageUrl + ")");
      };
      reader.readAsDataURL(file);
    });
    $("#removeImageBtn").on("click", function() {
        $(".content").css("background-image", "none");
        $("#imagePicker").attr('type', 'text');
        $("#imagePicker").val('1');

    });
    $('#sizeToggle').on('click', function(){
      console.log($('.content').css('background-size'))
        if ($('.content').css('background-size') == 'cover'){
            $('.content').css('background-size', 'contain')
        }
        else if ($('.content').css('background-size') == 'contain'){
          $('.content').css('background-size', 'cover')
      }
    })
  });