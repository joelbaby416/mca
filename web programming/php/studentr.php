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
$email=$_POST["email"];
$course=$_POST["course"];

$sql = "INSERT INTO reg (name, email,course) VALUES ('$name','$email','$course')";
if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
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
<h2>student registration form</h2>
<form method="post">
	name:<input type="text" name="n" required><br><br>
	email:<input type="email" name="email" required><br><br>
	course:<input type="text" name="course" required><br><br>
        <input type="submit"  value="submit" id="submit" required>
</form>
</body>
</html>

