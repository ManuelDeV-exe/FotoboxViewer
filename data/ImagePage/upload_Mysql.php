<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bildergalerie - Upload</title>
    <link rel="stylesheet" href="style_printImage.css">
</head>
<body>
<div id="inhalt">
    <?php
        $img_width = $_GET["width"];
        $img_height = $_GET["myheight"];
        $img_pos_x = $_GET["pos_x"];
        $img_pos_y = $_GET["pos_y"];
        $img_pos_width = $_GET["poswidth"];
        $img_pos_heigth = $_GET["posheigth"];
        $image_path = $_GET["mypath"];


            // Verbindungsdaten
        $servername = "myfritznas.3ddruck-mb.de";
        $username = "manuel_admin";
        $password = "N9\$zjYjXktnn5bfcr";
        $database = "ImageViewer";

        // Verbindung aufbauen
        $con = mysqli_connect($servername, $username, $password, $database);

        if (!$con) {
            die("Verbindung fehlgeschlagen: " . mysqli_connect_error());
        }

        $uhrzeit = date("dmYHis", time());

        $con = mysqli_connect($servername, $username, $password, "ImageViewer");
        $sql = "INSERT INTO `ImageViewer`.`DatenBank` (`index`, `img_width`, `img_height`, `img_pos_x`, `img_pos_y`, `img_pos_width`, `img_pos_heigth`, `image_path`) VALUES ('$uhrzeit', '$img_width', '$img_height', '$img_pos_x', '$img_pos_y', '$img_pos_width', '$img_pos_heigth', '$image_path')";

        // Ausführen des SQL-Befehls
        if (mysqli_query($con, $sql)) {
            echo "Das Ausdrucken kann etwas Zeit in Anspruch nehmen, danke für benutzen 😍";
            sleep(0.2);
            echo "<script>window.close();</script>";
        } else {
            echo "Fehler beim Erstellen des Eintrags: " . mysqli_error($con);
            sleep(10);
            echo "<script>window.close();</script>";
        }   
    ?>
</div>
</body>
</html>
