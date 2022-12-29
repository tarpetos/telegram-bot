-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: bot_db
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `'pass_gen_table_1342077785'`
--

DROP TABLE IF EXISTS `'pass_gen_table_1342077785'`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `'pass_gen_table_1342077785'` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password_description` varchar(384) DEFAULT NULL,
  `generated_password` varchar(384) DEFAULT NULL,
  `password_length` int DEFAULT NULL,
  `has_repetetive` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_data` (`password_description`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `'pass_gen_table_1342077785'`
--

LOCK TABLES `'pass_gen_table_1342077785'` WRITE;
/*!40000 ALTER TABLE `'pass_gen_table_1342077785'` DISABLE KEYS */;
/*!40000 ALTER TABLE `'pass_gen_table_1342077785'` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `'add_password_1342077785'` BEFORE INSERT ON `'pass_gen_table_1342077785'` FOR EACH ROW BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = 1342077785;
    
                    UPDATE statistics
                    SET pass_gen_insert_num = pass_gen_insert_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `'change_password_1342077785'` BEFORE UPDATE ON `'pass_gen_table_1342077785'` FOR EACH ROW BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = 1342077785;
    
                    UPDATE statistics
                    SET pass_gen_update_num = pass_gen_update_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `'delete_password_1342077785'` BEFORE DELETE ON `'pass_gen_table_1342077785'` FOR EACH ROW BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = 1342077785;
    
                    UPDATE statistics
                    SET pass_gen_delete_num = pass_gen_delete_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `'pass_gen_table_441547155'`
--

DROP TABLE IF EXISTS `'pass_gen_table_441547155'`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `'pass_gen_table_441547155'` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password_description` varchar(384) DEFAULT NULL,
  `generated_password` varchar(384) DEFAULT NULL,
  `password_length` int DEFAULT NULL,
  `has_repetetive` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_data` (`password_description`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `'pass_gen_table_441547155'`
--

LOCK TABLES `'pass_gen_table_441547155'` WRITE;
/*!40000 ALTER TABLE `'pass_gen_table_441547155'` DISABLE KEYS */;
INSERT INTO `'pass_gen_table_441547155'` VALUES (10,'password','|NdqGWdL^oW&n2pWdH',6,1),(15,'test','|NdG4asXZcU;tGBM*wO7QvfdjIsg',10,0),(16,'текст','|Ne3SPXI0ec>q!XUI0Y^cmQ|+Cjb',10,1),(17,'bebra','|NdJ5I{<G0djMeoS^!W0P5>bQHUI',10,0),(18,'gregeg','|NbffGyqosdjMnrXaH*fWB@n-Rsa',10,1),(19,'efwfwef wef ewf ew','|NeIXcmO~ELjZgLQ2=@XGXPNlU;q',10,1),(20,'text','|Nb-pJpgq8RsduGO8_kZEC5>oVgOG7WB^|PWB_CURRBi-IRGU9M*u|tQvhiIQUEjnC;)8$V*n=rH2?',30,1),(21,'beba','|NdS8EC3_`egJC#Apk`HbpSE|O#l',10,0);
/*!40000 ALTER TABLE `'pass_gen_table_441547155'` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `'add_password_441547155'` BEFORE INSERT ON `'pass_gen_table_441547155'` FOR EACH ROW BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = 441547155;
    
                    UPDATE statistics
                    SET pass_gen_insert_num = pass_gen_insert_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `'change_password_441547155'` BEFORE UPDATE ON `'pass_gen_table_441547155'` FOR EACH ROW BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = 441547155;
    
                    UPDATE statistics
                    SET pass_gen_update_num = pass_gen_update_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `'delete_password_441547155'` BEFORE DELETE ON `'pass_gen_table_441547155'` FOR EACH ROW BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = 441547155;
    
                    UPDATE statistics
                    SET pass_gen_delete_num = pass_gen_delete_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `'table_1342077785'`
--

DROP TABLE IF EXISTS `'table_1342077785'`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `'table_1342077785'` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_data` varchar(768) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_data` (`user_data`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `'table_1342077785'`
--

LOCK TABLES `'table_1342077785'` WRITE;
/*!40000 ALTER TABLE `'table_1342077785'` DISABLE KEYS */;
/*!40000 ALTER TABLE `'table_1342077785'` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `'add_task_1342077785'` BEFORE INSERT ON `'table_1342077785'` FOR EACH ROW BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = 1342077785;
    
                    UPDATE statistics
                    SET task_sched_insert_num = task_sched_insert_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `'change_task_1342077785'` BEFORE UPDATE ON `'table_1342077785'` FOR EACH ROW BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = 1342077785;
    
                    UPDATE statistics
                    SET task_sched_update_num = task_sched_update_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `'delete_task_1342077785'` BEFORE DELETE ON `'table_1342077785'` FOR EACH ROW BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = 1342077785;
    
                    UPDATE statistics
                    SET task_sched_delete_num = task_sched_delete_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `'table_441547155'`
--

DROP TABLE IF EXISTS `'table_441547155'`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `'table_441547155'` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_data` varchar(768) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_data` (`user_data`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `'table_441547155'`
--

LOCK TABLES `'table_441547155'` WRITE;
/*!40000 ALTER TABLE `'table_441547155'` DISABLE KEYS */;
INSERT INTO `'table_441547155'` VALUES (21,'Виконати зарядку'),(22,'Почитати книгу'),(23,'Вийти на прогулянку'),(24,'Полагодити годинник'),(32,'Повечеряти');
/*!40000 ALTER TABLE `'table_441547155'` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `'add_task_441547155'` BEFORE INSERT ON `'table_441547155'` FOR EACH ROW BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = 441547155;
    
                    UPDATE statistics
                    SET task_sched_insert_num = task_sched_insert_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `'change_task_441547155'` BEFORE UPDATE ON `'table_441547155'` FOR EACH ROW BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = 441547155;
    
                    UPDATE statistics
                    SET task_sched_update_num = task_sched_update_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `'delete_task_441547155'` BEFORE DELETE ON `'table_441547155'` FOR EACH ROW BEGIN
                    DECLARE date_now DATE;
                    DECLARE get_user_id INT;
    
                    SET date_now = CURDATE();
                    SET get_user_id = 441547155;
    
                    UPDATE statistics
                    SET task_sched_delete_num = task_sched_delete_num + 1
                    WHERE usage_date = date_now AND user_id = get_user_id;
                END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `generated_tokens`
--

DROP TABLE IF EXISTS `generated_tokens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `generated_tokens` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `user_token` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_token` (`user_id`),
  CONSTRAINT `generated_tokens_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users_info` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generated_tokens`
--

LOCK TABLES `generated_tokens` WRITE;
/*!40000 ALTER TABLE `generated_tokens` DISABLE KEYS */;
INSERT INTO `generated_tokens` VALUES (2,441547155,'|Nc<`d;op`d;mQFRsci*DgZ42W&l+HZ2)utVE|eHHvljIRsb#la{y@oV*qXdM*va)D*#6TC;&kKDFAZ-Q2-+VLjY6&KL9cSKmbGlE&y`?NC0jCS^#1Ia{w^_F#sq4QUC');
/*!40000 ALTER TABLE `generated_tokens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `statistics`
--

DROP TABLE IF EXISTS `statistics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `statistics` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usage_date` date NOT NULL,
  `user_id` int NOT NULL,
  `task_sched_delete_num` int DEFAULT '0',
  `task_sched_update_num` int DEFAULT '0',
  `task_sched_insert_num` int DEFAULT '0',
  `pass_gen_delete_num` int DEFAULT '0',
  `pass_gen_update_num` int DEFAULT '0',
  `pass_gen_insert_num` int DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_date_id` (`usage_date`,`user_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `statistics_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users_info` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statistics`
--

LOCK TABLES `statistics` WRITE;
/*!40000 ALTER TABLE `statistics` DISABLE KEYS */;
INSERT INTO `statistics` VALUES (9,'2022-12-23',639092726,1,1,10,1,1,1),(10,'2022-12-23',881067050,0,2,0,3,0,0),(34,'2022-12-25',1342077785,2,2,4,1,1,1),(77,'2022-12-28',441547155,0,0,0,0,0,4),(81,'2022-12-28',1342077785,3,1,1,0,0,0),(86,'2022-12-29',441547155,0,0,0,0,0,1);
/*!40000 ALTER TABLE `statistics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `statistics_view`
--

DROP TABLE IF EXISTS `statistics_view`;
/*!50001 DROP VIEW IF EXISTS `statistics_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `statistics_view` AS SELECT 
 1 AS `start_msg_date`,
 1 AS `usage_date`,
 1 AS `user_id`,
 1 AS `task_sched_delete_avg`,
 1 AS `task_sched_update_avg`,
 1 AS `task_sched_insert_avg`,
 1 AS `pass_gen_delete_avg`,
 1 AS `pass_gen_update_avg`,
 1 AS `pass_gen_insert_avg`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `stickers`
--

DROP TABLE IF EXISTS `stickers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stickers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sticker` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_sticker` (`sticker`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stickers`
--

LOCK TABLES `stickers` WRITE;
/*!40000 ALTER TABLE `stickers` DISABLE KEYS */;
INSERT INTO `stickers` VALUES (1,'CAACAgIAAxkBAAIfOGOofsgZfIgeAAHKizIbHf255iVfYgAC2AEAAmJlAwABrr93Q0yEp_osBA');
/*!40000 ALTER TABLE `stickers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_info`
--

DROP TABLE IF EXISTS `users_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_info` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `username` varchar(200) NOT NULL,
  `full_name` varchar(200) NOT NULL,
  `chat_id` varchar(30) NOT NULL,
  `start_msg_date` date DEFAULT (curdate()),
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_data` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1245 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_info`
--

LOCK TABLES `users_info` WRITE;
/*!40000 ALTER TABLE `users_info` DISABLE KEYS */;
INSERT INTO `users_info` VALUES (1,395897536,'anafaryniuk','ann','-1001400478962','2022-12-22'),(2,661245516,'draindeademogothprincess','metamorphose','-1001400478962','2022-12-22'),(3,441547155,'traus_mon','Tarpetos','441547155','2022-12-28'),(4,1342077785,'pompoussy','Mykola Bezrukyi','1342077785','2022-12-22'),(5,639092726,' ','Софі','-1001400478962','2022-12-22'),(6,881067050,' ','Perry Utkonos','-1001400478962','2022-12-22'),(7,891849290,'kosh1kkk','Артем Кошелюк','-1001400478962','2022-12-22'),(8,922145120,'FRXSTMXRN','Vlad','-1001400478962','2022-12-22'),(9,420823189,' ','Мироϟϟлав','-1001400478962','2022-12-22'),(10,428566833,'ost_adm','Євген','-1001400478962','2022-12-22'),(11,867324388,' ','Vlad','-1001400478962','2022-12-22'),(12,685244760,'dan1sssimo','dan1ssimo_','-1001400478962','2022-12-22');
/*!40000 ALTER TABLE `users_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `statistics_view`
--

/*!50001 DROP VIEW IF EXISTS `statistics_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `statistics_view` AS select `u`.`start_msg_date` AS `start_msg_date`,(select `s2`.`usage_date` from `statistics` `s2` where (`s2`.`user_id` = `s`.`user_id`) order by `s2`.`usage_date` desc limit 1) AS `usage_date`,`s`.`user_id` AS `user_id`,round(avg(`s`.`task_sched_delete_num`),0) AS `task_sched_delete_avg`,round(avg(`s`.`task_sched_update_num`),0) AS `task_sched_update_avg`,round(avg(`s`.`task_sched_insert_num`),0) AS `task_sched_insert_avg`,round(avg(`s`.`pass_gen_delete_num`),0) AS `pass_gen_delete_avg`,round(avg(`s`.`pass_gen_update_num`),0) AS `pass_gen_update_avg`,round(avg(`s`.`pass_gen_insert_num`),0) AS `pass_gen_insert_avg` from (`statistics` `s` join `users_info` `u` on((`s`.`user_id` = `u`.`user_id`))) where ((to_days(`s`.`usage_date`) - to_days(`u`.`start_msg_date`)) < 31) group by `s`.`user_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-29 20:51:56
