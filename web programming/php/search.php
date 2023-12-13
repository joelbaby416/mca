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
$title=$_POST["n"];
$sql="select * from lib where book_title='$title'";
$result=$conn->query($sql);
if($result->num_rows>0)
{
echo"<table><tr><th>book_no</th><th>book_title</th><th>author</th><th>edition</th><th>publisher</th></tr>";
while($row=$result->fetch_assoc()){
echo"<tr><td>".$row["book_no"]."</td><td>".$row["book_title"]."</td><td>".$row["auther"]."</td><td>".$row["edition"]."</td><td>".$row["publiser"]."</td></tr>";
}
echo"</table>";
}
else{
echo"0 results found";
}
}
$conn->close();
?>
<html>
<head>
<meta charset="UFT-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
</head>
<body>
<h2>LIBRARY</h2>
<form method="post">
	TITLE:<input type="text" name="n" required><br><br>
        <input type="submit"  value="search" id="submit" required>
</form>
</body>
</html>

