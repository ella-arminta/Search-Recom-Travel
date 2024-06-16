<!doctype html>
<html>

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Attractions</title>

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

    .price-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            max-width: 200px;
            margin: auto;
        }
        .price-text {
            text-align: end;
            color: gray;
        }
        .original-price {
            text-decoration: line-through;
            color: darkgrey;
            margin-top: 10px;
          
        }
        .discounted-price {
            color: rgba(255, 94, 31, 1.00);
            font-weight: bold;
        }
        .find-tickets {
            padding: 10px 20px;
            background-color: rgba(255, 94, 31, 1.00);
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .find-tickets:hover {
            background-color: rgba(255, 74, 11, 1.00);
        }
</style>

<body class="">
    <!-- default search -->
    <div class="w-full bg-gradient-custom-blue p-2 px-5 text-white shadow-lg">
        <div class="flex justify-center items-center gap-5">
            <h1 class="text-lg font-semibold">Attractions</h1>
            <div class="rounded w-full backdrop-blur-sm bg-white/30 p-2 flex justify-center items-center gap-3 text-sm font-semibold">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemCalendar">
                <path d="M14,4a1,1,0,0,1,1-1h2a1,1,0,0,1,0,2H15A1,1,0,0,1,14,4Zm11,6h2a1,1,0,0,0,0-2H25a1,1,0,0,0,0,2Zm2,7h2a1,1,0,0,0,0-2H27a1,1,0,0,0,0,2ZM5,15H3a1,1,0,0,0,0,2H5a1,1,0,0,0,0-2Zm0-5H7A1,1,0,0,0,7,8H5a1,1,0,0,0,0,2ZM30,29a1,1,0,0,1-1,1H3a1,1,0,0,1,0-2H6.48l3-4.4c-.19-.16-.37-.32-.54-.49A1,1,0,0,1,8,24H6a1,1,0,0,1,0-2H8a10,10,0,1,1,16,0h2a1,1,0,0,1,0,2H24a1,1,0,0,1-1-.89c-.17.17-.35.33-.54.49l3,4.4H29A1,1,0,0,1,30,29ZM15,23.93V19.2l-2.69,3.89A7.9,7.9,0,0,0,15,23.93ZM8.07,15h5.52l-3.9-3.9A7.94,7.94,0,0,0,8.07,15Zm14.24-3.9L18.41,15h5.52A7.94,7.94,0,0,0,22.31,11.1ZM20.9,9.69A7.94,7.94,0,0,0,17,8.07v5.52ZM15,8.07a7.94,7.94,0,0,0-3.9,1.62l3.9,3.9Zm2,15.86a7.9,7.9,0,0,0,2.69-.84L17,19.2Zm4.33-2A8,8,0,0,0,23.93,17h-6ZM10.67,22,14.09,17h-6A8,8,0,0,0,10.67,22ZM8.91,28H23.09l-2.25-3.25a10,10,0,0,1-9.68,0Z" fill="#FFFFFF"/>
                </svg>
                Jatim Park 1</div>
            <div class="rounded w-full backdrop-blur-sm bg-white/30 p-2 flex justify-center items-center gap-3 text-sm font-semibold"><svg width="16" height="16" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemMapLocationFill12">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M6 12C6 12 10.5 8.5 10.5 5.5C10.5 2.73858 8.76142 0.5 6 0.5C3.23858 0.5 1.5 2.73858 1.5 5.5C1.5 8.5 6 12 6 12ZM6 7C7.10457 7 8 6.10457 8 5C8 3.89543 7.10457 3 6 3C4.89543 3 4 3.89543 4 5C4 6.10457 4.89543 7 6 7Z" fill="#FFFFFF"></path>
                </svg>
                Batu, Malang</div>
            <div class="rounded w-full backdrop-blur-sm bg-white/30 p-2 flex justify-center items-center gap-3 text-sm font-semibold"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemCalendar">
                    <path d="M7 2V5M17 2V5M3 8H21M11.5 11.5H12.5V12.5H11.5V11.5ZM11.5 16.5H12.5V17.5H11.5V16.5ZM16.5 11.5H17.5V12.5H16.5V11.5ZM6.5 16.5H7.5V17.5H6.5V16.5ZM5 21H19C20.1046 21 21 20.1046 21 19V6C21 4.89543 20.1046 4 19 4H5C3.89543 4 3 4.89543 3 6V19C3 20.1046 3.89543 21 5 21Z" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M7.5 11.5V12.5H6.5V11.5H7.5Z" stroke="#0194F3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                </svg>
                15 Juni 2024</div>
        </div>
    </div>
    <!-- back button -->
    <div class="back-button absolute top-20 cursor-pointer text-gray-400 left-10">
        <a href="searchatraksi.php">
            <i class="fa-solid fa-arrow-left"></i>
        </a>
    </div>
    <!-- container -->
    <div class="w-3/4 m-auto mt-5">
        <!-- filters option -->
        <div class="flex justify-between items-center">
            <div class="flex gap-3 items-center">
                <!-- Price -->
                <div class="text-blue-500 justify-center gap-3 items-center flex drop-shadow-lg select-none rounded-full bg-white py-1 px-6 text-center align-middle font-sans text-sm font-bold shadow-md transition-all focus:opacity-[0.85] active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
                    
                    <!-- Minprice -->
                    <div class="flex  justify-center items-center gap-1">
                        <p class="text-md">Min</p>
                        <input name="minprice" id="minprice" type="number" class="text-gray-500 border w-32 p-1 rounded" min="0" placeholder="min price">
                    </div>
                    <!-- maxprice -->
                    <div class="flex justify-center items-center gap-1">
                        <p class="text-md">Max</p>
                        <input name="maxprice" id="maxprice" type="number" class="text-gray-500 border w-32 p-1 rounded" placeholder="max price">
                    </div>
                </div>

                <!-- Rating -->
                <div>
                    <!-- rating -->
                    <div>
                        <button data-ripple-light="true" data-popover-target="ratingmenu" class="justify-center items-center text-blue-500 flex drop-shadow-lg select-none rounded-full bg-white py-2 px-6 text-center align-middle font-sans text-sm font-bold shadow-md transition-all focus:opacity-[0.85] active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
                            <div>Rating Score</div>
                            <div dir="auto" aria-hidden="true" class="css-901oao r-1awozwy r-6koalj r-13hce6t" style="color: rgb(1, 148, 243);"><svg width="24" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemChevronDown">
                                    <path d="M6 9L12 15L18 9" stroke="#0194f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                                </svg></div>
                        </button>
                        <ul role="menu" data-popover="ratingmenu" data-popover-placement="bottom" class="absolute z-10 min-w-[180px] overflow-auto rounded-md border border-blue-gray-50 bg-white p-3 font-sans text-sm font-normal text-blue-gray-500 shadow-lg shadow-blue-gray-500/10 focus:outline-none transition-opacity duration-300 pointer-events-none opacity-0">
                            <form name="rating" id="ratingForm">
                                <?php
                                for ($i = 5; $i >= 1; $i--) {
                                    $stars = '';
                                    $num = 5.0;
                                    for ($j = 0; $j < $i; $j++) {
                                        $num = $num + 1;
                                    }
                                    $stars .= '<img class="mr-2" src="https://i.pinimg.com/originals/d5/da/ee/d5daeeaca986fb2655a4965884c0d6ea.png" width="16" height="16">';
                                ?>
                                    <li role="menuitem" class=" font-semibold text-blue-500 flex gap-2 block m-auto w-full cursor-pointer text-md select-none rounded-md px-3 pt-[9px] pb-2 text-start leading-tight transition-all hover:bg-blue-gray-50 hover:bg-opacity-80 hover:text-blue-gray-900 focus:bg-blue-gray-50 focus:bg-opacity-80 focus:text-blue-gray-900 active:bg-blue-gray-50 active:bg-opacity-80 active:text-blue-gray-900">
                                        <input type="checkbox" id="star<?= '-' .  $i ?>" name="rating[]" value="<?= $i ?>">
                                        <label for="star<?= '-'  .$i ?>">
                                            <div class="flex">
                                                <?= $num . $stars ?>
                                            </div>
                                        </label><br>
                                    </li>
                                <?php
                                }
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
                    </form>
                </ul>
            </div>
        </div>
        <br><br>
        <!-- Attractions Items -->
        <div class="attractionList">

            <!-- Jatim Park 1 -->
            <div class="hotelCard cursor-pointer hover:shadow-sky-200 hover:shadow-lg w-full h-56 rounded-md flex custom-shadow-card overflow-hidden">
                <div class="w-1/3 overflow-hidden	relative ">
                    <img class="object-cover h-56 w-full" src="https://ik.imagekit.io/tvlk/xpe-asset/AyJ40ZAo1DOyPyKLZ9c3RGQHTP2oT4ZXW+QmPVVkFQiXFSv42UaHGzSmaSzQ8DO5QIbWPZuF+VkYVRk6gh-Vg4ECbfuQRQ4pHjWJ5Rmbtkk=/2000625477092/Tiket-Jatim-Park-1-02d29f75-a2d0-45e0-a739-ba21235a1ffa.jpeg?_src=imagekit&tr=dpr-2,c-at_max,h-750,q-100,w-1000" alt="attraction">
                </div>
                
                <div class="w-2/3 flex "> 
                    <!-- Attraction Description -->
                    <div class="w-2/3 py-2 px-3">
                        <div class="flex justify-between items-start">
                            <div class="w-4/5">
                                <div class="flex mt-4 ml-3 items-center justify-start gap-2" >
                                    <!-- Icon location -->
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemMapLocationFill">
                                        <path fill-rule="evenodd" clip-rule="evenodd" d="M21 10C21 7.25554 20.0331 4.98482 18.3787 3.40236C16.7312 1.8265 14.4725 1 12 1C9.52754 1 7.26876 1.8265 5.62128 3.40236C3.96688 4.98482 3 7.25554 3 10C3 13.4069 5.24119 16.5278 7.2718 18.6854C8.31023 19.7887 9.34524 20.694 10.1194 21.323C10.5073 21.6381 10.8316 21.8855 11.0609 22.0554C11.0795 22.0692 11.0982 22.0831 11.1169 22.0971C11.3805 22.2937 11.6567 22.4998 12 22.4998C12.3432 22.4999 12.6194 22.2938 12.8829 22.0972C12.9017 22.0832 12.9205 22.0692 12.9391 22.0554C13.1684 21.8855 13.4927 21.6381 13.8806 21.323C14.6548 20.694 15.6898 19.7887 16.7282 18.6854C18.7588 16.5278 21 13.4069 21 10ZM15.5 9.5C15.5 11.433 13.933 13 12 13C10.067 13 8.5 11.433 8.5 9.5C8.5 7.567 10.067 6 12 6C13.933 6 15.5 7.567 15.5 9.5Z" fill="#687176"></path>
                                    </svg>
                                    <p>Oro-Oro Ombo</p>
                                </div>
                                <h1 class="font-bold text-lg mt-4 ml-4">Jatim Park 1 Tickets </h1>
                            </div>
                            <div class="w-1/5 flex items-center gap-2 pr-1 mt-1 justify-end">
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
                                <p class="font-semibold text-blue-500">8.0</p>
                            </div>
                        </div>
                        
                    </div>
                    <div class="w-1/3 flex flex-col justify-center items-center gap-5 shadow">
                        <div>
                            <h2 class="text-sm text-end text-darkgray-400 ">Starts From</h2>
                            <div class="original-price text-medium">Rp. 125.000</div>
                            <h1 class="font-semibold text-xl text-orange-700">Rp. 123.750</h1>
                        </div>
                        <button class="py-2 px-4 text-sm rounded bg-orange-600 hover:bg-orange-700 text-white font-semibold">Find Tickets</button>
                    </div>
                </div>
            </div>

            <!-- Jatim Park 2 -->
            <div class="hotelCard cursor-pointer hover:shadow-sky-200 hover:shadow-lg w-full h-56 rounded-md flex custom-shadow-card overflow-hidden mt-4">
                <div class="w-1/3 overflow-hidden	relative ">
                    <img class="object-cover h-56 w-full" src="https://ik.imagekit.io/tvlk/xpe-asset/AyJ40ZAo1DOyPyKLZ9c3RGQHTP2oT4ZXW+QmPVVkFQiXFSv42UaHGzSmaSzQ8DO5QIbWPZuF+VkYVRk6gh-Vg4ECbfuQRQ4pHjWJ5Rmbtkk=/2000625477100/Tiket-Jatim-Park-2-%2528Batu-Secret-Zoo-Museum-Satwa%2529-df359f63-f5f0-446b-8f57-f7e811500b19.jpeg?_src=imagekit&tr=dpr-2,c-at_max,h-750,q-100,w-1000" alt="attraction">
                </div>
                
                <div class="w-2/3 flex "> 
                    <!-- Attraction Description -->
                    <div class="w-2/3 py-2 px-3">
                        <div class="flex justify-between items-start">
                            <div class="w-4/5">
                                <div class="flex mt-4 ml-3 items-center justify-start gap-2" >
                                    <!-- Icon location -->
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemMapLocationFill">
                                        <path fill-rule="evenodd" clip-rule="evenodd" d="M21 10C21 7.25554 20.0331 4.98482 18.3787 3.40236C16.7312 1.8265 14.4725 1 12 1C9.52754 1 7.26876 1.8265 5.62128 3.40236C3.96688 4.98482 3 7.25554 3 10C3 13.4069 5.24119 16.5278 7.2718 18.6854C8.31023 19.7887 9.34524 20.694 10.1194 21.323C10.5073 21.6381 10.8316 21.8855 11.0609 22.0554C11.0795 22.0692 11.0982 22.0831 11.1169 22.0971C11.3805 22.2937 11.6567 22.4998 12 22.4998C12.3432 22.4999 12.6194 22.2938 12.8829 22.0972C12.9017 22.0832 12.9205 22.0692 12.9391 22.0554C13.1684 21.8855 13.4927 21.6381 13.8806 21.323C14.6548 20.694 15.6898 19.7887 16.7282 18.6854C18.7588 16.5278 21 13.4069 21 10ZM15.5 9.5C15.5 11.433 13.933 13 12 13C10.067 13 8.5 11.433 8.5 9.5C8.5 7.567 10.067 6 12 6C13.933 6 15.5 7.567 15.5 9.5Z" fill="#687176"></path>
                                    </svg>
                                    <p>Oro-Oro Ombo</p>
                                </div>
                                <h1 class="font-bold text-lg mt-4 ml-4">Jatim Park 2 Tickets (Batu Secret Zoo & Museum Satwa)</h1>
                            </div>
                            <div class="w-1/5 flex items-center gap-2 pr-1 mt-1 justify-end">
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
                                <p class="font-semibold text-blue-500">9.0</p>
                            </div>
                        </div>
                        
                    </div>
                    <div class="w-1/3 flex flex-col justify-center items-center gap-5 shadow">
                        <div>
                            <h2 class="text-sm text-end text-darkgray-400 ">Starts From</h2>
                            <div class="original-price text-medium">Rp. 140.000</div>
                            <h1 class="font-semibold text-xl text-orange-700">Rp. 138.600</h1>
                        </div>
                        <button class="py-2 px-4 text-sm rounded bg-orange-600 hover:bg-orange-700 text-white font-semibold">Find Tickets</button>
                    </div>
                </div>
            </div>

            <!-- BNS -->
            <div class="hotelCard cursor-pointer hover:shadow-sky-200 hover:shadow-lg w-full h-56 rounded-md flex custom-shadow-card overflow-hidden mt-4">
                <div class="w-1/3 overflow-hidden	relative ">
                    <img class="object-cover h-56 w-full" src="https://ik.imagekit.io/tvlk/xpe-asset/AyJ40ZAo1DOyPyKLZ9c3RGQHTP2oT4ZXW+QmPVVkFQiXFSv42UaHGzSmaSzQ8DO5QIbWPZuF+VkYVRk6gh-Vg4ECbfuQRQ4pHjWJ5Rmbtkk=/2000625477069/Batu-Night-Spectacular-%2528BNS%2529-Tickets-%2528Jatim-Park-Group%2529-1d832435-a006-4124-9223-df348f409e4f.jpeg?_src=imagekit&tr=dpr-2,c-at_max,h-750,q-100,w-1000" alt="attraction">
                </div>
                
                <div class="w-2/3 flex "> 
                    <!-- Attraction Description -->
                    <div class="w-2/3 py-2 px-3">
                        <div class="flex justify-between items-start">
                            <div class="w-4/5">
                                <div class="flex mt-4 ml-3 items-center justify-start gap-2" >
                                    <!-- Icon location -->
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemMapLocationFill">
                                        <path fill-rule="evenodd" clip-rule="evenodd" d="M21 10C21 7.25554 20.0331 4.98482 18.3787 3.40236C16.7312 1.8265 14.4725 1 12 1C9.52754 1 7.26876 1.8265 5.62128 3.40236C3.96688 4.98482 3 7.25554 3 10C3 13.4069 5.24119 16.5278 7.2718 18.6854C8.31023 19.7887 9.34524 20.694 10.1194 21.323C10.5073 21.6381 10.8316 21.8855 11.0609 22.0554C11.0795 22.0692 11.0982 22.0831 11.1169 22.0971C11.3805 22.2937 11.6567 22.4998 12 22.4998C12.3432 22.4999 12.6194 22.2938 12.8829 22.0972C12.9017 22.0832 12.9205 22.0692 12.9391 22.0554C13.1684 21.8855 13.4927 21.6381 13.8806 21.323C14.6548 20.694 15.6898 19.7887 16.7282 18.6854C18.7588 16.5278 21 13.4069 21 10ZM15.5 9.5C15.5 11.433 13.933 13 12 13C10.067 13 8.5 11.433 8.5 9.5C8.5 7.567 10.067 6 12 6C13.933 6 15.5 7.567 15.5 9.5Z" fill="#687176"></path>
                                    </svg>
                                    <p>Oro-Oro Ombo</p>
                                </div>
                                <h1 class="font-bold text-lg mt-4 ml-4">Batu Night Spectacular (BNS) Tickets (Jatim Park Group)</h1>
                            </div>
                            <div class="w-1/5 flex items-center gap-2 pr-1 mt-1 justify-end">
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
                        
                    </div>
                    <div class="w-1/3 flex flex-col justify-center items-center gap-5 shadow">
                        <div>
                            <h2 class="text-sm text-end text-darkgray-400 ">Starts From</h2>
                            <div class="original-price text-medium">Rp. 115.000</div>
                            <h1 class="font-semibold text-xl text-orange-700">Rp. 105.000</h1>
                        </div>
                        <button class="py-2 px-4 text-sm rounded bg-orange-600 hover:bg-orange-700 text-white font-semibold">Find Tickets</button>
                    </div>
                </div>
            </div>

            <!-- Eco Green Park -->
            <div class="hotelCard cursor-pointer hover:shadow-sky-200 hover:shadow-lg w-full h-56 rounded-md flex custom-shadow-card overflow-hidden mt-4 mb-4">
                <div class="w-1/3 overflow-hidden	relative ">
                    <img class="object-cover h-56 w-full" src="https://ik.imagekit.io/tvlk/xpe-asset/AyJ40ZAo1DOyPyKLZ9c3RGQHTP2oT4ZXW+QmPVVkFQiXFSv42UaHGzSmaSzQ8DO5QIbWPZuF+VkYVRk6gh-Vg4ECbfuQRQ4pHjWJ5Rmbtkk=/2000625477094/Eco-Green-Park-Tickets-%2528Jatim-Park-Group%2529-71cf91e0-7e71-4816-8113-92d684f28ee3.jpeg?_src=imagekit&tr=dpr-2,c-at_max,h-750,q-100,w-1000" alt="attraction">
                </div>
                
                <div class="w-2/3 flex "> 
                    <!-- Attraction Description -->
                    <div class="w-2/3 py-2 px-3">
                        <div class="flex justify-between items-start">
                            <div class="w-4/5">
                                <div class="flex mt-4 ml-3 items-center justify-start gap-2" >
                                    <!-- Icon location -->
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemMapLocationFill">
                                        <path fill-rule="evenodd" clip-rule="evenodd" d="M21 10C21 7.25554 20.0331 4.98482 18.3787 3.40236C16.7312 1.8265 14.4725 1 12 1C9.52754 1 7.26876 1.8265 5.62128 3.40236C3.96688 4.98482 3 7.25554 3 10C3 13.4069 5.24119 16.5278 7.2718 18.6854C8.31023 19.7887 9.34524 20.694 10.1194 21.323C10.5073 21.6381 10.8316 21.8855 11.0609 22.0554C11.0795 22.0692 11.0982 22.0831 11.1169 22.0971C11.3805 22.2937 11.6567 22.4998 12 22.4998C12.3432 22.4999 12.6194 22.2938 12.8829 22.0972C12.9017 22.0832 12.9205 22.0692 12.9391 22.0554C13.1684 21.8855 13.4927 21.6381 13.8806 21.323C14.6548 20.694 15.6898 19.7887 16.7282 18.6854C18.7588 16.5278 21 13.4069 21 10ZM15.5 9.5C15.5 11.433 13.933 13 12 13C10.067 13 8.5 11.433 8.5 9.5C8.5 7.567 10.067 6 12 6C13.933 6 15.5 7.567 15.5 9.5Z" fill="#687176"></path>
                                    </svg>
                                    <p>Oro-Oro Ombo</p>
                                </div>
                                <h1 class="font-bold text-lg mt-4 ml-4">Eco Green Park Tickets (Jatim Park Group)</h1>
                            </div>
                            <div class="w-1/5 flex items-center gap-2 pr-1 mt-1 justify-end">
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
                                <p class="font-semibold text-blue-500">7.0</p>
                            </div>
                        </div>
                        
                    </div>
                    <div class="w-1/3 flex flex-col justify-center items-center gap-5 shadow">
                        <div>
                            <h2 class="text-sm text-end text-darkgray-400 ">Starts From</h2>
                            <div class="original-price text-medium">Rp. 70.000</div>
                            <h1 class="font-semibold text-xl text-orange-700">Rp. 65.000</h1>
                        </div>
                        <button class="py-2 px-4 text-sm rounded bg-orange-600 hover:bg-orange-700 text-white font-semibold">Find Tickets</button>
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