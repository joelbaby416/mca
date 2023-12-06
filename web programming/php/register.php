<?php
	if ($_SERVER["REQUEST_METHOD"] == "POST") {
		$name = $_POST["name"];
		$email = $_POST["email"];
		$password = $_POST["password"];
		$confirmPassword = $_POST["confirm_password"];
		// Basic client-side validation
		if ($password !== $confirmPassword) {
			echo "Passwords do not match. Please try again.";
		} else {
			// Server-side validation (you can add more validation logic here)
			if (strlen($password) < 6) {
				echo "Password must be at least 6 characters long.";
			} else {
				// Registration logic (insert data into the database, etc.) can be added here
				echo "Registration successful! Welcome, " . $name . "!";
			}
		}
	}
?>
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width,initial-scale=1.0">
	<title>User Registration</title>
</head>
<body>
	<h2>User Registration</h2>
	<form method="post">
		Name:<input type="text" name="name"required><br><br>
		Email:<input type="email" name="email"required><br><br>
		Password:<input type="password" name="password"required><br><br>
Confirm Passwod:<input type="password" name="confirm_password"required><br><br>
		<input type="submit" value="Register">
	</form>
</body>
</html>
