<?php
  session_start();
  if (! isset($_SESSION['login']) || ! $_SESSION['login']) {
    $dirname = $_SERVER['REQUEST_URI'] ?? '';
    $dirname = preg_replace('/index.php$/', '', $dirname);

    header("Location: ".$dirname."{calibration}login.php?redirect={redirect}");
  }
?>
