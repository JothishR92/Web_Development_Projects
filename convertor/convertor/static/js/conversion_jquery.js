function conversion(){
        var req = {}
        var b  = $('#convert_bytes').val();
        var kb = $('#convert_kilobytes').val();
        var mb = $('#convert_megabytes').val();
        var gb = $('#convert_gigabytes').val();
	if (b != ''){
                req['B'] = b+" "+'B' ;
                console.log(b)
        } 
	if (kb != ''){
		req['KB'] = kb+" "+'KB' ;
                console.log(kb)
        } 
	if (mb != ''){
                req['MB'] = mb+" "+'MB' ;
                console.log(mb)
        } 
	if (gb != '') {
                req['GB'] = gb+" "+'GB';
                console.log(gb)
        }
	 $.ajax({
                type: "POST",
                url: "https://192.168.4.108:5000/unit_convertor",
                data:JSON.stringify(req),
                contentType: "application/json",
                success: function(response) {
			if(response.error == 1){
				alert("Don't give multiple values...!");
			}else {
				$('#convert_bytes').val(response.b);
                        	$('#convert_kilobytes').val(response.kb);
                        	$('#convert_megabytes').val(response.mb);
                        	$('#convert_gigabytes').val(response.gb);
			}

                },
                error: function(response, status) {
                },
                complete: function(response, status) {
                }
        });
        return false;
}
