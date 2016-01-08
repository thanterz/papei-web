var totalnews = [];
var limit = 2;
var curpage = 0;

$(function(me) {
	var token = getCookie('token');
	$('.maincms').css('display', 'none');
	if(token!=null){
		$( "#usermsg" ).append('<a href ="" onclick="Javascript:logout(this)">Logout</a>');
		getCategories();
		getNews();
		$('.maincms').css('display', 'inline');
	}
	else{
		window.location.href='login.html'
	}
});


$("#myModal").on('hidden.bs.modal', function () {
    $( "#editmodal" ).remove();
});

function logout(){
  document.cookie = 'token=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
  window.location.href='login.html'
}

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

function getCategories(){
	jQuery.ajax({
		url: "http://www.theama.info/curbweb/api/api/menu/?format=json",
		type: "GET",
		contentType: 'application/json; charset=utf-8',
		beforeSend: function(xhr, settings) {
            			xhr.setRequestHeader("X-CSRFToken", csrftoken);
    		},
		success: function(resultData) {
			//ταξινομηση κατγοριων με βάση το order
			  resultData.sort(function(a, b){
				  return a.order - b.order
				}
			  );
			  addTable(resultData);

		},
		error : function(jqXHR, textStatus, errorThrown) {
		},

		timeout: 120000,
	});
}


function editCategory(me){
	var order = parseInt(me.parentNode.parentNode.cells[0].innerHTML),
		title = me.parentNode.parentNode.cells[1].innerHTML,
		content = me.parentNode.parentNode.cells[2].innerHTML,
		uri   = me.parentNode.parentNode.cells[3].innerHTML,
		url   = me.parentNode.parentNode.cells[4].innerHTML;
		
	var dialog  = '<div class="modal-dialog" id="editmodal">'+
						'<div class="modal-content">'+
							'<div class="modal-header">'+
								'<button type="button" class="close" data-dismiss="modal">&times;</button>'+
								'<h4 class="modal-title">Modal Header</h4>'+
							'</div>'+
							'<div class="modal-body">'+
								'<form id="form">'+
									'<div class="form-group">'+
										'<label for="title">Title</label>'+
										'<input type="text" class="form-control" id="titleEdit" placeholder="title" value="'+title+'">'+
									'</div>'+
									'<div class="form-group">'+
										'<label for="order">Order</label>'+
										'<input type="number" class="form-control" id="orderEdit" placeholder="order" value="'+order+'">'+
									'</div>'+
									'<div class="form-group">'+
										'<label for="order">Content</label>'+
										'<textarea class="form-control" rows="5" id="contentEdit" placeholder="content" value="'+content+'"></textarea>'+
										'<script>'+
											'CKEDITOR.replace( \'contentEdit\' );'+
										'</script>'+
									'</div>'+
									'<div class="form-group">'+
										'<label for="uri">uri</label>'+
										'<input type="text" class="form-control" id="uriEdit" placeholder="uri" value="'+uri+'">'+
									'</div>'+
									'<div class="form-group">'+
										'<label for="url">url</label>'+
										'<input type="text" class="form-control" id="urlEdit" placeholder="url" value="'+url+'" disabled>'+
									'</div>'+
									'<div class="modal-footer">'+
										'<button type="button" class="btn btn-primary" data-dismiss="modal">Close</button>'+
										'<button type="button" class="btn btn-primary" onClick="Javascript:updateCategory(this)">Προσθήκη</button>'+
									'</div>'+
								'</form>'+
							'</div>'+
						'</div>'+
					'</div>';
			
	$( "#myModal" ).append(dialog);
	CKEDITOR.instances.contentEdit.setData( content, function(){
			this.checkDirty();  // true
	});	
}

