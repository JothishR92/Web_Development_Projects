function back(){
	var value = $('#textbox').val();
	$('#textbox').val(value.substring(0,value.length -1));
}
function loadDoc(){
	$.ajax({
		type: "POST",
		url: "http://10.132.243.88:5000/output",
		data: JSON.stringify({"input": $('#textbox').val()}),
		contentType: "application/json",
		success: function(response) {
			$('#textbox1').val(response.output);
		},
		error: function(response, status) {
		},
		complete: function(response, status) {
		}
	});
	return false;
}
