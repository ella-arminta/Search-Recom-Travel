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
            <h1 class="text-lg font-semibold">Package</h1>
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
                            <label for="highestprice">Highest Price</label><br>
                        </li>
                        <li role="menuitem" class="block m-auto w-full cursor-pointer text-md select-none rounded-md px-3 pt-[9px] pb-2 text-start leading-tight transition-all hover:bg-blue-gray-50 hover:bg-opacity-80 hover:text-blue-gray-900 focus:bg-blue-gray-50 focus:bg-opacity-80 focus:text-blue-gray-900 active:bg-blue-gray-50 active:bg-opacity-80 active:text-blue-gray-900">
                            <input type="radio" id="city" name="sort" value="city">
                            <label for="city">City</label><br>
                        </li>
                        <li role="menuitem" class="block m-auto w-full cursor-pointer text-md select-none rounded-md px-3 pt-[9px] pb-2 text-start leading-tight transition-all hover:bg-blue-gray-50 hover:bg-opacity-80 hover:text-blue-gray-900 focus:bg-blue-gray-50 focus:bg-opacity-80 focus:text-blue-gray-900 active:bg-blue-gray-50 active:bg-opacity-80 active:text-blue-gray-900">
                            <input type="radio" id="startdate" name="sort" value="startdate">
                            <label for="startdate">Departure Date</label><br>
                        </li>
                        <li role="menuitem" class="block m-auto w-full cursor-pointer text-md select-none rounded-md px-3 pt-[9px] pb-2 text-start leading-tight transition-all hover:bg-blue-gray-50 hover:bg-opacity-80 hover:text-blue-gray-900 focus:bg-blue-gray-50 focus:bg-opacity-80 focus:text-blue-gray-900 active:bg-blue-gray-50 active:bg-opacity-80 active:text-blue-gray-900">
                            <input type="radio" id="quota" name="sort" value="quota">
                            <label for="quota">Quota Passenger</label><br>
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
                <h2 class="text-lg font-bold mt-3 mb-2">Gili Trawangan, Meno, Air Package</h2>
                <div class="flex mt-3 mb-2 items-center justify-start gap-2">
                            <!-- Icon location -->
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemMapLocationFill">
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M21 10C21 7.25554 20.0331 4.98482 18.3787 3.40236C16.7312 1.8265 14.4725 1 12 1C9.52754 1 7.26876 1.8265 5.62128 3.40236C3.96688 4.98482 3 7.25554 3 10C3 13.4069 5.24119 16.5278 7.2718 18.6854C8.31023 19.7887 9.34524 20.694 10.1194 21.323C10.5073 21.6381 10.8316 21.8855 11.0609 22.0554C11.0795 22.0692 11.0982 22.0831 11.1169 22.0971C11.3805 22.2937 11.6567 22.4998 12 22.4998C12.3432 22.4999 12.6194 22.2938 12.8829 22.0972C12.9017 22.0832 12.9205 22.0692 12.9391 22.0554C13.1684 21.8855 13.4927 21.6381 13.8806 21.323C14.6548 20.694 15.6898 19.7887 16.7282 18.6854C18.7588 16.5278 21 13.4069 21 10ZM15.5 9.5C15.5 11.433 13.933 13 12 13C10.067 13 8.5 11.433 8.5 9.5C8.5 7.567 10.067 6 12 6C13.933 6 15.5 7.567 15.5 9.5Z" fill="#687176"></path>
                            </svg>
                            <p>Lombok Timur</p>
                        </div>
                <div class="rounded w-full backdrop-blur-sm mt-3 bg-white/30  flex justify-start gap-2 text-sm font-semibold"><svg width="24" height="24" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemCalendar">
                                <path d="M7 2V5M17 2V5M3 8H21M11.5 11.5H12.5V12.5H11.5V11.5ZM11.5 16.5H12.5V17.5H11.5V16.5ZM16.5 11.5H17.5V12.5H16.5V11.5ZM6.5 16.5H7.5V17.5H6.5V16.5ZM6.5 11.5H7.5V12.5H6.5V11.5ZM16.5 16.5H17.5V17.5H16.5V16.5ZM3 22H21V8H3V22Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                            </svg>
                    15 June - 21 June 2024
                </div>
                <div class="rounded w-full mt-3 backdrop-blur-sm bg-white/30 flex justify-start gap-2 text-sm font-semibold">
                <svg width="30" height="30" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemGroupOfPeople">
                    <path d="M8 8C9.65685 8 11 6.65685 11 5C11 3.34315 9.65685 2 8 2C6.34315 2 5 3.34315 5 5C5 6.65685 6.34315 8 8 8ZM8 9C5.87827 9 4.06849 10.0044 3 11.5147C3 13.5228 5.68629 14.5 8 14.5C10.3137 14.5 13 13.5228 13 11.5147C11.9315 10.0044 10.1217 9 8 9Z" fill="#000000"/>
                </svg>
                <p style="margin-left: -5px;">25 Quota Passengers</p></div>
                <div class="price-text">
                <h2 class="text-sm text-end text-darkgray-400 mb-3">Starts From</h2>
                    <span class="original-price">Rp. 4.800.000</span><br>
                    <span class="discounted-price">Rp. 4.600.000</span>
                </div>
                <button class="py-2 px-4 mt-2 text-sm rounded bg-blue-600 hover:bg-blue-700 text-white font-semibold ">Details</button>
            </div>
            <!-- Nusa Lembongan Tour -->
            <div class="w-full md:w-1/3 p-2">
                <div class="relative overflow-hidden" style="padding-top: 100%;">
                    <img class="absolute inset-0 w-full h-full object-cover" src="https://ik.imagekit.io/tvlk/xpe-asset/AyJ40ZAo1DOyPyKLZ9c3RGQHTP2oT4ZXW+QmPVVkFQiXFSv42UaHGzSmaSzQ8DO5QIbWPZuF+VkYVRk6gh-Vg4ECbfuQRQ4pHjWJ5Rmbtkk=/3063120899868/Bundling-Package-for-Fast-Boat-Tickets-from-Sanur-to-Nusa-Lembongan-PP-and-Vario-Motorbike-Rental-for-1-Day-by-Penidago-04c30cb7-7b07-4a91-989f-5e17ca9ec6c5.jpeg?_src=imagekit&tr=dpr-2,c-at_max,h-750,q-100,w-1000" alt="Image 2" />
                </div>
                <h2 class="text-lg font-bold mt-3 mb-2">Nusa Lembongan Package</h2>
                <div class="flex mt-3 mb-2 items-center justify-start gap-2">
                            <!-- Icon location -->
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemMapLocationFill">
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M21 10C21 7.25554 20.0331 4.98482 18.3787 3.40236C16.7312 1.8265 14.4725 1 12 1C9.52754 1 7.26876 1.8265 5.62128 3.40236C3.96688 4.98482 3 7.25554 3 10C3 13.4069 5.24119 16.5278 7.2718 18.6854C8.31023 19.7887 9.34524 20.694 10.1194 21.323C10.5073 21.6381 10.8316 21.8855 11.0609 22.0554C11.0795 22.0692 11.0982 22.0831 11.1169 22.0971C11.3805 22.2937 11.6567 22.4998 12 22.4998C12.3432 22.4999 12.6194 22.2938 12.8829 22.0972C12.9017 22.0832 12.9205 22.0692 12.9391 22.0554C13.1684 21.8855 13.4927 21.6381 13.8806 21.323C14.6548 20.694 15.6898 19.7887 16.7282 18.6854C18.7588 16.5278 21 13.4069 21 10ZM15.5 9.5C15.5 11.433 13.933 13 12 13C10.067 13 8.5 11.433 8.5 9.5C8.5 7.567 10.067 6 12 6C13.933 6 15.5 7.567 15.5 9.5Z" fill="#687176"></path>
                            </svg>
                            <p>Nusa Lembongan, Bali</p>
                </div>
                <div class="rounded w-full backdrop-blur-sm mt-3 bg-white/30  flex justify-start gap-2 text-sm font-semibold"><svg width="24" height="24" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemCalendar">
                                <path d="M7 2V5M17 2V5M3 8H21M11.5 11.5H12.5V12.5H11.5V11.5ZM11.5 16.5H12.5V17.5H11.5V16.5ZM16.5 11.5H17.5V12.5H16.5V11.5ZM6.5 16.5H7.5V17.5H6.5V16.5ZM6.5 11.5H7.5V12.5H6.5V11.5ZM16.5 16.5H17.5V17.5H16.5V16.5ZM3 22H21V8H3V22Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                            </svg>
                    07 July - 12 July 2024
                </div>
                <div class="rounded w-full mt-3 backdrop-blur-sm bg-white/30 flex justify-start gap-2 text-sm font-semibold">
                <svg width="30" height="30" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemGroupOfPeople">
                    <path d="M8 8C9.65685 8 11 6.65685 11 5C11 3.34315 9.65685 2 8 2C6.34315 2 5 3.34315 5 5C5 6.65685 6.34315 8 8 8ZM8 9C5.87827 9 4.06849 10.0044 3 11.5147C3 13.5228 5.68629 14.5 8 14.5C10.3137 14.5 13 13.5228 13 11.5147C11.9315 10.0044 10.1217 9 8 9Z" fill="#000000"/>
                </svg>
                <p style="margin-left: -5px;">30 Quota Passenger</p></div>
                <div class="price-text">
                <h2 class="text-sm text-end text-darkgray-400 mb-3">Starts From</h2>
                    <span class="original-price">Rp. 5.300.000</span><br>
                    <span class="discounted-price">Rp. 5.210.000</span>
                </div>
                <button class="py-2 px-4 mt-2 text-sm rounded bg-blue-600 hover:bg-blue-700 text-white font-semibold">Details</button>
            </div>

            <!-- Nusa Penida Tour -->
            <div class="w-full md:w-1/3 p-2">
                <div class="relative overflow-hidden" style="padding-top: 100%;">
                    <img class="absolute inset-0 w-full h-full object-cover" src="https://ik.imagekit.io/tvlk/xpe-asset/AyJ40ZAo1DOyPyKLZ9c3RGQHTP2oT4ZXW+QmPVVkFQiXFSv42UaHGzSmaSzQ8DO5QIbWPZuF+VkYVRk6gh-Vg4ECbfuQRQ4pHjWJ5Rmbtkk=/8122113313137/Bali-Nusa-Penida-Private-Tour-503900ee-bd33-49e2-9b3d-fc75d6fbfd84.jpeg?_src=imagekit&tr=dpr-2,c-at_max,h-750,q-100,w-1000" alt="Image 3" />
                </div>
                <h2 class="text-lg font-bold mt-3 mb-2">Nusa Penida Package</h2>
                <div class="flex mt-3 mb-2 items-center justify-start gap-2">
                            <!-- Icon location -->
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemMapLocationFill">
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M21 10C21 7.25554 20.0331 4.98482 18.3787 3.40236C16.7312 1.8265 14.4725 1 12 1C9.52754 1 7.26876 1.8265 5.62128 3.40236C3.96688 4.98482 3 7.25554 3 10C3 13.4069 5.24119 16.5278 7.2718 18.6854C8.31023 19.7887 9.34524 20.694 10.1194 21.323C10.5073 21.6381 10.8316 21.8855 11.0609 22.0554C11.0795 22.0692 11.0982 22.0831 11.1169 22.0971C11.3805 22.2937 11.6567 22.4998 12 22.4998C12.3432 22.4999 12.6194 22.2938 12.8829 22.0972C12.9017 22.0832 12.9205 22.0692 12.9391 22.0554C13.1684 21.8855 13.4927 21.6381 13.8806 21.323C14.6548 20.694 15.6898 19.7887 16.7282 18.6854C18.7588 16.5278 21 13.4069 21 10ZM15.5 9.5C15.5 11.433 13.933 13 12 13C10.067 13 8.5 11.433 8.5 9.5C8.5 7.567 10.067 6 12 6C13.933 6 15.5 7.567 15.5 9.5Z" fill="#687176"></path>
                            </svg>
                            <p>Nusa Penida, Bali</p>
                </div>
                <div class="rounded w-full backdrop-blur-sm mt-3 bg-white/30  flex justify-start gap-2 text-sm font-semibold"><svg width="24" height="24" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemCalendar">
                                <path d="M7 2V5M17 2V5M3 8H21M11.5 11.5H12.5V12.5H11.5V11.5ZM11.5 16.5H12.5V17.5H11.5V16.5ZM16.5 11.5H17.5V12.5H16.5V11.5ZM6.5 16.5H7.5V17.5H6.5V16.5ZM6.5 11.5H7.5V12.5H6.5V11.5ZM16.5 16.5H17.5V17.5H16.5V16.5ZM3 22H21V8H3V22Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                            </svg>
                    05 August - 15 August 2024
                </div>
                <div class="rounded w-full mt-3 backdrop-blur-sm bg-white/30 flex justify-start gap-2 text-sm font-semibold">
                <svg width="30" height="30" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemGroupOfPeople">
                    <path d="M8 8C9.65685 8 11 6.65685 11 5C11 3.34315 9.65685 2 8 2C6.34315 2 5 3.34315 5 5C5 6.65685 6.34315 8 8 8ZM8 9C5.87827 9 4.06849 10.0044 3 11.5147C3 13.5228 5.68629 14.5 8 14.5C10.3137 14.5 13 13.5228 13 11.5147C11.9315 10.0044 10.1217 9 8 9Z" fill="#000000"/>
                </svg>
                <p style="margin-left: -5px;">20 Quota Passenger</p></div>

                <div class="price-text">
                <h2 class="text-sm text-end text-darkgray-400 mb-3">Starts From</h2>
                    <span class="original-price">Rp. 4.900.000</span><br>
                    <span class="discounted-price">Rp. 4.850.000</span>
                </div>
                <button class="py-2 px-4 mt-2 text-sm rounded bg-blue-600 hover:bg-blue-700 text-white font-semibold">Details</button>
            </div>

            <!-- Ijen Crater Tour -->
            <div class="w-full md:w-1/3 p-2">
                <div class="relative overflow-hidden" style="padding-top: 100%;">
                    <img class="absolute inset-0 w-full h-full object-cover" src="https://ik.imagekit.io/tvlk/xpe-asset/AyJ40ZAo1DOyPyKLZ9c3RGQHTP2oT4ZXW+QmPVVkFQiXFSv42UaHGzSmaSzQ8DO5QIbWPZuF+VkYVRk6gh-Vg4ECbfuQRQ4pHjWJ5Rmbtkk=/2000262452109/Kawah-Ijen-dengan-Yuk-Banyuwangi---Tur-1-Hari--c10cc9d4-cbfb-4395-8fdc-d7ee0e2ae8f0.jpeg?_src=imagekit&tr=dpr-2,c-at_max,h-750,q-100,w-1000" alt="Image 1" />
                </div>
                <h2 class="text-lg font-bold mt-3 mb-2">Ijen Crater Package</h2>
                <div class="flex mt-3 mb-2 items-center justify-start gap-2">
                            <!-- Icon location -->
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemMapLocationFill">
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M21 10C21 7.25554 20.0331 4.98482 18.3787 3.40236C16.7312 1.8265 14.4725 1 12 1C9.52754 1 7.26876 1.8265 5.62128 3.40236C3.96688 4.98482 3 7.25554 3 10C3 13.4069 5.24119 16.5278 7.2718 18.6854C8.31023 19.7887 9.34524 20.694 10.1194 21.323C10.5073 21.6381 10.8316 21.8855 11.0609 22.0554C11.0795 22.0692 11.0982 22.0831 11.1169 22.0971C11.3805 22.2937 11.6567 22.4998 12 22.4998C12.3432 22.4999 12.6194 22.2938 12.8829 22.0972C12.9017 22.0832 12.9205 22.0692 12.9391 22.0554C13.1684 21.8855 13.4927 21.6381 13.8806 21.323C14.6548 20.694 15.6898 19.7887 16.7282 18.6854C18.7588 16.5278 21 13.4069 21 10ZM15.5 9.5C15.5 11.433 13.933 13 12 13C10.067 13 8.5 11.433 8.5 9.5C8.5 7.567 10.067 6 12 6C13.933 6 15.5 7.567 15.5 9.5Z" fill="#687176"></path>
                            </svg>
                            <p>Bondowoso, Jawa Timur</p>
                </div>
                <div class="rounded w-full backdrop-blur-sm mt-3 bg-white/30  flex justify-start gap-2 text-sm font-semibold"><svg width="24" height="24" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemCalendar">
                                <path d="M7 2V5M17 2V5M3 8H21M11.5 11.5H12.5V12.5H11.5V11.5ZM11.5 16.5H12.5V17.5H11.5V16.5ZM16.5 11.5H17.5V12.5H16.5V11.5ZM6.5 16.5H7.5V17.5H6.5V16.5ZM6.5 11.5H7.5V12.5H6.5V11.5ZM16.5 16.5H17.5V17.5H16.5V16.5ZM3 22H21V8H3V22Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                            </svg>
                    11 July - 19 July 2024
                </div>
                <div class="rounded w-full mt-3 backdrop-blur-sm bg-white/30 flex justify-start gap-2 text-sm font-semibold">
                <svg width="30" height="30" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemGroupOfPeople">
                    <path d="M8 8C9.65685 8 11 6.65685 11 5C11 3.34315 9.65685 2 8 2C6.34315 2 5 3.34315 5 5C5 6.65685 6.34315 8 8 8ZM8 9C5.87827 9 4.06849 10.0044 3 11.5147C3 13.5228 5.68629 14.5 8 14.5C10.3137 14.5 13 13.5228 13 11.5147C11.9315 10.0044 10.1217 9 8 9Z" fill="#000000"/>
                </svg>
                <p style="margin-left: -5px;">15 Quota Passenger</p></div>
                <div class="price-text">
                <h2 class="text-sm text-end text-darkgray-400 mb-3">Starts From</h2>
                    <span class="original-price">Rp. 3.950.000</span><br>
                    <span class="discounted-price">Rp. 3.800.000</span>
                </div>
                <button class="py-2 px-4 mt-2 text-sm rounded bg-blue-600 hover:bg-blue-700 text-white font-semibold">Details</button>
            </div>

            <!-- Bromo Tour -->
            <div class="w-full md:w-1/3 p-2">
                <div class="relative overflow-hidden" style="padding-top: 100%;">
                    <img class="absolute inset-0 w-full h-full object-cover" src="https://ik.imagekit.io/tvlk/xpe-asset/AyJ40ZAo1DOyPyKLZ9c3RGQHTP2oT4ZXW+QmPVVkFQiXFSv42UaHGzSmaSzQ8DO5QIbWPZuF+VkYVRk6gh-Vg4ECbfuQRQ4pHjWJ5Rmbtkk=/2000914428209/Gunung-Bromo-Trip-Sunrise---Start-Malang---1-Hari-79c6502f-0086-453c-a4c8-2d56001f1542.jpeg?_src=imagekit&tr=dpr-2,c-at_max,h-750,q-100,w-1000" alt="Image 2" />
                </div>
                <h2 class="text-lg font-bold mt-3 mb-2">Bromo & Semeru Package</h2>
                <div class="flex mt-3 mb-2 items-center justify-start gap-2">
                            <!-- Icon location -->
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemMapLocationFill">
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M21 10C21 7.25554 20.0331 4.98482 18.3787 3.40236C16.7312 1.8265 14.4725 1 12 1C9.52754 1 7.26876 1.8265 5.62128 3.40236C3.96688 4.98482 3 7.25554 3 10C3 13.4069 5.24119 16.5278 7.2718 18.6854C8.31023 19.7887 9.34524 20.694 10.1194 21.323C10.5073 21.6381 10.8316 21.8855 11.0609 22.0554C11.0795 22.0692 11.0982 22.0831 11.1169 22.0971C11.3805 22.2937 11.6567 22.4998 12 22.4998C12.3432 22.4999 12.6194 22.2938 12.8829 22.0972C12.9017 22.0832 12.9205 22.0692 12.9391 22.0554C13.1684 21.8855 13.4927 21.6381 13.8806 21.323C14.6548 20.694 15.6898 19.7887 16.7282 18.6854C18.7588 16.5278 21 13.4069 21 10ZM15.5 9.5C15.5 11.433 13.933 13 12 13C10.067 13 8.5 11.433 8.5 9.5C8.5 7.567 10.067 6 12 6C13.933 6 15.5 7.567 15.5 9.5Z" fill="#687176"></path>
                            </svg>
                            <p>Probolinggo, Jawa Timur</p>
                </div>
                <div class="rounded w-full backdrop-blur-sm mt-3 bg-white/30  flex justify-start gap-2 text-sm font-semibold"><svg width="24" height="24" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemCalendar">
                                <path d="M7 2V5M17 2V5M3 8H21M11.5 11.5H12.5V12.5H11.5V11.5ZM11.5 16.5H12.5V17.5H11.5V16.5ZM16.5 11.5H17.5V12.5H16.5V11.5ZM6.5 16.5H7.5V17.5H6.5V16.5ZM6.5 11.5H7.5V12.5H6.5V11.5ZM16.5 16.5H17.5V17.5H16.5V16.5ZM3 22H21V8H3V22Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                            </svg>
                    23 July - 29 July 2024
                </div>
                <div class="rounded w-full mt-3 backdrop-blur-sm bg-white/30 flex justify-start gap-2 text-sm font-semibold">
                <svg width="30" height="30" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemGroupOfPeople">
                    <path d="M8 8C9.65685 8 11 6.65685 11 5C11 3.34315 9.65685 2 8 2C6.34315 2 5 3.34315 5 5C5 6.65685 6.34315 8 8 8ZM8 9C5.87827 9 4.06849 10.0044 3 11.5147C3 13.5228 5.68629 14.5 8 14.5C10.3137 14.5 13 13.5228 13 11.5147C11.9315 10.0044 10.1217 9 8 9Z" fill="#000000"/>
                </svg>
                <p style="margin-left: -5px;">17 Quota Passenger</p></div>
                <div class="price-text">
                <h2 class="text-sm text-end text-darkgray-400 mb-3">Starts From</h2>
                    <span class="original-price">Rp. 3.500.000</span><br>
                    <span class="discounted-price">Rp. 3.350.000</span>
                </div>
                <button class="py-2 px-4 mt-2 text-sm rounded bg-blue-600 hover:bg-blue-700 text-white font-semibold">Details</button>
            </div>

            <!-- Komodo Labuan Bajo Tour -->
            <div class="w-full md:w-1/3 p-2">
                <div class="relative overflow-hidden" style="padding-top: 100%;">
                    <img class="absolute inset-0 w-full h-full object-cover" src="https://ik.imagekit.io/tvlk/xpe-asset/AyJ40ZAo1DOyPyKLZ9c3RGQHTP2oT4ZXW+QmPVVkFQiXFSv42UaHGzSmaSzQ8DO5QIbWPZuF+VkYVRk6gh-Vg4ECbfuQRQ4pHjWJ5Rmbtkk=/9140174499966/LABUAN-BAJO---KOMODO-TOUR-PACKAGE-TOUR-b23191f1-17f9-4078-985e-3e9fc9406193.jpeg?_src=imagekit&tr=dpr-2,c-at_max,h-750,q-100,w-1000" alt="Image 3" />
                </div>
                <h2 class="text-lg font-bold mt-3 mb-2">Komodo Island Package</h2>
                <div class="flex mt-3 mb-2 items-center justify-start gap-2">
                            <!-- Icon location -->
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemMapLocationFill">
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M21 10C21 7.25554 20.0331 4.98482 18.3787 3.40236C16.7312 1.8265 14.4725 1 12 1C9.52754 1 7.26876 1.8265 5.62128 3.40236C3.96688 4.98482 3 7.25554 3 10C3 13.4069 5.24119 16.5278 7.2718 18.6854C8.31023 19.7887 9.34524 20.694 10.1194 21.323C10.5073 21.6381 10.8316 21.8855 11.0609 22.0554C11.0795 22.0692 11.0982 22.0831 11.1169 22.0971C11.3805 22.2937 11.6567 22.4998 12 22.4998C12.3432 22.4999 12.6194 22.2938 12.8829 22.0972C12.9017 22.0832 12.9205 22.0692 12.9391 22.0554C13.1684 21.8855 13.4927 21.6381 13.8806 21.323C14.6548 20.694 15.6898 19.7887 16.7282 18.6854C18.7588 16.5278 21 13.4069 21 10ZM15.5 9.5C15.5 11.433 13.933 13 12 13C10.067 13 8.5 11.433 8.5 9.5C8.5 7.567 10.067 6 12 6C13.933 6 15.5 7.567 15.5 9.5Z" fill="#687176"></path>
                            </svg>
                            <p>Labuan Bajo, NTT</p>
                </div>
                <div class="rounded w-full backdrop-blur-sm mt-3 bg-white/30  flex justify-start gap-2 text-sm font-semibold"><svg width="24" height="24" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemCalendar">
                                <path d="M7 2V5M17 2V5M3 8H21M11.5 11.5H12.5V12.5H11.5V11.5ZM11.5 16.5H12.5V17.5H11.5V16.5ZM16.5 11.5H17.5V12.5H16.5V11.5ZM6.5 16.5H7.5V17.5H6.5V16.5ZM6.5 11.5H7.5V12.5H6.5V11.5ZM16.5 16.5H17.5V17.5H16.5V16.5ZM3 22H21V8H3V22Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                            </svg>
                    14 August - 19 August 2024
                </div>
                <div class="rounded w-full mt-3 backdrop-blur-sm bg-white/30 flex justify-start gap-2 text-sm font-semibold">
                <svg width="30" height="30" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemGroupOfPeople">
                    <path d="M8 8C9.65685 8 11 6.65685 11 5C11 3.34315 9.65685 2 8 2C6.34315 2 5 3.34315 5 5C5 6.65685 6.34315 8 8 8ZM8 9C5.87827 9 4.06849 10.0044 3 11.5147C3 13.5228 5.68629 14.5 8 14.5C10.3137 14.5 13 13.5228 13 11.5147C11.9315 10.0044 10.1217 9 8 9Z" fill="#000000"/>
                </svg>
                <p style="margin-left: -5px;">12 Quota Passenger</p></div>
                <div class="price-text">
                <h2 class="text-sm text-end text-darkgray-400 mb-3">Starts From</h2>
                    <span class="original-price">Rp. 9.650.000</span><br>
                    <span class="discounted-price">Rp. 9.550.000</span>
                </div>
                <button class="py-2 px-4 mt-2 text-sm rounded bg-blue-600 hover:bg-blue-700 text-white font-semibold">Details</button>
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