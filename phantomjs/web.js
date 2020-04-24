var page = require("webpage").create();
page.open("https : //developers.arcgis.com/javascript/latest/sample-code/widgets-print/live/index.html", function(status) {
	if(status == "success"){
		page.render("web.png");
	} else {
		console.log("cant load page");
	}
	
	phantom.exit();

});