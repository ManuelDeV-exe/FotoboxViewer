<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bildergalerie</title>
    <link rel="stylesheet" href="style.css">
	<script src="js/jquery-3.7.1.min.js"></script>
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
	
	<?php
	$verzeichnis = 'data/'; // Pfad zum Ordner, der die Bilder enthält
	$bilder = glob($verzeichnis . '*.{jpg,jpeg,png,gif}', GLOB_BRACE); // Suche nach Bild-Dateien
    
    $i = 0;
	foreach ($bilder as $bild) {
		echo '<img class="images" index="' . $i . '" name="' . $bild . '" src="' . $bild . '" >'; // Bilder anzeigen
        $i += 1; 
    }
    echo '<p id="max_Index" index="' . $i . '" hidden></p>'
	?>
</div>

<script src="js/script.js"></script>
</body>
</html>
