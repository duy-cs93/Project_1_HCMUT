-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: sale_management
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `bill` (
  `bill_code` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `employee_code` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `bill_date` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `bill_time` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_code` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `total_cost` float DEFAULT NULL,
  `discount` int(11) DEFAULT NULL,
  `bill_cost` float DEFAULT NULL,
  `bill_note` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bill_detail`
--

DROP TABLE IF EXISTS `bill_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `bill_detail` (
  `bill_code` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `product_code` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `product_quantity` int(11) DEFAULT NULL,
  `into_money` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill_detail`
--

LOCK TABLES `bill_detail` WRITE;
/*!40000 ALTER TABLE `bill_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `bill_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `customer` (
  `customer_code` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_address` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_phone` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_sex` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_DOB` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_DOP` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `employee` (
  `employee_code` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `employee_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `employee_sex` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `employee_address` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `employee_phone` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `employee_DOB` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `employee_FWD` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `employee_salary` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `product` (
  `product_code` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `product_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `product_category` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `product_image` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `product_brand` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `product_price` float DEFAULT NULL,
  `product_detail` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_table`
--

DROP TABLE IF EXISTS `test_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `test_table` (
  `id` int(11) DEFAULT NULL,
  `col_1` int(11) DEFAULT NULL,
  `col_2` int(11) DEFAULT NULL,
  `col_3` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_table`
--

LOCK TABLES `test_table` WRITE;
/*!40000 ALTER TABLE `test_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `warehouse`
--

DROP TABLE IF EXISTS `warehouse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `warehouse` (
  `product_code` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `inventory_number` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warehouse`
--

LOCK TABLES `warehouse` WRITE;
/*!40000 ALTER TABLE `warehouse` DISABLE KEYS */;
/*!40000 ALTER TABLE `warehouse` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-18 12:08:23
