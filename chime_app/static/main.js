window.onload = function() {
  function validateEmail(email) {
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    return re.test(email);
  }
  function validatePhoneNumber(number) {
    var re = /^\d+$/;
    return re.test(number);
  }
  function activateEmailField() {
    var emailBtn = document.getElementById('email-submit-btn');
    emailBtn.addEventListener('click', function() {
      var email = document.getElementById('email-field').value;
      if(validateEmail(email)) {
        console.log('this is a valid email address');
        /* now send valid email to backend */
        var jsonObj = { 'email': email };
        var post = $.post('/sendmail', jsonObj)
        .done( function(data) {
          console.log(JSON.stringify(data));
        })
        .fail( function(err) {
          console.log(err);
        });
      } else {
        console.log('not a valid email address');
      }
    }, false);
  }
  function activateTextField() {
    var textBtn = document.getElementById('sms-submit-btn');
    textBtn.addEventListener('click', function () {
      var n1 = document.getElementById('sms-field-1').value;
      var n2 = document.getElementById('sms-field-2').value;
      var n3 = document.getElementById('sms-field-3').value;
      var number = '1' + n1 + n2 + n3;
      if(validatePhoneNumber(number)) {
        /* send valid number to backend */
        console.log('valid phone number');
        var jsonObj = { 'number': number };
        var post = $.post('/sendtext', jsonObj)
        .done( function(data) {
          console.log(JSON.stringify(data));
        })
        .fail( function(err) {
          console.log(err);
        });
      } else {
        console.log('not a valid phone number');
      }
    });
  }
  activateEmailField();
  activateTextField();
};
