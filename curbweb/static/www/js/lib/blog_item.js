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

function getParameterByName(name) {
	    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
	    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
		results = regex.exec(location.search);
	    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
    };
    var bitem = getParameterByName('item');
    jQuery.ajax({
            url: "http://www.theama.info/curbweb/api/api/announcements/"+bitem+"/?format=json",
            type: "GET",
            contentType: 'application/json; charset=utf-8',
            success: function(value) {

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
					var item =  '<div class="blog-item">' +
								'<a href="#"><img class="img-responsive img-blog" src="'+value.image+'" width="100%" alt=""/></a>'+
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
								'<h2><a href="blog-item.html?item='+value.url.split("/")[7]+'">' +value.summary+ '</a></h2>'+
								'<h3>'+value.body+'</h3>'+
								'</div>'+
								'</div>'+    
								'</div>';

					$( ".blog .col-md-12" ).html(item);

            },
            error : function(jqXHR, textStatus, errorThrown) {
            },

            timeout: 120000,
        });
		