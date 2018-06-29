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
            $("#under #cart-me").html(data.html_book_list);
            $("#detail #tots").html(data.html_remove_me);
            $("#detail #sub").html(data.html_sub_me);
            $("#detail #coupo").html(data.html_coupo_me);
            $("#mobilee #mobile").html(data.html_mobile_me);
            var x = document.getElementById("snackbar");
            x.className = "show";
            setTimeout(function(){x.className = x.className.replace("show","");},3500);

          }
          else {
            alert("Try again!!");
          }
        }
      });
      return false;
    };

    var contactForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            alert('Your Request has been sent!!');
            $("#mecon #contact").html(data.html_contact_form);
            
          }
          else {
            $("#mecon #contact").html(data.html_contact_form);
          }
        }
      });
      return false;
    };

    var signupForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            alert('Successful SignUp!! Now you will be redirected to the home page...');
          }
          else {
            $("#log_me #skom").html(data.html_contact_form);
          }
        }
      }).done(function (data){
        if(data.url){
            
          window.location.href = data.url;
        }
      });
      return false;
    };

    var orderForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            alert("Good!");
            $("#order_me #js_order").html(data.html_order_form);
            
          }
          else {
            $("#order_me #js_order").html(data.html_order_form);
          }
        }
      }).done(function (data){
        if(data.url){
          window.location.href = data.url;
        }
      });
      return false;
    };

    var updateForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $("#under #cart-me").html(data.html_book_list);
            $("#detail #tots").html(data.html_remove_me);
            $("#detail #sub").html(data.html_sub_me);
            $("#detail #coupo").html(data.html_coupo_me);
            $("#mobilee #mobile").html(data.html_mobile_me);
            var x = document.getElementById("snackbar");
            x.className = "show";
            setTimeout(function(){x.className = x.className.replace("show","");},2500);

          }
          else {
            alert("Try again!!");
          }
        }
      });
      return false;
    };
  
    
    // Add to cart function and Contact form validation
    $(".js-book-create-form").on("submit",saveForm);
    $("#mecon").on("submit", ".js-contact-me",contactForm);
    $("#log_me").on("submit", ".js-user-cross",signupForm);
    $("#order_me").on("submit",".js-order-create",orderForm)
    $("#cartel").on("submit",".js-update-create-form",updateForm)
    
    //learn how to hook dom elements very well to avoid problems in code later

    
  });