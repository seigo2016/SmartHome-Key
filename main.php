<html>
<head>
<meta charset='utf-8'>
<title>Key</title>
</head>
<body>
<?php
//    ini_set('display_errors', 1);
    $text = "Key";
    echo "<p> $text </p>";
    if(isset($_POST['open'])) {
        $cmd = "/usr/bin/sudo -S /usr/bin/python3 /home/pi/Key/open.py";
        shell_exec($cmd);
    }
    if(isset($_POST['close'])) {
//        echo "open";
        $cmd = "/usr/bin/sudo -S /usr/bin/python3 /home/pi/Key/close.py";
        shell_exec($cmd);
?>
<form method="post">
    <button type='submit' name='open' value="1" style="font-size:45px;width:500px;height:250px">open</button>
    <button type='submit' name='close' value="1" style="font-size:45px;width:500px;height:250px">close</button>
</form>
</body>
</html>