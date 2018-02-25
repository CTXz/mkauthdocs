<!-- Authentication Guard -->
<?php
	session_start();
	if (!$_SESSION['login']) {
		header("Location: /login.php?redirect={redirect}");
	}
?>
