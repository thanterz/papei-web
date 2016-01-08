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
  //console.log( $( this ).serializeArray() );
  event.preventDefault();
  var serial = $( this ).serializeArray();
  var mydata = {};
  $( serial ).each(function( index ,obj ) {
  	//console.log( index + ": " + obj.name );
	mydata[obj.name] = obj.value;
  });
  console.log(mydata);
  jQuery.ajax({
	url: "http://www.theama.info/curbweb/api/api/sentmail/",
	type: "POST",
	contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(mydata),
        headers: {
        	"Authorization": "Basic " + window.btoa("thanterz:papei"),
        },
	 beforeSend: function(xhr, settings) {
		xhr.setRequestHeader("X-CSRFToken", csrftoken);
	},
	success: function(resultData) {
		//console.log(resultData); 
		//$( ".message" ).html( "<p>Message sent successfully</em></p>" );
		if($('.alert-danger').css('visibility') == 'visible'){
			$('.alert-danger').css('visibility','hidden');
		}
		$('.alert-success').css('visibility','visible');
	},
	error : function(jqXHR, textStatus, errorThrown) {
		 if($('.alert-success').css('visibility') == 'visible'){ 
                        $('.alert-success').css('visibility','hidden');
                }
		$('.alert-danger').css('visibility','visible');
	},

	timeout: 120000,
});
});

