$(document).ready(function(){
	// Open IMG in Overview
	$(".images").click(function(){
		LoadImage($(this).attr('name'), $(this).attr('src'), $(this).attr('index'));
	});

	// BTN in Overview
	$("#Close").click(function () {
		$("#modal").hide("slow");
	});

	$("#downloadImage").click(function () {
		downloadFile($("#big_img").attr('src'), $("#big_img").attr('name'));
	});

	$("#printImage").click(function () {
		printImage($("#big_img").attr('src'));
	});

	// weida & zruck
	$("#weida").click(function () {
		weida($("#big_img").attr('index'));
	});

	$("#zruck").click(function () {
		zruck($("#big_img").attr('index'));
	});

});

function searchImage(desiredIndex) {
	var images = document.querySelectorAll("img.images");
	
	for (var i = 0; i < images.length; i++) {
		if (parseInt($(images[i]).attr("index")) === desiredIndex) {
			return {
				name: $(images[i]).attr("name"),
				src: $(images[i]).attr("src"),
				index: $(images[i]).attr("index")
			};
		}
	}
}

function weida(index) {
	var max_Index = parseInt($("#max_Index").attr('index'))-1;
	var new_Index = parseInt(index) + 1;

	console.log(new_Index, max_Index)
	if (new_Index > max_Index) {
		new_Index = 0;
	}

	var imageDetails = searchImage(new_Index);

	LoadImage(imageDetails.name, imageDetails.src, imageDetails.index);
}

function zruck(index) {
	var max_Index = parseInt($("#max_Index").attr('index')) - 1;
	var new_Index = parseInt(index) - 1;

	console.log(new_Index, max_Index)
	if (new_Index < 0) {
		new_Index = max_Index;
	}

	var imageDetails = searchImage(new_Index);

	LoadImage(imageDetails.name, imageDetails.src, imageDetails.index);
}

function LoadImage(name, img_src, index) {
	$("#big_img").attr("src", img_src);
	segments = name.split('/');
	name = segments[segments.length - 1];
	$("#modal").show("slow");
	$("#caption").text(name);
	$("#big_img").attr("name", name);
	$("#big_img").attr("index", index);
}

function downloadFile(filepath, name) {
	const element = $('<a/>')
		.attr('href', filepath) // Setzen Sie den Pfad zur Datei
		.attr('download', name) // Setzen Sie den Namen der heruntergeladenen Datei
		.attr('target', '_blank')
		.appendTo('body'); // Fügen Sie es dem Body hinzu
	element[0].click();
	element.remove();
}

function printImage(filepath) {
	window.open("./printImage.php?path="+ filepath); 
}