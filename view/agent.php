<!doctype html>
<html>

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Package Tours</title>

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
            <h1 class="text-lg font-semibold">Tours</h1>
            <div class="rounded w-full backdrop-blur-sm bg-white/30 p-2 flex justify-center items-center gap-3 text-sm font-semibold"><svg width="16" height="16" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemMapLocationFill12">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M6 12C6 12 10.5 8.5 10.5 5.5C10.5 2.73858 8.76142 0.5 6 0.5C3.23858 0.5 1.5 2.73858 1.5 5.5C1.5 8.5 6 12 6 12ZM6 7C7.10457 7 8 6.10457 8 5C8 3.89543 7.10457 3 6 3C4.89543 3 4 3.89543 4 5C4 6.10457 4.89543 7 6 7Z" fill="#FFFFFF"></path>
                </svg>
                Bali</div>
            <div class="rounded w-full backdrop-blur-sm bg-white/30 p-2 flex justify-center items-center gap-3 text-sm font-semibold"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemCalendar">
                    <path d="M7 2V5M17 2V5M3 8H21M11.5 11.5H12.5V12.5H11.5V11.5ZM11.5 16.5H12.5V17.5H11.5V16.5ZM16.5 11.5H17.5V12.5H16.5V11.5ZM6.5 16.5H7.5V17.5H6.5V16.5ZM6.5 11.5H7.5V12.5H6.5V11.5ZM16.5 16.5H17.5V17.5H16.5V16.5ZM3 22H21V8H3V22Z" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                </svg>
                15 June - 21 June 2024</div>
            <div class="rounded w-full backdrop-blur-sm bg-white/30 p-2 flex justify-center items-center gap-3 text-sm font-semibold">
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemGroupOfPeople">
                    <path d="M8 8C9.65685 8 11 6.65685 11 5C11 3.34315 9.65685 2 8 2C6.34315 2 5 3.34315 5 5C5 6.65685 6.34315 8 8 8ZM8 9C5.87827 9 4.06849 10.0044 3 11.5147C3 13.5228 5.68629 14.5 8 14.5C10.3137 14.5 13 13.5228 13 11.5147C11.9315 10.0044 10.1217 9 8 9Z" fill="#FFFFFF"/>
                </svg>
                2 Visitors</div>
        </div>
    </div>
    <!-- back button -->
    <div class="back-button absolute top-20 cursor-pointer text-gray-400 left-10">
        <a href="searchagent.php">
            <i class="fa-solid fa-arrow-left"></i>
        </a>
    </div>
    <!-- container -->
    <div class=" w-3/4 m-auto mt-5">
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

        <div class="attractionList flex flex-wrap">
            <!-- Gili Trawangan Tour -->
            <div class="w-full md:w-1/3 p-2">
                <div class="relative overflow-hidden" style="padding-top: 100%;">
                    <img class="absolute inset-0 w-full h-full object-cover" src="https://ik.imagekit.io/tvlk/xpe-asset/AyJ40ZAo1DOyPyKLZ9c3RGQHTP2oT4ZXW+QmPVVkFQiXFSv42UaHGzSmaSzQ8DO5QIbWPZuF+VkYVRk6gh-Vg4ECbfuQRQ4pHjWJ5Rmbtkk=/8435154832259/Lombok-Tour-Package-6-days-5-nights-2342c1bf-20cc-4063-a4f4-0cf7c9932f87.jpeg?_src=imagekit&tr=dpr-2,c-at_max,h-750,q-100,w-1000" alt="Image 1" />
                </div>
                <h2 class="text-lg font-bold mt-3 mb-2">Gili Trawangan, Meno, Air Tour</h2>
                <div class="price-text">
                <h2 class="text-sm text-end text-darkgray-400 mb-3">Starts From</h2>
                    <span class="original-price">Rp. 4.800.000</span><br>
                    <span class="discounted-price">Rp. 4.600.000</span>
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
                                <p class="font-semibold text-blue-500">9.6</p>
                                
                </div>
                <h2 class="w-2/5 flex items-center  text-sm text-end text-gray-400 ">(32 reviews)</h2>
                <button class="py-2 px-4 mt-2 text-sm rounded bg-orange-600 hover:bg-orange-700 text-white font-semibold ">Select Package</button>
            </div>
            <!-- Nusa Lembongan Tour -->
            <div class="w-full md:w-1/3 p-2">
                <div class="relative overflow-hidden" style="padding-top: 100%;">
                    <img class="absolute inset-0 w-full h-full object-cover" src="https://ik.imagekit.io/tvlk/xpe-asset/AyJ40ZAo1DOyPyKLZ9c3RGQHTP2oT4ZXW+QmPVVkFQiXFSv42UaHGzSmaSzQ8DO5QIbWPZuF+VkYVRk6gh-Vg4ECbfuQRQ4pHjWJ5Rmbtkk=/3063120899868/Bundling-Package-for-Fast-Boat-Tickets-from-Sanur-to-Nusa-Lembongan-PP-and-Vario-Motorbike-Rental-for-1-Day-by-Penidago-04c30cb7-7b07-4a91-989f-5e17ca9ec6c5.jpeg?_src=imagekit&tr=dpr-2,c-at_max,h-750,q-100,w-1000" alt="Image 2" />
                </div>
                <h2 class="text-lg font-bold mt-3 mb-2">Nusa Lembongan Tour</h2>
                <div class="price-text">
                <h2 class="text-sm text-end text-darkgray-400 mb-3">Starts From</h2>
                    <span class="original-price">Rp. 5.300.000</span><br>
                    <span class="discounted-price">Rp. 5.210.000</span>
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
                                <p class="font-semibold text-blue-500">9.4</p>
                </div>
                <h2 class="w-2/5 flex items-center  text-sm text-end text-gray-400 ">(21 reviews)</h2>
                <button class="py-2 px-4 mt-2 text-sm rounded bg-orange-600 hover:bg-orange-700 text-white font-semibold">Select Package</button>
            </div>

            <!-- Nusa Penida Tour -->
            <div class="w-full md:w-1/3 p-2">
                <div class="relative overflow-hidden" style="padding-top: 100%;">
                    <img class="absolute inset-0 w-full h-full object-cover" src="https://ik.imagekit.io/tvlk/xpe-asset/AyJ40ZAo1DOyPyKLZ9c3RGQHTP2oT4ZXW+QmPVVkFQiXFSv42UaHGzSmaSzQ8DO5QIbWPZuF+VkYVRk6gh-Vg4ECbfuQRQ4pHjWJ5Rmbtkk=/8122113313137/Bali-Nusa-Penida-Private-Tour-503900ee-bd33-49e2-9b3d-fc75d6fbfd84.jpeg?_src=imagekit&tr=dpr-2,c-at_max,h-750,q-100,w-1000" alt="Image 3" />
                </div>
                <h2 class="text-lg font-bold mt-3 mb-2">Nusa Penida Tour</h2>
                <div class="price-text">
                <h2 class="text-sm text-end text-darkgray-400 mb-3">Starts From</h2>
                    <span class="original-price">Rp. 4.900.000</span><br>
                    <span class="discounted-price">Rp. 4.850.000</span>
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
                                <p class="font-semibold text-blue-500">9.7</p>
                </div>
                <h2 class="w-2/5 flex items-center  text-sm text-end text-gray-400 ">(40 reviews)</h2>
                <button class="py-2 px-4 mt-2 text-sm rounded bg-orange-600 hover:bg-orange-700 text-white font-semibold">Select Package</button>
            </div>

            <!-- Ijen Crater Tour -->
            <div class="w-full md:w-1/3 p-2">
                <div class="relative overflow-hidden" style="padding-top: 100%;">
                    <img class="absolute inset-0 w-full h-full object-cover" src="https://ik.imagekit.io/tvlk/xpe-asset/AyJ40ZAo1DOyPyKLZ9c3RGQHTP2oT4ZXW+QmPVVkFQiXFSv42UaHGzSmaSzQ8DO5QIbWPZuF+VkYVRk6gh-Vg4ECbfuQRQ4pHjWJ5Rmbtkk=/2000262452109/Kawah-Ijen-dengan-Yuk-Banyuwangi---Tur-1-Hari--c10cc9d4-cbfb-4395-8fdc-d7ee0e2ae8f0.jpeg?_src=imagekit&tr=dpr-2,c-at_max,h-750,q-100,w-1000" alt="Image 1" />
                </div>
                <h2 class="text-lg font-bold mt-3 mb-2">Ijen Crater Tour</h2>
                <div class="price-text">
                <h2 class="text-sm text-end text-darkgray-400 mb-3">Starts From</h2>
                    <span class="original-price">Rp. 3.950.000</span><br>
                    <span class="discounted-price">Rp. 3.800.000</span>
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
                                <p class="font-semibold text-blue-500">9.2</p>
                </div>
                <h2 class="w-2/5 flex items-center  text-sm text-end text-gray-400 ">(17 reviews)</h2>
                <button class="py-2 px-4 mt-2 text-sm rounded bg-orange-600 hover:bg-orange-700 text-white font-semibold">Select Package</button>
            </div>

            <!-- Bromo Tour -->
            <div class="w-full md:w-1/3 p-2">
                <div class="relative overflow-hidden" style="padding-top: 100%;">
                    <img class="absolute inset-0 w-full h-full object-cover" src="https://ik.imagekit.io/tvlk/xpe-asset/AyJ40ZAo1DOyPyKLZ9c3RGQHTP2oT4ZXW+QmPVVkFQiXFSv42UaHGzSmaSzQ8DO5QIbWPZuF+VkYVRk6gh-Vg4ECbfuQRQ4pHjWJ5Rmbtkk=/2000914428209/Gunung-Bromo-Trip-Sunrise---Start-Malang---1-Hari-79c6502f-0086-453c-a4c8-2d56001f1542.jpeg?_src=imagekit&tr=dpr-2,c-at_max,h-750,q-100,w-1000" alt="Image 2" />
                </div>
                <h2 class="text-lg font-bold mt-3 mb-2">Bromo & Semeru Tour</h2>
                <div class="price-text">
                <h2 class="text-sm text-end text-darkgray-400 mb-3">Starts From</h2>
                    <span class="original-price">Rp. 3.500.000</span><br>
                    <span class="discounted-price">Rp. 3.350.000</span>
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
                                <p class="font-semibold text-blue-500">8.3</p>
                </div>
                <h2 class="w-2/5 flex items-center  text-sm text-end text-gray-400 ">(65 reviews)</h2>
                <button class="py-2 px-4 mt-2 text-sm rounded bg-orange-600 hover:bg-orange-700 text-white font-semibold">Select Package</button>
            </div>

            <!-- Komodo Labuan Bajo Tour -->
            <div class="w-full md:w-1/3 p-2">
                <div class="relative overflow-hidden" style="padding-top: 100%;">
                    <img class="absolute inset-0 w-full h-full object-cover" src="https://ik.imagekit.io/tvlk/xpe-asset/AyJ40ZAo1DOyPyKLZ9c3RGQHTP2oT4ZXW+QmPVVkFQiXFSv42UaHGzSmaSzQ8DO5QIbWPZuF+VkYVRk6gh-Vg4ECbfuQRQ4pHjWJ5Rmbtkk=/9140174499966/LABUAN-BAJO---KOMODO-TOUR-PACKAGE-TOUR-b23191f1-17f9-4078-985e-3e9fc9406193.jpeg?_src=imagekit&tr=dpr-2,c-at_max,h-750,q-100,w-1000" alt="Image 3" />
                </div>
                <h2 class="text-lg font-bold mt-3 mb-2">Komodo Island Labuan Bajo Tour</h2>
                <div class="price-text">
                <h2 class="text-sm text-end text-darkgray-400 mb-3">Starts From</h2>
                    <span class="original-price">Rp. 9.650.000</span><br>
                    <span class="discounted-price">Rp. 9.550.000</span>
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
                                <p class="font-semibold text-blue-500">9.5</p>
                </div>
                <h2 class="w-2/5 flex items-center  text-sm text-end text-gray-400 ">(88 reviews)</h2>
                <button class="py-2 px-4 mt-2 text-sm rounded bg-orange-600 hover:bg-orange-700 text-white font-semibold">Select Package</button>
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