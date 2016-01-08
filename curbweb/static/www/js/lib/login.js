function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

	
$( "#main-contact-form" ).submit(function( event ) {

	event.preventDefault();
  var serial = $( this ).serializeArray();
  var mydata = {};
  $( serial ).each(function( index ,obj ) {
  	//console.log( index + ": " + obj.name );
	mydata[obj.name] = obj.value;
  });
  console.log(mydata);
          jQuery.ajax({
	    async: false,
            url: "http://www.theama.info/curbweb/rest-auth/login/",
	    data: mydata,
            beforeSend: function(xhr){xhr.setRequestHeader("X-CSRFToken", csrftoken);},
            type: "POST",
            success: function(data,status, xhr) {
				console.log(data);
				console.log(xhr.getResponseHeader('Set-Cookie'));
				document.cookie = "token = " + data.key;
				var date = new Date();
				date.setTime(date.getTime()+(60*60*1000));
				var expires = "; expires="+date.toGMTString()
				document.cookie ="token = "+data.key+expires+";";
				window.location.href='http://www.theama.info/cms.html'
            },
	    error : function(jqXHR, ajaxOptions, errorThrown) {
			//alert(jqXHR.status);
         		console.log(jqXHR.responseText);
			//window.location.href = "http://www.theama.info/login.html";
			//$( ".loginmsg" ).html( "<p>Please Check your credentials</em></p>" );
			$('.alert').css('visibility','visible');
	    },
	  });
        });
