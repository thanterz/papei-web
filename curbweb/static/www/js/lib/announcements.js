

jQuery.ajax({
	url: "http://www.theama.info/curbweb/api/api/announcements/?format=json",
	type: "GET",
	contentType: 'application/json; charset=utf-8',
	success: function(resultData) {
		
		
		resultData.sort(function(a, b){
			  return new Date(b.created) - new Date(a.created)
			}
		);
		resultData = resultData.slice(0, 3);
		$.each( resultData, function( key, value ) {
			
			var tpl	=	'<div class = "container">'+
						'<div class = "row">'+
						'<div class="well">'+
						'<div class="row">'+
						'<div class="col-md-2"><img src="'+value.image+'" alt="Smiley face" height="100" width="100"></div>'+
						'<div class="col-md-8">Posted on:' +createDate(new Date(value.created))+ '</div></br>'+
						'<div class="col-md-8"><strong>'+value.summary +'</strong></div></br>'+
						'<p class="lead">'+value.body.substr(0,200)+'...'+
						'<a class="btn btn-link readmore" href="blog-item.html?item='+value.url.split("/")[7]+'">Read More <i class="fa fa-angle-right"></i></a></p>'+
						'<div hidden id="titleNew">'+ value.summary +'</div>'+
						'<div hidden id="textNews">'+ value.body+'</div>'+
						'<div hidden id="urlNews">'+ value.url+'</div>'+
						'<div hidden id="imageNews">'+ value.image+'</div>'+
						'</div>'+
						'</div>'+
						'</div>'+
						'</div>'+
						'</div>'
		$( ".data" ).append(tpl);
				
		});     

	},
	error : function(jqXHR, textStatus, errorThrown) {
	},

	timeout: 120000,
});


function createDate(date){
	var year = date.getFullYear(),
		month= date.getMonth(),
		day  = date.getDate(),
		hours= date.getHours(),
		minutes = date.getMinutes();
	if(parseInt(minutes) < 10)
			minutes = 0+minutes;
	if(parseInt(hours) < 10)
			hours = 0+minutes;	
	return day+'/'+month+'/'+year+' '+hours+':'+minutes;
	
}


