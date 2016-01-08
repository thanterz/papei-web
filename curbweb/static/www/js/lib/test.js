jQuery.ajax({
	url: "http://www.theama.info/curbweb/api/api/menu/?format=json",
	type: "GET",
	contentType: 'application/json; charset=utf-8',
	success: function(resultData) {
		$.each( resultData, function( key, value ) {
			if(key == 2)
				$( ".data" ).append( "<center>"+value.title+"</center>" );        
		});     

	},
	error : function(jqXHR, textStatus, errorThrown) {
	},

	timeout: 120000,
});