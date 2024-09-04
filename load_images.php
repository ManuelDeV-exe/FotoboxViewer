<?php
$verzeichnis = ''; // Pfad zum Ordner, der die Bilder enthält
$bilder = glob($verzeichnis . '*.{JPG,jpg,jpeg,png,gif}', GLOB_BRACE);
usort($bilder, function($a, $b) {
    return filemtime($b) - filemtime($a);
});

// Sicherstellen, dass mindestens 5 Bilder vorhanden sind
for ($i = count($bilder); $i < 5; $i++) {
    $bilder[] = 'placeholder.png'; // Platzhalter-Bild verwenden, falls weniger als 5 Bilder vorhanden sind
}

echo json_encode(array_slice($bilder, 0, 5)); // Die ersten 5 Bilder zurückgeben
?>
