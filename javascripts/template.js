

// gets the relevant JSON from the json variable and does the main calculations
function get_json(json_var) {
	select_platform(json_var);
};

// selects a random platform/political opinion to support
function select_platform (positions) {
	// from http://stackoverflow.com/questions/6756104/get-size-of-json-object
	len = Object.keys(positions).length;
	chosen_position = positions[Object.keys(positions)[Math.floor(Math.random() * len)]];
	$("h1#title").html(chosen_position['title']);
	$("p#subtitle").html(chosen_position['subtitle']);
};


// test function for getting JSON from file
function get_json2(json_file) {
	$.getJSON(json_file, function(json) {
		select_platform2(json);
	});
};

// selects a random platform/political opinion to support
function select_platform2(json) {
	positions = json['positions'];
	// from http://stackoverflow.com/questions/6756104/get-size-of-json-object
	len = Object.keys(positions).length;
	chosen_position = positions[Object.keys(positions)[Math.floor(Math.random() * len)]];
	$("h1#title").html(chosen_position['title']);
	$("p#subtitle").html(chosen_position['subtitle']);
};


