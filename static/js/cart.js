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
            $('#boom').addClass('animated bounceOutLeft');
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
            $("#mecon #contact").html(data.html_contact_form);
            var x = document.getElementById("snackbar");
            x.className = "show";
            setTimeout(function(){x.className = x.className.replace("show","");},5500);
            
          }
          else {
            $("#mecon #contact").html(data.html_contact_form);
            var x = document.getElementById("errore");
            x.className = "show";
            setTimeout(function(){x.className = x.className.replace("show","");},3000);
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
            var x = document.getElementById("snackbar");
            x.className = "show";
            setTimeout(function(){x.className = x.className.replace("show","");},5500);
          }
          else {
            $("#log_me #skom").html(data.html_contact_form);
            var x = document.getElementById("errore");
            x.className = "show";
            setTimeout(function(){x.className = x.className.replace("show","");},3000);
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
            $("#order_me #js_order").html(data.html_order_form);
            var x = document.getElementById("snackbar");
            x.className = "show";
            setTimeout(function(){x.className = x.className.replace("show","");},5500);
            
            
          }
          else {
            $("#order_me #js_order").html(data.html_order_form);
            var x = document.getElementById("errore");
            x.className = "show";
            setTimeout(function(){x.className = x.className.replace("show","");},5500);
            
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
            setTimeout(function(){x.className = x.className.replace("show","");},5500);

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