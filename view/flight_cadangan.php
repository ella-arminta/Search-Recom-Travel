<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flight Booking App</title>
    <link rel="stylesheet" href="indexcss.css">
    <!-- Additional links for fonts and icons can be added here -->
</head>

<body>
    <div class="overlay"></div>
    <div class="wrap" data-pos="0">
        <!-- Flight booking app content -->
        <!-- <div class="headbar">Flight Booking</div> -->
        <div class="header">
            <div class="left-section">
                <button type="button" class="left-button active">One-way / Round-trip</button>
                <button type="button" class="left-button">Multi-city</button>
            </div>
            <div class="right-section">
                <button type="button" class="right-button">Need inspiration? Search for flights to anywhere</button>
            </div>
        </div>
        <div class="content">
            <!-- Form for selecting flight details -->
            <form id="flightForm">
                <div class="grid-container">
                    <div class="grid-item grid-sub-container-1"> <!-- Section 1 -->
                        <div>
                            <!-- from -->
                            <div>From</div>
                            <div class="grid-sub-input-1"></div>
                        </div>
                        <div></div>
                        <div>
                            <!-- to -->
                            <div>To</div>
                            <div class="grid-sub-input-1"></div>
                        </div>
                    </div>
                    <div class="grid-item"> <!-- Section 2 -->
                        <!-- no of passengers -->
                        <div>No. of Passengers</div>
                        <div></div>
                    </div>
                    <div class="grid-item grid-sub-container-3"> <!-- Section 3 -->
                        <div>
                            <!-- departure date -->
                            <div>Departure date</div>
                            <div></div>
                        </div>
                        <div></div>
                        <div>
                            <!-- checkbox return date -->
                            <div>Return Date</div>
                            <div></div>
                        </div>
                    </div>
                    <div class="grid-item"> <!-- Section 4 -->
                        <!-- seat clas -->
                        <div>Seat Class</div>
                        <div></div>
                    </div>
                </div>
                <label for="departure">Departure City:</label>
                <input type="text" id="departure" name="departure" placeholder="Enter departure city">
                <!-- Other input fields (destination, dates, passengers, etc.) -->
                <button type="submit">Search Flights</button>
            </form>
        </div>
        <!-- Other sections (list of flights, selected ticket details, etc.) -->
    </div>
    <script>
        // Get all the buttons with the 'button' class
        // Get all the buttons
        const buttons = document.querySelectorAll('.left-button, .right-button');

        // Add an event listener to each button
        buttons.forEach(button => {
            button.addEventListener('click', function () {
                // Remove the 'active' class from all buttons
                buttons.forEach(btn => btn.classList.remove('active'));
                // Add the 'active' class to the clicked button
                this.classList.add('active');
            });
        });

        // Get the wrap and overlay elements
        const wrap = document.querySelector('.wrap');
        const overlay = document.querySelector('.overlay');

        // Add an event listener to the wrap
        wrap.addEventListener('click', function () {
            // Toggle the visibility of the overlay
            if (overlay.classList.contains('visible')) {
                overlay.classList.remove('visible');
                this.classList.remove('highlighted'); // Remove the highlighted class
            } else {
                overlay.classList.add('visible');
                this.classList.add('highlighted'); // Add the highlighted class
            }
        });
    </script>
</body>

</html>