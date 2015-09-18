/*global $ */

var initialize=function(navigator, user, token, urls){
	$('#id_login').on('click',function(){
		navigator.id.request();
		
	});
	navigator.id.watch({
		loggedInUser: user,
		onlogin: function(assertion){
			data = {assertion: assertion, csrfmiddlewaretoken: token};
			// console.log('the csrfmiddlewaretoken includins:');
			// console.log(data.csrfmiddlewaretoken);
			$.post(
				urls.login,
				data
			)
				.done(function() { 
					console.log('post method succeed!');
					window.location.reload(); 
				})
				.fail(function() { 
					console.log('post method failed!');
					// console.log(urls.login);
					// console.log(assertion);
					// console.log(data.csrfmiddlewaretoken);
					navigator.id.logout();
				});
		},
		onlogout: function(){}
	});
};

window.Superlists = {
	Accounts: {
		initialize: initialize
	}
};

// navigator.id.watch({});