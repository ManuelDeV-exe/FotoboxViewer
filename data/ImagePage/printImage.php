<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bildergalerie - Crop</title>

    <link rel="stylesheet" href="style_printImage.css">
    <link rel="stylesheet" href="js/jcrop.css">

    <script src="js/jcrop.js"></script>
	<script src="js/jquery-3.7.1.min.js"></script>
</head>
<body>

<div id="img_gesamt">
    <div>
        <?php
            $img_path = $_GET["path"];
            echo '<img id="cropimage" src="' . $img_path . '" >';
        ?>
    </div>
    <div id="BTN_Box">
        <button class="BTN" id="Crop_BTN">Drucken</button>
        <button class="BTN" id="reload_BTN">Neu beginnen</button>
    </div>
</div>


<script src="js/printImage_crop.js"></script>
</body>
</html>
