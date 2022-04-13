#!/usr/bin/node

$.ajax({
    	url: "https://swapi-api.hbtn.io/api/people/5/?format=json",
    	success: function(data){ 
    	    $('DIV#character').text(data.name);
    	},
    	error: function(){
    		alert("There was an error.");
    	}
    });
