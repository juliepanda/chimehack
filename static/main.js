window.onload = function() {
  function validateEmail(email) {
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    return re.test(email);
  }
  function getEmail() {
    var emailBtn = document.getElementById('email-submit-btn');
    emailBtn.addEventListener('click', function() {
      var email = document.getElementById('email-field').value;
      if(validateEmail(email)) {
        console.log('this is a valid email address');
        /* now send valid email to backend */
        var jsonObj = { 'email': email };
        console.log(jsonObj);
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
  getEmail();
};