function updateCategory(){
	var category 	= {
		title 		: $('#titleEdit')[0].value,
		content 	: CKEDITOR.instances.contentEdit.getData(),
		order 		: parseInt($('#orderEdit')[0].value),
		uri 		: $('#uriEdit')[0].value
	}
	jQuery.ajax({
		url: $('#urlEdit')[0].value,
		type: "PUT",
		data: JSON.stringify(category),
		contentType: 'application/json; charset=utf-8',
		headers: {
        		"Authorization": "Basic " + window.btoa("thanterz:papei"),
    		},
		beforeSend: function(xhr, settings) {
        		//if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            			xhr.setRequestHeader("X-CSRFToken", csrftoken);
        		//}
    		},
		success: function() {
			location.reload();
			console.log('success')

		},
		error : function(jqXHR, ajaxOptions, errorThrown) {
			//alert(jqXHR.status);
			//alert(jqXHR.responseText);
		},

		timeout: 120000,
	});
}

function askDelete(me){

	var item = me,
		url;
		if($("li.active")[0].textContent == 'News'){
			url = item.parentNode.parentNode.childNodes[4].innerHTML;
		}
		else{
			url = item.parentNode.parentNode.cells[4].innerHTML;
		}	
	var dialog  = '<div class="modal-dialog" id="editmodal">'+
						'<div class="modal-content">'+
							'<div class="modal-header">'+
								'<button type="button" class="close" data-dismiss="modal">&times;</button>'+
								'<h4 class="modal-title">Modal Header</h4>'+
							'</div>'+
							'<div class="modal-body">'+
								'<p>Do you want to delete this record?</p>'+
								'<div class="modal-footer">'+
									'<button type="button" class="btn btn-primary" data-dismiss="modal">Cancel</button>'+
									'<button type="button" class="btn btn-primary" onClick="Javascript:deleteCategory(\''+url+'\')">Delete</button>'+
								'</div>'+
							'</div>'+
						'</div>'+
					'</div>';
					
	$( "#myModal" ).append(dialog);
}

function deleteCategory(url){
	
	var url = url;
	jQuery.ajax({
		url: url,
		type: "DELETE",
		contentType: 'application/json; charset=utf-8',
		headers: {
        		"Authorization": "Basic " + window.btoa("thanterz:papei"),
    		},
		beforeSend: function(xhr, settings) {
        		//if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            			xhr.setRequestHeader("X-CSRFToken", csrftoken);
        		//}
    		},
		success: function() {
			location.reload();
			console.log('success')

		},
		error : function(jqXHR, ajaxOptions, errorThrown) {
			//alert(jqXHR.status);
			//alert(jqXHR.responseText);
		},

		timeout: 120000,
	});
}

function addCategory(me){
	var category 	= {
		title 		: $('#title')[0].value,
		content 	: CKEDITOR.instances.content.getData(),
		order 		: $('#order')[0].value,
		uri 		: $('#uri')[0].value,
	}
	jQuery.ajax({
		url: "http://www.theama.info/curbweb/api/api/menu/?format=json",
		type: "POST",
		data: JSON.stringify(category),
		contentType: 'application/json; charset=utf-8',
		headers: {
        		"Authorization": "Basic " + window.btoa("thanterz:papei"),
    		},
		beforeSend: function(xhr, settings) {
        		//if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            			xhr.setRequestHeader("X-CSRFToken", csrftoken);
        		//}
    		},
		success: function() {
			location.reload();
			console.log('success')

		},
		error : function(jqXHR, ajaxOptions, errorThrown) {
			//alert(jqXHR.status);
         	//	alert(jqXHR.responseText);
		},

		timeout: 120000,
	});
}

var entityMap = {
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': '&quot;',
    "'": '&#39;',
    "/": '&#x2F;'
  };

function escapeHtml(string) {
	var entityMap = {
		"&": "&amp;",
		"<": "&lt;",
		">": "&gt;",
		'"': '&quot;',
		"'": '&#39;',
		"/": '&#x2F;'
	};
	return String(string).replace(/[&<>"'\/]/g, function (s) {
		return entityMap[s];
	});
}

function addTable(result) {
      
    var table = document.getElementById("myTableData");
     
    for (var i=0; i<result.length; i++){
       addRow(table , result[i], i);
    }
	$('td:nth-child(3),th:nth-child(3)').hide(); 
	$('td:nth-child(5),th:nth-child(5)').hide(); 
    
}

