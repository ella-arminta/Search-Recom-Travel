<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
</head>
<body>
    <h1>Travel agent traveloka This Is Attraction Search</h1>
    {% for attraction in data %}
        <li>
            <strong>Name:</strong> {{ attraction['attraction_name'] }} <br>
            <strong>Address:</strong> {{ attraction['attraction_address'] }} <br>
            <strong>Price:</strong> {{ attraction['attraction_price'] }}
        </li>
    {% endfor %}
</body>
</html>