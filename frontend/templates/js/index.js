 $("#login-button").click(function(event){
		 event.preventDefault();

	 var serialized = $("form").serializeArray();
	 var s = '';
        var data = {};
        for(s in serialized){
            data[serialized[s]['name']] = serialized[s]['value']
        }
        formData = JSON.stringify(data);
	 console.log(formData);	 
	 $('form').fadeOut(500);
	 $('.wrapper').addClass('form-success');


	 var url = "https://vyaapicr.herokuapp.com/login";
     var xhr = new XMLHttpRequest();
     xhr.open("POST", url, true);

     //Send the proper header information along with the request
     xhr.setRequestHeader("Content-type", "application/json");

     xhr.onreadystatechange = function() {//Call a function when the state changes.
        if(xhr.readyState == 4 && xhr.status == 200) {
        	var data = xhr.responseText;
        	console.log("response : " + data);
        	data = JSON.parse(data); 
            sessionStorage.token = data.auth_token;
            window.location="dashboard.html";
        }
        else
        {
            console.log("xhr.status : ");
            console.log(xhr.status);
        }
     }
     
     xhr.send(formData);
     //   var response = xhr.send(formData);
        
 });