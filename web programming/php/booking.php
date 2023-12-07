<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "joeldb";
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
if($_POST){
$name=$_POST["n"];
$des=$_POST["de"];
$da=$_POST["da"];

$sql = "INSERT INTO db_book (name, des,da) VALUES ('$name','$des','$da')";
if ($conn->query($sql) === TRUE) {
  echo "Booking has beeen successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}
$conn->close();
}
?>
<html>
<head>
<meta charset="UFT-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>user register</title>
</head>
<body>
<h2>Airline Ticket Booking</h2>
<form method="post">
	name:<input type="text" name="n" required><br><br>
	destination:<input type="text" name="de" required><br><br>
	date:<input type="date" name="da" required><br><br>
        <input type="submit"  value="submit" id="submit" required>
</form>
</body>
</html>

