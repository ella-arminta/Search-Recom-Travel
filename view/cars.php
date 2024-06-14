<!doctype html>
<html>

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Cars Rental</title>

    <!-- Roboto font -->
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900&display=swap" rel="stylesheet" />

    <!-- Tailwind CSS config -->
    <script src="https://cdn.tailwindcss.com/3.3.0"></script>

    <!-- stylesheet -->
    <link rel="stylesheet" href="https://unpkg.com/@material-tailwind/html@latest/styles/material-tailwind.css" />

    <!-- Font Awesome Icon -->
    <script src="https://kit.fontawesome.com/e52db3bf8a.js" crossorigin="anonymous"></script>
</head>

<style>
    .bg-gradient-custom-blue {
        background: rgb(25, 50, 124);
        background: linear-gradient(143deg, rgba(25, 50, 124, 1) 0%, rgba(42, 123, 209, 1) 56%, rgba(75, 145, 224, 1) 100%);
    }

    .custom-shadow-card {
        box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
    }
</style>

<body class="">
    <!-- default search -->
    <div class="w-full bg-gradient-custom-blue p-2 px-5 text-white shadow-lg">
        <div class="flex justify-center items-center gap-5">
            <h1 class="text-lg font-semibold w-1/3">Car Rentals</h1>
            <div class="rounded w-full backdrop-blur-sm bg-white/30 p-2 flex justify-center items-center gap-3 text-sm font-semibold"><svg width="16" height="16" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemMapLocationFill12">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M6 12C6 12 10.5 8.5 10.5 5.5C10.5 2.73858 8.76142 0.5 6 0.5C3.23858 0.5 1.5 2.73858 1.5 5.5C1.5 8.5 6 12 6 12ZM6 7C7.10457 7 8 6.10457 8 5C8 3.89543 7.10457 3 6 3C4.89543 3 4 3.89543 4 5C4 6.10457 4.89543 7 6 7Z" fill="#FFFFFF"></path>
                </svg>
                Yogyakarta</div>
            <div class="rounded w-full backdrop-blur-sm bg-white/30 p-2 flex justify-center items-center gap-3 text-sm font-semibold"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemCalendar">
                    <path d="M7 2V5M17 2V5M3 8H21M11.5 11.5H12.5V12.5H11.5V11.5ZM11.5 16.5H12.5V17.5H11.5V16.5ZM16.5 11.5H17.5V12.5H16.5V11.5ZM6.5 16.5H7.5V17.5H6.5V16.5ZM5 21H19C20.1046 21 21 20.1046 21 19V6C21 4.89543 20.1046 4 19 4H5C3.89543 4 3 4.89543 3 6V19C3 20.1046 3.89543 21 5 21Z" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M7.5 11.5V12.5H6.5V11.5H7.5Z" stroke="#0194F3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                </svg>
                15 Juni - 16 Juni</div>
        </div>
    </div>
    <!-- back button -->
    <div class="back-button absolute top-20 cursor-pointer text-gray-400 left-10">
        <a href="searchcar.php">
            <i class="fa-solid fa-arrow-left"></i>
        </a>
    </div>
    <!-- container -->
    <div class="w-3/4 m-auto mt-5">
        <!-- filters option -->
        <div class="flex justify-between items-center">
            <div class="flex gap-3 items-center">
                <div>
                    <!-- Pasanger Capacity -->
                    <div>
                        <button data-ripple-light="true" data-popover-target="passangermenu" class="justify-center items-center text-blue-500 flex drop-shadow-lg select-none rounded-full bg-white py-2 px-6 text-center align-middle font-sans text-sm font-bold shadow-md transition-all focus:opacity-[0.85] active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
                            <div>Passanger Capacity</div>
                            <div dir="auto" aria-hidden="true" class="css-901oao r-1awozwy r-6koalj r-13hce6t" style="color: rgb(1, 148, 243);"><svg width="24" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemChevronDown">
                                    <path d="M6 9L12 15L18 9" stroke="#0194f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                                </svg></div>
                        </button>
                        <ul role="menu" data-popover="passangermenu" data-popover-placement="bottom" class="absolute z-10 min-w-[180px] overflow-auto rounded-md border border-blue-gray-50 bg-white p-3 font-sans text-sm font-normal text-blue-gray-500 shadow-lg shadow-blue-gray-500/10 focus:outline-none transition-opacity duration-300 pointer-events-none opacity-0">
                            <form name="capacity" id="capacityForm">
                                <li role="capitem" class="flex gap-2 block m-auto w-full cursor-pointer text-md select-none rounded-md px-3 pt-[9px] pb-2 text-start leading-tight transition-all hover:bg-blue-gray-50 hover:bg-opacity-80 hover:text-blue-gray-900 focus:bg-blue-gray-50 focus:bg-opacity-80 focus:text-blue-gray-900 active:bg-blue-gray-50 active:bg-opacity-80 active:text-blue-gray-900">
                                    <input type="checkbox" id="cap4" name="capacity[]" value="4">
                                    <label for="cap4">
                                        4
                                    </label><br>
                                </li>
                                <li role="capitem" class="flex gap-2 block m-auto w-full cursor-pointer text-md select-none rounded-md px-3 pt-[9px] pb-2 text-start leading-tight transition-all hover:bg-blue-gray-50 hover:bg-opacity-80 hover:text-blue-gray-900 focus:bg-blue-gray-50 focus:bg-opacity-80 focus:text-blue-gray-900 active:bg-blue-gray-50 active:bg-opacity-80 active:text-blue-gray-900">
                                    <input type="checkbox" id="cap56" name="capacity[]" value="56">
                                    <label for="cap56">
                                        5 - 6
                                    </label><br>
                                </li>
                                <li role="capitem" class="flex gap-2 block m-auto w-full cursor-pointer text-md select-none rounded-md px-3 pt-[9px] pb-2 text-start leading-tight transition-all hover:bg-blue-gray-50 hover:bg-opacity-80 hover:text-blue-gray-900 focus:bg-blue-gray-50 focus:bg-opacity-80 focus:text-blue-gray-900 active:bg-blue-gray-50 active:bg-opacity-80 active:text-blue-gray-900">
                                    <input type="checkbox" id="cap7" name="capacity[]" value="7">
                                    <label for="cap7">
                                        > 6
                                    </label><br>
                                </li>
                            </form>
                        </ul>
                    </div>
                </div>

                <div>
                    <!-- Transmission -->
                    <div>
                        <button data-ripple-light="true" data-popover-target="transmissionmenu" class="justify-center items-center text-blue-500 flex drop-shadow-lg select-none rounded-full bg-white py-2 px-6 text-center align-middle font-sans text-sm font-bold shadow-md transition-all focus:opacity-[0.85] active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
                            <div>Transmission</div>
                            <div dir="auto" aria-hidden="true" class="css-901oao r-1awozwy r-6koalj r-13hce6t" style="color: rgb(1, 148, 243);"><svg width="24" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemChevronDown">
                                    <path d="M6 9L12 15L18 9" stroke="#0194f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                                </svg></div>
                        </button>
                        <ul role="menu" data-popover="transmissionmenu" data-popover-placement="bottom" class="absolute z-10 min-w-[180px] overflow-auto rounded-md border border-blue-gray-50 bg-white p-3 font-sans text-sm font-normal text-blue-gray-500 shadow-lg shadow-blue-gray-500/10 focus:outline-none transition-opacity duration-300 pointer-events-none opacity-0">
                            <form name="transmission" id="transmissionForm">
                                <li role="transitem" class="flex gap-2 block m-auto w-full cursor-pointer text-md select-none rounded-md px-3 pt-[9px] pb-2 text-start leading-tight transition-all hover:bg-blue-gray-50 hover:bg-opacity-80 hover:text-blue-gray-900 focus:bg-blue-gray-50 focus:bg-opacity-80 focus:text-blue-gray-900 active:bg-blue-gray-50 active:bg-opacity-80 active:text-blue-gray-900">
                                    <input type="checkbox" id="manual" name="transmission[]" value="manual">
                                    <label for="manual">
                                        Manual
                                    </label><br>
                                </li>
                                <li role="transitem" class="flex gap-2 block m-auto w-full cursor-pointer text-md select-none rounded-md px-3 pt-[9px] pb-2 text-start leading-tight transition-all hover:bg-blue-gray-50 hover:bg-opacity-80 hover:text-blue-gray-900 focus:bg-blue-gray-50 focus:bg-opacity-80 focus:text-blue-gray-900 active:bg-blue-gray-50 active:bg-opacity-80 active:text-blue-gray-900">
                                    <input type="checkbox" id="automatic" name="transmission[]" value="automatic">
                                    <label for="automatic">
                                        Automatic
                                    </label><br>
                                </li>
                            </form>
                        </ul>
                    </div>
                </div>

                <!-- Car Type -->
                <div>
                    <div>
                        <button data-ripple-light="true" data-popover-target="cartypemenu" class="justify-center items-center text-blue-500 flex drop-shadow-lg select-none rounded-full bg-white py-2 px-6 text-center align-middle font-sans text-sm font-bold shadow-md transition-all focus:opacity-[0.85] active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
                            <div>Car Type</div>
                            <div dir="auto" aria-hidden="true" class="css-901oao r-1awozwy r-6koalj r-13hce6t" style="color: rgb(1, 148, 243);"><svg width="24" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemChevronDown">
                                    <path d="M6 9L12 15L18 9" stroke="#0194f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                                </svg></div>
                        </button>
                        <ul role="menu" data-popover="cartypemenu" data-popover-placement="bottom" class="absolute z-10 min-w-[180px] overflow-auto rounded-md border border-blue-gray-50 bg-white p-3 font-sans text-sm font-normal text-blue-gray-500 shadow-lg shadow-blue-gray-500/10 focus:outline-none transition-opacity duration-300 pointer-events-none opacity-0">
                            <form name="cartype" id="cartypeForm">
                                <?php
                                    // Send to API get all car type
                                    // $ch = curl_init();
                                    // $url = "https://domain/carrental/cartype/lokasi/<int:id_lokasi>";
                                    // curl_setopt($ch, CURLOPT_URL, $url);
                                    // // Set options to return the response as a string
                                    // curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
                                    // $response = curl_exec($ch);
                                    // // Check for errors
                                    // if (curl_errno($ch)) {
                                    //     echo 'Error:' . curl_error($ch);
                                    // } else {
                                    //     // Parse the JSON response
                                    //     $data = json_decode($response, true);
                                    //     // Check if the JSON was parsed correctly
                                    //     if (json_last_error() === JSON_ERROR_NONE) {
                                    //         // Print the parsed data
                                    //         print_r($data);
                                    //     } else {
                                    //         echo 'Error parsing JSON: ' . json_last_error_msg();
                                    //     }
                                    // }
                                    // curl_close($ch);
                                    // foreach ($data as $key => $value) {
                                ?>
                                <!-- <li role="caritem" class="flex gap-2 block m-auto w-full cursor-pointer text-md select-none rounded-md px-3 pt-[9px] pb-2 text-start leading-tight transition-all hover:bg-blue-gray-50 hover:bg-opacity-80 hover:text-blue-gray-900 focus:bg-blue-gray-50 focus:bg-opacity-80 focus:text-blue-gray-900 active:bg-blue-gray-50 active:bg-opacity-80 active:text-blue-gray-900">
                                    <input type="checkbox" id="<?='' //$key ?>" name="cartype[]" value="<?='' //$key ?>">
                                    <label for="<?=''// $key ?>">
                                        <?=''// $key ?>
                                    </label><br>
                                </li> -->
                                <li role="caritem" class="flex gap-2 block m-auto w-full cursor-pointer text-md select-none rounded-md px-3 pt-[9px] pb-2 text-start leading-tight transition-all hover:bg-blue-gray-50 hover:bg-opacity-80 hover:text-blue-gray-900 focus:bg-blue-gray-50 focus:bg-opacity-80 focus:text-blue-gray-900 active:bg-blue-gray-50 active:bg-opacity-80 active:text-blue-gray-900">
                                    <input type="checkbox" id="car type 1" name="cartype[]" value="car type 1">
                                    <label for="car type 1">
                                        car type 1
                                    </label><br>
                                </li>
                                <?php
                                    //}
                                ?>
                            </form>
                        </ul>
                    </div>
                </div>

                <!-- Provider -->
                <div>
                    <div>
                        <button data-ripple-light="true" data-popover-target="providermenu" class="justify-center items-center text-blue-500 flex drop-shadow-lg select-none rounded-full bg-white py-2 px-6 text-center align-middle font-sans text-sm font-bold shadow-md transition-all focus:opacity-[0.85] active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
                            <div>Provider</div>
                            <div dir="auto" aria-hidden="true" class="css-901oao r-1awozwy r-6koalj r-13hce6t" style="color: rgb(1, 148, 243);"><svg width="24" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemChevronDown">
                                    <path d="M6 9L12 15L18 9" stroke="#0194f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                                </svg></div>
                        </button>
                        <ul role="menu" data-popover="providermenu" data-popover-placement="bottom" class="absolute z-10 min-w-[180px] overflow-auto rounded-md border border-blue-gray-50 bg-white p-3 font-sans text-sm font-normal text-blue-gray-500 shadow-lg shadow-blue-gray-500/10 focus:outline-none transition-opacity duration-300 pointer-events-none opacity-0">
                            <form name="provider" id="providerForm">
                                <?php
                                    // Send to API get all car type
                                    // $ch = curl_init();
                                    // $url = "https://domain/carrental/provider/lokasi/<int:id_lokasi>";
                                    // curl_setopt($ch, CURLOPT_URL, $url);
                                    // // Set options to return the response as a string
                                    // curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
                                    // $response = curl_exec($ch);
                                    // // Check for errors
                                    // if (curl_errno($ch)) {
                                    //     echo 'Error:' . curl_error($ch);
                                    // } else {
                                    //     // Parse the JSON response
                                    //     $data = json_decode($response, true);
                                    //     // Check if the JSON was parsed correctly
                                    //     if (json_last_error() === JSON_ERROR_NONE) {
                                    //         // Print the parsed data
                                    //         print_r($data);
                                    //     } else {
                                    //         echo 'Error parsing JSON: ' . json_last_error_msg();
                                    //     }
                                    // }
                                    // curl_close($ch);
                                    // foreach ($data as $d) {
                                ?>
                                <!-- <li role="provideritem" class="flex gap-2 block m-auto w-full cursor-pointer text-md select-none rounded-md px-3 pt-[9px] pb-2 text-start leading-tight transition-all hover:bg-blue-gray-50 hover:bg-opacity-80 hover:text-blue-gray-900 focus:bg-blue-gray-50 focus:bg-opacity-80 focus:text-blue-gray-900 active:bg-blue-gray-50 active:bg-opacity-80 active:text-blue-gray-900">
                                    <input type="checkbox" id="<?='' //$d['provider_id'] ?>" name="provider[]" value="<?='' //$d['provider_id'] ?>">
                                    <label for="<?='' //$d['provider_id'] ?>" class="w-full">
                                        <div class="flex gap-1 items-center justify-between">
                                            <div>
                                                <?='' //$d['provider_name'] ?>
                                            </div>
                                            <div class="flex">
                                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcBrandTraveloka">
                                                    <g clip-path="url(#clip0_5387_0)">
                                                        <path d="M15.9886 16.0268C15.9886 14.0528 18.3724 11.6204 19.4865 10.1939C21.5632 7.53787 24 5.00369 24 5.00369C24 5.00369 21.2666 5.31206 18.465 6.21272C16.7087 6.77652 15.0488 7.59063 13.3958 8.3995C13.3073 6.27545 13.4489 4.12079 13.5969 2C13.5969 2 9.56369 3.00599 8.26139 5.90024C7.5257 7.53724 8.72553 9.70817 9.01454 11.3204C9.14141 12.0365 8.74246 14.1024 7.52665 13.4945C7.0365 13.2401 6.22054 12.8296 5.52132 12.8223C5.03946 12.8223 4.69858 12.9923 4.41455 13.1339C4.16528 13.2582 3.90097 13.3748 3.61625 13.3698L0 12.6424C0 12.6424 2.36095 13.5555 4.25 14.5C5.22762 14.9888 5.75278 15.4971 6.25943 15.9874C6.78926 16.5002 7.29886 16.9934 8.28455 17.4243C10.2083 18.2631 13.0065 18.7688 15.5 19.5C18.0862 20.2674 20.0568 21.0384 20.6976 21.3836C20.4968 21.2735 20.4721 21.0343 20.5 21C20.553 20.9223 21.1995 21.1212 21.1995 21.1212C19.2753 20.2945 15.9478 18.5279 15.9886 16.0268Z" fill="#1BA0E2"></path>
                                                        <path d="M15.9887 16.0043C15.9886 16.0118 15.9886 16.0193 15.9886 16.0268C15.9783 16.6591 16.1833 17.2445 16.5265 17.7797C14.8854 15.6821 13.3292 9.05031 13.3973 8.3987L13.4263 8.3845C14.0737 8.0677 14.7223 7.75033 15.3774 7.44775C15.358 7.97928 15.2069 12.824 15.9887 16.0043Z" fill="#0F7EA6"></path>
                                                    </g>
                                                    <defs>
                                                        <clipPath id="clip0_5387_0">
                                                            <rect width="24" height="24" fill="white"></rect>
                                                        </clipPath>
                                                    </defs>
                                                </svg>
                                                <p class="font-semibold text-blue-500">
                                                    <?='' //$d['rating'] ?>
                                                </p>
                                            </div>
                                        </div>
                                    </label><br>
                                </li> -->
                                <li role="provideritem" class="flex gap-2 block m-auto w-full cursor-pointer text-md select-none rounded-md px-3 pt-[9px] pb-2 text-start leading-tight transition-all hover:bg-blue-gray-50 hover:bg-opacity-80 hover:text-blue-gray-900 focus:bg-blue-gray-50 focus:bg-opacity-80 focus:text-blue-gray-900 active:bg-blue-gray-50 active:bg-opacity-80 active:text-blue-gray-900">
                                    <input type="checkbox" id="Provider 1" name="provider[]" value="Provider 1">
                                    <label for="Provider 1" class="w-full">
                                        <div class="flex gap-1 items-center justify-between">
                                            <div>
                                                Provider 1
                                            </div>
                                            <div class="flex">
                                                <!-- icon burung -->
                                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcBrandTraveloka">
                                                    <g clip-path="url(#clip0_5387_0)">
                                                        <path d="M15.9886 16.0268C15.9886 14.0528 18.3724 11.6204 19.4865 10.1939C21.5632 7.53787 24 5.00369 24 5.00369C24 5.00369 21.2666 5.31206 18.465 6.21272C16.7087 6.77652 15.0488 7.59063 13.3958 8.3995C13.3073 6.27545 13.4489 4.12079 13.5969 2C13.5969 2 9.56369 3.00599 8.26139 5.90024C7.5257 7.53724 8.72553 9.70817 9.01454 11.3204C9.14141 12.0365 8.74246 14.1024 7.52665 13.4945C7.0365 13.2401 6.22054 12.8296 5.52132 12.8223C5.03946 12.8223 4.69858 12.9923 4.41455 13.1339C4.16528 13.2582 3.90097 13.3748 3.61625 13.3698L0 12.6424C0 12.6424 2.36095 13.5555 4.25 14.5C5.22762 14.9888 5.75278 15.4971 6.25943 15.9874C6.78926 16.5002 7.29886 16.9934 8.28455 17.4243C10.2083 18.2631 13.0065 18.7688 15.5 19.5C18.0862 20.2674 20.0568 21.0384 20.6976 21.3836C20.4968 21.2735 20.4721 21.0343 20.5 21C20.553 20.9223 21.1995 21.1212 21.1995 21.1212C19.2753 20.2945 15.9478 18.5279 15.9886 16.0268Z" fill="#1BA0E2"></path>
                                                        <path d="M15.9887 16.0043C15.9886 16.0118 15.9886 16.0193 15.9886 16.0268C15.9783 16.6591 16.1833 17.2445 16.5265 17.7797C14.8854 15.6821 13.3292 9.05031 13.3973 8.3987L13.4263 8.3845C14.0737 8.0677 14.7223 7.75033 15.3774 7.44775C15.358 7.97928 15.2069 12.824 15.9887 16.0043Z" fill="#0F7EA6"></path>
                                                    </g>
                                                    <defs>
                                                        <clipPath id="clip0_5387_0">
                                                            <rect width="24" height="24" fill="white"></rect>
                                                        </clipPath>
                                                    </defs>
                                                </svg>
                                                <p class="font-semibold text-blue-500">10.0</p>
                                            </div>
                                        </div>
                                    </label><br>
                                </li>
                                <?php
                                    //}
                                ?>
                            </form>
                        </ul>
                    </div>
                </div>

            </div>

            <!-- sort -->
            <div>
                <button data-ripple-light="true" data-popover-target="menu" class="justify-center items-center text-blue-500 flex drop-shadow-lg select-none rounded-full bg-white py-2 px-6 text-center align-middle font-sans text-sm font-bold shadow-md transition-all focus:opacity-[0.85] active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
                    <div>Sort</div>
                    <div dir="auto" aria-hidden="true" class="css-901oao r-1awozwy r-6koalj r-13hce6t" style="color: rgb(1, 148, 243);"><svg width="24" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemChevronDown">
                            <path d="M6 9L12 15L18 9" stroke="#0194f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                        </svg></div>
                </button>
                <ul role="menu" data-popover="menu" data-popover-placement="bottom" class="absolute z-10 min-w-[180px] overflow-auto rounded-md border border-blue-gray-50 bg-white p-3 font-sans text-sm font-normal text-blue-gray-500 shadow-lg shadow-blue-gray-500/10 focus:outline-none transition-opacity duration-300 pointer-events-none opacity-0">
                    <form name="sort" id="sortForm">
                        <li role="menuitem" class="block m-auto w-full cursor-pointer text-md select-none rounded-md px-3 pt-[9px] pb-2 text-start leading-tight transition-all hover:bg-blue-gray-50 hover:bg-opacity-80 hover:text-blue-gray-900 focus:bg-blue-gray-50 focus:bg-opacity-80 focus:text-blue-gray-900 active:bg-blue-gray-50 active:bg-opacity-80 active:text-blue-gray-900">
                            <input type="radio" id="lowestprice" name="sort" value="lowestprice">
                            <label for="lowestprice">Lowest Price</label><br>
                        </li>
                        <li role="menuitem" class="block m-auto w-full cursor-pointer text-md select-none rounded-md px-3 pt-[9px] pb-2 text-start leading-tight transition-all hover:bg-blue-gray-50 hover:bg-opacity-80 hover:text-blue-gray-900 focus:bg-blue-gray-50 focus:bg-opacity-80 focus:text-blue-gray-900 active:bg-blue-gray-50 active:bg-opacity-80 active:text-blue-gray-900">
                            <input type="radio" id="lowestprice" name="sort" value="highestprice">
                            <label for="lowestprice">Highest Price</label><br>
                        </li>
                        <li role="menuitem" class="block m-auto w-full cursor-pointer text-md select-none rounded-md px-3 pt-[9px] pb-2 text-start leading-tight transition-all hover:bg-blue-gray-50 hover:bg-opacity-80 hover:text-blue-gray-900 focus:bg-blue-gray-50 focus:bg-opacity-80 focus:text-blue-gray-900 active:bg-blue-gray-50 active:bg-opacity-80 active:text-blue-gray-900">
                            <input type="radio" id="lowestprice" name="sort" value="lowestcapacity">
                            <label for="lowestprice">Lowest Capacity</label><br>
                        </li>
                        <li role="menuitem" class="block m-auto w-full cursor-pointer text-md select-none rounded-md px-3 pt-[9px] pb-2 text-start leading-tight transition-all hover:bg-blue-gray-50 hover:bg-opacity-80 hover:text-blue-gray-900 focus:bg-blue-gray-50 focus:bg-opacity-80 focus:text-blue-gray-900 active:bg-blue-gray-50 active:bg-opacity-80 active:text-blue-gray-900">
                            <input type="radio" id="reviewscore" name="sort" value="highestcapacity">
                            <label for="reviewscore">Highest Capacity</label><br>
                        </li>
                    </form>
                </ul>
            </div>
        </div>
        <br><br>
        <!-- cars Items -->
        <div class="carsList">
            <div class="carsCard cursor-pointer hover:shadow-sky-200 hover:shadow-lg w-full h-56 rounded-md flex custom-shadow-card overflow-hidden">
                <div class="w-1/4 overflow-hidden	relative">
                    <img class="object-contain h-56 w-full" importance="low" loading="lazy" src="https://ik.imagekit.io/tvlk/image/imageResource/2023/06/29/1688042794913-9ef77485d4831ee86faedff5521d77b6.jpeg?tr=q-75,w-140" srcset="https://ik.imagekit.io/tvlk/image/imageResource/2023/06/29/1688042794913-9ef77485d4831ee86faedff5521d77b6.jpeg?tr=q-75,w-140 1x, https://ik.imagekit.io/tvlk/image/imageResource/2023/06/29/1688042794913-9ef77485d4831ee86faedff5521d77b6.jpeg?tr=dpr-2,q-75,w-140 2x, https://ik.imagekit.io/tvlk/image/imageResource/2023/06/29/1688042794913-9ef77485d4831ee86faedff5521d77b6.jpeg?tr=dpr-3,q-75,w-140 3x" decoding="async">
                </div>
                <div class="w-3/4 flex">
                    <!-- cars Description -->
                    <div class="w-2/3 py-2 px-3">
                        <div class="w-full">
                            <h1 class="font-bold text-lg">Toyota Agya</h1>
                        </div>
                        <div class="flex mt-4 items-center justify-start gap-2">
                            <svg width="14" height="14" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M6 0C2.6865 0 0 2.6865 0 6C0 9.3135 2.6865 12 6 12C9.3135 12 12 9.3135 12 6C12 2.6865 9.3135 0 6 0ZM6 1.5C7.9643 1.5 9.6234 2.75775 10.25 4.5H1.75C2.3766 2.75775 4.0357 1.5 6 1.5ZM5.25 6.25C5.25 6.66437 5.58563 7 6 7C6.41437 7 6.75 6.66437 6.75 6.25C6.75 5.83563 6.41437 5.5 6 5.5C5.58563 5.5 5.25 5.83563 5.25 6.25ZM1.5 6C3.55266 6 5.21507 8.00873 5.25 10.5C3.1256 10.1304 1.5 8.26049 1.5 6ZM6.75601 10.5C6.79094 8.00873 8.45335 6 10.506 6C10.506 8.26049 8.88041 10.1304 6.75601 10.5Z" fill="#687176"></path></svg>
                            <p>Manual</p>
                        </div>
                        <div class="flex mt-2 items-center justify-start gap-2">
                            <div class="flex gap-2 items-center">
                                <svg width="16" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcBagBaggageFill"><path fill-rule="evenodd" clip-rule="evenodd" d="M3.5 7C2.11929 7 1 8.11929 1 9.5V18.5C1 19.8807 2.11929 21 3.5 21H20.5C21.8807 21 23 19.8807 23 18.5V9.5C23 8.11929 21.8807 7 20.5 7H17V6C17 4.34315 15.6569 3 14 3H10C8.34315 3 7 4.34315 7 6V7H3.5ZM10 5C9.44772 5 9 5.44772 9 6V7H15V6C15 5.44772 14.5523 5 14 5H10ZM5 10C5 9.44772 5.44772 9 6 9C6.55228 9 7 9.44772 7 10V18C7 18.5523 6.55228 19 6 19C5.44772 19 5 18.5523 5 18V10ZM18 9C17.4477 9 17 9.44772 17 10V18C17 18.5523 17.4477 19 18 19C18.5523 19 19 18.5523 19 18V10C19 9.44772 18.5523 9 18 9Z" fill="#0194f3"></path></svg>
                                <p>2 baggages</p>
                            </div>
                            <div class="flex gap-2 items-center">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-id="IcTransportSeatClassFill16"><g fill="none" fill-rule="evenodd"><rect width="16" height="16"></rect><path fill="#0194F3" d="M5,13 L13,13 C13.5522847,13 14,13.4477153 14,14 C14,14.5522847 13.5522847,15 13,15 L5,15 C4.44771525,15 4,14.5522847 4,14 C4,13.4477153 4.44771525,13 5,13 Z M5.50372906,12 C4.05387063,12 2.81147789,10.9631284 2.55211933,9.53665631 L1.40249224,3.2137073 C1.38234043,3.10287235 1.3722032,2.99044883 1.3722032,2.8777968 C1.3722032,1.84071826 2.21292147,1 3.25,1 C4.57234041,1 5.7249905,1.89996199 6.04570516,3.18282063 L6.81063391,6.24253563 C6.92192566,6.68770263 7.32190876,7 7.78077641,7 L11.9586889,7 C12.6113165,7 13.2228954,7.31842196 13.5971527,7.85307531 L14.75,9.5 C14.936942,9.76705999 15.0372139,10.085159 15.0372139,10.4111472 C15.0372139,11.2886464 14.3258602,12 13.4483611,12 L5.50372906,12 Z"></path><rect width="5" height="2" x="8" y="4" fill="#0194f3" fill-rule="nonzero" rx="1"></rect></g></svg>
                                <p>4 seats</p>
                            </div>
                        </div>
                        <div class="flex mt-16 gap-2 items-center">
                            <div>Without Driver</div>
                            <div class="text-blue-500">2 providers available</div>
                        </div>
                    </div>
                    <div class="w-1/3 flex flex-col justify-center items-center gap-5 shadow">
                        <div>
                            <h2 class="text-sm text-end text-gray-400">From</h2>
                            <h1 class="font-semibold text-xl text-orange-700">Rp. 200.000 <span class="text-sm text-gray-400 font-normal">/day</span></h1>
                        </div>
                        <button class="py-2 px-4 text-sm rounded bg-orange-600 hover:bg-orange-700 text-white font-semibold">Continue</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Jquery -->
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <!-- Tailwind Materials -->
    <script src="https://unpkg.com/@material-tailwind/html@latest/scripts/script-name.js"></script>
    <script type="module" src="https://unpkg.com/@material-tailwind/html@latest/scripts/popover.js"></script>


    <!-- <script>
        $(document).ready(function() {
            // Initialize TW Elements
            window['tw-elements'].init();
        });
    </script> -->
</body>

</html>