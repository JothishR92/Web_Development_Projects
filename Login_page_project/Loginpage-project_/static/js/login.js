jQuery(document).ready(function() {
	jQuery('.login-form .tab-group a').on('click', function(e) {
		var currentAttrValue = jQuery(this).attr('href');

		// Show/Hide Tabs
		jQuery('.login-form ' + currentAttrValue).show().siblings().hide();

		// Change/remove current tab to active
		jQuery(this).parent('li').addClass('active').siblings().removeClass('active');

		e.preventDefault();
	});
});

$(document).ready(function(){
			$('.otp-number').hide();
		});

$(document).ready(function(){
	$('#send-otp').click(function(){
		$('#send-otp').hide();
		$('.otp-number').show()
	});

	});

$(document).ready(function() {
	$('#submit').click(function() {
		var user_details = {}
		user_details['user'] = $('#username').val();
		user_details['pwd'] = $('#password').val();
		console.log(user_details);
		$.ajax({
			type: "POST",
			url: "http://localhost:5000/login-page",
			data: JSON.stringify(user_details),
			contentType: "application/json",
			success: function(response){
				console.log(response['out'])
				if (response['out'] == 0) {
					alert("Username and password is correct...!")
				} else if (response['out'] == 1) {
					alert("Username and password is Incorrect...!")
				} else if (response['out'] == 2) {
					alert("Database connectivity problem...!")
				}
			},
			error: function(response, status){

			},
			complete: function(response, status){

			}
		});
		return false;
	});	
		
});

$(document).ready(function(){
	$('#signup-submit').click(function(){
		var signup_details = {};
		if ($('#pwd').val() != $('#c_password').val()) {
			alert("password didn't match...!");

		} else {
			signup_details['pwd'] = $('#pwd').val();
		}
		signup_details['user'] = $('#user').val();
		signup_details['email'] = $('#email-id').val();
		signup_details['p_no'] = $('#mobile_no').val();
		console.log(signup_details);
		$.ajax({
			type: "POST",
			url: "http://localhost:5000/signup-page",
			data: JSON.stringify(signup_details),
			contentType: "application/json",
			success: function(response){
				console.log(response['out'])
				if (response['out'] == 0) {
					alert("Signup details inserted sucessfully in database...!")
				} else if (response['out'] == 1) {
					alert("Already registered your details...!");
				} else if (response['out'] == 2) {
					alert("Database connectivity problem...!")
				}
			},
			error: function(response, status){

			},
			complete: function(response, status){

			}
		});
		return false;

	});
});