<!DOCTYPE html>
<html>
<head>
    <title>Control de Acceso</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>

<h1>Registro de Accesos</h1>

<table>
    <tr>
        <th>Evento</th>
    </tr>

<?php
$archivo = "logs/auditoria.txt";

if(file_exists($archivo)){
    $lineas = file($archivo);

    foreach($lineas as $linea){
        $clase = "";

        if(strpos($linea, "DENEGADO") !== false){
            $clase = "denegado";
        } elseif(strpos($linea, "PERMITIDO") !== false){
            $clase = "permitido";
        } elseif(strpos($linea, "INACTIVO") !== false){
            $clase = "inactivo";
        }

        echo "<tr class='$clase'><td>$linea</td></tr>";
    }
}
?>

</table>

</body>
</html>