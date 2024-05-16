<?php
$servername = "myfritznas.3ddruck-mb.de";
$username = "manuel_admin";
$password = "N9$zjYjXktnn5bfcr";
$dbname = "ImageViewer";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$leftCorner = $_POST['leftCorner'];
$rightCorner = $_POST['rightCorner'];
$imageName = $_POST['imageName'];

$sql = "INSERT INTO DatenBank (leftCorner, rightCorner, imageName)
VALUES ('$leftCorner', '$rightCorner', '$imageName')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
