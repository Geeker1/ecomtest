$(function () {

  
    var saveForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            alert("HEY!!");
          }
          else {
            alert("Try again!!");
          }
        }
      });
      return false;
    };
  
  
    /* Binding */


    // Create item
    $(".js-contact-me").on("submit",saveForm);

  });