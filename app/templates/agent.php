<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
</head>
<body>
    <h1>Travel agent traveloka This Is Travel Agent Search</h1>
    {% for agent in data %}
        <li>
            <strong>Travel Agent Name:</strong> {{ agent['agent_name'] }} <br>
            <strong>Travel Agent Address:</strong> {{ agent['agent_address'] }} <br>
            <strong>Travel Agent Phone:</strong> {{ agent['agent_phone'] }} <br>
            <strong>Travel Agent City:</strong> {{ agent['agent_city'] }} <br>
        </li>
    {% endfor %}
</body>
</html>