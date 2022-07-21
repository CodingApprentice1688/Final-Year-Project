-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 08, 2022 at 09:50 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `healthcare_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointments`
--

CREATE TABLE `appointments` (
  `appointment_id` int(11) NOT NULL,
  `queue_number` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `nric` varchar(10) NOT NULL,
  `date_slot` date NOT NULL,
  `app_time` time NOT NULL,
  `department` varchar(50) NOT NULL,
  `attending` varchar(50) NOT NULL,
  `reason` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `appointments`
--

INSERT INTO `appointments` (`appointment_id`, `queue_number`, `username`, `name`, `nric`, `date_slot`, `app_time`, `department`, `attending`, `reason`) VALUES
(1, 0, 'wenling', 'Leong Wen Ling', 'H32345678', '2022-06-18', '13:00:00', 'ENT', 'Greg Han', 'Follow up on middle ear infection'),
(2, 0, 'wenling', 'Leong Wen Ling', 'H32345678', '2022-06-01', '13:00:00', 'A&E', 'Greg Han', 'Middle ear infection'),
(3, 0, 'morgan', 'Kuo Tzu-Chi', 'P32345678', '2022-07-15', '15:30:00', 'Radiology', 'Shin Tan', 'take lung x-ray'),
(7, 0, 'morgan', 'Kuo Tzu-Chi', 'P32345678', '2022-07-22', '16:00:00', 'Radiology', 'Shin Tan', 'Follow up on the treatment'),
(8, 0, 'wenling', 'Leong Wen Ling', 'H32345678', '2022-07-18', '10:00:00', 'ENT', 'Greg Han', 'Follow up on middle ear infection'),
(9, 0, 'davidgenius', 'David Genius', 'T1234567P', '2022-06-29', '11:45:00', 'GP', 'Stephen Strange', 'High fever');

-- --------------------------------------------------------

--
-- Table structure for table `medicalrecords`
--

CREATE TABLE `medicalrecords` (
  `record_id` int(11) NOT NULL,
  `appointment_id` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `vaccination_status` varchar(255) DEFAULT NULL,
  `blood_pressure` varchar(255) DEFAULT NULL,
  `temperature` varchar(255) DEFAULT NULL,
  `heart_rate` varchar(255) DEFAULT NULL,
  `allergies` varchar(255) DEFAULT NULL,
  `medicine` varchar(255) DEFAULT NULL,
  `diagnosis` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `medicalrecords`
--

INSERT INTO `medicalrecords` (`record_id`, `appointment_id`, `username`, `vaccination_status`, `blood_pressure`, `temperature`, `heart_rate`, `allergies`, `medicine`, `diagnosis`) VALUES
(1, 3, 'morgan', 'Vaccinated', '120/80 mmHg', '37.6 degrees Celsius', '70 bpm', 'Pet allergies', 'Telfast D. Qty: 20 tab/s', 'Flu symptoms, nasal congestion.'),
(2, 7, 'morgan', 'Vaccinated', '100/50 mmHg', '37.6 degrees Celsius', '70 bpm', 'Pet allergies', 'Some lung medicine, etc.', 'Noisy breathing and wheezing.'),
(3, 9, 'davidgenius', 'Vaccinated', '200/98 mmHg', '37.0 degrees Celsius', '170 bpm', 'Pollens, Peanuts', 'Insulin', 'Elevated blood sugar levels and dehydration. Diagnosed with type II diabetes.');

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `role_id` int(11) NOT NULL,
  `roleName` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`role_id`, `roleName`) VALUES
(1, 'wenling'),
(2, 'helloooo');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `name` varchar(50) NOT NULL,
  `nric` varchar(10) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `role` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `password`, `name`, `nric`, `age`, `gender`, `role`) VALUES
('davidgenius', 'password', 'David Genius', 'T1234567P', 21, 'Male', 'patient'),
('hugotan', 'password', 'Hugo Tan', 'M12345678', 23, 'Male', 'patient'),
('johnbenedict', 'password', 'John Benedict', 'G22345678', 21, 'Male', 'patient'),
('jonathandoe', 'password', 'Jonathan Doe', 'Q12345678', 30, 'Male', 'patient'),
('kings', 'password', 'Seah Kings Lee', 'J32345654', 21, 'Male', 'healthcare staff'),
('morgan', 'password', 'Kuo Tzu-Chi', 'P32345678', 20, 'Female', 'patient'),
('oswal', 'password', 'Oswal', 'F34542343', 30, 'Male', 'patient'),
('oswaldo', 'password', 'Oswaldo', 'T1235467P', 21, 'Male', 'IT admin'),
('rebeccabetty', 'password', 'Rebecca Betty', 'P12345678', 25, 'Female', 'patient'),
('robertwilson', 'password', 'Robert Wilson', 'Y12345678', 33, 'Male', 'patient'),
('wenling', 'password', 'Leong Wen Ling', 'H32345678', 30, 'Female', 'patient');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointments`
--
ALTER TABLE `appointments`
  ADD PRIMARY KEY (`appointment_id`);

--
-- Indexes for table `medicalrecords`
--
ALTER TABLE `medicalrecords`
  ADD PRIMARY KEY (`record_id`),
  ADD KEY `appointment_id` (`appointment_id`),
  ADD KEY `username` (`username`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`role_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointments`
--
ALTER TABLE `appointments`
  MODIFY `appointment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `medicalrecords`
--
ALTER TABLE `medicalrecords`
  MODIFY `record_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `role_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `medicalrecords`
--
ALTER TABLE `medicalrecords`
  ADD CONSTRAINT `medicalrecords_ibfk_1` FOREIGN KEY (`appointment_id`) REFERENCES `appointments` (`appointment_id`),
  ADD CONSTRAINT `medicalrecords_ibfk_2` FOREIGN KEY (`username`) REFERENCES `user` (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
