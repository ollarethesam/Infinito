$(document).ready(function() {
    $("#colorPicker").on("input", function() {
        var selectedColor = $(this).val();
        var text_color = determineTextColor(selectedColor)
        $(".content").css("background-color", selectedColor);
        $(document).find('.container').css("background-color", selectedColor);
        $(document).find('.form-label, p, table *').css("color", text_color);
        $(document).find('.container').css("box-shadow", '0 12px 24px {0}4d, 0 6px 12px {1}26'.format(text_color, text_color));
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


  function determineTextColor(hexColor) {
    // Extract RGB values from hex color
    const r = parseInt(hexColor.slice(1, 3), 16);
    const g = parseInt(hexColor.slice(3, 5), 16);
    const b = parseInt(hexColor.slice(5, 7), 16);

    // Calculate luminance
    const luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255;

    // Set a threshold (0.5) for luminance, adjust as needed
    return luminance > 0.5 ? '#000000' : '#ffffff';
}