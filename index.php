<?php

$output = shell_exec("python3 conversor.py");
echo ($output);
$imagick = new Imagick();
$imagick->readImage('myfile.pdf');
$pages = $imagick->getNumberImages();
$myfile = fopen("index.html", "w");
$txt = "<title>HTML PAGE</title>";
fwrite($myfile, $txt);
for ($i = 0; $i < $pages; $i++) {
    $txt = "<img style=\"width: 100%;\"width=\"1080\" src=\"{$i}imagem.jpg\">";
    fwrite($myfile, $txt);
}
fclose($myfile);
