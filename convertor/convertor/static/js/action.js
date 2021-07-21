function conversion(){
	req = {}
	var b  = document.getElementById('convert_bytes').value
	var kb = document.getElementById('convert_kilobytes').value
	var mb = document.getElementById('convert_megabytes').value
	var gb = document.getElementById('convert_gigabytes').value
	if (b != ''){
		req['B'] = b+" "+'B' ;
		console.log(b)	
	} else if (kb != ''){
		req['KB'] = kb+" "+'KB' ;
		console.log(kb)
	} else if (mb != ''){
		req['MB'] = mb+" "+'MB' ;
		console.log(mb)
	} else if (gb != '') {
		req['GB'] = gb+" "+'GB';
		console.log(gb)
	}
	var ajax_req = new XMLHttpRequest();
	ajax_req.open("POST","http://10.132.243.88:5000/unit_convertor",true);
	ajax_req.setRequestHeader('content-type','application/json');

	ajax_req.onreadystatechange = function (){
		if (ajax_req.readyState == 4 && ajax_req.status == 200) {
			var out = JSON.parse(ajax_req.responseText);
			document.getElementById('convert_bytes').value = out.b;
			document.getElementById('convert_kilobytes').value = out.kb;
			document.getElementById('convert_megabytes').value = out.mb;
			document.getElementById('convert_gigabytes').value = out.gb;
		}
		return false;
	};
	ajax_req.send(JSON.stringify(req));
	return false;
}
