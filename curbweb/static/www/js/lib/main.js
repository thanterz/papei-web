jQuery.ajax({
	url: "http://www.theama.info/curbweb/api/api/menu/?format=json",
	type: "GET",
	contentType: 'application/json; charset=utf-8',
	success: function(resultData) {
		//ταξινομηση κατγοριων με βάση το order
		  resultData.sort(function(a, b){
			  return a.order - b.order
			}
		  );
		$.each( resultData, function( key, value ) {
			$( ".navbar-nav" ).append( "<li><a href="+ value.uri +">" + value.title + "</a></li>" );        
		});

	},
	error : function(jqXHR, textStatus, errorThrown) {
	},

	timeout: 120000,
});