function addRow(table, item, order) {
 
    var row = table.insertRow(order+1);
    row.insertCell(0).innerHTML= item.order;
    row.insertCell(1).innerHTML= item.title;
	row.insertCell(2).innerHTML= escapeHtml(item.content);
	row.insertCell(3).innerHTML= item.uri;
	row.insertCell(4).innerHTML= item.url;
    row.insertCell(5).innerHTML='<input type="button" value = "Delete"  class="btn btn-danger" data-toggle="modal" data-target="#myModal" onClick="Javascript:askDelete(this)"> '+
							     '<input type="button" value = "Edit"  class="btn btn-danger" data-toggle="modal" data-target="#myModal" onClick="Javascript:editCategory(this)">';
	
}

function getNews(){
	jQuery.ajax({
		url: "http://www.theama.info/curbweb/api/api/announcements/?format=json",
		type: "GET",
		contentType: 'application/json; charset=utf-8',
		success: function(resultData) {
			resultData.sort(function(a, b){
				return new Date(b.created) - new Date(a.created)
			});
			totalnews = resultData;
			createPagination();
		},
		error : function(jqXHR, textStatus, errorThrown) {
		},

		timeout: 120000,
	});
}

function addTplNews(me){
	var page	= (me === null) ? 1 : me.textContent,
		up		= limit*page,
		down	= up-limit,
		news= totalnews.slice(down,up),
		tpl	= "";
		if(me!==null){
			$("li.active").removeClass('active');
			me.parentNode.className ='active'
		}
		curpage = page;
	
		$( "#news" ).html('');
	for(var i = 0; i < news.length; i++){
		tpl	=	'<div class="well">'+
					'<div class="row">'+
						'<div class="col-sm-2"><img src="'+news[i].image+'" alt="Smiley face" height="70" width="70"></div>'+
						'<div class="col-sm-8">'+ news[i].summary +'</br>'+news[i].body.substr(0,200)+'...'+'</div>'+
						'<div hidden id="titleNew">'+ news[i].summary +'</div>'+
						'<div hidden id="textNews">'+ news[i].body+'</div>'+
						'<div hidden id="urlNews">'+ news[i].url+'</div>'+
						'<div hidden id="imageNews">'+ news[i].image+'</div>'+
						'<div class="col-sm-2"><input type="button" value = "Delete"  class="btn btn-danger" data-toggle="modal" data-target="#myModal" onClick="Javascript:askDelete(this)">  '+
											   '<input type="button" value = "Edit"  class="btn btn-danger" data-toggle="modal" data-target="#myModal" onClick="Javascript:editNews(this)">'+
					   '</div>'+
					'</div>'+
				'</div>'		
		$( "#news" ).append(tpl);
	}
}

function createPagination(){
	var pages = Math.ceil(totalnews.length/limit);
	var paging = '<ul class="pagination pagination-lg">';//+
				 //'<li><a href="#"><i class="fa fa-long-arrow-left" onclick="loadposts(this)></i>Previous Page</a></li>';
	for(var i = 0 ; i < pages; i++){
		if(i === 0){
			paging = paging + '<li class="active"><a href="#" onclick="addTplNews(this)">1</a></li>'
		}
		else{
			paging = paging + '<li><a href="#" onclick="addTplNews(this)">'+(i+1)+'</a></li>'
		}
	}
    paging = paging+'</ul>';//'<li><a href="#">Next Page<i class="fa fa-long-arrow-right onclick="loadposts(this)"></i></a></li></ul>'
	
	$( "#paging" ).append(paging);
	addTplNews(null);
	
}

