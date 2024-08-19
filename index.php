<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        body {
            position: absolute;
            left: 0;
            right: 0;
            width: 100vw;
            height: 100vh;
            text-align: center;
            margin: 0;
            background-image: url(##hintergrund_img##);
            background-size: cover;
            background-position: top;
            display: inline;
        }

        .logo {
            width: ##logo_breite##;
            height: auto;
        }

        #logo_rechts {
            position: absolute;
            right: 5%;
            top: 25%;
            width: 175px;
            height: auto;
        }
        #logo_links {
            position: absolute;
            left: 5%;
            top: 18%;
            width: 150px;
            height: auto;
        }

        #qr_code_pos { 
            position: absolute;
            left: 5%;
            top: 46%;
            width: 150px;
        }
        #qr_code {
            transform: translateY(-50%);
            width: 100%;
            height: auto;
            position: sticky;
            bottom: 50%;
        }

        #qr_code_logo {
            position: relative;
            transform: translateY(-50%);
            width: 25%;
            height: auto;
            z-index: 100;
        }

        #big_img {
            position: absolute;
            width: ##big_img_width##;
            height: auto;
            transform: translate(-50%,-50%);
            top: 34.5%;
            border-radius: 0.85vw;
        }

        #box {
            transform: translateX(3.5%);
            top: 70%;
            position: absolute;
            display: flex;
            justify-content: space-around;
            width: 93vw;
            height: auto;
        }

        .img_small {
            width: ##breite_small##;
            height: auto;
            border-radius: 0.35vw;
        }

    </style>
</head>
<body id="body">
    
    <img id="logo_links" class="logo" src="##werbung_links##" alt="">

    <div id="qr_code_pos">
        <img id="qr_code_logo" class="logo" src="##werbung_rechts##" alt="">
        <img id="qr_code" class="logo" src="data/qrcode.svg" alt="">
    </div>

    <img id="logo_rechts" class="logo" src="##werbung_rechts##" alt="">

	<?php
	$verzeichnis = '##verzeichnis##'; // Pfad zum Ordner, der die Bilder enthält
	$bilder = glob($verzeichnis . '*.{JPG,jpg,jpeg,png,gif}', GLOB_BRACE); // Suche nach Bild-Dateien
    
    $i = 0;

	foreach ($bilder as $bild) {
		if ($i == 0) {
			echo '<img id="big_img" src="' . $bild . '" alt="" loading="lazy">';
			echo '</div>';
			echo '<div id="box">';
		 } else {
			echo '<img id="img_'. $i .'" class="img_small" src="' . $bild . '" alt="" loading="lazy">';
		}
		
        $i += 1; 
    }
	echo '</div>';
	?>
    
	

</body>
</html>