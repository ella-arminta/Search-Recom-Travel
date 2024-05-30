<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
</head>
<body>
    <h1>Travel agent traveloka This Is Attraction Search</h1>
    {% for insurance in data %}
        <li>
        <strong>ID:</strong> {{ insurance['id_user'] }} <br>
            <strong>Name:</strong> {{ insurance['nama_user'] }} <br>
            <strong>Nomor Telepon:</strong> {{ insurance['nomor_telepon'] }} <br>
            <strong>Alamat:</strong> {{ insurance['alamat'] }} <br>
        </li>
    {% endfor %}
</body>
</html>