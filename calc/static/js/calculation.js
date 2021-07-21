function back(){
	var value = document.getElementById('textbox').value;
	document.getElementById('textbox').value = value.substring(0,value.length -1);
}
function loadDoc(){
	var request = {}
	request['input'] = document.getElementById('textbox').value;

	var xhttp = new XMLHttpRequest();
	xhttp.open("POST","http://10.132.243.88:5000/output",true);
	xhttp.setRequestHeader('content-type','application/json');
	xhttp.onreadystatechange = function () {
		if (xhttp.readyState == 4 && xhttp.status == 200) {
			console.log(xhttp.responseText);
			var a = JSON.parse(xhttp.responseText)
			document.getElementById("textbox1").value = a.output;
		}
		return false;
	};
	xhttp.send(JSON.stringify(request));
	return false;
}
