<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <title>Search Flight</title>
</head>
<style>
    input[type="date"]::-webkit-inner-spin-button,
    input[type="date"]::-webkit-calendar-picker-indicator {
        display: hidden;
        -webkit-appearance: none;
        left: 0.6em;
        width: 5%;
        opacity: 0;
        position: absolute;
        z-index: 2;
        cursor: pointer;
    }
    .bg-gradient-custom-blue {
        background: rgb(25, 50, 124);
        background: linear-gradient(143deg, rgba(25, 50, 124, 1) 0%, rgba(42, 123, 209, 1) 56%, rgba(75, 145, 224, 1) 100%);
    }
</style>
<body class="bg-sky-400">  
    <div class="container flex items-center justify-center h-[100vh] w-full">
        <div class="rounded-md w-[80vw] flex flex-col gap-5 bg-slate-50 p-5 shadow-md">  
            <div class="text-sky-500 font-bold">
                Search flight
            </div>
            
            <!-- origin & destination place -->
            <div class="flex w-full relative gap-4">
                <div class="w-1/2 relative">
                    <label for="originplace">From</label>
                    <div class="relative mt-2">
                        <select name="originplace" id="originplace"
                            class="w-full p-2 pl-10 rounded border border-gray-300 focus:bg-white focus:outline-none focus:ring-2 focus:ring-yellow-600 focus:border-transparent">
                            <option selected>Choose City</option>
                            <option value="JKTA">Jakarta</option>
                            <option value="DPS">Bali</option>
                            <option value="SUB">Surabaya</option>
                            <option value="BTH">Batam</option>

                        </select>
                        <svg class="absolute top-2.5 left-2 w-6 h-6 text-gray-400" fill="#000000" viewBox="0 0 256 256"
                            xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M172,216a4.0002,4.0002,0,0,1-4,4H24a4,4,0,0,1,0-8H168A4.0002,4.0002,0,0,1,172,216ZM247.93555,92.71289a3.99731,3.99731,0,0,1-1.92481,2.74512L94.60352,183.48584a35.78229,35.78229,0,0,1-42.7168-4.85938L14.19141,143.28711h-.001a12.00032,12.00032,0,0,1,3.48145-19.78418l16.75292-7.17969a4.00251,4.00251,0,0,1,3.1504,0l26.16992,11.21533L85.21191,115.272,58.625,91.34375A12.00078,12.00078,0,0,1,61.9248,71.394l16.5-7.0708a4.00808,4.00808,0,0,1,2.83985-.11816l58.27441,19.4248,42.80176-25.17724a35.81374,35.81374,0,0,1,46.11523,8.2334L247.0957,89.4668A3.99849,3.99849,0,0,1,247.93555,92.71289Zm-10.00293-1.812-15.668-19.14893a27.85578,27.85578,0,0,0-35.86719-6.40381L142.02832,91.44775a4.00787,4.00787,0,0,1-3.293.34717L80.17773,72.27539,65.07617,78.74756a4.00039,4.00039,0,0,0-1.09961,6.6499l30.69922,27.6294a3.99945,3.99945,0,0,1-.6914,6.44628l-28,16a4.00142,4.00142,0,0,1-3.55958.20362L36,124.35205l-15.17773,6.5044a4.00056,4.00056,0,0,0-1.16016,6.59472l37.69531,35.33936A27.82907,27.82907,0,0,0,90.582,176.56982Z" />
                        </svg>
                    </div>
                </div>
                <div class="w-1/2 relative">
                    <label for="destinationplace">To</label>
                    <div class="relative mt-2">
                        <select name="destinationplace" id="destinationplace"
                            class="w-full p-2 pl-10 rounded border border-gray-300 focus:bg-white focus:outline-none focus:ring-2 focus:ring-yellow-600 focus:border-transparent">
                            <option selected>Choose City</option>
                            <option value="JKTA">Jakarta</option>
                            <option value="DPS">Bali</option>
                            <option value="SUB">Surabaya</option>
                            <option value="BTH">Batam</option>
                        </select>
                        <?xml version="1.0" encoding="utf-8"?><!-- Uploaded to: SVG Repo, www.svgrepo.com, Generator: SVG Repo Mixer Tools -->
                        <svg class="absolute top-2.5 left-2 w-6 h-6 text-gray-400" fill="#000000" viewBox="0 0 256 256"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M244,216a4.0002,4.0002,0,0,1-4,4H96a4,4,0,0,1,0-8H240A4.0002,4.0002,0,0,1,244,216Zm-21.07812-28.148L46.294,138.396A36.11994,36.11994,0,0,1,20,103.72949V51.09961A12.00071,12.00071,0,0,1,35.79492,39.71484l13.46973,4.49024a4.00065,4.00065,0,0,1,2.26465,1.9126L66.75781,74.6709,92,82.55908V51.09961a12.00071,12.00071,0,0,1,15.79492-11.38477l13.46973,4.49024a4.00193,4.00193,0,0,1,2.208,1.81054l31.18359,54.57081,46.97852,13.0498A36.10691,36.10691,0,0,1,228,148.32275V184a4.00026,4.00026,0,0,1-5.07812,3.852ZM220,148.32275a28.08386,28.08386,0,0,0-20.50586-26.97851L150.92969,107.854a3.996,3.996,0,0,1-2.40235-1.86962L117.28516,51.31152l-12.01954-4.00683A4.00029,4.00029,0,0,0,100,51.09961V88a4.00033,4.00033,0,0,1-5.19336,3.81787l-32-10a3.99911,3.99911,0,0,1-2.33594-1.93555L45.22168,51.29,33.26562,47.30469a4.02734,4.02734,0,0,0-1.27734-.20948A4.00877,4.00877,0,0,0,28,51.09961v52.62988a28.09229,28.09229,0,0,0,20.4502,26.9624L220,178.72607Z"/>
                        </svg>
                    </div>
                </div>
            </div>
            <!-- Departure Date -->
            <div class="flex w-full relative gap-4">
                <div class="w-1/2">
                    <label for="departuredate">Departure Date</label>
                    <div class="relative w-full mt-2">
                        <input type="date" name="departuredate" id="departuredate" class="date-input w-full p-2 pl-10 rounded border border-gray-300 focus:bg-white focus:outline-none focus:ring-2 focus:ring-yellow-600 focus:border-transparent" placeholder="search..."  />
                        <svg class="absolute top-2.5 left-2" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" data-id="IcSystemCalendar"><path d="M7 2V5M17 2V5M3 8H21M11.5 11.5H12.5V12.5H11.5V11.5ZM11.5 16.5H12.5V17.5H11.5V16.5ZM16.5 11.5H17.5V12.5H16.5V11.5ZM6.5 16.5H7.5V17.5H6.5V16.5ZM5 21H19C20.1046 21 21 20.1046 21 19V6C21 4.89543 20.1046 4 19 4H5C3.89543 4 3 4.89543 3 6V19C3 20.1046 3.89543 21 5 21Z" stroke="#687176" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M7.5 11.5V12.5H6.5V11.5H7.5Z" stroke="#0194F3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>    
                    </div>
                </div>
                <div class="w-1/2 relative">
                    <label for="departuredate">Seat Class</label>
                    <div class="relative mt-2">
                        <select name="seatclass" id="seatclass" class="w-full p-2 pl-10 rounded border border-gray-300 focus:bg-white focus:outline-none focus:ring-2 focus:ring-yellow-600 focus:border-transparent">
                            <option selected>Choose Classs</option>
                            <option value="economy">Economy</option>
                            <option value="business">Business</option>
                        </select>
                        <svg class="absolute top-2.5 left-2.5 w-5 h-5"viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#ff4242"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M22.5 20V22C22.5 22.5523 22.0523 23 21.5 23H7.59646C6.66266 23 5.85314 22.3538 5.64619 21.4432L1.27764 2.22162C1.13542 1.59586 1.61105 1 2.25277 1H5.70799C6.17204 1 6.57512 1.31925 6.6814 1.77096L10.5 18H20.5C21.6046 18 22.5 18.8954 22.5 20Z" stroke="#71717A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M6.96729 3H8.99999C9.55228 3 10 3.44772 10 4V6L8 7.5" stroke="#71717A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M13.5 14.375H9.625H7.5" stroke="#71717A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
                    </div>
                </div>
            </div>
            <div class="flex justify-end">
                <a href="flight.php" class="w-1/2">
                <button id="btnsearch"class="w-full text-white p-2 mt-2 rounded bg-orange-600 hover:bg-orange-700	font-bold flex items-center justify-center gap-1"><img src="https://d1785e74lyxkqq.cloudfront.net/_next/static/v2/6/68a17a4492b3b7647bb89a5a03b15de0.svg"> <div>Search Flight</div></button>
                </a>
            </div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
</body>
</html>