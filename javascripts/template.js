

// gets the relevant JSON from file and does the main calculations
function get_json(json_var) {
	select_platform(json_var);
}

// selects a random platform/political opinion to support
function select_platform (positions) {
	// from http://stackoverflow.com/questions/6756104/get-size-of-json-object
	len = Object.keys(positions).length;
	chosen_position = positions[Object.keys(positions)[Math.floor(Math.random() * len)]];
	$("h1#title").html(chosen_position['title']);
	$("p#subtitle").html(chosen_position['subtitle']);
};



