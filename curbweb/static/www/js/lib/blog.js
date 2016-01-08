var posts = [];
var limit = 2;
var curpage = 0;
var month = new Array();
month[0] = "January";
month[1] = "February";
month[2] = "March";
month[3] = "April";
month[4] = "May";
month[5] = "June";
month[6] = "July";
month[7] = "August";
month[8] = "September";
month[9] = "October";
month[10] = "November";
month[11] = "December";

$("#pagination").on("click",function(){
  alert('test');
});


jQuery.ajax({
            url: "http://www.theama.info/curbweb/api/api/announcements/?format=json",
            type: "GET",
            contentType: 'application/json; charset=utf-8',
            success: function(resultData) {
				resultData.sort(function(a, b){
					return new Date(b.created) - new Date(a.created)
				});
				console.log(resultData);
				posts = resultData;
				createPagination();
            },
            error : function(jqXHR, textStatus, errorThrown) {
            },

            timeout: 120000,
});

function createPagination(){
	var pages = Math.ceil(posts.length/limit);
	var paging = '<ul class="pagination pagination-lg">';//+
				 //'<li><a href="#"><i class="fa fa-long-arrow-left" onclick="loadposts(this)></i>Previous Page</a></li>';
	for(var i = 0 ; i < pages; i++){
		if(i === 0){
			paging = paging + '<li class="active"><a href="#" onclick="loadposts(this)">1</a></li>'
		}
		else{
			paging = paging + '<li><a href="#" onclick="loadposts(this)">'+(i+1)+'</a></li>'
		}
	}
    paging = paging+'</ul>';//'<li><a href="#">Next Page<i class="fa fa-long-arrow-right onclick="loadposts(this)"></i></a></li></ul>'
	
	$( ".blog .col-md-12" ).append(paging);
	loadposts(null);
	
}

function loadposts(me){
	
	var page	= (me === null) ? parseInt($("li.active")[0].textContent) : me.textContent,
		up		= limit*page,
		down	= up-limit,
		pagepost= posts.slice(down,up),
		bitem	= "";
		if(me!==null){
			$("li.active").removeClass('active');
			me.parentNode.className ='active'
		}
		curpage = page;
		
		$.each( pagepost, function( key, value ) {
			var date = new Date(value.created),
				year = date.getFullYear(),
				monthnum= date.getMonth(),
				day  = date.getDate(),
				hours= date.getHours(),
				minutes = date.getMinutes();
			if(parseInt(minutes) < 10)
					minutes = 0+minutes;
			if(parseInt(hours) < 10)
					hours = 0+minutes;	
			bitem += '<div class="blog-item">' +
				   '<div class="row">'+
								'<div class="col-xs-12 col-sm-2 text-center">'+
									'<div class="entry-meta">'+
										'<span id="publish_date">'+day+' '+month[monthnum] +'</span>'+
										'<span><i class="fa fa-user"></i> <a href="#">John Doe</a></span>'+
										'<span><i class="fa fa-comment"></i> <a href="blog-item.html">0 Comments</a></span>'+
										'<span><i class="fa fa-heart"></i><a href="#">56 Likes</a></span>'+
									'</div>'+
								'</div>'+
					'<div class="col-xs-12 col-sm-10 blog-content">'+
									'<a href="#"><img class="img-responsive img-blog" src="'+value.image+'" width="100%" alt=""/></a>'+
					'<h2><a href="blog-item.html?item='+value.url.split("/")[7]+'">' +value.summary+ '</a></h2>'+
									'<h3>'+value.body+'</h3>'+
									'<a class="btn btn-primary readmore" href="blog-item.html?item='+value.url.split("/")[7]+'">Read More <i class="fa fa-angle-right"></i></a>'+
								'</div>'+
							'</div>'+    
						'</div>';;
                            
			});
		$( ".posts" ).html('');	
		$( ".posts" ).html(bitem);
	
}
