$(document).ready(function(){
    $("#showpw").on("change", function() {
      if ($(this).is(":checked")) {
        $("#password").attr("type", "text"); // Show the password
      } else {
        $("#password").attr("type", "password"); // Hide the password
      }
    });
})