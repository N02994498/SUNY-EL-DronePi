<?php
$db = new SQLite3('database/pi_database.db');
print_r($db);
$results = $db->query('SELECT * FROM images');
print_r($results);
while ($row = $results->fetchArray()) {
var_dump($row);
}
?>