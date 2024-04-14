-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 22, 2023 at 05:21 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `car-rental`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `name`, `email`, `password`) VALUES
(1, 'admin', 'admin@gmail.com', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

CREATE TABLE `bookings` (
  `id` int(20) NOT NULL,
  `to_booking_date` varchar(265) NOT NULL,
  `from_booking_date` varchar(255) NOT NULL,
  `car_id` varchar(255) NOT NULL,
  `cus_id` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`id`, `to_booking_date`, `from_booking_date`, `car_id`, `cus_id`) VALUES
(48, 'None', 'None', '1', '7'),
(49, '2023-04-22', '2023-04-23', '9', '14'),
(50, '2023-04-22', '2023-04-23', '6', '14');

-- --------------------------------------------------------

--
-- Table structure for table `cab_booking`
--

CREATE TABLE `cab_booking` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `from_location` varchar(255) NOT NULL,
  `to_location` varchar(255) NOT NULL,
  `booking_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `car_type` varchar(255) NOT NULL,
  `cab_id` int(11) DEFAULT NULL,
  `completed_on` timestamp NULL DEFAULT NULL,
  `created_on` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cab_booking`
--

INSERT INTO `cab_booking` (`id`, `user_id`, `from_location`, `to_location`, `booking_date`, `car_type`, `cab_id`, `completed_on`, `created_on`) VALUES
(12, 16, 'Viman Nagar', 'Mumbai Central', '2023-04-22 13:09:01', 'HatchBack', 3, '2023-04-22 13:09:01', '2023-04-22 13:07:28'),
(13, 3, 'Andheri', 'Juhu', '2023-04-22 13:21:24', 'HatchBack', 3, '2023-04-22 13:21:24', '2023-04-22 13:10:39'),
(14, 17, 'Mumbai Central', 'Kurla', '2023-04-22 14:01:54', 'Sedan', 14, '2023-04-22 14:01:54', '2023-04-22 13:59:03'),
(15, 7, 'Worli', 'Deccan', '2023-04-22 15:03:35', 'Sedan', 15, '2023-04-22 15:03:35', '2023-04-22 15:02:20'),
(16, 15, 'Andheri', 'Kothrud', '2023-04-22 15:05:21', 'Sedan', 16, '2023-04-22 15:05:21', '2023-04-22 15:04:21');

-- --------------------------------------------------------

--
-- Table structure for table `cab_driver`
--

CREATE TABLE `cab_driver` (
  `id` int(11) NOT NULL,
  `dirver_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `car_category` varchar(255) NOT NULL,
  `seats` int(11) NOT NULL,
  `status` int(11) NOT NULL DEFAULT 0,
  `created_on` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cab_driver`
--

INSERT INTO `cab_driver` (`id`, `dirver_name`, `email`, `password`, `car_category`, `seats`, `status`, `created_on`) VALUES
(1, 'cab', 'cab@gmail.com', '123456', 'Sedan', 7, 0, '2023-04-07 10:10:06'),
(2, 'Jacky Chain', 'jacky@gmail.com', '123456', 'Sedan', 3, 0, '2023-04-08 12:12:53'),
(3, 'hatchback', 'hatchback@gmail.com', '123456', 'HatchBack', 5, 0, '2023-04-21 15:29:34'),
(4, 'abby', 'abby@gmail.com', '123456', 'SUV', 4, 0, '2023-04-22 11:04:54'),
(5, 'abby', 'abby@gmail.com', '123456', 'SUV', 5, 0, '2023-04-22 11:07:22'),
(6, 'bb', 'bb@gmail.com', '123456', 'Sedan', 5, 0, '2023-04-22 11:08:35'),
(14, 'abcd', 'abcd@gmail.com', '123456', 'Sedan', 4, 0, '2023-04-22 14:01:41'),
(15, 'aayush', 'aayushchintre2002@gmail.com', '123456', 'Sedan', 4, 0, '2023-04-22 15:03:16'),
(16, 'aaa', 'aaa@gmail.com', '123456', 'Sedan', 4, 0, '2023-04-22 15:05:01');

-- --------------------------------------------------------

--
-- Table structure for table `car`
--

CREATE TABLE `car` (
  `id` int(255) NOT NULL,
  `car_name` varchar(255) NOT NULL,
  `driver_id` varchar(255) NOT NULL,
  `vehicle_no` varchar(255) NOT NULL,
  `allocated_status` varchar(255) NOT NULL,
  `cat_id` varchar(255) NOT NULL,
  `car_image` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `car`
--

INSERT INTO `car` (`id`, `car_name`, `driver_id`, `vehicle_no`, `allocated_status`, `cat_id`, `car_image`) VALUES
(1, 'drizer', '2', '3252', 'no', '1', 'https://imgd.aeplcdn.com/1200x900/n/cw/ec/45691/marutisuzuki-dzire-right-front-three-quarter8.jpeg?q=75'),
(2, 'wagonar', '9', '3563', 'no', '2', 'https://rb.gy/8oese'),
(3, 'xuv 700', '1', '4642', 'yes', '1', 'https://www.drivespark.com/car-image/320x225x100/car/x33804656-mahindra_xuv700.jpg.pagespeed.ic.EqO6GE1GEn.jpg'),
(4, 'Forturner', '1', '5679', 'yes', '1', 'https://cdni.autocarindia.com/Utils/ImageResizer.ashx?n=http://cms.haymarketindia.net/model/uploads/modelimages/Toyota-Fortuner-110120211829.jpg&w=730&h=484&q=75&c=1'),
(5, 'Honda Civic', '1', '3532', 'yes', '7', 'https://images.hgmsites.net/lrg/2020-honda-civic-sport-manual-angular-front-exterior-view_100751892_l.jpg'),
(6, 'i10', '1', '4567', 'yes', '8', 'https://imgd.aeplcdn.com/1056x594/n/dstjksa_1470085.jpg?q=75&wm=1');

-- --------------------------------------------------------

--
-- Table structure for table `car_catergory`
--

CREATE TABLE `car_catergory` (
  `id` int(25) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `car_catergory`
--

INSERT INTO `car_catergory` (`id`, `name`) VALUES
(1, 'SUV'),
(2, 'Sedan'),
(3, 'HatchBack'),
(4, 'Premium'),
(5, 'prime');

-- --------------------------------------------------------

--
-- Table structure for table `driver`
--

CREATE TABLE `driver` (
  `Id` int(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `mobile` int(10) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `driver`
--

INSERT INTO `driver` (`Id`, `name`, `email`, `gender`, `mobile`, `created_at`, `updated_at`) VALUES
(2, 'addy', 'addy@gmail.com', 'male', 919191919, '2022-04-18 05:23:29', NULL),
(9, 'pqr', 'pqr@gmail.com', 'male', 929292929, '2022-04-18 10:59:36', NULL),
(10, 'santy', 'santy@gmail.com', 'male', 939393939, '2022-04-18 11:49:00', NULL),
(12, 'Tom Cruz', 'tom@gmail.com', 'male', 949494949, '2023-04-08 11:55:41', NULL),
(13, 'Alex', 'alex@gmail.com', 'male', 959595959, '2023-04-22 10:52:15', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `fair_tb`
--

CREATE TABLE `fair_tb` (
  `id` int(255) NOT NULL,
  `cat_type` varchar(255) NOT NULL,
  `per_km` int(70) NOT NULL,
  `basic_charge` int(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fair_tb`
--

INSERT INTO `fair_tb` (`id`, `cat_type`, `per_km`, `basic_charge`) VALUES
(1, '1', 70, 200),
(2, '6', 450, 1000),
(3, '3', 50, 300),
(4, '7', 30, 700),
(5, '8', 40, 400);

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

CREATE TABLE `location` (
  `id` int(255) NOT NULL,
  `to_location` varchar(255) NOT NULL,
  `from_location` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `location`
--

INSERT INTO `location` (`id`, `to_location`, `from_location`) VALUES
(1, 'Mumbai', 'Mumbai'),
(2, 'Pune', 'Pune'),
(3, 'Thane', 'Thane'),
(4, 'Nagpur', 'Nagpur'),
(5, 'Andheri', 'Andheri\r\n'),
(6, 'Bandra', 'Bandra');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(10) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES
(1, 'aayush', 'aayush@gmail.com', '123456'),
(5, 'abc', 'abc@gmail.com', '123456'),
(7, 'xyz', 'xyz@gmail.com', '123456'),
(13, 'AAyu', 'aayushchintre2002@gmail.com', '123456'),
(14, 'aa', 'aa@gmail.com', '123456'),
(15, 'virat', 'virat@gmail.com', '123456'),
(16, 'alok', 'alok@gmail.com', '123456'),
(17, 'qwe', 'qwe@gmail.com', '123456'),
(18, 'tre', 'tre@gmail.com', '123456'),
(19, 'xyz', 'xyz@gmail.com', '123456'),
(20, 'poi', 'poi@gmail.com', '123456'),
(21, 'bhbh', 'bhbh@gmail.com', '123456');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bookings`
--
ALTER TABLE `bookings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cab_booking`
--
ALTER TABLE `cab_booking`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cab_driver`
--
ALTER TABLE `cab_driver`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `car`
--
ALTER TABLE `car`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `car_catergory`
--
ALTER TABLE `car_catergory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `driver`
--
ALTER TABLE `driver`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `fair_tb`
--
ALTER TABLE `fair_tb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `bookings`
--
ALTER TABLE `bookings`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `cab_booking`
--
ALTER TABLE `cab_booking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `cab_driver`
--
ALTER TABLE `cab_driver`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `car`
--
ALTER TABLE `car`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `car_catergory`
--
ALTER TABLE `car_catergory`
  MODIFY `id` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `driver`
--
ALTER TABLE `driver`
  MODIFY `Id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `fair_tb`
--
ALTER TABLE `fair_tb`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `location`
--
ALTER TABLE `location`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