function editNews(me){
	var url 	= me.parentNode.parentNode.childNodes[4].innerHTML,
		title 	= me.parentNode.parentNode.childNodes[2].innerHTML,
		content = me.parentNode.parentNode.childNodes[3].innerHTML,
		image   = me.parentNode.parentNode.childNodes[5].innerHTML;
		
	var dialog  = '<div class="modal-dialog" id="editmodal">'+
						'<div class="modal-content">'+
							'<div class="modal-header">'+
								'<button type="button" class="close" data-dismiss="modal">&times;</button>'+
								'<h4 class="modal-title">Modal Header</h4>'+
							'</div>'+
							'<div class="modal-body">'+
								'<form id="form">'+
									'<div class="form-group">'+
										'<label for="title">Title</label>'+
										'<input type="text" class="form-control" id="titleEdit" placeholder="title" value="'+title+'">'+
									'</div>'+
									'<div class="form-group">'+
										'<label for="order">Order</label>'+
										'<input type="file" class="form-control" id="imageEdit" placeholder="image" value="'+image+'">'+
									'</div>'+
									'<div class="form-group">'+
										'<label for="order">Content</label>'+
										'<textarea class="form-control" rows="5" id="editorNews" placeholder="content"></textarea>'+
										'<script>'+
											'CKEDITOR.replace( \'editorNews\' );'+
										'</script>'+
									'</div>'+
									'<div class="form-group">'+
										'<label for="url">url</label>'+
										'<input type="text" class="form-control" id="urlEdit" placeholder="url" value="'+url+'" disabled>'+
									'</div>'+
									'<div class="modal-footer">'+
										'<button type="button" class="btn btn-primary" data-dismiss="modal">Close</button>'+
										'<button type="button" class="btn btn-primary" onClick="Javascript:updateNews(this)">Προσθήκη</button>'+
									'</div>'+
								'</form>'+
							'</div>'+
						'</div>'+
					'</div>';
			
	$( "#myModal" ).append(dialog);
	CKEDITOR.instances.editorNews.setData( content, function(){
			this.checkDirty();  // true
	});	
}

function updateNews(me){
	/*var category 	= {
		summary 		: $('#titleEdit')[0].value,
		body 	: CKEDITOR.instances.editorNews.getData()
	}*/
	var file = me.form[1].files[0]
	var category = new FormData();
	category.append('summary', $('#titleEdit')[0].value);
	category.append('body', CKEDITOR.instances.editorNews.getData());
	category.append('image', file , file.name);
	jQuery.ajax({
		url: $('#urlEdit')[0].value,
		type: "PUT",
		data: category,//JSON.stringify(category),//,
		//contentType: 'application/json; charset=utf-8',
		cache: false,
		dataType: 'json',
        processData: false, // Don't process the files
        contentType: false,
		headers: {
        		"Authorization": "Basic " + window.btoa("thanterz:papei"),
    		},
		beforeSend: function(xhr, settings) {
        		//if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            			xhr.setRequestHeader("X-CSRFToken", csrftoken);
        		//}
    		},
		success: function() {
			location.reload();
			console.log('success')

		},
		error : function(jqXHR, ajaxOptions, errorThrown) {
			alert(jqXHR.status);
         	alert(jqXHR.responseText);
		},

		timeout: 120000,
	});
}

function addNews(me){
	/*var category = {
		summary 		: $('#titleNews')[0].value,
		body 	: CKEDITOR.instances.contentNews.getData(),
		image    :me.form[1].files[0]
		
	}*/
	var file = me.form[1].files[0]
	var category = new FormData();
	category.append('summary', $('#titleNews')[0].value);
	category.append('body', CKEDITOR.instances.contentNews.getData());
	category.append('image', file , file.name);
	jQuery.ajax({
		url: "http://www.theama.info/curbweb/api/api/announcements/?format=json",
		type: "POST",
		data: category,//JSON.stringify(category),//,
		//contentType: 'application/json; charset=utf-8',
		cache: false,
		dataType: 'json',
        processData: false, // Don't process the files
        contentType: false,
		headers: {
        		"Authorization": "Basic " + window.btoa("thanterz:papei"),
    		},
		beforeSend: function(xhr, settings) {
        		//if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            			xhr.setRequestHeader("X-CSRFToken", csrftoken);
        		//}
    		},
		success: function() {
			location.reload();
			console.log('success')

		},
		error : function(jqXHR, ajaxOptions, errorThrown) {
			alert(jqXHR.status);
         	alert(jqXHR.responseText);
		},

		timeout: 120000,
	});
}
