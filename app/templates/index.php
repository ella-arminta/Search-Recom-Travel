<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
</head>
<body>
    <h1>Travel agent traveloka This Is Hotel Search</h1>
    {% for hotel in data %}
        <li>
            <strong>Name:</strong> {{ hotel['hotel_name'] }} <br>
            <strong>Address:</strong> {{ hotel['hotel_address'] }} <br>
            <strong>Price:</strong> {{ hotel['hotel_price'] }}
        </li>
    {% endfor %}
</body>
</html>