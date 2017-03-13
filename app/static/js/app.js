$("#get-json").click(function(){
	$.ajax({
		type: 'POST',
		contentType: 'application/json',
		success: function(data) {
			console.log(data);
		}
    });
});
