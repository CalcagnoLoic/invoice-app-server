-- Adminer 4.8.1 MySQL 11.3.2-MariaDB-1:11.3.2+maria~ubu2204 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `client_address`;
CREATE TABLE `client_address` (
  `client_street` varchar(128) NOT NULL,
  `invoice_id` varchar(128) DEFAULT NULL,
  `client_city` varchar(128) DEFAULT NULL,
  `client_postCode` varchar(128) DEFAULT NULL,
  `client_country` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`client_street`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `client_address` (`client_street`, `invoice_id`, `client_city`, `client_postCode`, `client_country`) VALUES
('',	'FV2353',	NULL,	NULL,	NULL),
('106 Kendell Street',	'RT3080',	'Sharrington',	'NR24 5WQ',	'United Kingdom'),
('3964  Queens Lane',	'TY9141',	'Gotham',	'60457',	'United States of America'),
('46 Abbey Row',	'AA1449',	'Cambridge',	'CB5 6EG',	'United Kingdom'),
('63 Warwick Road',	'RT2080',	'Carlisle',	'CA20 2TG',	'United Kingdom'),
('79 Dover Road',	'RG0314',	'Westhall',	'IP19 3PF',	'United Kingdom'),
('84 Church Way',	'XM9141',	'Bradford',	'BD1 9PB',	'United Kingdom');

DROP TABLE IF EXISTS `invoice`;
CREATE TABLE `invoice` (
  `id` varchar(6) NOT NULL,
  `sender_id` int(11) DEFAULT NULL,
  `client_id` varchar(128) DEFAULT NULL,
  `created_at` varchar(128) DEFAULT NULL,
  `payment_due` varchar(128) DEFAULT NULL,
  `description` varchar(128) DEFAULT NULL,
  `payment_terms` varchar(128) DEFAULT NULL,
  `client_name` varchar(128) DEFAULT NULL,
  `client_email` varchar(128) DEFAULT NULL,
  `status` varchar(128) DEFAULT NULL,
  `total` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sender_id` (`sender_id`),
  KEY `client_id` (`client_id`),
  CONSTRAINT `invoice_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `sender_address` (`id_sender`),
  CONSTRAINT `invoice_ibfk_2` FOREIGN KEY (`client_id`) REFERENCES `client_address` (`client_street`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `invoice` (`id`, `sender_id`, `client_id`, `created_at`, `payment_due`, `description`, `payment_terms`, `client_name`, `client_email`, `status`, `total`) VALUES
('AA1449',	5,	'46 Abbey Row',	'2021-10-7',	'2021-10-14',	'Re-branding',	'7',	'Mellisa Clarke',	'mellisa.clarke@example.com',	'pending',	4032.33),
('FV2353',	7,	NULL,	'2021-11-05',	'2021-11-12',	'Logo Re-design',	'7',	'Anita Wainwright',	NULL,	'draft',	3102.04),
('RG0314',	3,	'79 Dover Road',	'2021-9-24',	'2021-10-01',	'Website Redesign',	'7',	'John Morrison',	'jm@myco.com',	'paid',	14002.3),
('RT2080',	4,	'63 Warwick Road',	'2021-10-11',	'2021-10-12',	'Logo Concept',	'1',	'Alysa Werner',	'alysa@email.co.uk',	'pending',	102.04),
('RT3080',	1,	'106 Kendell Street',	'2021-8-18',	'2021-8-19',	'Re-branding',	'1',	'Jensen Huang',	'jensenh@mail.com',	'paid',	1800.9),
('TY9141',	6,	'3964  Queens Lane',	'2021-10-01',	'2021-10-31',	'Landing Page Design',	'30',	'Thomas Wayne',	'thomas@dc.com',	'pending',	6155.91),
('XM9141',	2,	'84 Church Way',	'2021-8-21',	'2021-9-20',	'Graphic Design',	'30',	'Alex Grim',	'alexgrim@mail.com',	'pending',	556);

DROP TABLE IF EXISTS `items`;
CREATE TABLE `items` (
  `items_id` int(11) NOT NULL AUTO_INCREMENT,
  `invoice_id` varchar(128) DEFAULT NULL,
  `name` varchar(128) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `total` float DEFAULT NULL,
  PRIMARY KEY (`items_id`),
  KEY `invoice_id` (`invoice_id`),
  CONSTRAINT `items_ibfk_1` FOREIGN KEY (`invoice_id`) REFERENCES `invoice` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `items` (`items_id`, `invoice_id`, `name`, `quantity`, `price`, `total`) VALUES
(1,	'RT3080',	'Brand Guidelines',	1,	1800.9,	1800.9),
(2,	'XM9141',	'Banner Design',	1,	156,	156),
(3,	'XM9141',	'Email Design',	2,	200,	400),
(4,	'RG0314',	'Website Redesign',	1,	14002.3,	14002.3),
(5,	'RT2080',	'Logo Sketches',	1,	102.04,	102.04),
(6,	'AA1449',	'New Logo',	1,	1532.33,	1532.33),
(7,	'AA1449',	'Brand Guidelines',	1,	2500,	2500),
(8,	'TY9141',	'Web Design',	1,	6155.91,	6155.91),
(9,	'FV2353',	'Logo Re-design',	1,	3102.04,	3102.04);

DROP TABLE IF EXISTS `sender_address`;
CREATE TABLE `sender_address` (
  `id_sender` int(11) NOT NULL AUTO_INCREMENT,
  `street` varchar(128) DEFAULT NULL,
  `invoice_id` varchar(128) DEFAULT NULL,
  `city` varchar(128) DEFAULT NULL,
  `postCode` varchar(128) DEFAULT NULL,
  `country` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id_sender`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `sender_address` (`id_sender`, `street`, `invoice_id`, `city`, `postCode`, `country`) VALUES
(1,	'19 Union Terrace',	'RT3080',	'London',	'E1 3EZ',	'United Kingdom'),
(2,	'19 Union Terrace',	'XM9141',	'London',	'E1 3EZ',	'United Kingdom'),
(3,	'19 Union Terrace',	'RG0314',	'London',	'E1 3EZ',	'United Kingdom'),
(4,	'19 Union Terrace',	'RT2080',	'London',	'E1 3EZ',	'United Kingdom'),
(5,	'19 Union Terrace',	'AA1449',	'London',	'E1 3EZ',	'United Kingdom'),
(6,	'19 Union Terrace',	'TY9141',	'London',	'E1 3EZ',	'United Kingdom'),
(7,	'19 Union Terrace',	'FV2353',	'London',	'E1 3EZ',	'United Kingdom');

-- 2024-05-31 08:07:07