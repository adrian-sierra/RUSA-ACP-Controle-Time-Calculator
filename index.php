<html>
    <head>
        <title>CIS 322 REST-api Project</title>
    </head>

    <body>
        <h1>All Times</h1>
        <ul>
            <?php
            $json = file_get_contents('http://web/listOpenOnly');
            $obj = json_decode($json);
                  $times = $obj->open;
            foreach ($times as $t) {
                echo "<li>$t</li>";
            }
            ?>
            <?php
            $json = file_get_contents('http://web/listCloseOnly');
            $obj = json_decode($json);
                  $times = $obj->close;
            foreach ($times as $t) {
                echo "<li>$t</li>";
            }
            ?>
        </ul>
        <h1>Open Times</h1>
        <ul>
            <?php
            $json = file_get_contents('http://web/listOpenOnly');
            $obj = json_decode($json);
	          $times = $obj->open;
            foreach ($times as $t) {
                echo "<li>$t</li>";
            }
            ?>
        </ul>
        <h1>Close Times</h1>
        <ul>
            <?php
            $json = file_get_contents('http://web/listCloseOnly');
            $obj = json_decode($json);
                  $times = $obj->close;
            foreach ($times as $t) {
                echo "<li>$t</li>";
            }
            ?>
        </ul>
    </body>
</html>
