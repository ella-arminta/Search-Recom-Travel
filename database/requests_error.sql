-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 10, 2024 at 06:25 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.1.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `soa_searchrecom`
--

-- --------------------------------------------------------

--
-- Table structure for table `requests_error`
--

CREATE TABLE `requests_error` (
  `id` int(11) NOT NULL,
  `id_service` int(11) DEFAULT NULL,
  `id_service_type` int(11) DEFAULT NULL,
  `path` text NOT NULL,
  `error_message` text NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `requests_error`
--

--
-- Indexes for dumped tables
--

--
-- Indexes for table `requests_error`
--
ALTER TABLE `requests_error`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_service` (`id_service`),
  ADD KEY `id_service_type` (`id_service_type`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `requests_error`
--
ALTER TABLE `requests_error`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `requests_error`
--
ALTER TABLE `requests_error`
  ADD CONSTRAINT `requests_error_ibfk_1` FOREIGN KEY (`id_service`) REFERENCES `services` (`id`),
  ADD CONSTRAINT `requests_error_ibfk_2` FOREIGN KEY (`id_service_type`) REFERENCES `service_type` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
