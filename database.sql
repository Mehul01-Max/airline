-- MySQL dump 10.13  Distrib 8.0.34, for macos13 (arm64)
--
-- Host: localhost    Database: flight_ticket_booking_system
-- ------------------------------------------------------
-- Server version	8.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Available_flights`
--

DROP TABLE IF EXISTS `Available_flights`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Available_flights` (
  `Flight_No` int NOT NULL,
  `Airline` varchar(30) DEFAULT NULL,
  `Departure` varchar(30) DEFAULT NULL,
  `Arrival` varchar(30) DEFAULT NULL,
  `Departure_time` time DEFAULT NULL,
  `departure_date` date DEFAULT NULL,
  `arrival_time` time DEFAULT NULL,
  `arrival_date` date DEFAULT NULL,
  `PRICE` float DEFAULT NULL,
  `Available_seat` int DEFAULT NULL,
  PRIMARY KEY (`Flight_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Available_flights`
--

LOCK TABLES `Available_flights` WRITE;
/*!40000 ALTER TABLE `Available_flights` DISABLE KEYS */;
INSERT INTO `Available_flights` VALUES (401,'AIR INDIA EXPRESS','KOLKATA','SURAT','11:20:00','2023-11-06','14:25:00','2023-11-06',5999,144),(402,'AIR INDIA','MUMBAI','KOLKATA','06:00:00','2023-11-05','08:40:00','2023-11-05',9227,88),(403,'VISTARA','NEW DELHI','PARIS','13:45:00','2023-11-03','18:40:00','2023-11-03',27910,14),(404,'VISTARA','LONDON','MUMBAI','20:55:00','2023-11-04','11:45:00','2023-11-05',63357,51),(501,'INDIGO','NEW DELHI','MUMBAI','14:00:00','2023-11-03','16:20:00','2023-11-03',5357,0),(502,'INDIGO','KOLKATA','JAIPUR','08:15:00','2023-11-02','20:40:00','2023-11-02',8624,99),(601,'SPICEJET','NEW DELHI','DUBAI','19:15:00','2023-11-03','22:05:00','2023-11-03',13279,0);
/*!40000 ALTER TABLE `Available_flights` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking_details`
--

DROP TABLE IF EXISTS `booking_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking_details` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Passenger_Name` varchar(30) DEFAULT NULL,
  `Booking_ID` bigint DEFAULT NULL,
  `PNR_no` bigint DEFAULT NULL,
  `Booked_By` varchar(40) DEFAULT NULL,
  `Flight_no` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking_details`
--

LOCK TABLES `booking_details` WRITE;
/*!40000 ALTER TABLE `booking_details` DISABLE KEYS */;
INSERT INTO `booking_details` VALUES (17,'Harshil Agarwal',1003,6011003,'Anita Agarwal(8)',601),(50,'c',1004,4011004,'a(11)',401),(51,'aa',1005,5011005,'Mehul Agarwal(6)',501),(52,'bb',1005,5011005,'Mehul Agarwal(6)',501),(53,'cc',1005,5011005,'Mehul Agarwal(6)',501),(54,'dd',1005,5011005,'Mehul Agarwal(6)',501);
/*!40000 ALTER TABLE `booking_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer_details`
--

DROP TABLE IF EXISTS `Customer_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer_details` (
  `CUS_ID` bigint NOT NULL AUTO_INCREMENT,
  `CUSTOMER_Name` varchar(30) DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `Phone_no` bigint DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`CUS_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer_details`
--

LOCK TABLES `Customer_details` WRITE;
/*!40000 ALTER TABLE `Customer_details` DISABLE KEYS */;
INSERT INTO `Customer_details` VALUES (6,'Mehul Agarwal','Hindmotor',9330562599,'agarwalmehul423@gmail.com'),(7,'Hardik Kaushik','Dankuni',8100242583,'hardikkaushik18@gmail.com'),(8,'Anita Agarwal','Hindmotor',877291963,'anu.agrl501@gmail.com'),(9,'Harshil Agarwal','Hindmotor',6291771357,'harshilagarwal300@gmail.com'),(10,'Mehul Agarwal','199, Debai Pukur Road',9836392379,'agarwalajay300@gmail.com'),(11,'a','abc',0,'ajc@gmail.com');
/*!40000 ALTER TABLE `Customer_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-27 17:54:17
