<html>
<head>
<meta charset='utf-8'>
<title>Key</title>
</head>
<body>
<?php
    if(isset($_POST['open'])) {
        $cmd = "/usr/bin/sudo -S /usr/bin/python3 Key/open.py";
        shell_exec($cmd);
    }
    if(isset($_POST['close'])) {
        $cmd = "/usr/bin/sudo -S /usr/bin/python3 Key/close.py";
        shell_exec($cmd);
?>
<form method="post">
    <button type='submit' name='open' value="1" style="font-size:45px;width:500px;height:250px">open</button>
    <button type='submit' name='close' value="1" style="font-size:45px;width:500px;height:250px">close</button>
</form>
</body>
</html>
