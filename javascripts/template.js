function randomize_title (arg1, arg2) {
	// picks a random title for the page
	args = [arg1, arg2];
	selected_arg = args[Math.floor(Math.random() * 2)];
	$("h1#title").html(selected_arg);
};