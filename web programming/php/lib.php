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
$bno=$_POST["b"];
$bt=$_POST["bt"];
$au=$_POST["a"];
$ed=$_POST["e"];
$pu=$_POST["p"];
$sql = "INSERT INTO lib (book_no, book_title,auther,edition,publiser)
VALUES ('$bno','$bt','$au','$ed','$pu')";
if ($conn->query($sql) === TRUE) {
  echo "new record inserted successfully";
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
</head>
<body>
<h2>LIBRARY MANANAGEMENT</h2>
<form method="post">
	Book No:<input type="numeric" name="b" required><br><br>
	Book title :<input type="text" name="bt" required><br><br>
	Author:<input type="text" name="a"required><br><br>
        Edition:<input type="text" name="e"required><br><br>
	Publisher:<input type="text" name="p"required><br><br>
        <input type="submit"  value="SUBMIT" id="submit" required>
</form>
<a href="search.php">Search</a>
</body>
</html>

