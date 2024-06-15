<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>

     <!-- Roboto font -->

    <!-- Tailwind CSS config -->
    <script src="https://cdn.tailwindcss.com/3.3.0"></script>

    <title>Document</title>
</head>
<style>
    .bg-gradient-custom-blue {
        background: rgb(25, 50, 124);
        background: linear-gradient(143deg, rgba(25, 50, 124, 1) 0%, rgba(42, 123, 209, 1) 56%, rgba(75, 145, 224, 1) 100%);
    }

    .custom-shadow-card {
        box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
    }
    .line-container {
        display: flex;
        align-items: center;
    }
    .circle {
        width: 20px;
        height: 20px;
        border: 2px solid #00aaff;
        border-radius: 50%;
        background-color: white;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .circle.filled {
        background-color: #00aaff;
    }
    .line {
        width: 200px;
        height: 2px;
        background-color: lightgray;
        display: inline-block;
    }
</style>
<body>
    <div class="m-5">
        <div class="w-full rounded-md bg-gradient-custom-blue text-white p-3 ">
            <div class="flex justify-center items-center gap-4">
                <h1 class="text-lg font-semibold">Flight</h1>
                <div class="rounded w-full font-semibold flex items-center justify-center backdrop-blur-sm bg-white/30 p-2 gap-3">
                    <svg class="w-6 h-6 text-gray-400" fill="#000000" viewBox="0 0 256 256"xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M172,216a4.0002,4.0002,0,0,1-4,4H24a4,4,0,0,1,0-8H168A4.0002,4.0002,0,0,1,172,216ZM247.93555,92.71289a3.99731,3.99731,0,0,1-1.92481,2.74512L94.60352,183.48584a35.78229,35.78229,0,0,1-42.7168-4.85938L14.19141,143.28711h-.001a12.00032,12.00032,0,0,1,3.48145-19.78418l16.75292-7.17969a4.00251,4.00251,0,0,1,3.1504,0l26.16992,11.21533L85.21191,115.272,58.625,91.34375A12.00078,12.00078,0,0,1,61.9248,71.394l16.5-7.0708a4.00808,4.00808,0,0,1,2.83985-.11816l58.27441,19.4248,42.80176-25.17724a35.81374,35.81374,0,0,1,46.11523,8.2334L247.0957,89.4668A3.99849,3.99849,0,0,1,247.93555,92.71289Zm-10.00293-1.812-15.668-19.14893a27.85578,27.85578,0,0,0-35.86719-6.40381L142.02832,91.44775a4.00787,4.00787,0,0,1-3.293.34717L80.17773,72.27539,65.07617,78.74756a4.00039,4.00039,0,0,0-1.09961,6.6499l30.69922,27.6294a3.99945,3.99945,0,0,1-.6914,6.44628l-28,16a4.00142,4.00142,0,0,1-3.55958.20362L36,124.35205l-15.17773,6.5044a4.00056,4.00056,0,0,0-1.16016,6.59472l37.69531,35.33936A27.82907,27.82907,0,0,0,90.582,176.56982Z" />
                    </svg>
                    Jakarta (JKTA)
                </div>
                <div class="rounded w-full font-semibold flex items-center justify-center backdrop-blur-sm bg-white/30 p-2 gap-3">
                    <?xml version="1.0" encoding="utf-8"?>
                    <svg class="w-6 h-6 text-gray-400" fill="#000000" viewBox="0 0 256 256"
                    xmlns="http://www.w3.org/2000/svg">
                    <path d="M244,216a4.0002,4.0002,0,0,1-4,4H96a4,4,0,0,1,0-8H240A4.0002,4.0002,0,0,1,244,216Zm-21.07812-28.148L46.294,138.396A36.11994,36.11994,0,0,1,20,103.72949V51.09961A12.00071,12.00071,0,0,1,35.79492,39.71484l13.46973,4.49024a4.00065,4.00065,0,0,1,2.26465,1.9126L66.75781,74.6709,92,82.55908V51.09961a12.00071,12.00071,0,0,1,15.79492-11.38477l13.46973,4.49024a4.00193,4.00193,0,0,1,2.208,1.81054l31.18359,54.57081,46.97852,13.0498A36.10691,36.10691,0,0,1,228,148.32275V184a4.00026,4.00026,0,0,1-5.07812,3.852ZM220,148.32275a28.08386,28.08386,0,0,0-20.50586-26.97851L150.92969,107.854a3.996,3.996,0,0,1-2.40235-1.86962L117.28516,51.31152l-12.01954-4.00683A4.00029,4.00029,0,0,0,100,51.09961V88a4.00033,4.00033,0,0,1-5.19336,3.81787l-32-10a3.99911,3.99911,0,0,1-2.33594-1.93555L45.22168,51.29,33.26562,47.30469a4.02734,4.02734,0,0,0-1.27734-.20948A4.00877,4.00877,0,0,0,28,51.09961v52.62988a28.09229,28.09229,0,0,0,20.4502,26.9624L220,178.72607Z"/>
                    </svg>
                    Bali (DPS)
                </div>
                <div class="rounded w-full font-semibold flex items-center justify-center backdrop-blur-sm bg-white/30 p-2 gap-3">
                    <svg class="w-5 h-5"viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#ff4242"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M22.5 20V22C22.5 22.5523 22.0523 23 21.5 23H7.59646C6.66266 23 5.85314 22.3538 5.64619 21.4432L1.27764 2.22162C1.13542 1.59586 1.61105 1 2.25277 1H5.70799C6.17204 1 6.57512 1.31925 6.6814 1.77096L10.5 18H20.5C21.6046 18 22.5 18.8954 22.5 20Z" stroke="#71717A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M6.96729 3H8.99999C9.55228 3 10 3.44772 10 4V6L8 7.5" stroke="#71717A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M13.5 14.375H9.625H7.5" stroke="#71717A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
                    Economy
                </div>
            </div>
        </div>
        <div class="absolute cursor-pointer mt-10 pl-8">
            <a href="searchflight.php">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5 3 12m0 0 7.5-7.5M3 12h18" />
            </svg>
            </a>
        </div>
        <div class="w-3/4 m-auto mt-7 pl-8">
            <div class="flex justify-between items-center">
                <div class="flex gap-3 items-center">
                    <!-- Price -->
                    <div class="text-blue-500 justify-center gap-3 items-center flex drop-shadow-lg select-none rounded-full bg-white py-1 px-6 text-center align-middle font-sans text-sm font-bold shadow-md transition-all focus:opacity-[0.85] active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
                        <!-- Minprice -->
                        <div class="flex  justify-center items-center gap-1">
                            <p class="text-xs">Min</p>
                            <input name="minprice" id="minprice" type="number" class="text-gray-500 border w-32 p-1 rounded" min="0" placeholder="min price">
                        </div>
                        <!-- maxprice -->
                        <div class="flex justify-center items-center gap-1">
                            <p class="text-xs">Max</p>
                            <input name="maxprice" id="maxprice" type="number" class="text-gray-500 border w-32 p-1 rounded" placeholder="max price">
                        </div>
                    </div>
                </div>
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
                                <input type="radio" id="earlydeparture" name="sort" value="earlydeparture">
                                <label for="earlydeparture">Early Departure</label><br>
                            </li>
                        </form>
                    </ul>
                </div>
            </div>
            <br><br>
            <div class="flightList">
                <!-- component -->
                <div class="w-full hover:shadow-sky-200 hover:shadow-lg ">
                    <div class="max-w-full  bg-white flex flex-col rounded overflow-hidden shadow-lg ">
                        <div class="flex flex-row items-baseline flex-nowrap p-2">
                            <svg viewBox="0 0 64 64" data-testid="tripDetails-bound-plane-icon" pointer-events="all" aria-hidden="true" class="mt-2 mr-1" role="presentation" style="fill: rgb(102, 102, 102); height: 0.9rem; width: 0.9rem;">
                                <path d="M43.389 38.269L29.222 61.34a1.152 1.152 0 01-1.064.615H20.99a1.219 1.219 0 01-1.007-.5 1.324 1.324 0 01-.2-1.149L26.2 38.27H11.7l-3.947 6.919a1.209 1.209 0 01-1.092.644H1.285a1.234 1.234 0 01-.895-.392l-.057-.056a1.427 1.427 0 01-.308-1.036L1.789 32 .025 19.656a1.182 1.182 0 01.281-1.009 1.356 1.356 0 01.951-.448l5.4-.027a1.227 1.227 0 01.9.391.85.85 0 01.2.252L11.7 25.73h14.5L19.792 3.7a1.324 1.324 0 01.2-1.149A1.219 1.219 0 0121 2.045h7.168a1.152 1.152 0 011.064.615l14.162 23.071h8.959a17.287 17.287 0 017.839 1.791Q63.777 29.315 64 32q-.224 2.685-3.807 4.478a17.282 17.282 0 01-7.84 1.793h-9.016z"></path>
                            </svg>
                            <h1 class="ml-2 uppercase font-bold text-gray-500">departure</h1>
                            <div class="ml-2 font-normal text-gray-500" name="departuredate" id="departuredate">Wednesday 18 Aug</div>
                        </div>
                        <div class="mt-2 flex justify-start bg-white p-2">
                            <div class="flex mx-2 ml-6 h8 px-2 flex-row items-baseline rounded-full bg-gray-100 p-1">
                                <svg viewBox="0 0 64 64" pointer-events="all" aria-hidden="true" class="etiIcon css-jbc4oa" role="presentation" style="fill: rgb(102, 102, 102); height: 12px; width: 12px;">
                                <path d="M43.389 38.269L29.222 61.34a1.152 1.152 0 01-1.064.615H20.99a1.219 1.219 0 01-1.007-.5 1.324 1.324 0 01-.2-1.149L26.2 38.27H11.7l-3.947 6.919a1.209 1.209 0 01-1.092.644H1.285a1.234 1.234 0 01-.895-.392l-.057-.056a1.427 1.427 0 01-.308-1.036L1.789 32 .025 19.656a1.182 1.182 0 01.281-1.009 1.356 1.356 0 01.951-.448l5.4-.027a1.227 1.227 0 01.9.391.85.85 0 01.2.252L11.7 25.73h14.5L19.792 3.7a1.324 1.324 0 01.2-1.149A1.219 1.219 0 0121 2.045h7.168a1.152 1.152 0 011.064.615l14.162 23.071h8.959a17.287 17.287 0 017.839 1.791Q63.777 29.315 64 32q-.224 2.685-3.807 4.478a17.282 17.282 0 01-7.84 1.793h-9.016z"></path>
                                </svg>
                                <p class="font-normal text-sm ml-1 text-gray-500" name="seatclass" id="seatclass">Economy</p>
                            </div>
                        </div>
                        <div class="mt-2 flex sm:flex-row mx-6 sm:justify-between flex-wrap ">
                            <div class="flex flex-row place-items-center p-2">
                                <img alt="Qatar Airways" class="w-10 h-10" src="data:image/png;base64,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" style="opacity: 1; transform-origin: 0% 50% 0px; transform: none;" />
                                <div class="flex flex-col ml-2">
                                    <p class="text-sm text-gray-500 font-bold" name="flightname" id="flightname">Qatar Airways</p>
                                    <p class="text-sm text-gray-500" name="flightcode" id="flightcode">QR1456</p>
                                    <div class="flex flex-row ">
                                        <svg class="h-5 w-5"version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
                                            viewBox="0 0 224.039 224.039" xml:space="preserve">
                                        <path d="M216.539,52.26h-64.434V27.599c0-4.142-3.357-7.5-7.5-7.5H75.631c-4.143,0-7.5,3.358-7.5,7.5V52.26H7.5
                                            c-4.143,0-7.5,3.358-7.5,7.5v136.68c0,4.142,3.357,7.5,7.5,7.5h209.039c4.143,0,7.5-3.358,7.5-7.5V59.76
                                            C224.039,55.618,220.682,52.26,216.539,52.26z M75.631,67.26h68.975h21.852v121.68H57.582V67.26H75.631z M83.131,35.099h53.975
                                            V52.26H83.131V35.099z M15,67.26h27.582v121.68H15V67.26z M209.039,188.94h-27.582V67.26h27.582V188.94z"/>
                                        </svg>
                                        <div class="pl-1 text-sm text-gray-500" name="flightcapacity" id="flightcapacity">
                                            30kg
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="w-3/4 flex flex-row">
                                <div class="flex flex-col p-2">
                                    <p class="font-bold" name="starttime" id="starttime">18:25</p>
                                    <p class="text-gray-500"><span class="font-bold" name="originlocationcode" id="originlocationcode">HRE</span></p>
                                    <p class="text-gray-500" name="origincityname" id="origincityname">Zimbabwe</p>
                                </div>
                                <div class="line-container">
                                    <div class="circle"></div>
                                    <div class="line"></div>
                                    <div class="circle filled"></div>
                                </div>
                                <div class="flex flex-col flex-wrap p-2">
                                    <p class="font-bold"name="endtime" id="endtime">19:25</p>
                                    <p class="text-gray-500"><span class="font-bold" name="destinationlocationcode" id="destinationlocationcode">LUN</span></p>
                                    <p class="text-gray-500"name="destinationcityname" id="destinationcityname">Zambia</p>
                                </div>
                            </div>
                        </div>
                        <div class="mt-4 flex flex-row flex-wrap md:flex-nowrap justify-end items-baseline">
                            <div class="md:border-l-2 mx-6 md:border-dotted flex flex-row py-4 mr-6 flex-wrap">
                                <div class="text-md mx-2 flex flex-row items-center justify-center font-bold  text-orange-400">
                                    <p name="flightprice" id="flightprice">Rp3.000.000</p><span>/pax</span>
                                </div>
                                <button id="btnchoose" class="relative flex h-[50px] w-40 items-center justify-center overflow-hidden border border-cyan-400 bg-sky-400 text-white transition-all before:absolute before:h-0 before:w-0 before:rounded-full  before:bg-white before:duration-500 before:ease-out hover:text-cyan-400 hover:before:h-56 hover:before:w-56">
                                <span class="relative z-10">Choose</span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="https://unpkg.com/@material-tailwind/html@latest/scripts/script-name.js"></script>
    <script type="module" src="https://unpkg.com/@material-tailwind/html@latest/scripts/popover.js"></script>
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
</body>
</html>