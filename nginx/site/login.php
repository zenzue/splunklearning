<?php
$valid_username = 'admin';
$valid_password = 'password123';

$username = $_POST['username'];
$password = $_POST['password'];

if ($username === $valid_username && $password === $valid_password) {
    echo "Logged in as: " . htmlspecialchars($username) . "<br>";
} else {
    echo "Failed to login";
}
?>
