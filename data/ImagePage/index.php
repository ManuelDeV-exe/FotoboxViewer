<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bildergalerie</title>
    <link rel="stylesheet" href="style.css">
	<script src="js/jquery-3.7.1.min.js"></script>
	
	<meta property="og:image" content="https://3ddruck-mb.de/AbschiedPaul/image.jpg"/>
	<meta property="og:title" content="Bildergalerie - Abschied Paul 2024"/>
	<meta property="og:description" content="Abschiedsparty für Paul Kowalski 2024"/>
	
</head>
<body>

 <!-- Modalfenster für Bildanzeige -->
    <div id="modal" hidden>
        <h1 id="caption"></h1>
        <div>    
            <div id="BTN_Container">
                <button id="zruck"><</button>
                <img id="big_img" name="" index="">
                <button id="weida">></button>
            </div>
        </div>
        <button id="Close">Close</button>
        <button id="downloadImage">Herunterladen</button>
        <button id="printImage">Drucken</button>
    </div>
	
<div id="gallery">
	<a href="https://3ddruck-mb.de/"><img src="./Logo.png" style="width: 10vw; cursor: pointer;"></a>
	<?php 
        include("header.html");
    ?>
	
	<?php
	$verzeichnis = 'data/'; // Pfad zum Ordner, der die Bilder enthält
	$bilder = glob($verzeichnis . '*.{JPG,jpg,jpeg,png,gif}', GLOB_BRACE); // Suche nach Bild-Dateien
    
    $i = 0;
	foreach ($bilder as $bild) {
		echo '<img class="images" index="' . $i . '" name="' . $bild . '" src="' . $bild . '" loading="lazy">'; // Bilder anzeigen
        $i += 1; 
    }
    echo '<p id="max_Index" index="' . $i . '" hidden></p>'
	?>
</div>

<script src="js/script.js"></script>
</body>
</html>
