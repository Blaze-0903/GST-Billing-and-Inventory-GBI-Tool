-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: 27auhpt8094l1zn
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `Name` varchar(50) DEFAULT NULL,
  `Mob_No` varchar(10) DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `Gst_No` varchar(15) DEFAULT NULL,
  `State` varchar(20) DEFAULT NULL,
  `last_T` date DEFAULT NULL,
  `Total_T` int DEFAULT NULL,
  `Last_Ttime` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES ('BLAZE','9422707704','NEW DELHI','01ASDFGH123456A','DELHI','2022-02-25',73251700,'11:11:58'),('SAHIL ','9503012981','BAGADGANJ, NAGPUR','27POIUYT1478522','MAHARASHTRA','2022-02-25',320960,'12:13:15');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoices`
--

DROP TABLE IF EXISTS `invoices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoices` (
  `Invoice_no` int DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Customer` varchar(20) DEFAULT NULL,
  `Time` time DEFAULT NULL,
  `T_amt` int DEFAULT NULL,
  `GST_Type` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoices`
--

LOCK TABLES `invoices` WRITE;
/*!40000 ALTER TABLE `invoices` DISABLE KEYS */;
INSERT INTO `invoices` VALUES (5,'2022-02-23','ARCHANA JUNGHARE','19:36:06',64900,0),(6,'2022-02-24','BLAZE','19:16:31',354000,1),(7,'2022-02-24','RAMESH JUNGHARE','19:21:17',59590,0),(8,'2022-02-25','SAHIL JUNGHARE','10:35:44',132160,0),(9,'2022-02-25','BLAZE','11:11:58',354000,1),(10,'2022-03-05','RAMESH','22:13:39',70800,0);
/*!40000 ALTER TABLE `invoices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_details`
--

DROP TABLE IF EXISTS `product_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_details` (
  `Items` varchar(50) DEFAULT NULL,
  `QTY` int DEFAULT NULL,
  `Rate` int DEFAULT NULL,
  `Tax_amt` int DEFAULT NULL,
  `Percent` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_details`
--

LOCK TABLES `product_details` WRITE;
/*!40000 ALTER TABLE `product_details` DISABLE KEYS */;
INSERT INTO `product_details` VALUES ('REFRIGERATOR',1,55000,64900,18,'2022-02-23','19:36:06'),('REFRIGERATOR',1,55000,64900,18,'2022-02-23','19:36:06'),('REFRIGERATOR',1,55000,64900,18,'2022-02-23','19:36:06'),('TELEVISION',1,60000,70800,18,'2022-02-23','19:40:36'),('TELEVISION',1,60000,70800,18,'2022-02-23','19:40:36'),('TELEVISION',1,60000,70800,18,'2022-02-23','19:40:36'),('TELEVISION',1,60000,70800,18,'2022-02-23','19:40:36'),('TELEVISION',5,60000,354000,18,'2022-02-24','19:16:31'),('TELEVISION',5,60000,354000,18,'2022-02-24','19:16:31'),('TELEVISION',5,60000,354000,18,'2022-02-24','19:16:31'),('TELEVISION',5,60000,354000,18,'2022-02-24','19:16:31'),('LAPTOP',1,50000,59590,18,'2022-02-24','19:21:17'),('WIRED KEYBOARD',1,500,59590,18,'2022-02-24','19:21:17'),('LAPTOP',1,50000,59590,18,'2022-02-24','19:21:17'),('WIRED KEYBOARD',1,500,59590,18,'2022-02-24','19:21:17'),('LAPTOP',1,50000,59590,18,'2022-02-24','19:21:17'),('WIRED KEYBOARD',1,500,59590,18,'2022-02-24','19:21:17'),('LAPTOP',1,50000,59590,18,'2022-02-24','19:21:17'),('WIRED KEYBOARD',1,500,59590,18,'2022-02-24','19:21:17'),('LAPTOP',1,50000,132160,18,'2022-02-25','10:35:44'),('TELEVISION',1,60000,132160,18,'2022-02-25','10:35:44'),('HEADPHONE',1,2000,132160,18,'2022-02-25','10:35:44'),('LAPTOP',1,50000,132160,18,'2022-02-25','10:35:44'),('TELEVISION',1,60000,132160,18,'2022-02-25','10:35:44'),('HEADPHONE',1,2000,132160,18,'2022-02-25','10:35:44'),('LAPTOP',1,50000,132160,18,'2022-02-25','10:35:44'),('TELEVISION',1,60000,132160,18,'2022-02-25','10:35:44'),('HEADPHONE',1,2000,132160,18,'2022-02-25','10:35:44'),('TELEVISION',5,60000,354000,18,'2022-02-25','11:11:58'),('TELEVISION',5,60000,354000,18,'2022-02-25','11:11:58'),('TELEVISION',5,60000,354000,18,'2022-02-25','11:11:58'),('TELEVISION',5,60000,354000,18,'2022-02-25','11:11:58'),('TELEVISION',1,6000,7080,18,'2022-02-25','11:50:44'),('LAPTOP',1,50000,59000,18,'2022-02-25','12:03:21'),('TELEVISION',1,60000,70800,18,'2022-02-25','12:13:15'),('TELEVISION',1,60000,70800,18,'2022-03-05','22:13:39');
/*!40000 ALTER TABLE `product_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `Name` varchar(100) DEFAULT NULL,
  `Total_stock` int DEFAULT NULL,
  `Rate` int DEFAULT NULL,
  `Gst_P` int DEFAULT NULL,
  `last_T` date DEFAULT NULL,
  `TIME` time DEFAULT NULL,
  `P_id` int NOT NULL,
  PRIMARY KEY (`P_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('TELEVISION',77,60000,18,'2022-03-05','22:13:39',1),('LAPTOP',10,50000,18,'2022-02-24','19:21:17',5),('WIRED KEYBOARD',10,500,18,'2022-02-24','19:21:17',6),('HEADPHONE',20,2000,18,'2022-02-25','10:35:44',9);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-18 20:35:23
