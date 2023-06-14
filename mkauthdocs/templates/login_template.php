<?php
session_start();
$uname = $_POST["uname"] ?? '';
$pwd = $_POST["pwd"] ?? '';

if ($uname == "{username}" && $pwd == "{password}") {
  $_SESSION['login'] = true;
  header("Location: ".$_GET["redirect"]);
}

if (isset($_POST['submit'])) {
  print('<div class="alert alert-danger" role="alert"><center>The username or password is invalid</center></div>');
}

?>

<!DOCTYPE html>

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>{heading}</title>

  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>

<body>
  <form id='login' action='login.php<?php if (empty($_GET['redirect'])) { echo ("?redirect=index.php"); } else { echo ("?redirect=".$_GET['redirect']); } ?>' method='post' accept-charset='UTF-8'>
    <div class="container">

      <center><h1>{heading}</h1></center>
      <hr>

      <div class="form-group">
        <h4><label for="uname">Username</label></h4>
        <input type="text" class="form-control" id="uname" name="uname" placeholder="Username">
      </div>

      <div class="form-group">
        <h4><label for="pwd">Password</label></h4>
        <input type="password" class="form-control" id="pwd" name="pwd" placeholder="Password">
      </div>

      <br>

      <button type="submit" id="submit" name="submit" class="btn btn-lg btn-primary btn-block">Login</button>

    </div>
  </form>
</body>
