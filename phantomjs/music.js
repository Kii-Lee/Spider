var page=require('webpage').create();
console.log("start now. ");
page.open('http://music.163.com/',function(status){
	console.log("status: "+status);
	if(status=="success"){
		page.render('music.png');
	}
	phantom.exit();
});