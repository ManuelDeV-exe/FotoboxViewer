$(document).ready(function () {
	var Koordinaten = "";
	var Ratio = 1.56;
	var breitenfaktor = 0.95;

	const stage = Jcrop.attach('cropimage');
	const rect = Jcrop.Rect.create(($("#cropimage").width() - ($("#cropimage").width() * breitenfaktor)) / 2, ($("#cropimage").height() - ($("#cropimage").width() * breitenfaktor) / Ratio) / 2, ($("#cropimage").width() * breitenfaktor), ($("#cropimage").width() * breitenfaktor) / Ratio);

	stage.setOptions({
		canResize: false, // Deaktiviert das Ändern der Größe
		aspectRatio: Ratio   // Verhältnis von Breite zu Höhe, 1:1 für Quadrat
	});

	stage.newWidget(rect);

	stage.listen('crop.update', (widget, e) => {
		Koordinaten = widget.pos;
	});

	$("#Crop_BTN").click(function () {
		Write_MySQL($("#cropimage").attr('src'), $("#cropimage").width(), $("#cropimage").height(), Koordinaten)
	});

	$("#reload_BTN").click(function () {
		location.reload();
	});

	$(window).on('orientationchange', function (event) {
		if (window.orientation == 0) {
			location.reload();
		} else {
			location.reload();
		}
	});

});

function Write_MySQL(img_src, img_w, img_h, cords) {
	segments = img_src.split('/');
	img_src = segments[segments.length - 1];
	window.open("./upload_Mysql.php?width=" + String(img_w.toFixed(2)) + "&myheight=" + String(img_h.toFixed(2)) + "&pos_x=" + String(cords.x.toFixed(2)) + "&pos_y=" + String(cords.y.toFixed(2)) + "&poswidth=" + String(cords.w.toFixed(2)) + "&posheigth=" + String(cords.h.toFixed(2)) + "&mypath=" + String(img_src));
	window.close();
}