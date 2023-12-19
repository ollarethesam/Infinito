$(document).ready(function() {
    $("#colorPicker").on("input", function() {
      var selectedColor = $(this).val();
      console.log(selectedColor)
      $("body").css("background-color", selectedColor);
    });
  });