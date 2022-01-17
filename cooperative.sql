-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 17, 2022 at 06:41 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.3.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cooperative`
--

-- --------------------------------------------------------

--
-- Table structure for table `account_deductions`
--

CREATE TABLE `account_deductions` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `ippis_no` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `salary_institution_id` int(11) NOT NULL,
  `transaction_period_id` int(11) NOT NULL,
  `transaction_status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `account_types`
--

CREATE TABLE `account_types` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `account_types`
--

INSERT INTO `account_types` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'SAVINGS', '2021-12-14 00:49:14.725527', '2021-12-14 00:49:14.725527'),
(2, 'CURRENT', '2021-12-14 00:49:14.752418', '2021-12-14 00:49:14.752418');

-- --------------------------------------------------------

--
-- Table structure for table `admin_charges`
--

CREATE TABLE `admin_charges` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin_charges`
--

INSERT INTO `admin_charges` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'PERCENTAGE', '2021-12-07 19:03:17.635680', '2021-12-07 19:03:17.635680'),
(2, 'CASH', '2021-12-07 19:03:17.683649', '2021-12-07 19:03:17.684649');

-- --------------------------------------------------------

--
-- Table structure for table `admin_master`
--

CREATE TABLE `admin_master` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `admin_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin_master`
--

INSERT INTO `admin_master` (`id`, `created_at`, `updated_at`, `admin_id`) VALUES
(1, '2021-12-07 18:50:59.018807', '2021-12-07 18:50:59.118783', 1);

-- --------------------------------------------------------

--
-- Table structure for table `approvable_transactions`
--

CREATE TABLE `approvable_transactions` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `status_id` int(11) NOT NULL,
  `transaction_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `approvable_transactions`
--

INSERT INTO `approvable_transactions` (`id`, `created_at`, `updated_at`, `status_id`, `transaction_id`) VALUES
(1, '2021-12-13 17:42:24.857216', '2021-12-13 17:42:24.857216', 1, 16),
(2, '2021-12-13 19:08:22.536488', '2021-12-13 19:08:22.536488', 1, 15),
(3, '2021-12-15 05:14:18.351147', '2021-12-15 05:14:18.351147', 1, 18),
(4, '2021-12-15 22:25:45.222402', '2021-12-15 22:25:45.222402', 1, 19),
(5, '2021-12-16 07:43:13.266603', '2021-12-16 07:43:13.266603', 1, 1),
(6, '2021-12-16 13:29:43.623352', '2021-12-16 13:29:43.623352', 1, 8),
(8, '2021-12-31 07:07:57.480483', '2021-12-31 07:07:57.480483', 1, 12),
(9, '2021-12-31 07:46:05.974015', '2021-12-31 07:46:05.974015', 1, 7);

-- --------------------------------------------------------

--
-- Table structure for table `approval_officers`
--

CREATE TABLE `approval_officers` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `officer_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL,
  `transaction_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `approval_officers`
--

INSERT INTO `approval_officers` (`id`, `created_at`, `updated_at`, `officer_id`, `status_id`, `transaction_id`) VALUES
(1, '2021-12-13 17:43:08.869987', '2021-12-13 17:43:08.869987', 11, 1, 1),
(2, '2021-12-13 19:08:46.085755', '2021-12-13 19:08:46.085755', 2, 1, 2),
(3, '2021-12-13 19:08:51.427240', '2021-12-13 19:08:51.427240', 3, 1, 2),
(4, '2021-12-15 05:14:42.165916', '2021-12-15 05:14:42.165916', 2, 1, 3),
(5, '2021-12-15 04:49:01.010588', '2021-12-15 04:49:01.010588', 3, 1, 3),
(6, '2021-12-15 22:26:20.885632', '2021-12-15 22:26:20.885632', 11, 1, 4),
(7, '2021-12-16 07:43:35.294368', '2021-12-16 07:43:35.294368', 2, 1, 5),
(8, '2021-12-16 07:43:40.722433', '2021-12-16 07:43:40.722433', 3, 1, 5),
(9, '2021-12-16 13:33:46.509407', '2021-12-16 13:33:46.509407', 2, 1, 6),
(11, '2021-12-31 07:08:30.812343', '2021-12-31 07:08:30.812343', 11, 1, 8),
(12, '2021-12-31 07:46:39.695344', '2021-12-31 07:46:39.695344', 11, 1, 9);

-- --------------------------------------------------------

--
-- Table structure for table `approval_status`
--

CREATE TABLE `approval_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `approval_status`
--

INSERT INTO `approval_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'PENDING', '2021-12-07 19:00:15.679772', '2021-12-07 19:00:15.679772'),
(2, 'APPROVED', '2021-12-07 19:00:15.723748', '2021-12-07 19:00:15.723748'),
(3, 'NOT APPROVED', '2021-12-07 19:00:15.866656', '2021-12-07 19:00:15.866656');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_customuser'),
(22, 'Can change user', 6, 'change_customuser'),
(23, 'Can delete user', 6, 'delete_customuser'),
(24, 'Can view user', 6, 'view_customuser'),
(25, 'Can add account types', 7, 'add_accounttypes'),
(26, 'Can change account types', 7, 'change_accounttypes'),
(27, 'Can delete account types', 7, 'delete_accounttypes'),
(28, 'Can view account types', 7, 'view_accounttypes'),
(29, 'Can add admin charges', 8, 'add_admincharges'),
(30, 'Can change admin charges', 8, 'change_admincharges'),
(31, 'Can delete admin charges', 8, 'delete_admincharges'),
(32, 'Can view admin charges', 8, 'view_admincharges'),
(33, 'Can add approvable transactions', 9, 'add_approvabletransactions'),
(34, 'Can change approvable transactions', 9, 'change_approvabletransactions'),
(35, 'Can delete approvable transactions', 9, 'delete_approvabletransactions'),
(36, 'Can view approvable transactions', 9, 'view_approvabletransactions'),
(37, 'Can add approval officers', 10, 'add_approvalofficers'),
(38, 'Can change approval officers', 10, 'change_approvalofficers'),
(39, 'Can delete approval officers', 10, 'delete_approvalofficers'),
(40, 'Can view approval officers', 10, 'view_approvalofficers'),
(41, 'Can add approval status', 11, 'add_approvalstatus'),
(42, 'Can change approval status', 11, 'change_approvalstatus'),
(43, 'Can delete approval status', 11, 'delete_approvalstatus'),
(44, 'Can view approval status', 11, 'view_approvalstatus'),
(45, 'Can add auto receipt', 12, 'add_autoreceipt'),
(46, 'Can change auto receipt', 12, 'change_autoreceipt'),
(47, 'Can delete auto receipt', 12, 'delete_autoreceipt'),
(48, 'Can view auto receipt', 12, 'view_autoreceipt'),
(49, 'Can add banks', 13, 'add_banks'),
(50, 'Can change banks', 13, 'change_banks'),
(51, 'Can delete banks', 13, 'delete_banks'),
(52, 'Can view banks', 13, 'view_banks'),
(53, 'Can add certifiable transactions', 14, 'add_certifiabletransactions'),
(54, 'Can change certifiable transactions', 14, 'change_certifiabletransactions'),
(55, 'Can delete certifiable transactions', 14, 'delete_certifiabletransactions'),
(56, 'Can view certifiable transactions', 14, 'view_certifiabletransactions'),
(57, 'Can add certification officers', 15, 'add_certificationofficers'),
(58, 'Can change certification officers', 15, 'change_certificationofficers'),
(59, 'Can delete certification officers', 15, 'delete_certificationofficers'),
(60, 'Can view certification officers', 15, 'view_certificationofficers'),
(61, 'Can add certification status', 16, 'add_certificationstatus'),
(62, 'Can change certification status', 16, 'change_certificationstatus'),
(63, 'Can delete certification status', 16, 'delete_certificationstatus'),
(64, 'Can view certification status', 16, 'view_certificationstatus'),
(65, 'Can add cooperative bank accounts', 17, 'add_cooperativebankaccounts'),
(66, 'Can change cooperative bank accounts', 17, 'change_cooperativebankaccounts'),
(67, 'Can delete cooperative bank accounts', 17, 'delete_cooperativebankaccounts'),
(68, 'Can view cooperative bank accounts', 17, 'view_cooperativebankaccounts'),
(69, 'Can add customer id', 18, 'add_customerid'),
(70, 'Can change customer id', 18, 'change_customerid'),
(71, 'Can delete customer id', 18, 'delete_customerid'),
(72, 'Can view customer id', 18, 'view_customerid'),
(73, 'Can add customers', 19, 'add_customers'),
(74, 'Can change customers', 19, 'change_customers'),
(75, 'Can delete customers', 19, 'delete_customers'),
(76, 'Can view customers', 19, 'view_customers'),
(77, 'Can add daily_ sales', 20, 'add_daily_sales'),
(78, 'Can change daily_ sales', 20, 'change_daily_sales'),
(79, 'Can delete daily_ sales', 20, 'delete_daily_sales'),
(80, 'Can view daily_ sales', 20, 'view_daily_sales'),
(81, 'Can add date joined upload status', 21, 'add_datejoineduploadstatus'),
(82, 'Can change date joined upload status', 21, 'change_datejoineduploadstatus'),
(83, 'Can delete date joined upload status', 21, 'delete_datejoineduploadstatus'),
(84, 'Can view date joined upload status', 21, 'view_datejoineduploadstatus'),
(85, 'Can add default password', 22, 'add_defaultpassword'),
(86, 'Can change default password', 22, 'change_defaultpassword'),
(87, 'Can delete default password', 22, 'delete_defaultpassword'),
(88, 'Can view default password', 22, 'view_defaultpassword'),
(89, 'Can add departments', 23, 'add_departments'),
(90, 'Can change departments', 23, 'change_departments'),
(91, 'Can delete departments', 23, 'delete_departments'),
(92, 'Can view departments', 23, 'view_departments'),
(93, 'Can add exclusive status', 24, 'add_exclusivestatus'),
(94, 'Can change exclusive status', 24, 'change_exclusivestatus'),
(95, 'Can delete exclusive status', 24, 'delete_exclusivestatus'),
(96, 'Can view exclusive status', 24, 'view_exclusivestatus'),
(97, 'Can add gender', 25, 'add_gender'),
(98, 'Can change gender', 25, 'change_gender'),
(99, 'Can delete gender', 25, 'delete_gender'),
(100, 'Can view gender', 25, 'view_gender'),
(101, 'Can add interest deduction source', 26, 'add_interestdeductionsource'),
(102, 'Can change interest deduction source', 26, 'change_interestdeductionsource'),
(103, 'Can delete interest deduction source', 26, 'delete_interestdeductionsource'),
(104, 'Can view interest deduction source', 26, 'view_interestdeductionsource'),
(105, 'Can add lga', 27, 'add_lga'),
(106, 'Can change lga', 27, 'change_lga'),
(107, 'Can delete lga', 27, 'delete_lga'),
(108, 'Can view lga', 27, 'view_lga'),
(109, 'Can add loan application', 28, 'add_loanapplication'),
(110, 'Can change loan application', 28, 'change_loanapplication'),
(111, 'Can delete loan application', 28, 'delete_loanapplication'),
(112, 'Can view loan application', 28, 'view_loanapplication'),
(113, 'Can add loan category', 29, 'add_loancategory'),
(114, 'Can change loan category', 29, 'change_loancategory'),
(115, 'Can delete loan category', 29, 'delete_loancategory'),
(116, 'Can view loan category', 29, 'view_loancategory'),
(117, 'Can add loan merge status', 30, 'add_loanmergestatus'),
(118, 'Can change loan merge status', 30, 'change_loanmergestatus'),
(119, 'Can delete loan merge status', 30, 'delete_loanmergestatus'),
(120, 'Can view loan merge status', 30, 'view_loanmergestatus'),
(121, 'Can add loan number', 31, 'add_loannumber'),
(122, 'Can change loan number', 31, 'change_loannumber'),
(123, 'Can delete loan number', 31, 'delete_loannumber'),
(124, 'Can view loan number', 31, 'view_loannumber'),
(125, 'Can add loan request', 32, 'add_loanrequest'),
(126, 'Can change loan request', 32, 'change_loanrequest'),
(127, 'Can delete loan request', 32, 'delete_loanrequest'),
(128, 'Can view loan request', 32, 'view_loanrequest'),
(129, 'Can add loan schedule status', 33, 'add_loanschedulestatus'),
(130, 'Can change loan schedule status', 33, 'change_loanschedulestatus'),
(131, 'Can delete loan schedule status', 33, 'delete_loanschedulestatus'),
(132, 'Can view loan schedule status', 33, 'view_loanschedulestatus'),
(133, 'Can add loans upload status', 34, 'add_loansuploadstatus'),
(134, 'Can change loans upload status', 34, 'change_loansuploadstatus'),
(135, 'Can delete loans upload status', 34, 'delete_loansuploadstatus'),
(136, 'Can view loans upload status', 34, 'view_loansuploadstatus'),
(137, 'Can add locations', 35, 'add_locations'),
(138, 'Can change locations', 35, 'change_locations'),
(139, 'Can delete locations', 35, 'delete_locations'),
(140, 'Can view locations', 35, 'view_locations'),
(141, 'Can add locked status', 36, 'add_lockedstatus'),
(142, 'Can change locked status', 36, 'change_lockedstatus'),
(143, 'Can delete locked status', 36, 'delete_lockedstatus'),
(144, 'Can view locked status', 36, 'view_lockedstatus'),
(145, 'Can add members', 37, 'add_members'),
(146, 'Can change members', 37, 'change_members'),
(147, 'Can delete members', 37, 'delete_members'),
(148, 'Can view members', 37, 'view_members'),
(149, 'Can add members bank accounts', 38, 'add_membersbankaccounts'),
(150, 'Can change members bank accounts', 38, 'change_membersbankaccounts'),
(151, 'Can delete members bank accounts', 38, 'delete_membersbankaccounts'),
(152, 'Can view members bank accounts', 38, 'view_membersbankaccounts'),
(153, 'Can add members cash withdrawals', 39, 'add_memberscashwithdrawals'),
(154, 'Can change members cash withdrawals', 39, 'change_memberscashwithdrawals'),
(155, 'Can delete members cash withdrawals', 39, 'delete_memberscashwithdrawals'),
(156, 'Can view members cash withdrawals', 39, 'view_memberscashwithdrawals'),
(157, 'Can add member ship request', 40, 'add_membershiprequest'),
(158, 'Can change member ship request', 40, 'change_membershiprequest'),
(159, 'Can delete member ship request', 40, 'delete_membershiprequest'),
(160, 'Can view member ship request', 40, 'view_membershiprequest'),
(161, 'Can add membership status', 41, 'add_membershipstatus'),
(162, 'Can change membership status', 41, 'change_membershipstatus'),
(163, 'Can delete membership status', 41, 'delete_membershipstatus'),
(164, 'Can view membership status', 41, 'view_membershipstatus'),
(165, 'Can add members id manager', 42, 'add_membersidmanager'),
(166, 'Can change members id manager', 42, 'change_membersidmanager'),
(167, 'Can delete members id manager', 42, 'delete_membersidmanager'),
(168, 'Can view members id manager', 42, 'view_membersidmanager'),
(169, 'Can add members share accounts', 43, 'add_membersshareaccounts'),
(170, 'Can change members share accounts', 43, 'change_membersshareaccounts'),
(171, 'Can delete members share accounts', 43, 'delete_membersshareaccounts'),
(172, 'Can view members share accounts', 43, 'view_membersshareaccounts'),
(173, 'Can add members share configurations', 44, 'add_membersshareconfigurations'),
(174, 'Can change members share configurations', 44, 'change_membersshareconfigurations'),
(175, 'Can delete members share configurations', 44, 'delete_membersshareconfigurations'),
(176, 'Can view members share configurations', 44, 'view_membersshareconfigurations'),
(177, 'Can add members welfare', 45, 'add_memberswelfare'),
(178, 'Can change members welfare', 45, 'change_memberswelfare'),
(179, 'Can delete members welfare', 45, 'delete_memberswelfare'),
(180, 'Can view members welfare', 45, 'view_memberswelfare'),
(181, 'Can add multiple loan status', 46, 'add_multipleloanstatus'),
(182, 'Can change multiple loan status', 46, 'change_multipleloanstatus'),
(183, 'Can delete multiple loan status', 46, 'delete_multipleloanstatus'),
(184, 'Can view multiple loan status', 46, 'view_multipleloanstatus'),
(185, 'Can add next of kins maximun', 47, 'add_nextofkinsmaximun'),
(186, 'Can change next of kins maximun', 47, 'change_nextofkinsmaximun'),
(187, 'Can delete next of kins maximun', 47, 'delete_nextofkinsmaximun'),
(188, 'Can view next of kins maximun', 47, 'view_nextofkinsmaximun'),
(189, 'Can add nok relationships', 48, 'add_nokrelationships'),
(190, 'Can change nok relationships', 48, 'change_nokrelationships'),
(191, 'Can delete nok relationships', 48, 'delete_nokrelationships'),
(192, 'Can view nok relationships', 48, 'view_nokrelationships'),
(193, 'Can add payment channels', 49, 'add_paymentchannels'),
(194, 'Can change payment channels', 49, 'change_paymentchannels'),
(195, 'Can delete payment channels', 49, 'delete_paymentchannels'),
(196, 'Can view payment channels', 49, 'view_paymentchannels'),
(197, 'Can add processing status', 50, 'add_processingstatus'),
(198, 'Can change processing status', 50, 'change_processingstatus'),
(199, 'Can delete processing status', 50, 'delete_processingstatus'),
(200, 'Can view processing status', 50, 'view_processingstatus'),
(201, 'Can add product category', 51, 'add_productcategory'),
(202, 'Can change product category', 51, 'change_productcategory'),
(203, 'Can delete product category', 51, 'delete_productcategory'),
(204, 'Can view product category', 51, 'view_productcategory'),
(205, 'Can add receipt status', 52, 'add_receiptstatus'),
(206, 'Can change receipt status', 52, 'change_receiptstatus'),
(207, 'Can delete receipt status', 52, 'delete_receiptstatus'),
(208, 'Can view receipt status', 52, 'view_receiptstatus'),
(209, 'Can add receipt types', 53, 'add_receipttypes'),
(210, 'Can change receipt types', 53, 'change_receipttypes'),
(211, 'Can delete receipt types', 53, 'delete_receipttypes'),
(212, 'Can view receipt types', 53, 'view_receipttypes'),
(213, 'Can add salary institution', 54, 'add_salaryinstitution'),
(214, 'Can change salary institution', 54, 'change_salaryinstitution'),
(215, 'Can delete salary institution', 54, 'delete_salaryinstitution'),
(216, 'Can view salary institution', 54, 'view_salaryinstitution'),
(217, 'Can add sales category', 55, 'add_salescategory'),
(218, 'Can change sales category', 55, 'change_salescategory'),
(219, 'Can delete sales category', 55, 'delete_salescategory'),
(220, 'Can view sales category', 55, 'view_salescategory'),
(221, 'Can add savings upload status', 56, 'add_savingsuploadstatus'),
(222, 'Can change savings upload status', 56, 'change_savingsuploadstatus'),
(223, 'Can delete savings upload status', 56, 'delete_savingsuploadstatus'),
(224, 'Can view savings upload status', 56, 'view_savingsuploadstatus'),
(225, 'Can add shares units', 57, 'add_sharesunits'),
(226, 'Can change shares units', 57, 'change_sharesunits'),
(227, 'Can delete shares units', 57, 'delete_sharesunits'),
(228, 'Can view shares units', 57, 'view_sharesunits'),
(229, 'Can add shares upload status', 58, 'add_sharesuploadstatus'),
(230, 'Can change shares upload status', 58, 'change_sharesuploadstatus'),
(231, 'Can delete shares upload status', 58, 'delete_sharesuploadstatus'),
(232, 'Can view shares upload status', 58, 'view_sharesuploadstatus'),
(233, 'Can add states', 59, 'add_states'),
(234, 'Can change states', 59, 'change_states'),
(235, 'Can delete states', 59, 'delete_states'),
(236, 'Can view states', 59, 'view_states'),
(237, 'Can add submission status', 60, 'add_submissionstatus'),
(238, 'Can change submission status', 60, 'change_submissionstatus'),
(239, 'Can delete submission status', 60, 'delete_submissionstatus'),
(240, 'Can view submission status', 60, 'view_submissionstatus'),
(241, 'Can add ticket status', 61, 'add_ticketstatus'),
(242, 'Can change ticket status', 61, 'change_ticketstatus'),
(243, 'Can delete ticket status', 61, 'delete_ticketstatus'),
(244, 'Can view ticket status', 61, 'view_ticketstatus'),
(245, 'Can add titles', 62, 'add_titles'),
(246, 'Can change titles', 62, 'change_titles'),
(247, 'Can delete titles', 62, 'delete_titles'),
(248, 'Can view titles', 62, 'view_titles'),
(249, 'Can add transaction sources', 63, 'add_transactionsources'),
(250, 'Can change transaction sources', 63, 'change_transactionsources'),
(251, 'Can delete transaction sources', 63, 'delete_transactionsources'),
(252, 'Can view transaction sources', 63, 'view_transactionsources'),
(253, 'Can add transaction status', 64, 'add_transactionstatus'),
(254, 'Can change transaction status', 64, 'change_transactionstatus'),
(255, 'Can delete transaction status', 64, 'delete_transactionstatus'),
(256, 'Can view transaction status', 64, 'view_transactionstatus'),
(257, 'Can add transaction types', 65, 'add_transactiontypes'),
(258, 'Can change transaction types', 65, 'change_transactiontypes'),
(259, 'Can delete transaction types', 65, 'delete_transactiontypes'),
(260, 'Can view transaction types', 65, 'view_transactiontypes'),
(261, 'Can add user levels', 66, 'add_userlevels'),
(262, 'Can change user levels', 66, 'change_userlevels'),
(263, 'Can delete user levels', 66, 'delete_userlevels'),
(264, 'Can view user levels', 66, 'view_userlevels'),
(265, 'Can add users level', 67, 'add_userslevel'),
(266, 'Can change users level', 67, 'change_userslevel'),
(267, 'Can delete users level', 67, 'delete_userslevel'),
(268, 'Can view users level', 67, 'view_userslevel'),
(269, 'Can add user type', 68, 'add_usertype'),
(270, 'Can change user type', 68, 'change_usertype'),
(271, 'Can delete user type', 68, 'delete_usertype'),
(272, 'Can view user type', 68, 'view_usertype'),
(273, 'Can add welfare upload status', 69, 'add_welfareuploadstatus'),
(274, 'Can change welfare upload status', 69, 'change_welfareuploadstatus'),
(275, 'Can delete welfare upload status', 69, 'delete_welfareuploadstatus'),
(276, 'Can view welfare upload status', 69, 'view_welfareuploadstatus'),
(277, 'Can add withdrawal status', 70, 'add_withdrawalstatus'),
(278, 'Can change withdrawal status', 70, 'change_withdrawalstatus'),
(279, 'Can delete withdrawal status', 70, 'delete_withdrawalstatus'),
(280, 'Can view withdrawal status', 70, 'view_withdrawalstatus'),
(281, 'Can add withdrawable transactions', 71, 'add_withdrawabletransactions'),
(282, 'Can change withdrawable transactions', 71, 'change_withdrawabletransactions'),
(283, 'Can delete withdrawable transactions', 71, 'delete_withdrawabletransactions'),
(284, 'Can view withdrawable transactions', 71, 'view_withdrawabletransactions'),
(285, 'Can add transaction periods', 72, 'add_transactionperiods'),
(286, 'Can change transaction periods', 72, 'change_transactionperiods'),
(287, 'Can delete transaction periods', 72, 'delete_transactionperiods'),
(288, 'Can view transaction periods', 72, 'view_transactionperiods'),
(289, 'Can add transaction ajustment request', 73, 'add_transactionajustmentrequest'),
(290, 'Can change transaction ajustment request', 73, 'change_transactionajustmentrequest'),
(291, 'Can delete transaction ajustment request', 73, 'delete_transactionajustmentrequest'),
(292, 'Can view transaction ajustment request', 73, 'view_transactionajustmentrequest'),
(293, 'Can add task manager', 74, 'add_taskmanager'),
(294, 'Can change task manager', 74, 'change_taskmanager'),
(295, 'Can delete task manager', 74, 'delete_taskmanager'),
(296, 'Can view task manager', 74, 'view_taskmanager'),
(297, 'Can add stock', 75, 'add_stock'),
(298, 'Can change stock', 75, 'change_stock'),
(299, 'Can delete stock', 75, 'delete_stock'),
(300, 'Can view stock', 75, 'view_stock'),
(301, 'Can add standing order accounts', 76, 'add_standingorderaccounts'),
(302, 'Can change standing order accounts', 76, 'change_standingorderaccounts'),
(303, 'Can delete standing order accounts', 76, 'delete_standingorderaccounts'),
(304, 'Can view standing order accounts', 76, 'view_standingorderaccounts'),
(305, 'Can add staff', 77, 'add_staff'),
(306, 'Can change staff', 77, 'change_staff'),
(307, 'Can delete staff', 77, 'delete_staff'),
(308, 'Can view staff', 77, 'view_staff'),
(309, 'Can add shares deduction savings', 78, 'add_sharesdeductionsavings'),
(310, 'Can change shares deduction savings', 78, 'change_sharesdeductionsavings'),
(311, 'Can delete shares deduction savings', 78, 'delete_sharesdeductionsavings'),
(312, 'Can view shares deduction savings', 78, 'view_sharesdeductionsavings'),
(313, 'Can add savings uploaded', 79, 'add_savingsuploaded'),
(314, 'Can change savings uploaded', 79, 'change_savingsuploaded'),
(315, 'Can delete savings uploaded', 79, 'delete_savingsuploaded'),
(316, 'Can view savings uploaded', 79, 'view_savingsuploaded'),
(317, 'Can add receipts_ shop', 80, 'add_receipts_shop'),
(318, 'Can change receipts_ shop', 80, 'change_receipts_shop'),
(319, 'Can delete receipts_ shop', 80, 'delete_receipts_shop'),
(320, 'Can view receipts_ shop', 80, 'view_receipts_shop'),
(321, 'Can add receipts', 81, 'add_receipts'),
(322, 'Can change receipts', 81, 'change_receipts'),
(323, 'Can delete receipts', 81, 'delete_receipts'),
(324, 'Can view receipts', 81, 'view_receipts'),
(325, 'Can add receipt_ cancelled', 82, 'add_receipt_cancelled'),
(326, 'Can change receipt_ cancelled', 82, 'change_receipt_cancelled'),
(327, 'Can delete receipt_ cancelled', 82, 'delete_receipt_cancelled'),
(328, 'Can view receipt_ cancelled', 82, 'view_receipt_cancelled'),
(329, 'Can add personal ledger', 83, 'add_personalledger'),
(330, 'Can change personal ledger', 83, 'change_personalledger'),
(331, 'Can delete personal ledger', 83, 'delete_personalledger'),
(332, 'Can view personal ledger', 83, 'view_personalledger'),
(333, 'Can add norminal roll', 84, 'add_norminalroll'),
(334, 'Can change norminal roll', 84, 'change_norminalroll'),
(335, 'Can delete norminal roll', 84, 'delete_norminalroll'),
(336, 'Can view norminal roll', 84, 'view_norminalroll'),
(337, 'Can add non member account deductions', 85, 'add_nonmemberaccountdeductions'),
(338, 'Can change non member account deductions', 85, 'change_nonmemberaccountdeductions'),
(339, 'Can delete non member account deductions', 85, 'delete_nonmemberaccountdeductions'),
(340, 'Can view non member account deductions', 85, 'view_nonmemberaccountdeductions'),
(341, 'Can add monthly group generated transactions', 86, 'add_monthlygroupgeneratedtransactions'),
(342, 'Can change monthly group generated transactions', 86, 'change_monthlygroupgeneratedtransactions'),
(343, 'Can delete monthly group generated transactions', 86, 'delete_monthlygroupgeneratedtransactions'),
(344, 'Can view monthly group generated transactions', 86, 'view_monthlygroupgeneratedtransactions'),
(345, 'Can add monthly generated transactions', 87, 'add_monthlygeneratedtransactions'),
(346, 'Can change monthly generated transactions', 87, 'change_monthlygeneratedtransactions'),
(347, 'Can delete monthly generated transactions', 87, 'delete_monthlygeneratedtransactions'),
(348, 'Can view monthly generated transactions', 87, 'view_monthlygeneratedtransactions'),
(349, 'Can add monthly deduction list generated', 88, 'add_monthlydeductionlistgenerated'),
(350, 'Can change monthly deduction list generated', 88, 'change_monthlydeductionlistgenerated'),
(351, 'Can delete monthly deduction list generated', 88, 'delete_monthlydeductionlistgenerated'),
(352, 'Can view monthly deduction list generated', 88, 'view_monthlydeductionlistgenerated'),
(353, 'Can add monthly deduction list', 89, 'add_monthlydeductionlist'),
(354, 'Can change monthly deduction list', 89, 'change_monthlydeductionlist'),
(355, 'Can delete monthly deduction list', 89, 'delete_monthlydeductionlist'),
(356, 'Can view monthly deduction list', 89, 'view_monthlydeductionlist'),
(357, 'Can add members welfare accounts main', 90, 'add_memberswelfareaccountsmain'),
(358, 'Can change members welfare accounts main', 90, 'change_memberswelfareaccountsmain'),
(359, 'Can delete members welfare accounts main', 90, 'delete_memberswelfareaccountsmain'),
(360, 'Can view members welfare accounts main', 90, 'view_memberswelfareaccountsmain'),
(361, 'Can add members welfare accounts', 91, 'add_memberswelfareaccounts'),
(362, 'Can change members welfare accounts', 91, 'change_memberswelfareaccounts'),
(363, 'Can delete members welfare accounts', 91, 'delete_memberswelfareaccounts'),
(364, 'Can view members welfare accounts', 91, 'view_memberswelfareaccounts'),
(365, 'Can add members share purchase request', 92, 'add_memberssharepurchaserequest'),
(366, 'Can change members share purchase request', 92, 'change_memberssharepurchaserequest'),
(367, 'Can delete members share purchase request', 92, 'delete_memberssharepurchaserequest'),
(368, 'Can view members share purchase request', 92, 'view_memberssharepurchaserequest'),
(369, 'Can add members share initial update request', 93, 'add_membersshareinitialupdaterequest'),
(370, 'Can change members share initial update request', 93, 'change_membersshareinitialupdaterequest'),
(371, 'Can delete members share initial update request', 93, 'delete_membersshareinitialupdaterequest'),
(372, 'Can view members share initial update request', 93, 'view_membersshareinitialupdaterequest'),
(373, 'Can add members share accounts main', 94, 'add_membersshareaccountsmain'),
(374, 'Can change members share accounts main', 94, 'change_membersshareaccountsmain'),
(375, 'Can delete members share accounts main', 94, 'delete_membersshareaccountsmain'),
(376, 'Can view members share accounts main', 94, 'view_membersshareaccountsmain'),
(377, 'Can add members salary update request', 95, 'add_memberssalaryupdaterequest'),
(378, 'Can change members salary update request', 95, 'change_memberssalaryupdaterequest'),
(379, 'Can delete members salary update request', 95, 'delete_memberssalaryupdaterequest'),
(380, 'Can view members salary update request', 95, 'view_memberssalaryupdaterequest'),
(381, 'Can add members next of kins', 96, 'add_membersnextofkins'),
(382, 'Can change members next of kins', 96, 'change_membersnextofkins'),
(383, 'Can delete members next of kins', 96, 'delete_membersnextofkins'),
(384, 'Can view members next of kins', 96, 'view_membersnextofkins'),
(385, 'Can add member ship request additional info', 97, 'add_membershiprequestadditionalinfo'),
(386, 'Can change member ship request additional info', 97, 'change_membershiprequestadditionalinfo'),
(387, 'Can delete member ship request additional info', 97, 'delete_membershiprequestadditionalinfo'),
(388, 'Can view member ship request additional info', 97, 'view_membershiprequestadditionalinfo'),
(389, 'Can add member ship request additional attachment', 98, 'add_membershiprequestadditionalattachment'),
(390, 'Can change member ship request additional attachment', 98, 'change_membershiprequestadditionalattachment'),
(391, 'Can delete member ship request additional attachment', 98, 'delete_membershiprequestadditionalattachment'),
(392, 'Can view member ship request additional attachment', 98, 'view_membershiprequestadditionalattachment'),
(393, 'Can add member ship form sales record', 99, 'add_membershipformsalesrecord'),
(394, 'Can change member ship form sales record', 99, 'change_membershipformsalesrecord'),
(395, 'Can delete member ship form sales record', 99, 'delete_membershipformsalesrecord'),
(396, 'Can view member ship form sales record', 99, 'view_membershipformsalesrecord'),
(397, 'Can add members exclusiveness', 100, 'add_membersexclusiveness'),
(398, 'Can change members exclusiveness', 100, 'change_membersexclusiveness'),
(399, 'Can delete members exclusiveness', 100, 'delete_membersexclusiveness'),
(400, 'Can view members exclusiveness', 100, 'view_membersexclusiveness'),
(401, 'Can add members cash withdrawals main', 101, 'add_memberscashwithdrawalsmain'),
(402, 'Can change members cash withdrawals main', 101, 'change_memberscashwithdrawalsmain'),
(403, 'Can delete members cash withdrawals main', 101, 'delete_memberscashwithdrawalsmain'),
(404, 'Can view members cash withdrawals main', 101, 'view_memberscashwithdrawalsmain'),
(405, 'Can add members cash deposits', 102, 'add_memberscashdeposits'),
(406, 'Can change members cash deposits', 102, 'change_memberscashdeposits'),
(407, 'Can delete members cash deposits', 102, 'delete_memberscashdeposits'),
(408, 'Can view members cash deposits', 102, 'view_memberscashdeposits'),
(409, 'Can add members accounts domain', 103, 'add_membersaccountsdomain'),
(410, 'Can change members accounts domain', 103, 'change_membersaccountsdomain'),
(411, 'Can delete members accounts domain', 103, 'delete_membersaccountsdomain'),
(412, 'Can view members accounts domain', 103, 'view_membersaccountsdomain'),
(413, 'Can add members_ credit_ sales_ selected', 104, 'add_members_credit_sales_selected'),
(414, 'Can change members_ credit_ sales_ selected', 104, 'change_members_credit_sales_selected'),
(415, 'Can delete members_ credit_ sales_ selected', 104, 'delete_members_credit_sales_selected'),
(416, 'Can view members_ credit_ sales_ selected', 104, 'view_members_credit_sales_selected'),
(417, 'Can add members_ credit_ sales_external_fascilities', 105, 'add_members_credit_sales_external_fascilities'),
(418, 'Can change members_ credit_ sales_external_fascilities', 105, 'change_members_credit_sales_external_fascilities'),
(419, 'Can delete members_ credit_ sales_external_fascilities', 105, 'delete_members_credit_sales_external_fascilities'),
(420, 'Can view members_ credit_ sales_external_fascilities', 105, 'view_members_credit_sales_external_fascilities'),
(421, 'Can add members_credit_purchase_summary', 106, 'add_members_credit_purchase_summary'),
(422, 'Can change members_credit_purchase_summary', 106, 'change_members_credit_purchase_summary'),
(423, 'Can delete members_credit_purchase_summary', 106, 'delete_members_credit_purchase_summary'),
(424, 'Can view members_credit_purchase_summary', 106, 'view_members_credit_purchase_summary'),
(425, 'Can add members_credit_purchase_analysis', 107, 'add_members_credit_purchase_analysis'),
(426, 'Can change members_credit_purchase_analysis', 107, 'change_members_credit_purchase_analysis'),
(427, 'Can delete members_credit_purchase_analysis', 107, 'delete_members_credit_purchase_analysis'),
(428, 'Can view members_credit_purchase_analysis', 107, 'view_members_credit_purchase_analysis'),
(429, 'Can add members_ cash_ sales_ selected', 108, 'add_members_cash_sales_selected'),
(430, 'Can change members_ cash_ sales_ selected', 108, 'change_members_cash_sales_selected'),
(431, 'Can delete members_ cash_ sales_ selected', 108, 'delete_members_cash_sales_selected'),
(432, 'Can view members_ cash_ sales_ selected', 108, 'view_members_cash_sales_selected'),
(433, 'Can add loans uploaded', 109, 'add_loansuploaded'),
(434, 'Can change loans uploaded', 109, 'change_loansuploaded'),
(435, 'Can delete loans uploaded', 109, 'delete_loansuploaded'),
(436, 'Can view loans uploaded', 109, 'view_loansuploaded'),
(437, 'Can add loans repayment base', 110, 'add_loansrepaymentbase'),
(438, 'Can change loans repayment base', 110, 'change_loansrepaymentbase'),
(439, 'Can delete loans repayment base', 110, 'delete_loansrepaymentbase'),
(440, 'Can view loans repayment base', 110, 'view_loansrepaymentbase'),
(441, 'Can add loans disbursed', 111, 'add_loansdisbursed'),
(442, 'Can change loans disbursed', 111, 'change_loansdisbursed'),
(443, 'Can delete loans disbursed', 111, 'delete_loansdisbursed'),
(444, 'Can view loans disbursed', 111, 'view_loansdisbursed'),
(445, 'Can add loans cleared', 112, 'add_loanscleared'),
(446, 'Can change loans cleared', 112, 'change_loanscleared'),
(447, 'Can delete loans cleared', 112, 'delete_loanscleared'),
(448, 'Can view loans cleared', 112, 'view_loanscleared'),
(449, 'Can add loan request settings', 113, 'add_loanrequestsettings'),
(450, 'Can change loan request settings', 113, 'change_loanrequestsettings'),
(451, 'Can delete loan request settings', 113, 'delete_loanrequestsettings'),
(452, 'Can view loan request settings', 113, 'view_loanrequestsettings'),
(453, 'Can add loan request attachments', 114, 'add_loanrequestattachments'),
(454, 'Can change loan request attachments', 114, 'change_loanrequestattachments'),
(455, 'Can delete loan request attachments', 114, 'delete_loanrequestattachments'),
(456, 'Can view loan request attachments', 114, 'view_loanrequestattachments'),
(457, 'Can add loan guarantors', 115, 'add_loanguarantors'),
(458, 'Can change loan guarantors', 115, 'change_loanguarantors'),
(459, 'Can delete loan guarantors', 115, 'delete_loanguarantors'),
(460, 'Can view loan guarantors', 115, 'view_loanguarantors'),
(461, 'Can add loan form issuance', 116, 'add_loanformissuance'),
(462, 'Can change loan form issuance', 116, 'change_loanformissuance'),
(463, 'Can delete loan form issuance', 116, 'delete_loanformissuance'),
(464, 'Can view loan form issuance', 116, 'view_loanformissuance'),
(465, 'Can add loan based savings', 117, 'add_loanbasedsavings'),
(466, 'Can change loan based savings', 117, 'change_loanbasedsavings'),
(467, 'Can delete loan based savings', 117, 'delete_loanbasedsavings'),
(468, 'Can view loan based savings', 117, 'view_loanbasedsavings'),
(469, 'Can add loan application settings', 118, 'add_loanapplicationsettings'),
(470, 'Can change loan application settings', 118, 'change_loanapplicationsettings'),
(471, 'Can delete loan application settings', 118, 'delete_loanapplicationsettings'),
(472, 'Can view loan application settings', 118, 'view_loanapplicationsettings'),
(473, 'Can add loan application guarnators', 119, 'add_loanapplicationguarnators'),
(474, 'Can change loan application guarnators', 119, 'change_loanapplicationguarnators'),
(475, 'Can delete loan application guarnators', 119, 'delete_loanapplicationguarnators'),
(476, 'Can view loan application guarnators', 119, 'view_loanapplicationguarnators'),
(477, 'Can add general_ cash_ sales_ selected temp', 120, 'add_general_cash_sales_selectedtemp'),
(478, 'Can change general_ cash_ sales_ selected temp', 120, 'change_general_cash_sales_selectedtemp'),
(479, 'Can delete general_ cash_ sales_ selected temp', 120, 'delete_general_cash_sales_selectedtemp'),
(480, 'Can view general_ cash_ sales_ selected temp', 120, 'view_general_cash_sales_selectedtemp'),
(481, 'Can add general_ cash_ sales_ selected', 121, 'add_general_cash_sales_selected'),
(482, 'Can change general_ cash_ sales_ selected', 121, 'change_general_cash_sales_selected'),
(483, 'Can delete general_ cash_ sales_ selected', 121, 'delete_general_cash_sales_selected'),
(484, 'Can view general_ cash_ sales_ selected', 121, 'view_general_cash_sales_selected'),
(485, 'Can add external fascilities temp', 122, 'add_externalfascilitiestemp'),
(486, 'Can change external fascilities temp', 122, 'change_externalfascilitiestemp'),
(487, 'Can delete external fascilities temp', 122, 'delete_externalfascilitiestemp'),
(488, 'Can view external fascilities temp', 122, 'view_externalfascilitiestemp'),
(489, 'Can add external fascilities main', 123, 'add_externalfascilitiesmain'),
(490, 'Can change external fascilities main', 123, 'change_externalfascilitiesmain'),
(491, 'Can delete external fascilities main', 123, 'delete_externalfascilitiesmain'),
(492, 'Can view external fascilities main', 123, 'view_externalfascilitiesmain'),
(493, 'Can add disbursement officers', 124, 'add_disbursementofficers'),
(494, 'Can change disbursement officers', 124, 'change_disbursementofficers'),
(495, 'Can delete disbursement officers', 124, 'delete_disbursementofficers'),
(496, 'Can view disbursement officers', 124, 'view_disbursementofficers'),
(497, 'Can add data capture manager', 125, 'add_datacapturemanager'),
(498, 'Can change data capture manager', 125, 'change_datacapturemanager'),
(499, 'Can delete data capture manager', 125, 'delete_datacapturemanager'),
(500, 'Can view data capture manager', 125, 'view_datacapturemanager'),
(501, 'Can add daily_ sales_ summary', 126, 'add_daily_sales_summary'),
(502, 'Can change daily_ sales_ summary', 126, 'change_daily_sales_summary'),
(503, 'Can delete daily_ sales_ summary', 126, 'delete_daily_sales_summary'),
(504, 'Can view daily_ sales_ summary', 126, 'view_daily_sales_summary'),
(505, 'Can add cooperative shop ledger', 127, 'add_cooperativeshopledger'),
(506, 'Can change cooperative shop ledger', 127, 'change_cooperativeshopledger'),
(507, 'Can delete cooperative shop ledger', 127, 'delete_cooperativeshopledger'),
(508, 'Can view cooperative shop ledger', 127, 'view_cooperativeshopledger'),
(509, 'Can add cheque_ table', 128, 'add_cheque_table'),
(510, 'Can change cheque_ table', 128, 'change_cheque_table'),
(511, 'Can delete cheque_ table', 128, 'delete_cheque_table'),
(512, 'Can view cheque_ table', 128, 'view_cheque_table'),
(513, 'Can add cash book', 129, 'add_cashbook'),
(514, 'Can change cash book', 129, 'change_cashbook'),
(515, 'Can delete cash book', 129, 'delete_cashbook'),
(516, 'Can view cash book', 129, 'view_cashbook'),
(517, 'Can add admin master', 130, 'add_adminmaster'),
(518, 'Can change admin master', 130, 'change_adminmaster'),
(519, 'Can delete admin master', 130, 'delete_adminmaster'),
(520, 'Can view admin master', 130, 'view_adminmaster'),
(521, 'Can add account deductions', 131, 'add_accountdeductions'),
(522, 'Can change account deductions', 131, 'change_accountdeductions'),
(523, 'Can delete account deductions', 131, 'delete_accountdeductions'),
(524, 'Can view account deductions', 131, 'view_accountdeductions'),
(525, 'Can add shares sales record', 132, 'add_sharessalesrecord'),
(526, 'Can change shares sales record', 132, 'change_sharessalesrecord'),
(527, 'Can delete shares sales record', 132, 'delete_sharessalesrecord'),
(528, 'Can view shares sales record', 132, 'view_sharessalesrecord'),
(529, 'Can add members cash withdrawals application', 133, 'add_memberscashwithdrawalsapplication'),
(530, 'Can change members cash withdrawals application', 133, 'change_memberscashwithdrawalsapplication'),
(531, 'Can delete members cash withdrawals application', 133, 'delete_memberscashwithdrawalsapplication'),
(532, 'Can view members cash withdrawals application', 133, 'view_memberscashwithdrawalsapplication'),
(533, 'Can add transaction loan ajustment request', 134, 'add_transactionloanajustmentrequest'),
(534, 'Can change transaction loan ajustment request', 134, 'change_transactionloanajustmentrequest'),
(535, 'Can delete transaction loan ajustment request', 134, 'delete_transactionloanajustmentrequest'),
(536, 'Can view transaction loan ajustment request', 134, 'view_transactionloanajustmentrequest'),
(537, 'Can add compulsory savings', 135, 'add_compulsorysavings'),
(538, 'Can change compulsory savings', 135, 'change_compulsorysavings'),
(539, 'Can delete compulsory savings', 135, 'delete_compulsorysavings'),
(540, 'Can view compulsory savings', 135, 'view_compulsorysavings'),
(541, 'Can add daily_ sales_ cash_ flow_ summary', 136, 'add_daily_sales_cash_flow_summary'),
(542, 'Can change daily_ sales_ cash_ flow_ summary', 136, 'change_daily_sales_cash_flow_summary'),
(543, 'Can delete daily_ sales_ cash_ flow_ summary', 136, 'delete_daily_sales_cash_flow_summary'),
(544, 'Can view daily_ sales_ cash_ flow_ summary', 136, 'view_daily_sales_cash_flow_summary'),
(545, 'Can add suppliers', 137, 'add_suppliers'),
(546, 'Can change suppliers', 137, 'change_suppliers'),
(547, 'Can delete suppliers', 137, 'delete_suppliers'),
(548, 'Can view suppliers', 137, 'view_suppliers'),
(549, 'Can add suppliers_ reps', 138, 'add_suppliers_reps'),
(550, 'Can change suppliers_ reps', 138, 'change_suppliers_reps'),
(551, 'Can delete suppliers_ reps', 138, 'delete_suppliers_reps'),
(552, 'Can view suppliers_ reps', 138, 'view_suppliers_reps'),
(553, 'Can add suppliers_ majors', 139, 'add_suppliers_majors'),
(554, 'Can change suppliers_ majors', 139, 'change_suppliers_majors'),
(555, 'Can delete suppliers_ majors', 139, 'delete_suppliers_majors'),
(556, 'Can view suppliers_ majors', 139, 'view_suppliers_majors'),
(557, 'Can add suppliers_ branches', 140, 'add_suppliers_branches'),
(558, 'Can change suppliers_ branches', 140, 'change_suppliers_branches'),
(559, 'Can delete suppliers_ branches', 140, 'delete_suppliers_branches'),
(560, 'Can view suppliers_ branches', 140, 'view_suppliers_branches'),
(561, 'Can add purchases', 141, 'add_purchases'),
(562, 'Can change purchases', 141, 'change_purchases'),
(563, 'Can delete purchases', 141, 'delete_purchases'),
(564, 'Can view purchases', 141, 'view_purchases'),
(565, 'Can add purchases_ temp', 142, 'add_purchases_temp'),
(566, 'Can change purchases_ temp', 142, 'change_purchases_temp'),
(567, 'Can delete purchases_ temp', 142, 'delete_purchases_temp'),
(568, 'Can view purchases_ temp', 142, 'view_purchases_temp'),
(569, 'Can add purchase_ header', 143, 'add_purchase_header'),
(570, 'Can change purchase_ header', 143, 'change_purchase_header'),
(571, 'Can delete purchase_ header', 143, 'delete_purchase_header'),
(572, 'Can view purchase_ header', 143, 'view_purchase_header'),
(573, 'Can add item write off reasons', 144, 'add_itemwriteoffreasons'),
(574, 'Can change item write off reasons', 144, 'change_itemwriteoffreasons'),
(575, 'Can delete item write off reasons', 144, 'delete_itemwriteoffreasons'),
(576, 'Can view item write off reasons', 144, 'view_itemwriteoffreasons');

-- --------------------------------------------------------

--
-- Table structure for table `auto_receipt`
--

CREATE TABLE `auto_receipt` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `receipt` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auto_receipt`
--

INSERT INTO `auto_receipt` (`id`, `created_at`, `updated_at`, `receipt`) VALUES
(1, '2021-12-07 21:23:50.000000', '2022-01-17 04:03:22.443096', '319');

-- --------------------------------------------------------

--
-- Table structure for table `banks`
--

CREATE TABLE `banks` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `banks`
--

INSERT INTO `banks` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'Access Bank Plc ', '2021-12-07 19:01:07.350082', '2021-12-07 19:01:07.350082'),
(2, 'Citibank Nigeria Limited ', '2021-12-07 19:01:07.395086', '2021-12-07 19:01:07.395086'),
(3, 'Ecobank Nigeria Plc ', '2021-12-07 19:01:07.516190', '2021-12-07 19:01:07.516190'),
(4, 'Fidelity Bank Plc ', '2021-12-07 19:01:07.558479', '2021-12-07 19:01:07.558479'),
(5, 'FIRST BANK NIGERIA LIMITED ', '2021-12-07 19:01:07.605573', '2021-12-07 19:01:07.606572'),
(6, 'First City Monument Bank Plc ', '2021-12-07 19:01:07.647473', '2021-12-07 19:01:07.648470'),
(7, 'Globus Bank Limited ', '2021-12-07 19:01:07.695783', '2021-12-07 19:01:07.695783'),
(8, 'Guaranty Trust Bank Plc ', '2021-12-07 19:01:07.728808', '2021-12-07 19:01:07.728808'),
(9, 'Heritage Banking Company Ltd. ', '2021-12-07 19:01:07.761411', '2021-12-07 19:01:07.761411'),
(10, 'Key Stone Bank ', '2021-12-07 19:01:07.795320', '2021-12-07 19:01:07.795320'),
(11, 'Polaris Bank ', '2021-12-07 19:01:07.839454', '2021-12-07 19:01:07.840456'),
(12, 'Providus Bank ', '2021-12-07 19:01:07.874435', '2021-12-07 19:01:07.874435'),
(13, 'Stanbic IBTC Bank Ltd. ', '2021-12-07 19:01:07.916407', '2021-12-07 19:01:07.916407'),
(14, 'Standard Chartered Bank Nigeria Ltd. ', '2021-12-07 19:01:07.951385', '2021-12-07 19:01:07.951385'),
(15, 'Sterling Bank Plc ', '2021-12-07 19:01:08.050808', '2021-12-07 19:01:08.050808'),
(16, 'SunTrust Bank Nigeria Limited ', '2021-12-07 19:01:08.118430', '2021-12-07 19:01:08.118430'),
(17, 'Titan Trust Bank Ltd ', '2021-12-07 19:01:08.216186', '2021-12-07 19:01:08.216186'),
(18, 'Union Bank of Nigeria Plc ', '2021-12-07 19:01:08.329630', '2021-12-07 19:01:08.329630'),
(19, 'United Bank For Africa Plc ', '2021-12-07 19:01:08.385595', '2021-12-07 19:01:08.385595'),
(20, 'Unity Bank Plc ', '2021-12-07 19:01:08.439074', '2021-12-07 19:01:08.439074'),
(21, 'Wema Bank Plc ', '2021-12-07 19:01:08.475011', '2021-12-07 19:01:08.475011'),
(22, 'Zenith Bank Plc', '2021-12-07 19:01:08.506785', '2021-12-07 19:01:08.506785');

-- --------------------------------------------------------

--
-- Table structure for table `cashbook`
--

CREATE TABLE `cashbook` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `particulars` varchar(255) NOT NULL,
  `debit` decimal(20,2) NOT NULL,
  `credit` decimal(20,2) NOT NULL,
  `balance` decimal(20,2) NOT NULL,
  `ref_no` varchar(255) NOT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `certifiable_transactions`
--

CREATE TABLE `certifiable_transactions` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `status_id` int(11) NOT NULL,
  `transaction_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `certifiable_transactions`
--

INSERT INTO `certifiable_transactions` (`id`, `created_at`, `updated_at`, `status_id`, `transaction_id`) VALUES
(1, '2021-12-15 05:11:29.060345', '2021-12-15 05:11:29.060345', 1, 18),
(2, '2021-12-16 07:42:41.631585', '2021-12-16 07:42:41.632584', 1, 1),
(3, '2021-12-16 13:30:00.969362', '2021-12-16 13:30:00.969362', 1, 8),
(4, '2021-12-16 13:33:14.434120', '2021-12-16 13:33:14.434120', 1, 9);

-- --------------------------------------------------------

--
-- Table structure for table `certification_officers`
--

CREATE TABLE `certification_officers` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `officer_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL,
  `transaction_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `certification_officers`
--

INSERT INTO `certification_officers` (`id`, `created_at`, `updated_at`, `officer_id`, `status_id`, `transaction_id`) VALUES
(1, '2021-12-15 05:12:08.342668', '2021-12-15 09:12:08.771353', 7, 2, 1),
(2, '2021-12-16 07:43:07.573953', '2021-12-16 07:43:07.573953', 4, 1, 2),
(3, '2021-12-16 13:34:00.213120', '2021-12-16 13:34:00.213120', 4, 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `certification_status`
--

CREATE TABLE `certification_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `certification_status`
--

INSERT INTO `certification_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'PENDING', '2021-12-07 18:59:59.916009', '2021-12-07 18:59:59.916009'),
(2, 'CERTIFIED', '2021-12-07 18:59:59.967974', '2021-12-07 18:59:59.967974'),
(3, 'NOT CERTIFIED', '2021-12-07 19:00:00.156444', '2021-12-07 19:00:00.156444');

-- --------------------------------------------------------

--
-- Table structure for table `cheque_table`
--

CREATE TABLE `cheque_table` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `cheque_name` varchar(255) NOT NULL,
  `cheque_number` varchar(255) NOT NULL,
  `cheque_due_date` date NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `date_cleared` date DEFAULT NULL,
  `approval_status_id` int(11) NOT NULL,
  `bank_id` int(11) DEFAULT NULL,
  `sales_id` int(11) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `compulsory_savings`
--

CREATE TABLE `compulsory_savings` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `transaction_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `compulsory_savings`
--

INSERT INTO `compulsory_savings` (`id`, `created_at`, `updated_at`, `transaction_id`) VALUES
(2, '2022-01-10 16:26:25.218098', '2022-01-10 16:26:25.218098', 2);

-- --------------------------------------------------------

--
-- Table structure for table `cooperative_bank_accounts`
--

CREATE TABLE `cooperative_bank_accounts` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `account_name` varchar(255) NOT NULL,
  `account_number` varchar(255) NOT NULL,
  `account_type_id` int(11) NOT NULL,
  `bank_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cooperative_bank_accounts`
--

INSERT INTO `cooperative_bank_accounts` (`id`, `created_at`, `updated_at`, `account_name`, `account_number`, `account_type_id`, `bank_id`) VALUES
(1, '2021-12-14 00:52:44.857801', '2021-12-14 00:52:44.857801', 'welfare account', '7464746777', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `cooperative_shop_ledger`
--

CREATE TABLE `cooperative_shop_ledger` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `particulars` varchar(255) DEFAULT NULL,
  `debit` decimal(20,2) NOT NULL,
  `credit` decimal(20,2) NOT NULL,
  `balance` decimal(20,2) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL,
  `receipt` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cooperative_shop_ledger`
--

INSERT INTO `cooperative_shop_ledger` (`id`, `created_at`, `updated_at`, `particulars`, `debit`, `credit`, `balance`, `member_id`, `processed_by_id`, `status_id`, `receipt`) VALUES
(5, '2022-01-06 07:34:18.948687', '2022-01-06 07:34:18.948687', 'Purchases with receipt No 292', '22700.00', '0.00', '-22700.00', 713, 12, 1, '292'),
(6, '2022-01-10 17:22:10.492790', '2022-01-10 17:22:10.492790', 'Purchases with receipt No 293', '16000.00', '0.00', '-16000.00', 714, 12, 1, '293'),
(7, '2022-01-10 18:56:28.707306', '2022-01-10 18:56:28.708307', 'Purchases with receipt No 294', '13800.00', '0.00', '-13800.00', 715, 12, 1, '294'),
(8, '2022-01-17 04:03:23.622122', '2022-01-17 04:03:23.622122', 'Purchases with receipt No 318', '41250.00', '0.00', '-41250.00', 716, 13, 1, '318');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `customer_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone_no` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `birthdate` date DEFAULT NULL,
  `active_ticket` varchar(255) DEFAULT NULL,
  `cust_status_id` int(11) DEFAULT NULL,
  `locked_status_id` int(11) NOT NULL,
  `status_id` int(11) DEFAULT NULL,
  `ticket_status_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `created_at`, `updated_at`, `customer_id`, `name`, `phone_no`, `address`, `birthdate`, `active_ticket`, `cust_status_id`, `locked_status_id`, `status_id`, `ticket_status_id`, `processed_by_id`) VALUES
(5, '2022-01-11 03:22:11.702706', '2022-01-11 03:58:29.060013', 'C00005', 'Anonymous', '', 'Anonymous', NULL, NULL, 1, 2, 2, NULL, NULL),
(6, '2022-01-11 04:00:48.426801', '2022-01-11 04:15:51.868569', 'C00006', 'benco', '', 'Abakaliki', NULL, '202211151551', 1, 2, 2, 1, NULL),
(13, '2022-01-11 05:33:18.889994', '2022-01-11 05:42:46.070273', 'C00013', 'Aloke Philip Sunday', '08095757464', 'Amuzu', NULL, NULL, 1, 2, 2, NULL, 12),
(14, '2022-01-11 18:36:28.127011', '2022-01-11 18:36:44.999895', 'C00014', 'Anonymous', 'Anonymous', 'Anonymous', NULL, NULL, 1, 2, 2, NULL, 12),
(15, '2022-01-11 18:38:46.831877', '2022-01-11 18:38:52.937687', 'C00015', 'Anonymous', 'Anonymous', 'Anonymous', NULL, '2022111193852', 1, 1, 2, 1, 12),
(16, '2022-01-17 03:38:09.277565', '2022-01-17 03:47:17.867459', 'C00016', 'Anonymous', 'Anonymous', 'Anonymous', NULL, NULL, 1, 2, 2, NULL, 13);

-- --------------------------------------------------------

--
-- Table structure for table `customer_id`
--

CREATE TABLE `customer_id` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `title` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_id`
--

INSERT INTO `customer_id` (`id`, `created_at`, `updated_at`, `title`) VALUES
(1, '2021-12-07 20:00:12.595090', '2022-01-17 03:38:09.333008', '00017');

-- --------------------------------------------------------

--
-- Table structure for table `customuser`
--

CREATE TABLE `customuser` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `user_type` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customuser`
--

INSERT INTO `customuser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `user_type`) VALUES
(1, 'pbkdf2_sha256$260000$32YxiL3Ua8QNbmylDXX0qY$0UoeH/uqVA5iXYzN3bDPfxp18DfZUG3C7SeJmPhW/VE=', '2022-01-16 16:02:42.331632', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2021-12-07 18:50:58.504932', '1'),
(2, 'pbkdf2_sha256$260000$jTl5qFnl9pnVXlgGhzJhHu$Fywehh7bctwCKWQuTMJWF0GcuEvsgaXEuTCxAtCq8jg=', '2022-01-06 07:06:45.929102', 0, 'iyare', 'Festus', 'Iyare', 'iyare@gmail.com', 0, 1, '2021-12-07 19:42:36.060017', '2'),
(3, 'pbkdf2_sha256$260000$IC3rZOrx2NROW7OOHifwCC$SVAHRitbe5LvMZzlPSPPu5v4A1eih2Vx5dRZ1gt7zeU=', NULL, 0, 'mission', 'Mission', 'Egwu', 'mission@gmail.com', 0, 1, '2021-12-07 19:43:34.285541', '2'),
(4, 'pbkdf2_sha256$260000$fCsaikrWD9JtSqMQumVW2e$e6AMZ7eZO844qm+PjwAkKjzNVxotEsR80G5XxdjkKzA=', '2022-01-01 08:44:19.812347', 0, 'benjamin', 'Benjamin', 'Akpueze', 'benjamin@gmail.com', 0, 1, '2021-12-07 19:44:24.871864', '3'),
(5, 'pbkdf2_sha256$260000$z4HJvupZucKQ1Fg5kj9b0d$Zh/TxnwykCZLz4Bk7YLZhFijCmcLVqqystgOdtQwMzc=', NULL, 0, 'kinsley', 'Kingsley', 'Igwe', 'kingsley@gmail.com', 0, 1, '2021-12-07 19:45:10.423954', '3'),
(6, 'pbkdf2_sha256$260000$Sul8s1LLmb6LYHez8JS8Fe$lHin38O9hMseyeSpJsSoKTJTNprjw7P9py1rpQvIUac=', '2021-12-15 21:15:27.146672', 0, 'nneka', 'Nneka', 'Ogah', 'nneka@gmail.com', 0, 1, '2021-12-07 19:46:16.106235', '4'),
(7, 'pbkdf2_sha256$260000$X65PJFMIcbqauOcXMUyUeO$+SUgcA+FxfpHrjl5kJ5aj7+c5DeKvOQUfq2mcbdxCJQ=', '2021-12-15 21:14:55.065539', 0, 'ofoke', 'Sunday', 'Ofoke', 'ofoke@gmail.com', 0, 1, '2021-12-07 19:47:20.327903', '5'),
(8, 'pbkdf2_sha256$260000$Fjcn9NSpnhtPeUZBKxHtBT$3sYXRFc/kTpaZMIMmEG9F0VpBLfFy2uNQ/8K9cKYzQY=', NULL, 0, 'nnenna', 'Nnnenna', 'Udu', 'nnenna@gmail.com', 0, 1, '2021-12-07 19:48:22.291528', '9'),
(9, 'pbkdf2_sha256$260000$52uRCNpA0H8eCurYpf0Eo3$ccpXbJhRFaznPmgT63fE6GGSTjNHz5Nu3YgYgVthIWs=', '2022-01-17 04:02:54.208654', 0, 'chinwendu', 'Chinwendu', 'Okafor', 'chinwendu@gmail.com', 0, 1, '2021-12-07 19:49:28.259710', '6'),
(10, 'pbkdf2_sha256$260000$W8TZuwETjwyHA6aqcUbxbO$4f8mJ7LgGgUoJCv/uhxGfUXHkzh/3bNUrtFyNPCVODQ=', '2021-12-23 02:12:43.335425', 0, 'omiko', 'Mary', 'Omiko', 'mary@gmail.com', 0, 1, '2021-12-07 19:50:04.034981', '6'),
(11, 'pbkdf2_sha256$260000$4C8c2gTJjdoZmKJvgtMrst$CNXqAqWHlWxWoR+IO1gU0LLDq1aY7VVCX3S0RWkg8W8=', '2022-01-17 04:01:41.480541', 0, 'emmanuella', 'Nwankaego', 'Elijah', 'emmanuella@gmail.com', 0, 1, '2021-12-07 19:50:50.489249', '7'),
(12, 'pbkdf2_sha256$260000$zBjS16wmKq77bRDASHYzTJ$ExM9Oz1tU8xjXlncOK96ZEFzgK283zczZP8rzoPaq5U=', '2022-01-14 11:35:16.432251', 0, 'onuoha', 'Esther', 'Onuoha', 'esther@gmail.com', 0, 1, '2021-12-07 19:51:52.194475', '8'),
(13, 'pbkdf2_sha256$260000$dwnI1i4m1iDtSRD5kzGYWQ$Q12EEgxGbcpHyeRmhJtgELZMpgS4UpJT+eJ/Bv3z5uA=', '2022-01-17 17:38:27.417249', 0, 'onuoha1', 'Esther', 'Onuoha', 'esther1@gmail.com', 0, 1, '2021-12-07 19:52:48.700293', '8'),
(167, 'pbkdf2_sha256$260000$yYpjxzGQ4BcAiedGvs6iU3$//88eAp4hMm3ANYQJQBu1jQ86+LooZFsiRPtFgAdtqg=', NULL, 0, 'BENIDAKA00001', 'BEN', 'IDAKA', 'BEN00001@gmail.com', 0, 1, '2021-12-07 21:04:28.256219', '10'),
(168, 'pbkdf2_sha256$260000$Vz2cSFKoSbvIZ6O8WI4Sbm$7ByEWGUeDZcGi1EzzvmrLYqloaxVzqKeNbPkswiMxb4=', NULL, 0, 'UCHENNAOKOLI00002', 'UCHENNA', 'OKOLI', 'UCHENNA00002@gmail.com', 0, 1, '2021-12-07 21:04:29.704326', '10'),
(169, 'pbkdf2_sha256$260000$dCw9Mr8Q41FmZLBuVfLCpI$2tkkfQYn4rSStlHvS9F19dKJu3No+cG66pE2boDOt/o=', NULL, 0, 'NKONYELUOKONKWO00003', 'NKONYELU', 'OKONKWO', 'NKONYELU00003@gmail.com', 0, 1, '2021-12-07 21:04:30.378892', '10'),
(170, 'pbkdf2_sha256$260000$syhKR4RSRIZZ4VdUR1rj3e$yWjDa6jPFMQXfqGwdVDmtqLrPmq+kyWmd9CRl1JA5Pg=', NULL, 0, 'OPHELIAAMADI00004', 'OPHELIA', 'AMADI', 'OPHELIA00004@gmail.com', 0, 1, '2021-12-07 21:04:31.237945', '10'),
(171, 'pbkdf2_sha256$260000$4vKgLNroBiKGVAAV8QBfBk$kg5h/yTgBWFd5eCsDIZlsmB0Qyo6/9dav1LDzM2v87M=', NULL, 0, 'IKWUONNACHI00005', 'IKWUO', 'NNACHI', 'IKWUO00005@gmail.com', 0, 1, '2021-12-07 21:04:31.885465', '10'),
(172, 'pbkdf2_sha256$260000$WdzrEsJgdCsukb7i9oEDpp$FkU9+vMDql9CXBhMrDn0yt/0w/M7mxYXmeTe+rz//wc=', NULL, 0, 'IFEOMAAGBOWO00006', 'IFEOMA', 'AGBOWO', 'IFEOMA00006@gmail.com', 0, 1, '2021-12-07 21:04:32.514032', '10'),
(173, 'pbkdf2_sha256$260000$yS7f4rzNSsThI8flRKy6pW$E/OmbICkB9W/tACRB8yGL022kN5EBKVZpLX5VGm5UR4=', NULL, 0, 'DRNWANKWO00007', 'DR', 'NWANKWO', 'DR00007@gmail.com', 0, 1, '2021-12-07 21:04:33.142411', '10'),
(174, 'pbkdf2_sha256$260000$Kid9wTCptVkYdc9Fg9YLwr$zVLZ/eXD+N+rMZpWK7BwLbVbG7KO1ytfcoo1XkFt1VM=', NULL, 0, 'EMMANUELABAA00008', 'EMMANUEL', 'ABAA', 'EMMANUEL00008@gmail.com', 0, 1, '2021-12-07 21:04:33.939816', '10'),
(175, 'pbkdf2_sha256$260000$PvmScGHydYRxSihL0OcJzC$5dL+trsDNSvVwHwkQITNi2MZ2qB6/M3R9WGq0xKFMUw=', NULL, 0, 'UGOABAGHA00009', 'UGO', 'ABAGHA', 'UGO00009@gmail.com', 0, 1, '2021-12-07 21:04:34.946640', '10'),
(176, 'pbkdf2_sha256$260000$SYkNnRpuVism7sRZ9GeDnv$X7G1u2wxIy+bJ6lBB9AqTeJe/SEHJ7F09f2RA18P95U=', NULL, 0, 'CHIGOZIABAGHAUGWU00010', 'CHIGOZI', 'ABAGHAUGWU', 'CHIGOZI00010@gmail.com', 0, 1, '2021-12-07 21:04:35.665065', '10'),
(177, 'pbkdf2_sha256$260000$npe42zwyotXbYCKeKBwFek$BP9ZBZ0B3h6yMOOv4CmoJKDuBHrtrQP6SjcAezoPjLI=', NULL, 0, 'NWACHINAMEABANIFI00011', 'NWACHINAME', 'ABANIFI', 'NWACHINAME00011@gmail.com', 0, 1, '2021-12-07 21:04:36.568773', '10'),
(178, 'pbkdf2_sha256$260000$c8pnVLm1b6rTMvzA5EOFdB$ayu2OiwbSVa2MVcqaOe+eFRk06vJqNjWRoMh0Yoszpc=', NULL, 0, 'NNENWAOGOABARA00012', 'NNENWAOGO', 'ABARA', 'NNENWAOGO00012@gmail.com', 0, 1, '2021-12-07 21:04:37.200857', '10'),
(179, 'pbkdf2_sha256$260000$Jco5N8OFsdhwgdQBfGr5ex$of8jqFKQWDmaTuVga5WwvleLWKspLyRAapStOEcHxIc=', NULL, 0, 'LAWRENCEABARA00013', 'LAWRENCE', 'ABARA', 'LAWRENCE00013@gmail.com', 0, 1, '2021-12-07 21:04:37.815713', '10'),
(180, 'pbkdf2_sha256$260000$91bP2RL1qC29p0EW9B2Rfn$KEkEDbNv/+xJgjiZ6k+AP+qqjlu3Ww1Ge5uT9hvXYKw=', NULL, 0, 'NWAKAEGOABARA00014', 'NWAKAEGO', 'ABARA', 'NWAKAEGO00014@gmail.com', 0, 1, '2021-12-07 21:04:38.906581', '10'),
(181, 'pbkdf2_sha256$260000$n71iQat4wAvgN19h1BCGPc$f/eODDy/+bAjI3nkUmRppr7dutHvgfm7O6Jzu9Gngh0=', NULL, 0, 'OBASIABBA00015', 'OBASI', 'ABBA', 'OBASI00015@gmail.com', 0, 1, '2021-12-07 21:04:39.614662', '10'),
(182, 'pbkdf2_sha256$260000$U0vLIJkThxu4tAIMY41cgz$YWYB7u9c5MI9QrvGtBFD+z0sq0jbI31gx7t/NM6+2xI=', NULL, 0, 'EFFIONGABIA00016', 'EFFIONG', 'ABIA', 'EFFIONG00016@gmail.com', 0, 1, '2021-12-07 21:04:40.550051', '10'),
(183, 'pbkdf2_sha256$260000$OBZ1weTnKpEVz9rsPbCGui$rql5CR4kCImHuAJReyP5kp7kUSzPGOdCxKJtCTZ6U+4=', NULL, 0, 'NKIRUKAABIA00017', 'NKIRUKA', 'ABIA', 'NKIRUKA00017@gmail.com', 0, 1, '2021-12-07 21:04:41.091009', '10'),
(184, 'pbkdf2_sha256$260000$xrkE2LzytohsJeC5toxyKE$QKJEDtxd9cNBGDJtndv+CtIA6275ZKFS+rIygXbx9yM=', NULL, 0, 'DRABIA00018', 'DR', 'ABIA', 'DR00018@gmail.com', 0, 1, '2021-12-07 21:04:41.652579', '10'),
(185, 'pbkdf2_sha256$260000$z1ED1vLPAk5hKNgfAGzeRc$k5F6PxVhGB1i2NXI5iUIWUTCbNzE/glPCbfR4OvS4Rg=', NULL, 0, 'UGOCHIABII00019', 'UGOCHI', 'ABII', 'UGOCHI00019@gmail.com', 0, 1, '2021-12-07 21:04:42.284174', '10'),
(186, 'pbkdf2_sha256$260000$h1zbWca8PD12SOkhBZemzW$+rnf87hBlSeX+gtp6x1DyDpgYb9f4/gqLYFdmmxVVpE=', NULL, 0, 'ABEKEABIOLA00020', 'ABEKE', 'ABIOLA', 'ABEKE00020@gmail.com', 0, 1, '2021-12-07 21:04:42.996898', '10'),
(187, 'pbkdf2_sha256$260000$liO2dzxIRYvBgyweEKGraw$/Abu0i70V5h5YwUm4/yCA+m0O047UDntieF3y36rZaw=', NULL, 0, 'CHIOMAABIRI00021', 'CHIOMA', 'ABIRI', 'CHIOMA00021@gmail.com', 0, 1, '2021-12-07 21:04:43.804573', '10'),
(188, 'pbkdf2_sha256$260000$dUu6SPTHgEjQVpeeuQScZ2$rK9bCypSqGDq91AnaF/oDjfYvCYyubV5LCyCJrfQx74=', NULL, 0, 'OLADELEABOKEDE00022', 'OLADELE', 'ABOKEDE', 'OLADELE00022@gmail.com', 0, 1, '2021-12-07 21:04:44.513543', '10'),
(189, 'pbkdf2_sha256$260000$LVSEvCLLoqCrR9j5slly40$Y753KAmJGPlkq1QTR1tQRg7v+tS3k5/iddKxR9Yo0jA=', NULL, 0, 'OMOLARAABOKEDE00023', 'OMOLARA', 'ABOKEDE', 'OMOLARA00023@gmail.com', 0, 1, '2021-12-07 21:04:45.682194', '10'),
(190, 'pbkdf2_sha256$260000$3a8L7Egubx8GohrgxDpqTI$S0buOEfALsAMqoU670ny9nwFVDcG/7mjHILxHuflZ1o=', NULL, 0, 'LEONARDABOR00024', 'LEONARD', 'ABOR', 'LEONARD00024@gmail.com', 0, 1, '2021-12-07 21:04:46.633484', '10'),
(191, 'pbkdf2_sha256$260000$OQxbSLOOWkv00lK64Q8Npp$Iyjay2Vpsh6GJcLSN7HDmam7iL8yR4IOyfllbkd/xEE=', NULL, 0, 'MOMOHABU00025', 'MOMOH', 'ABU', 'MOMOH00025@gmail.com', 0, 1, '2021-12-07 21:04:47.282007', '10'),
(192, 'pbkdf2_sha256$260000$YlFsn0OHCRxbPqtl6RsqtD$fbT0mfhPRPn9fyAhShTgLWrEzf9FG7rhOfPiFcz7IIM=', NULL, 0, 'MMADUABUCHIABUWA00026', 'MMADUABUCHI', 'ABUWA', 'MMADUABUCHI00026@gmail.com', 0, 1, '2021-12-07 21:04:48.469909', '10'),
(193, 'pbkdf2_sha256$260000$vgjdPatZ5Gk2gfSKboGIft$cUH6j897XBBBXSJ5ayqqMecPglEFEUhXhwUKusxiOME=', NULL, 0, 'MAXWELLACHI00027', 'MAXWELL', 'ACHI', 'MAXWELL00027@gmail.com', 0, 1, '2021-12-07 21:04:49.853889', '10'),
(194, 'pbkdf2_sha256$260000$T6eg6L1M9bbXJ4A3uXgLBM$kvAfsocBFYaEDMDBpxw7Ivrf/5DSs1aTdAPLNQf8Gsw=', NULL, 0, 'EZEKIELACHONWA00028', 'EZEKIEL', 'ACHONWA', 'EZEKIEL00028@gmail.com', 0, 1, '2021-12-07 21:04:50.500986', '10'),
(195, 'pbkdf2_sha256$260000$oR35dN4Z5TowvbHcnLld7U$0sHF2H3JLTTWMrZMvjeYYCAKb2yvtb/Gw7rup0k/+dQ=', NULL, 0, 'UDOCHRISACHUGONYE00029', 'UDOCHRIS', 'ACHUGONYE', 'UDOCHRIS00029@gmail.com', 0, 1, '2021-12-07 21:04:51.153057', '10'),
(196, 'pbkdf2_sha256$260000$YU2juB8jyN70ApOqDqkSAw$xcpZzl4lc3Xajq8RfLWxFsZbB2MaqNkpg0yXl1KLzJY=', NULL, 0, 'MATTHEWADAMA00030', 'MATTHEW', 'ADAMA', 'MATTHEW00030@gmail.com', 0, 1, '2021-12-07 21:04:51.884385', '10'),
(197, 'pbkdf2_sha256$260000$hE8XABo68tC5Z3MUogC2V5$NRtOzgJcDzJ7xZP7zbPj3ZJXXkt1DVJFsVUAt6Q1FvU=', NULL, 0, 'BEATRIADAMSOKORIE00031', 'BEATRI', 'ADAMSOKORIE', 'BEATRI00031@gmail.com', 0, 1, '2021-12-07 21:04:52.801719', '10'),
(198, 'pbkdf2_sha256$260000$kchCBzcRV8Fn3DmF4DxHNT$yfCywcK/NXJjb3bRVIvQ7ghCR4CBt1DEC0hmm4VYdyU=', NULL, 0, 'IFEOMAADANI00032', 'IFEOMA', 'ADANI', 'IFEOMA00032@gmail.com', 0, 1, '2021-12-07 21:04:53.766507', '10'),
(199, 'pbkdf2_sha256$260000$Vzxgx9HV5mcWYflZcgV6ac$YLDFGApYRlRhWsE23SAN4d1vC3ElenGuzOBzP8H8yMQ=', NULL, 0, 'IBUKUNADEOLU00033', 'IBUKUN', 'ADEOLU', 'IBUKUN00033@gmail.com', 0, 1, '2021-12-07 21:04:55.066947', '10'),
(200, 'pbkdf2_sha256$260000$KONpQ5lLsulamfWGKUuPRG$AdcdqRYFXDA5JH/HOToskIWFLu3BIwAQvmN13h2JaNg=', NULL, 0, 'KUSSADEOYE00034', 'KUSS', 'ADEOYE', 'KUSS00034@gmail.com', 0, 1, '2021-12-07 21:04:55.596334', '10'),
(201, 'pbkdf2_sha256$260000$kljhpCxmdJaJGJr8UCiV4w$iHJzqs17nAnBSGPY0GkD0GzrLklH2MolNz399HQQJzA=', NULL, 0, 'SAMSONADEYEMI00035', 'SAMSON', 'ADEYEMI', 'SAMSON00035@gmail.com', 0, 1, '2021-12-07 21:04:56.199523', '10'),
(202, 'pbkdf2_sha256$260000$MMSDxgBaX2imHaqbk8kbAv$ePlusmHfhaSK8+z0Xrr2QdFVKddBVeq+xJZKpfolbyY=', NULL, 0, 'EMMANUELADIDU00036', 'EMMANUEL', 'ADIDU', 'EMMANUEL00036@gmail.com', 0, 1, '2021-12-07 21:04:56.863740', '10'),
(203, 'pbkdf2_sha256$260000$yGHNAI8n2KlpOL1JdvLpDq$EjYUjEq+Wri2OHy0tfj9uI8G57K+A+ffM1ErfFC2Xsw=', NULL, 0, 'NWANYIEZEADIELE00037', 'NWANYIEZE', 'ADIELE', 'NWANYIEZE00037@gmail.com', 0, 1, '2021-12-07 21:04:57.538494', '10'),
(204, 'pbkdf2_sha256$260000$Mc0fbitHQXynWQFddGPzA6$WJchcqzr5E1tTAKQzMWXvhd5o2/B7fY0egzOYGWOOXM=', NULL, 0, 'EMMANUELADIGWE00038', 'EMMANUEL', 'ADIGWE', 'EMMANUEL00038@gmail.com', 0, 1, '2021-12-07 21:04:58.327339', '10'),
(205, 'pbkdf2_sha256$260000$zg5WAY1sjU2mBUsKYK4GSh$h2bsTfc76y43YVbFVlBQX/IgG5h+56iNGTr3ttVX2gg=', NULL, 0, 'JULIANAADIKWU00039', 'JULIANA', 'ADIKWU', 'JULIANA00039@gmail.com', 0, 1, '2021-12-07 21:04:59.221230', '10'),
(206, 'pbkdf2_sha256$260000$jEAGGIDWouxetWlviz877B$SHJ+YzBTf8j99gzhlav0vBs674KuMTB1xPMojgWY4hY=', NULL, 0, 'CAROLINEADIMORAH00040', 'CAROLINE', 'ADIMORAH', 'CAROLINE00040@gmail.com', 0, 1, '2021-12-07 21:04:59.895911', '10'),
(207, 'pbkdf2_sha256$260000$XKO8g1toO6g8fpDhC9vBYB$uF3R+5arVnxH9KOLWAeJsFc3ex+TdsuCzfqC7zSk1AQ=', NULL, 0, 'ORAEKIADIMORAH00041', 'ORAEKI', 'ADIMORAH', 'ORAEKI00041@gmail.com', 0, 1, '2021-12-07 21:05:00.764871', '10'),
(208, 'pbkdf2_sha256$260000$on7H2Scc78v12vFrH2t1ZO$ftzgMIbWDz168uPSy9CHno2n8JC5Wg4t3z0Q9TWY1hU=', NULL, 0, 'IFEYINWAADOGU00042', 'IFEYINWA', 'ADOGU', 'IFEYINWA00042@gmail.com', 0, 1, '2021-12-07 21:05:01.529186', '10'),
(209, 'pbkdf2_sha256$260000$izW5D6a6kJ9WOQhQ9mJT3M$IgFd6Hg9YT5WRfOLt05512XCIW48VLomLwpqqZ5ag8c=', NULL, 0, 'OGHENEOCHUKOADOKA00043', 'OGHENEOCHUKO', 'ADOKA', 'OGHENEOCHUKO00043@gmail.com', 0, 1, '2021-12-07 21:05:02.089202', '10'),
(210, 'pbkdf2_sha256$260000$yZoVs5uMWXAoliWFBlBUA0$fEXf/6aEgCwif2hUs7zyJSj7XjzPXm7swh+EcZI/UM4=', NULL, 0, 'NWOVAADOKE00044', 'NWOVA', 'ADOKE', 'NWOVA00044@gmail.com', 0, 1, '2021-12-07 21:05:02.629138', '10'),
(211, 'pbkdf2_sha256$260000$7lKzvix7uswn1HF04JRa79$pRsrLvzwNEki8QDCsdsWvHTV0p944db5xdegouVtWHE=', NULL, 0, 'EDACHEADOKWU00045', 'EDACHE', 'ADOKWU', 'EDACHE00045@gmail.com', 0, 1, '2021-12-07 21:05:03.217295', '10'),
(212, 'pbkdf2_sha256$260000$uf4twgmPXPBk2a61zFnsYN$ftPjEFLy4hDQtya6pKblan/O5INug83B8ijovtDzqtU=', NULL, 0, 'OBINNAADONU00046', 'OBINNA', 'ADONU', 'OBINNA00046@gmail.com', 0, 1, '2021-12-07 21:05:03.779337', '10'),
(213, 'pbkdf2_sha256$260000$QpxZ7fBJ19QRLahmHMigPA$HloDuRyWgZYKaGvv+2P/qy22hGLQjrfBoBNx68Kw8Xs=', NULL, 0, 'LINDAADUAKA00047', 'LINDA', 'ADUAKA', 'LINDA00047@gmail.com', 0, 1, '2021-12-07 21:05:04.447497', '10'),
(214, 'pbkdf2_sha256$260000$MgAx1kUQvooxDLbvgG5T1p$XMZ4eX6yyYBeKJhz+kt8tpOQEwPAxhuyzzDuQ+D2o68=', NULL, 0, 'NGOZIADUAKA00048', 'NGOZI', 'ADUAKA', 'NGOZI00048@gmail.com', 0, 1, '2021-12-07 21:05:05.133033', '10'),
(215, 'pbkdf2_sha256$260000$lLz6ByLwxXFktz09mW6lm0$h4Bp1y+2YFF4k5F8gkv+v2x7DH+JgICCP/Na9K7EEuo=', NULL, 0, 'VIVIANADUAKA00049', 'VIVIAN', 'ADUAKA', 'VIVIAN00049@gmail.com', 0, 1, '2021-12-07 21:05:05.875124', '10'),
(216, 'pbkdf2_sha256$260000$cFEPlxTshfE2JFJ04egUjf$ElkGoOL5WfMTU1yqes10zFocr8UVZFlF3GGZOrAp02U=', NULL, 0, 'ADAGBAADUWA00050', 'ADAGBA', 'ADUWA', 'ADAGBA00050@gmail.com', 0, 1, '2021-12-07 21:05:06.453588', '10'),
(227, 'pbkdf2_sha256$260000$j9XsoFqb9p9zRNRyoWMTEx$LXXtTtuH5UkduAuBTT0ETByYMw6Vqgnn7LVB+aRT26I=', NULL, 0, 'fred11144', 'FRED', 'EKPE', 'fred1@gmail.com', 0, 1, '2021-12-16 10:06:52.288295', '10');

-- --------------------------------------------------------

--
-- Table structure for table `customuser_groups`
--

CREATE TABLE `customuser_groups` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `customuser_user_permissions`
--

CREATE TABLE `customuser_user_permissions` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `daily_sales`
--

CREATE TABLE `daily_sales` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `ticket` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone_no` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `item_code` varchar(255) NOT NULL,
  `item_name` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `unit_selling_price` decimal(20,2) NOT NULL,
  `total` decimal(20,2) NOT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL,
  `receipt` varchar(20) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `daily_sales`
--

INSERT INTO `daily_sales` (`id`, `created_at`, `updated_at`, `ticket`, `name`, `phone_no`, `address`, `item_code`, `item_name`, `quantity`, `unit_selling_price`, `total`, `processed_by_id`, `status_id`, `receipt`, `product_id`) VALUES
(8, '2022-01-11 07:34:17.956003', '2022-01-06 07:34:17.956003', '20221681119', 'BEN IDAKA MAUREEN', '08064004355', 'Abakaliki', '00001', 'BOURNVITA 900G', 5, '2300.00', '11500.00', 12, 1, '292', NULL),
(9, '2022-01-11 07:34:18.316020', '2022-01-06 07:34:18.317021', '20221681119', 'BEN IDAKA MAUREEN', '08064004355', 'Abakaliki', '00055', 'ANGEL WIPES', 10, '700.00', '7000.00', 12, 1, '292', NULL),
(10, '2022-01-11 07:34:18.616834', '2022-01-06 07:34:18.616834', '20221681119', 'BEN IDAKA MAUREEN', '08064004355', 'Abakaliki', '00070', 'ARDEN CARROT SOAP', 2, '2100.00', '4200.00', 12, 1, '292', NULL),
(11, '2022-01-11 17:22:09.617141', '2022-01-10 17:22:09.617141', '2022110133719', 'OPHELIA AMADI CHIB', '08064004358', '', '00055', 'ANGEL WIPES', 10, '700.00', '7000.00', 12, 1, '293', NULL),
(12, '2022-01-11 17:22:09.736316', '2022-01-10 17:22:09.736316', '2022110133719', 'OPHELIA AMADI CHIB', '08064004358', '', '00101', 'ARIEL DETERGENT', 5, '1800.00', '9000.00', 12, 1, '293', NULL),
(13, '2022-01-11 18:56:27.634729', '2022-01-10 18:56:27.634729', '2022110194419', 'IKWUO NNACHI IJEM', '08064004359', '', '00001', 'BOURNVITA 900G', 3, '2300.00', '6900.00', 12, 1, '294', NULL),
(14, '2022-01-11 18:56:27.804232', '2022-01-10 18:56:27.804232', '2022110194419', 'IKWUO NNACHI IJEM', '08064004359', '', '00070', 'ARDEN CARROT SOAP', 3, '2100.00', '6300.00', 12, 1, '294', NULL),
(15, '2022-01-11 18:56:28.195342', '2022-01-10 18:56:28.195342', '2022110194419', 'IKWUO NNACHI IJEM', '08064004359', '', '00108', 'APPLE JELLY', 4, '150.00', '600.00', 12, 1, '294', NULL),
(29, '2022-01-11 03:21:19.267994', '2022-01-11 03:21:19.267994', '2022110222029', 'MMADUABUCHI ABUWA ', '08064004380', '', '00001', 'BOURNVITA 900G', 2, '2300.00', '4600.00', 12, 1, '306', NULL),
(30, '2022-01-11 03:21:19.397031', '2022-01-11 03:21:19.397031', '2022110222029', 'MMADUABUCHI ABUWA ', '08064004380', '', '00055', 'ANGEL WIPES', 5, '700.00', '3500.00', 12, 1, '306', NULL),
(31, '2022-01-11 03:21:19.517513', '2022-01-11 03:21:19.517513', '2022110222029', 'MMADUABUCHI ABUWA ', '08064004380', '', '00070', 'ARDEN CARROT SOAP', 5, '2100.00', '10500.00', 12, 1, '306', NULL),
(34, '2022-01-11 03:58:29.217861', '2022-01-11 03:58:29.217861', '202211142555', 'Anonymous', 'Anonymous', 'Anonymous', '00055', 'ANGEL WIPES', 5, '700.00', '3500.00', 12, 1, '308', NULL),
(35, '2022-01-11 03:58:29.336232', '2022-01-11 03:58:29.336232', '202211142555', 'Anonymous', 'Anonymous', 'Anonymous', '00108', 'APPLE JELLY', 2, '150.00', '300.00', 12, 1, '308', NULL),
(36, '2022-01-11 04:04:33.489485', '2022-01-11 04:04:33.489485', '2022111549', 'benco', 'Anonymous', 'Abakaliki', '00001', 'BOURNVITA 900G', 6, '2300.00', '13800.00', 12, 1, '309', NULL),
(37, '2022-01-11 04:05:29.438107', '2022-01-11 04:05:29.438107', '20221115451', 'benco', '07809575858', 'Abakaliki', '00055', 'ANGEL WIPES', 5, '700.00', '3500.00', 12, 1, '310', NULL),
(38, '2022-01-11 04:08:47.219602', '2022-01-11 04:08:47.219602', '2022111560', 'benco', '54554545545', 'Abakaliki', '00055', 'ANGEL WIPES', 5, '700.00', '3500.00', 12, 1, '311', NULL),
(39, '2022-01-11 04:08:47.441144', '2022-01-11 04:08:47.441144', '2022111560', 'benco', '54554545545', 'Abakaliki', '00101', 'ARIEL DETERGENT', 3, '1800.00', '5400.00', 12, 1, '311', NULL),
(40, '2022-01-11 04:13:47.197396', '2022-01-11 04:13:47.197396', '20221115129', 'benco', '56567776666', 'Abakaliki', '00070', 'ARDEN CARROT SOAP', 3, '2100.00', '6300.00', 12, 1, '312', NULL),
(41, '2022-01-11 05:42:46.332591', '2022-01-11 05:42:46.332591', '202211163622', 'Aloke Philip Sunday', '08095757464', 'Amuzu', '00001', 'BOURNVITA 900G', 5, '2300.00', '11500.00', 12, 1, '313', NULL),
(42, '2022-01-11 18:36:45.320524', '2022-01-11 18:36:45.320524', '2022111193636', 'Anonymous', 'Anonymous', 'Anonymous', '00001', 'BOURNVITA 900G', 5, '2300.00', '11500.00', 12, 1, '314', NULL),
(43, '2022-01-17 03:47:18.181179', '2022-01-17 03:47:18.181179', '202211744235', 'Anonymous', 'Anonymous', 'Anonymous', '', '', 5, '700.00', '3500.00', 13, 1, '316', 971),
(44, '2022-01-17 03:53:25.102192', '2022-01-17 03:53:25.102192', '202211745141', 'BEN IDAKA MAUREEN', '08064004355', 'Abakaliki', '', '', 5, '2300.00', '11500.00', 13, 1, '317', 917),
(45, '2022-01-17 04:03:22.562025', '2022-01-17 04:03:22.562025', '20221174540', 'UCHENNA OKOLI OBIA', '08064004356', '', '00008', 'COWBELL MILK 380G', 5, '950.00', '4750.00', 13, 1, '318', NULL),
(46, '2022-01-17 04:03:22.719926', '2022-01-17 04:03:22.719926', '20221174540', 'UCHENNA OKOLI OBIA', '08064004356', '', '00002', 'BOURNVITA 500G', 5, '1200.00', '6000.00', 13, 1, '318', NULL),
(47, '2022-01-17 04:03:22.932929', '2022-01-17 04:03:22.932929', '20221174540', 'UCHENNA OKOLI OBIA', '08064004356', '', '00055', 'ANGEL WIPES', 5, '700.00', '3500.00', 13, 1, '318', NULL),
(48, '2022-01-17 04:03:23.032365', '2022-01-17 04:03:23.032365', '20221174540', 'UCHENNA OKOLI OBIA', '08064004356', '', '00039', 'LOYA MILK 900G', 10, '2700.00', '27000.00', 13, 1, '318', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `daily_sales_cash_flow_summary`
--

CREATE TABLE `daily_sales_cash_flow_summary` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `description` varchar(255) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `sales_category_id` int(11) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `daily_sales_cash_flow_summary`
--

INSERT INTO `daily_sales_cash_flow_summary` (`id`, `created_at`, `updated_at`, `description`, `amount`, `processed_by_id`, `sales_category_id`, `status_id`) VALUES
(5, '2022-01-11 20:36:49.158353', '2022-01-11 20:36:49.158353', 'CASH SALES', '62800.00', 12, 1, 1),
(6, '2022-01-11 20:36:49.225580', '2022-01-11 20:36:49.225580', 'CREDIT SALES', '52500.00', 12, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `daily_sales_summary`
--

CREATE TABLE `daily_sales_summary` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `receipt` varchar(255) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `sale_id` int(11) DEFAULT NULL,
  `sales_category_id` int(11) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `daily_sales_summary`
--

INSERT INTO `daily_sales_summary` (`id`, `created_at`, `updated_at`, `receipt`, `amount`, `sale_id`, `sales_category_id`, `status_id`) VALUES
(7, '2022-01-11 07:34:18.756166', '2022-01-06 07:34:18.757170', '292', '22700.00', 8, 2, 2),
(8, '2022-01-11 17:22:10.205874', '2022-01-10 17:22:10.205874', '293', '16000.00', 11, 2, 2),
(9, '2022-01-11 18:56:28.414420', '2022-01-10 18:56:28.414420', '294', '13800.00', 13, 2, 2),
(13, '2022-01-11 03:21:19.705249', '2022-01-11 03:21:19.705249', '306', '10500.00', 29, 1, 2),
(14, '2022-01-11 03:58:29.473150', '2022-01-11 03:58:29.473150', '308', '300.00', 34, 1, 2),
(15, '2022-01-11 04:04:33.509370', '2022-01-11 04:04:33.509370', '309', '13800.00', 36, 1, 2),
(16, '2022-01-11 04:05:29.485118', '2022-01-11 04:05:29.485118', '310', '3500.00', 37, 1, 2),
(17, '2022-01-11 04:08:47.486175', '2022-01-11 04:08:47.486175', '311', '5400.00', 38, 1, 2),
(18, '2022-01-11 04:13:47.263398', '2022-01-11 04:13:47.263398', '312', '6300.00', 40, 1, 2),
(19, '2022-01-11 05:42:46.561483', '2022-01-11 05:42:46.561483', '313', '11500.00', 41, 1, 2),
(20, '2022-01-11 18:36:45.390677', '2022-01-11 18:36:45.391676', '314', '11500.00', 42, 1, 2),
(21, '2022-01-17 03:47:18.351918', '2022-01-17 03:47:18.351918', '316', '3500.00', 43, 1, 1),
(22, '2022-01-17 03:53:25.220119', '2022-01-17 03:53:25.220119', '317', '11500.00', 44, 1, 1),
(23, '2022-01-17 04:03:23.308114', '2022-01-17 04:03:23.308114', '318', '41250.00', 45, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `data_capture_manager`
--

CREATE TABLE `data_capture_manager` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `datejoined_upload_status`
--

CREATE TABLE `datejoined_upload_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `datejoined_upload_status`
--

INSERT INTO `datejoined_upload_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'PENDING', '2021-12-07 19:08:57.497360', '2021-12-07 19:08:57.497360'),
(2, 'UPLOADED', '2021-12-07 19:08:57.531401', '2021-12-07 19:08:57.531401'),
(3, 'VERIFIED', '2021-12-07 19:08:57.688625', '2021-12-07 19:08:57.688625');

-- --------------------------------------------------------

--
-- Table structure for table `default_password`
--

CREATE TABLE `default_password` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `title` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `default_password`
--

INSERT INTO `default_password` (`id`, `created_at`, `updated_at`, `title`) VALUES
(1, '2021-12-07 20:32:33.331615', '2021-12-07 20:32:33.331615', 'Password123');

-- --------------------------------------------------------

--
-- Table structure for table `departments`
--

CREATE TABLE `departments` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `departments`
--

INSERT INTO `departments` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'ACCIDENT AND EMERGENCY', '2021-12-16 07:41:32.320343', '2021-12-16 07:41:32.320343'),
(2, 'ACCOUNTS', '2021-12-16 07:41:32.390299', '2021-12-16 07:41:32.390299'),
(3, 'ANAESTHESIOLOGY', '2021-12-16 07:41:32.609172', '2021-12-16 07:41:32.609172'),
(4, 'AUDIT', '2021-12-16 07:41:32.674133', '2021-12-16 07:41:32.674133'),
(5, 'CALABAR CANCER REGISTRY', '2021-12-16 07:41:32.773068', '2021-12-16 07:41:32.773068'),
(6, 'CARDIOLOGY', '2021-12-16 07:41:32.819036', '2021-12-16 07:41:32.820043'),
(7, 'CHEMICAL PATHOLOGY', '2021-12-16 07:41:32.871002', '2021-12-16 07:41:32.871002'),
(8, 'CHILD DENTAL HEALTH', '2021-12-16 07:41:32.943956', '2021-12-16 07:41:32.943956'),
(9, 'CLINICAL SERVICES & TRAINING', '2021-12-16 07:41:32.972944', '2021-12-16 07:41:32.972944'),
(10, 'COMMUNITY HEALTH OFFICERS TRAINING PROGRAM', '2021-12-16 07:41:33.019158', '2021-12-16 07:41:33.019158'),
(11, 'COMMUNITY MEDICINE', '2021-12-16 07:41:33.361726', '2021-12-16 07:41:33.361726'),
(12, 'DENTAL DEPARTMENT', '2021-12-16 07:41:33.406694', '2021-12-16 07:41:33.406694'),
(13, 'FAMILY MEDICINE', '2021-12-16 07:41:33.465654', '2021-12-16 07:41:33.465654'),
(14, 'GENERAL ADMINISTRATION', '2021-12-16 07:41:33.507630', '2021-12-16 07:41:33.507630'),
(15, 'HAEMATOLOGY', '2021-12-16 07:41:33.560599', '2021-12-16 07:41:33.560599'),
(16, 'HUMAN RESOURCE MANAGEMENT', '2021-12-16 07:41:33.606568', '2021-12-16 07:41:33.606568'),
(17, 'ICT', '2021-12-16 07:41:33.676525', '2021-12-16 07:41:33.676525'),
(18, 'INTERNAL MEDICINE', '2021-12-16 07:41:33.718504', '2021-12-16 07:41:33.718504'),
(19, 'LAUNDRY', '2021-12-16 07:41:33.775467', '2021-12-16 07:41:33.775467'),
(20, 'LEGAL SERVICES', '2021-12-16 07:41:33.835425', '2021-12-16 07:41:33.835425'),
(21, 'MEDICAL LIBRARY', '2021-12-16 07:41:33.932369', '2021-12-16 07:41:33.932369'),
(22, 'MEDICAL MICROBIOLOGY & PARASITOLOGY', '2021-12-16 07:41:34.105258', '2021-12-16 07:41:34.105258'),
(23, 'MEDICAL SOCIAL SERVICES', '2021-12-16 07:41:34.263189', '2021-12-16 07:41:34.263189'),
(24, 'NHIS', '2021-12-16 07:41:34.461071', '2021-12-16 07:41:34.461071'),
(25, 'NURSING SERVICES', '2021-12-16 07:41:34.522028', '2021-12-16 07:41:34.522028'),
(26, 'OBSTETRICS & GYNAECOLOGY', '2021-12-16 07:41:34.589985', '2021-12-16 07:41:34.589985'),
(27, 'OPHTHALMOLOGY', '2021-12-16 07:41:34.655953', '2021-12-16 07:41:34.655953'),
(28, 'ORAL & MAXILLOFACIAL SURGERY', '2021-12-16 07:41:34.707913', '2021-12-16 07:41:34.708913'),
(29, 'ORTHOPAEDICS & TRAUMATOLOGY', '2021-12-16 07:41:34.768877', '2021-12-16 07:41:34.769877'),
(30, 'PAEDIATRICS', '2021-12-16 07:41:34.804856', '2021-12-16 07:41:34.804856'),
(31, 'PATHOLOGY', '2021-12-16 07:41:34.869812', '2021-12-16 07:41:34.869812'),
(32, 'PHARMACY', '2021-12-16 07:41:34.905790', '2021-12-16 07:41:34.905790'),
(33, 'PHYSIOTHERAPY', '2021-12-16 07:41:34.951763', '2021-12-16 07:41:34.952761'),
(34, 'PREVENTIVE DENTISTRY', '2021-12-16 07:41:34.994735', '2021-12-16 07:41:34.994735'),
(35, 'RADIOLOGY', '2021-12-16 07:41:35.038709', '2021-12-16 07:41:35.038709'),
(36, 'RESTORATIVE DENTISTRY', '2021-12-16 07:41:35.080680', '2021-12-16 07:41:35.080680'),
(37, 'SERVICOM', '2021-12-16 07:41:35.128652', '2021-12-16 07:41:35.128652'),
(38, 'SURGERY', '2021-12-16 07:41:35.192628', '2021-12-16 07:41:35.192628'),
(39, 'TREASURY', '2021-12-16 07:41:35.260578', '2021-12-16 07:41:35.260578'),
(40, 'UROLOGY', '2021-12-16 07:41:35.308544', '2021-12-16 07:41:35.308544'),
(41, 'WORKS', '2021-12-16 07:41:35.376504', '2021-12-16 07:41:35.376504');

-- --------------------------------------------------------

--
-- Table structure for table `disbursement_officers`
--

CREATE TABLE `disbursement_officers` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `officer_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `disbursement_officers`
--

INSERT INTO `disbursement_officers` (`id`, `created_at`, `updated_at`, `officer_id`, `status_id`) VALUES
(1, '2021-12-15 09:11:08.564882', '2021-12-15 09:13:38.046705', 6, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(131, 'cooperative', 'accountdeductions'),
(7, 'cooperative', 'accounttypes'),
(8, 'cooperative', 'admincharges'),
(130, 'cooperative', 'adminmaster'),
(9, 'cooperative', 'approvabletransactions'),
(10, 'cooperative', 'approvalofficers'),
(11, 'cooperative', 'approvalstatus'),
(12, 'cooperative', 'autoreceipt'),
(13, 'cooperative', 'banks'),
(129, 'cooperative', 'cashbook'),
(14, 'cooperative', 'certifiabletransactions'),
(15, 'cooperative', 'certificationofficers'),
(16, 'cooperative', 'certificationstatus'),
(128, 'cooperative', 'cheque_table'),
(135, 'cooperative', 'compulsorysavings'),
(17, 'cooperative', 'cooperativebankaccounts'),
(127, 'cooperative', 'cooperativeshopledger'),
(18, 'cooperative', 'customerid'),
(19, 'cooperative', 'customers'),
(6, 'cooperative', 'customuser'),
(20, 'cooperative', 'daily_sales'),
(136, 'cooperative', 'daily_sales_cash_flow_summary'),
(126, 'cooperative', 'daily_sales_summary'),
(125, 'cooperative', 'datacapturemanager'),
(21, 'cooperative', 'datejoineduploadstatus'),
(22, 'cooperative', 'defaultpassword'),
(23, 'cooperative', 'departments'),
(124, 'cooperative', 'disbursementofficers'),
(24, 'cooperative', 'exclusivestatus'),
(123, 'cooperative', 'externalfascilitiesmain'),
(122, 'cooperative', 'externalfascilitiestemp'),
(25, 'cooperative', 'gender'),
(121, 'cooperative', 'general_cash_sales_selected'),
(120, 'cooperative', 'general_cash_sales_selectedtemp'),
(26, 'cooperative', 'interestdeductionsource'),
(144, 'cooperative', 'itemwriteoffreasons'),
(27, 'cooperative', 'lga'),
(28, 'cooperative', 'loanapplication'),
(119, 'cooperative', 'loanapplicationguarnators'),
(118, 'cooperative', 'loanapplicationsettings'),
(117, 'cooperative', 'loanbasedsavings'),
(29, 'cooperative', 'loancategory'),
(116, 'cooperative', 'loanformissuance'),
(115, 'cooperative', 'loanguarantors'),
(30, 'cooperative', 'loanmergestatus'),
(31, 'cooperative', 'loannumber'),
(32, 'cooperative', 'loanrequest'),
(114, 'cooperative', 'loanrequestattachments'),
(113, 'cooperative', 'loanrequestsettings'),
(33, 'cooperative', 'loanschedulestatus'),
(112, 'cooperative', 'loanscleared'),
(111, 'cooperative', 'loansdisbursed'),
(110, 'cooperative', 'loansrepaymentbase'),
(109, 'cooperative', 'loansuploaded'),
(34, 'cooperative', 'loansuploadstatus'),
(35, 'cooperative', 'locations'),
(36, 'cooperative', 'lockedstatus'),
(37, 'cooperative', 'members'),
(103, 'cooperative', 'membersaccountsdomain'),
(38, 'cooperative', 'membersbankaccounts'),
(102, 'cooperative', 'memberscashdeposits'),
(39, 'cooperative', 'memberscashwithdrawals'),
(133, 'cooperative', 'memberscashwithdrawalsapplication'),
(101, 'cooperative', 'memberscashwithdrawalsmain'),
(100, 'cooperative', 'membersexclusiveness'),
(99, 'cooperative', 'membershipformsalesrecord'),
(40, 'cooperative', 'membershiprequest'),
(98, 'cooperative', 'membershiprequestadditionalattachment'),
(97, 'cooperative', 'membershiprequestadditionalinfo'),
(41, 'cooperative', 'membershipstatus'),
(42, 'cooperative', 'membersidmanager'),
(96, 'cooperative', 'membersnextofkins'),
(95, 'cooperative', 'memberssalaryupdaterequest'),
(43, 'cooperative', 'membersshareaccounts'),
(94, 'cooperative', 'membersshareaccountsmain'),
(44, 'cooperative', 'membersshareconfigurations'),
(93, 'cooperative', 'membersshareinitialupdaterequest'),
(92, 'cooperative', 'memberssharepurchaserequest'),
(45, 'cooperative', 'memberswelfare'),
(91, 'cooperative', 'memberswelfareaccounts'),
(90, 'cooperative', 'memberswelfareaccountsmain'),
(108, 'cooperative', 'members_cash_sales_selected'),
(107, 'cooperative', 'members_credit_purchase_analysis'),
(106, 'cooperative', 'members_credit_purchase_summary'),
(105, 'cooperative', 'members_credit_sales_external_fascilities'),
(104, 'cooperative', 'members_credit_sales_selected'),
(89, 'cooperative', 'monthlydeductionlist'),
(88, 'cooperative', 'monthlydeductionlistgenerated'),
(87, 'cooperative', 'monthlygeneratedtransactions'),
(86, 'cooperative', 'monthlygroupgeneratedtransactions'),
(46, 'cooperative', 'multipleloanstatus'),
(47, 'cooperative', 'nextofkinsmaximun'),
(48, 'cooperative', 'nokrelationships'),
(85, 'cooperative', 'nonmemberaccountdeductions'),
(84, 'cooperative', 'norminalroll'),
(49, 'cooperative', 'paymentchannels'),
(83, 'cooperative', 'personalledger'),
(50, 'cooperative', 'processingstatus'),
(51, 'cooperative', 'productcategory'),
(141, 'cooperative', 'purchases'),
(142, 'cooperative', 'purchases_temp'),
(143, 'cooperative', 'purchase_header'),
(81, 'cooperative', 'receipts'),
(52, 'cooperative', 'receiptstatus'),
(80, 'cooperative', 'receipts_shop'),
(53, 'cooperative', 'receipttypes'),
(82, 'cooperative', 'receipt_cancelled'),
(54, 'cooperative', 'salaryinstitution'),
(55, 'cooperative', 'salescategory'),
(79, 'cooperative', 'savingsuploaded'),
(56, 'cooperative', 'savingsuploadstatus'),
(78, 'cooperative', 'sharesdeductionsavings'),
(132, 'cooperative', 'sharessalesrecord'),
(57, 'cooperative', 'sharesunits'),
(58, 'cooperative', 'sharesuploadstatus'),
(77, 'cooperative', 'staff'),
(76, 'cooperative', 'standingorderaccounts'),
(59, 'cooperative', 'states'),
(75, 'cooperative', 'stock'),
(60, 'cooperative', 'submissionstatus'),
(137, 'cooperative', 'suppliers'),
(140, 'cooperative', 'suppliers_branches'),
(139, 'cooperative', 'suppliers_majors'),
(138, 'cooperative', 'suppliers_reps'),
(74, 'cooperative', 'taskmanager'),
(61, 'cooperative', 'ticketstatus'),
(62, 'cooperative', 'titles'),
(73, 'cooperative', 'transactionajustmentrequest'),
(134, 'cooperative', 'transactionloanajustmentrequest'),
(72, 'cooperative', 'transactionperiods'),
(63, 'cooperative', 'transactionsources'),
(64, 'cooperative', 'transactionstatus'),
(65, 'cooperative', 'transactiontypes'),
(66, 'cooperative', 'userlevels'),
(67, 'cooperative', 'userslevel'),
(68, 'cooperative', 'usertype'),
(69, 'cooperative', 'welfareuploadstatus'),
(71, 'cooperative', 'withdrawabletransactions'),
(70, 'cooperative', 'withdrawalstatus'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-12-07 18:39:54.757726'),
(2, 'contenttypes', '0002_remove_content_type_name', '2021-12-07 18:39:55.431695'),
(3, 'auth', '0001_initial', '2021-12-07 18:40:01.473047'),
(4, 'auth', '0002_alter_permission_name_max_length', '2021-12-07 18:40:03.219430'),
(5, 'auth', '0003_alter_user_email_max_length', '2021-12-07 18:40:03.273308'),
(6, 'auth', '0004_alter_user_username_opts', '2021-12-07 18:40:03.333734'),
(7, 'auth', '0005_alter_user_last_login_null', '2021-12-07 18:40:03.366249'),
(8, 'auth', '0006_require_contenttypes_0002', '2021-12-07 18:40:03.412434'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2021-12-07 18:40:03.484916'),
(10, 'auth', '0008_alter_user_username_max_length', '2021-12-07 18:40:03.549516'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2021-12-07 18:40:03.732294'),
(12, 'auth', '0010_alter_group_name_max_length', '2021-12-07 18:40:03.903392'),
(13, 'auth', '0011_update_proxy_permissions', '2021-12-07 18:40:03.986542'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2021-12-07 18:40:04.205547'),
(15, 'cooperative', '0001_initial', '2021-12-07 18:49:11.776927'),
(16, 'admin', '0001_initial', '2021-12-07 18:49:16.863156'),
(17, 'admin', '0002_logentry_remove_auto_add', '2021-12-07 18:49:17.113222'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2021-12-07 18:49:17.589100'),
(19, 'sessions', '0001_initial', '2021-12-07 18:49:18.412949'),
(20, 'cooperative', '0002_auto_20211207_2232', '2021-12-07 21:32:21.367190'),
(21, 'cooperative', '0003_auto_20211208_0006', '2021-12-07 23:06:24.843658'),
(22, 'cooperative', '0004_alter_standingorderaccounts_transaction', '2021-12-08 00:32:15.041884'),
(23, 'cooperative', '0005_auto_20211213_1754', '2021-12-13 16:55:09.771836'),
(24, 'cooperative', '0006_auto_20211213_1816', '2021-12-13 17:16:54.826060'),
(25, 'cooperative', '0007_alter_memberssharepurchaserequest_member', '2021-12-13 19:16:01.973570'),
(26, 'cooperative', '0008_sharessalesrecord', '2021-12-14 01:11:31.930599'),
(27, 'cooperative', '0009_rename_applicant_sharessalesrecord_member', '2021-12-14 01:12:53.414498'),
(28, 'cooperative', '0010_rename_bank_ccount_sharessalesrecord_bank_account', '2021-12-14 01:23:07.721357'),
(29, 'cooperative', '0011_alter_memberscashdeposits_member', '2021-12-14 04:12:13.186054'),
(30, 'cooperative', '0012_auto_20211214_0527', '2021-12-14 04:27:12.441461'),
(31, 'cooperative', '0013_auto_20211215_0356', '2021-12-15 02:56:44.854795'),
(32, 'cooperative', '0014_auto_20211215_0430', '2021-12-15 03:30:29.761872'),
(33, 'cooperative', '0015_memberscashwithdrawalsapplication', '2021-12-15 03:31:56.400250'),
(34, 'cooperative', '0016_auto_20211215_0608', '2021-12-15 05:08:34.019406'),
(35, 'cooperative', '0017_auto_20211215_0613', '2021-12-15 05:14:06.504375'),
(36, 'cooperative', '0018_auto_20211215_1029', '2021-12-15 09:29:53.075718'),
(37, 'cooperative', '0019_auto_20211215_2329', '2021-12-15 22:30:01.676442'),
(38, 'cooperative', '0020_transactionloanajustmentrequest', '2021-12-16 02:14:10.956188'),
(39, 'cooperative', '0021_productcategory_code', '2021-12-23 01:12:05.833326'),
(40, 'cooperative', '0022_stock_details', '2021-12-23 02:10:03.425644'),
(41, 'cooperative', '0023_alter_stock_details', '2021-12-23 02:10:36.166704'),
(42, 'cooperative', '0024_alter_cooperativeshopledger_member', '2021-12-31 11:25:30.663805'),
(43, 'cooperative', '0025_compulsorysavings', '2022-01-10 15:21:10.940715'),
(44, 'cooperative', '0026_cooperativeshopledger_receipt', '2022-01-10 18:40:18.575898'),
(45, 'cooperative', '0027_daily_sales_receipt', '2022-01-10 18:55:21.588116'),
(46, 'cooperative', '0028_customers_processed_by', '2022-01-11 04:58:18.780395'),
(47, 'cooperative', '0029_alter_customers_processed_by', '2022-01-11 04:58:48.048608'),
(48, 'cooperative', '0030_daily_sales_cash_flow_summary', '2022-01-11 20:16:05.739207'),
(49, 'cooperative', '0031_delete_userlevels', '2022-01-11 18:49:18.139400'),
(50, 'cooperative', '0032_stock_lock_status', '2022-01-11 19:53:07.403305'),
(51, 'cooperative', '0033_remove_stock_lock_status', '2022-01-11 19:53:31.862754'),
(52, 'cooperative', '0034_stock_lock_status', '2022-01-11 19:54:54.704049'),
(53, 'cooperative', '0035_suppliers_suppliers_majors_suppliers_reps', '2022-01-12 04:26:23.296919'),
(54, 'cooperative', '0036_auto_20220112_0539', '2022-01-12 04:40:00.236151'),
(55, 'cooperative', '0037_alter_suppliers_branches_address', '2022-01-12 05:49:29.549512'),
(56, 'cooperative', '0038_remove_suppliers_reps_supplier', '2022-01-12 06:14:13.437683'),
(57, 'cooperative', '0039_purchases_purchases_temp', '2022-01-13 06:52:09.743991'),
(58, 'cooperative', '0040_auto_20220113_0819', '2022-01-13 07:19:46.141456'),
(59, 'cooperative', '0041_alter_purchase_header_personnel', '2022-01-13 07:33:23.659628'),
(60, 'cooperative', '0042_purchase_header_status', '2022-01-13 07:38:39.272685'),
(61, 'cooperative', '0043_suppliers_prefix', '2022-01-13 07:43:15.359912'),
(62, 'cooperative', '0044_alter_purchase_header_table', '2022-01-13 20:05:29.994282'),
(63, 'cooperative', '0045_alter_purchase_header_table', '2022-01-13 20:07:54.188792'),
(64, 'cooperative', '0046_auto_20220113_2122', '2022-01-13 20:22:49.729551'),
(65, 'cooperative', '0047_auto_20220113_2134', '2022-01-13 20:35:17.210647'),
(66, 'cooperative', '0048_auto_20220114_0047', '2022-01-13 23:47:13.709837'),
(67, 'cooperative', '0049_auto_20220114_0105', '2022-01-14 00:05:31.056401'),
(68, 'cooperative', '0050_purchase_header_certification_status', '2022-01-14 01:12:54.228433'),
(69, 'cooperative', '0051_alter_stock_table', '2022-01-14 10:52:48.341610'),
(70, 'cooperative', '0052_itemwriteoffreasons', '2022-01-16 15:54:28.428701'),
(71, 'cooperative', '0053_auto_20220116_1732', '2022-01-16 16:33:19.651418'),
(72, 'cooperative', '0054_auto_20220116_1748', '2022-01-16 16:48:53.950679'),
(73, 'cooperative', '0055_auto_20220116_1811', '2022-01-16 17:11:55.925124'),
(74, 'cooperative', '0056_auto_20220116_1847', '2022-01-16 17:48:47.602867'),
(75, 'cooperative', '0057_stock_unit_cost_price', '2022-01-16 20:36:09.802519'),
(76, 'cooperative', '0058_daily_sales_product', '2022-01-17 03:37:43.816879');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1ipiv63lrp9txistsoi6r0k8kz2nf5z8', '.eJxVjEEOwiAQRe_C2hBAOoBL956BDMwgVUOT0q6Md7dNutDtf--_t4i4LjWunec4krgIbcTpd0yYn9x2Qg9s90nmqS3zmOSuyIN2eZuIX9fD_QtU7HV7s3Yq-aAQCLDAQM6hzWiSQxNSCLClzqCLYszovXWgFITCxRIXGrT4fAEZeTjM:1n5Mqo:NiNS3TRxdfKCEYhVva5G-QLyBhHrBBmZg9QxasAvilM', '2022-01-20 07:06:18.813528'),
('3oab3pgcaggqd8d2p1fjugxm3bt0zo1n', '.eJxVjDsOwjAQBe_iGllZf2IvJT1nsNafxQHkSHFSIe4OkVJA-2bmvUSgba1h62UJUxZnYcTpd4uUHqXtIN-p3WaZ5rYuU5S7Ig_a5XXO5Xk53L-DSr1-awJGPxBnZwyrmJUzGi1ZxkLeOwAsyVpiUKiN42g1I4IaRmP1CKDE-wPhYTb2:1n3Zzv:c6rtzB6BF0Y5-Uq7s4MXVAiJs2U1u4V4IOMWaBZadJk', '2022-01-15 08:44:19.886311'),
('508a25jt9a528crclmq3g8gmlk3pwaxg', '.eJxVjEEOwiAQRe_C2pAyFESX7j0DGWYGqRpISrsy3l2bdKHb_977LxVxXUpcu8xxYnVWxqjD75iQHlI3wnest6ap1WWekt4UvdOur43ledndv4OCvXxrcChgkBFJwEkKREfnZTAZTtYOAbOENAoG8SAORrJGAtvEFCgje_X-ADIOOXU:1n9JDB:BfGN0_9E5JsM73LRObxRYbdpw8NZOU6zPi6dch0e1Fc', '2022-01-31 04:01:41.671193'),
('875xfiobrcsjiu0ulbkq5xf48t2vjbp8', '.eJxVjEEOwiAQRe_C2hAKQwGX7j0DgZlBqqYkpV0Z765NutDtf-_9l4hpW2vcOi9xInEWQZx-t5zwwfMO6J7mW5PY5nWZstwVedAur434eTncv4Oaev3WUIwij6wMaE1QEiI7zyVYBuswZO01hQCDT04NY7EjAhk22iMUrQbx_gDv6Te1:1n9JEM:l6y816OQMSODQIzcWXcVVOmN1u7b1CsW1ThCeZ3kj_s', '2022-01-31 04:02:54.422647'),
('99nlsla6irwomah1eu3hdu3n4cqedg8p', '.eJxVjEsOwjAMBe-SNYqa1HYqluw5Q-QkNimgVupnVXF3FKkL2L6ZeYeJvG817qsscSzmalxvLr9j4vySqZHy5Okx2zxP2zIm2xR70tXe5yLv2-n-HVRea6szZqc0KHtWPwj3oRCzYieqDqAPiJAAAnqfXGIcSBAyKRB14sB8vifBODE:1n9Vxb:-yOe7nHK76_qe2sGrMABPSrlwYYIEOJSXWn3js2z5n8', '2022-01-31 17:38:27.623768'),
('b5bqdvtswzmta2ihe8vagnll9b0iwg93', '.eJxVjEEOwiAQRe_C2hBkpgO4dN8zkGGgUjVtUtqV8e7apAvd_vfef6nI21rj1soSx6wu6qxOv1tieZRpB_nO023WMk_rMia9K_qgTfdzLs_r4f4dVG71WyN67JixUMnWOgGSIYQuDQQWjQMgxgQoJllPJju0DC4Ie0oEJYh6fwDL1DdH:1n2Y3E:mR2RvAud8Re50ToUkmOvrzbNVHkftMVP4ukxnpOe6wI', '2022-01-12 12:27:28.168534'),
('gdz9k66v1ursiugb6ho1st6zw1ynlsja', '.eJxVjEEOwiAQRe_C2hBkpgO4dN8zkGGgUjVtUtqV8e7apAvd_vfef6nI21rj1soSx6wu6qxOv1tieZRpB_nO023WMk_rMia9K_qgTfdzLs_r4f4dVG71WyN67JixUMnWOgGSIYQuDQQWjQMgxgQoJllPJju0DC4Ie0oEJYh6fwDL1DdH:1n7hbv:PSUZPXOL9oNdNZeCOw1ctmP6pDbkn_lIHF44gTZq12k', '2022-01-26 17:40:35.902605'),
('n8gda5op5w28js67ysq6ri73am5w8c4y', '.eJxVjEEOwiAQRe_C2hBkpgO4dN8zkGGgUjVtUtqV8e7apAvd_vfef6nI21rj1soSx6wu6qxOv1tieZRpB_nO023WMk_rMia9K_qgTfdzLs_r4f4dVG71WyN67JixUMnWOgGSIYQuDQQWjQMgxgQoJllPJju0DC4Ie0oEJYh6fwDL1DdH:1n0BHE:zAvo2jMVCj2nwn5hlYskIoo3ptXgZYAzvbKmi72-Gs4', '2022-01-05 23:44:08.689984'),
('wep7kdrpybce8tssiuln7pt4bcfo8cvn', '.eJxVjEEOwiAQRe_C2hBkpgO4dN8zkGGgUjVtUtqV8e7apAvd_vfef6nI21rj1soSx6wu6qxOv1tieZRpB_nO023WMk_rMia9K_qgTfdzLs_r4f4dVG71WyN67JixUMnWOgGSIYQuDQQWjQMgxgQoJllPJju0DC4Ie0oEJYh6fwDL1DdH:1n3Bia:9mynIoTLJbMupMOUtA_SZ-qN_7am48YWOaBX51InEUo', '2022-01-14 06:48:48.216062');

-- --------------------------------------------------------

--
-- Table structure for table `exclusive_status`
--

CREATE TABLE `exclusive_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `exclusive_status`
--

INSERT INTO `exclusive_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'EXCLUSIVE', '2021-12-07 19:05:36.312068', '2021-12-07 19:05:36.312068'),
(2, 'NON EXCLUSIVE', '2021-12-07 19:05:36.367666', '2021-12-07 19:05:36.367666');

-- --------------------------------------------------------

--
-- Table structure for table `external_fascilities_main`
--

CREATE TABLE `external_fascilities_main` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `external_fascilities_temp`
--

CREATE TABLE `external_fascilities_temp` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `amount` decimal(20,2) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `approval_comment` longtext DEFAULT NULL,
  `approved_at` date DEFAULT NULL,
  `approval_officer_id` int(11) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `status_id` int(11) NOT NULL,
  `transaction_status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `gender`
--

CREATE TABLE `gender` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `gender`
--

INSERT INTO `gender` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'MALE', '2021-12-07 19:00:57.756393', '2021-12-07 19:00:57.756393'),
(2, 'FEMALE', '2021-12-07 19:00:57.805437', '2021-12-07 19:00:57.805437');

-- --------------------------------------------------------

--
-- Table structure for table `general_cash_sales_selected`
--

CREATE TABLE `general_cash_sales_selected` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `ticket` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `unit_selling_price` decimal(20,2) NOT NULL,
  `total` decimal(20,2) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `general_cash_sales_selected`
--

INSERT INTO `general_cash_sales_selected` (`id`, `created_at`, `updated_at`, `ticket`, `quantity`, `unit_selling_price`, `total`, `customer_id`, `processed_by_id`, `product_id`, `status_id`) VALUES
(14, '2022-01-11 18:38:53.017553', '2022-01-11 18:38:53.017553', '2022111193852', 5, '700.00', '3500.00', 15, 12, 971, 1);

-- --------------------------------------------------------

--
-- Table structure for table `general_cash_sales_selected_temp`
--

CREATE TABLE `general_cash_sales_selected_temp` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `ticket` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `unit_selling_price` decimal(20,2) NOT NULL,
  `total` decimal(20,2) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `interest_deduction_source`
--

CREATE TABLE `interest_deduction_source` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `interest_deduction_source`
--

INSERT INTO `interest_deduction_source` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'SOURCE', '2021-12-07 19:02:44.989478', '2021-12-07 19:02:44.989478'),
(2, 'SPREAD', '2021-12-07 19:02:45.046500', '2021-12-07 19:02:45.046500');

-- --------------------------------------------------------

--
-- Table structure for table `item_write_off_reasons`
--

CREATE TABLE `item_write_off_reasons` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `item_write_off_reasons`
--

INSERT INTO `item_write_off_reasons` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'DAMAGED', '2022-01-16 16:06:41.934803', '2022-01-16 16:06:41.934803'),
(2, 'STOLEN', '2022-01-16 16:06:41.985784', '2022-01-16 16:06:41.985784'),
(3, 'USED', '2022-01-16 16:06:42.227823', '2022-01-16 16:06:42.227823'),
(4, 'EXPIRED', '2022-01-16 16:06:42.372987', '2022-01-16 16:06:42.372987'),
(5, 'RETURNED', '2022-01-16 16:06:42.422956', '2022-01-16 16:06:42.422956');

-- --------------------------------------------------------

--
-- Table structure for table `lga`
--

CREATE TABLE `lga` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `state_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lga`
--

INSERT INTO `lga` (`id`, `created_at`, `updated_at`, `title`, `state_id`) VALUES
(1, '2021-12-07 18:57:11.012652', '2021-12-07 18:57:11.012652', 'Aba North', 1),
(2, '2021-12-07 18:57:11.062566', '2021-12-07 18:57:11.062566', 'Aba South', 1),
(3, '2021-12-07 18:57:11.345575', '2021-12-07 18:57:11.345575', 'Arochukwu', 1),
(4, '2021-12-07 18:57:11.550646', '2021-12-07 18:57:11.550646', 'Bende', 1),
(5, '2021-12-07 18:57:11.584005', '2021-12-07 18:57:11.584005', 'Ikwuano', 1),
(6, '2021-12-07 18:57:11.625762', '2021-12-07 18:57:11.625762', 'Isiala Ngwa North', 1),
(7, '2021-12-07 18:57:11.687020', '2021-12-07 18:57:11.688016', 'Isiala Ngwa South', 1),
(8, '2021-12-07 18:57:11.742979', '2021-12-07 18:57:11.742979', 'Isuikwuato', 1),
(9, '2021-12-07 18:57:11.795949', '2021-12-07 18:57:11.795949', 'Obi Ngwa', 1),
(10, '2021-12-07 18:57:11.813935', '2021-12-07 18:57:11.813935', 'Ohafia', 1),
(11, '2021-12-07 18:57:11.846915', '2021-12-07 18:57:11.846915', 'Osisioma', 1),
(12, '2021-12-07 18:57:11.889888', '2021-12-07 18:57:11.890889', 'Ugwunagbo', 1),
(13, '2021-12-07 18:57:11.947920', '2021-12-07 18:57:11.947920', 'Ukwa East', 1),
(14, '2021-12-07 18:57:12.007296', '2021-12-07 18:57:12.007296', 'Ukwa West', 1),
(15, '2021-12-07 18:57:12.035422', '2021-12-07 18:57:12.035422', 'Umuahia North', 1),
(16, '2021-12-07 18:57:12.058481', '2021-12-07 18:57:12.058481', 'Umuahia South', 1),
(17, '2021-12-07 18:57:12.091830', '2021-12-07 18:57:12.092814', 'Umu Nneochi', 1),
(18, '2021-12-07 18:57:12.135872', '2021-12-07 18:57:12.135872', 'Demsa', 2),
(19, '2021-12-07 18:57:12.193155', '2021-12-07 18:57:12.193155', 'Fufure', 2),
(20, '2021-12-07 18:57:12.358512', '2021-12-07 18:57:12.358512', 'Ganye', 2),
(21, '2021-12-07 18:57:12.410686', '2021-12-07 18:57:12.410686', 'Gayuk', 2),
(22, '2021-12-07 18:57:12.457239', '2021-12-07 18:57:12.457239', 'Gombi', 2),
(23, '2021-12-07 18:57:12.603703', '2021-12-07 18:57:12.603703', 'Girei', 2),
(24, '2021-12-07 18:57:12.678515', '2021-12-07 18:57:12.678515', 'Hong', 2),
(25, '2021-12-07 18:57:12.723815', '2021-12-07 18:57:12.723815', 'Jada', 2),
(26, '2021-12-07 18:57:12.757272', '2021-12-07 18:57:12.757272', 'Lamurde', 2),
(27, '2021-12-07 18:57:12.779099', '2021-12-07 18:57:12.779099', 'Madagali', 2),
(28, '2021-12-07 18:57:12.837083', '2021-12-07 18:57:12.837083', 'Maiha', 2),
(29, '2021-12-07 18:57:12.870037', '2021-12-07 18:57:12.870037', 'Mayo Belwa', 2),
(30, '2021-12-07 18:57:12.903757', '2021-12-07 18:57:12.903757', 'Michika', 2),
(31, '2021-12-07 18:57:12.936607', '2021-12-07 18:57:12.936607', 'Mubi North', 2),
(32, '2021-12-07 18:57:12.969587', '2021-12-07 18:57:12.969587', 'Mubi South', 2),
(33, '2021-12-07 18:57:13.003566', '2021-12-07 18:57:13.003566', 'Numan', 2),
(34, '2021-12-07 18:57:13.037546', '2021-12-07 18:57:13.037546', 'Shelleng', 2),
(35, '2021-12-07 18:57:13.078521', '2021-12-07 18:57:13.079519', 'Song', 2),
(36, '2021-12-07 18:57:13.111499', '2021-12-07 18:57:13.111499', 'Toungo', 2),
(37, '2021-12-07 18:57:13.158556', '2021-12-07 18:57:13.158556', 'Yola North', 2),
(38, '2021-12-07 18:57:13.191491', '2021-12-07 18:57:13.191491', 'Yola South', 2),
(39, '2021-12-07 18:57:13.225573', '2021-12-07 18:57:13.225573', 'Abak', 3),
(40, '2021-12-07 18:57:13.359151', '2021-12-07 18:57:13.359151', 'Eastern Obolo', 3),
(41, '2021-12-07 18:57:13.435534', '2021-12-07 18:57:13.435534', 'Eket', 3),
(42, '2021-12-07 18:57:13.521634', '2021-12-07 18:57:13.521634', 'Esit Eket', 3),
(43, '2021-12-07 18:57:13.703099', '2021-12-07 18:57:13.703099', 'Essien Udim', 3),
(44, '2021-12-07 18:57:13.727747', '2021-12-07 18:57:13.728751', 'Etim Ekpo', 3),
(45, '2021-12-07 18:57:13.769566', '2021-12-07 18:57:13.769566', 'Etinan', 3),
(46, '2021-12-07 18:57:13.833920', '2021-12-07 18:57:13.833920', 'Ibeno', 3),
(47, '2021-12-07 18:57:13.919965', '2021-12-07 18:57:13.919965', 'Ibesikpo Asutan', 3),
(48, '2021-12-07 18:57:13.937942', '2021-12-07 18:57:13.937942', 'Ibiono-Ibom', 3),
(49, '2021-12-07 18:57:13.969693', '2021-12-07 18:57:13.969693', 'Ika', 3),
(50, '2021-12-07 18:57:14.023118', '2021-12-07 18:57:14.023118', 'Ikono', 3),
(51, '2021-12-07 18:57:14.127997', '2021-12-07 18:57:14.128997', 'Ikot Abasi', 3),
(52, '2021-12-07 18:57:14.183961', '2021-12-07 18:57:14.183961', 'Ikot Ekpene', 3),
(53, '2021-12-07 18:57:14.214939', '2021-12-07 18:57:14.214939', 'Ini', 3),
(54, '2021-12-07 18:57:14.272903', '2021-12-07 18:57:14.272903', 'Itu', 3),
(55, '2021-12-07 18:57:14.302886', '2021-12-07 18:57:14.302886', 'Mbo', 3),
(56, '2021-12-07 18:57:14.472412', '2021-12-07 18:57:14.472412', 'Mkpat-Enin', 3),
(57, '2021-12-07 18:57:14.619867', '2021-12-07 18:57:14.620867', 'Nsit-Atai', 3),
(58, '2021-12-07 18:57:14.904760', '2021-12-07 18:57:14.904760', 'Nsit-Ibom', 3),
(59, '2021-12-07 18:57:14.963023', '2021-12-07 18:57:14.963023', 'Nsit-Ubium', 3),
(60, '2021-12-07 18:57:15.022683', '2021-12-07 18:57:15.022683', 'Obot Akara', 3),
(61, '2021-12-07 18:57:15.073775', '2021-12-07 18:57:15.073775', 'Okobo', 3),
(62, '2021-12-07 18:57:15.133903', '2021-12-07 18:57:15.133903', 'Onna', 3),
(63, '2021-12-07 18:57:15.177902', '2021-12-07 18:57:15.177902', 'Oron', 3),
(64, '2021-12-07 18:57:15.284825', '2021-12-07 18:57:15.284825', 'Oruk Anam', 3),
(65, '2021-12-07 18:57:15.352927', '2021-12-07 18:57:15.352927', 'Udung-Uko', 3),
(66, '2021-12-07 18:57:15.378895', '2021-12-07 18:57:15.379894', 'Ukanafun', 3),
(67, '2021-12-07 18:57:15.441857', '2021-12-07 18:57:15.442853', 'Uruan', 3),
(68, '2021-12-07 18:57:15.459842', '2021-12-07 18:57:15.459842', 'Urue-Offong/Oruko', 3),
(69, '2021-12-07 18:57:15.513811', '2021-12-07 18:57:15.513811', 'Uyo', 3),
(70, '2021-12-07 18:57:15.647071', '2021-12-07 18:57:15.647071', 'Aguata', 4),
(71, '2021-12-07 18:57:15.681365', '2021-12-07 18:57:15.681365', 'Anambra East', 4),
(72, '2021-12-07 18:57:15.835424', '2021-12-07 18:57:15.835424', 'Anambra West', 4),
(73, '2021-12-07 18:57:15.868855', '2021-12-07 18:57:15.868855', 'Anaocha', 4),
(74, '2021-12-07 18:57:15.949173', '2021-12-07 18:57:15.949173', 'Awka North', 4),
(75, '2021-12-07 18:57:15.981690', '2021-12-07 18:57:15.981690', 'Awka South', 4),
(76, '2021-12-07 18:57:16.035082', '2021-12-07 18:57:16.035082', 'Ayamelum', 4),
(77, '2021-12-07 18:57:16.096795', '2021-12-07 18:57:16.096795', 'Dunukofia', 4),
(78, '2021-12-07 18:57:16.156785', '2021-12-07 18:57:16.157787', 'Ekwusigo', 4),
(79, '2021-12-07 18:57:16.221031', '2021-12-07 18:57:16.221031', 'Idemili North', 4),
(80, '2021-12-07 18:57:16.288271', '2021-12-07 18:57:16.288271', 'Idemili South', 4),
(81, '2021-12-07 18:57:16.328343', '2021-12-07 18:57:16.329336', 'Ihiala', 4),
(82, '2021-12-07 18:57:16.374376', '2021-12-07 18:57:16.374376', 'Njikoka', 4),
(83, '2021-12-07 18:57:16.420082', '2021-12-07 18:57:16.420082', 'Nnewi North', 4),
(84, '2021-12-07 18:57:16.463230', '2021-12-07 18:57:16.463230', 'Nnewi South', 4),
(85, '2021-12-07 18:57:16.529374', '2021-12-07 18:57:16.529374', 'Ogbaru', 4),
(86, '2021-12-07 18:57:16.624376', '2021-12-07 18:57:16.624376', 'Onitsha North', 4),
(87, '2021-12-07 18:57:16.736305', '2021-12-07 18:57:16.736305', 'Onitsha South', 4),
(88, '2021-12-07 18:57:16.873740', '2021-12-07 18:57:16.873740', 'Orumba North', 4),
(89, '2021-12-07 18:57:16.951049', '2021-12-07 18:57:16.951049', 'Orumba South', 4),
(90, '2021-12-07 18:57:17.013273', '2021-12-07 18:57:17.013273', 'Oyi', 4),
(91, '2021-12-07 18:57:17.073543', '2021-12-07 18:57:17.073543', 'Alkaleri', 5),
(92, '2021-12-07 18:57:17.127835', '2021-12-07 18:57:17.127835', 'Bauchi', 5),
(93, '2021-12-07 18:57:17.173363', '2021-12-07 18:57:17.173363', 'Bogoro', 5),
(94, '2021-12-07 18:57:17.232479', '2021-12-07 18:57:17.232479', 'Damban', 5),
(95, '2021-12-07 18:57:17.279615', '2021-12-07 18:57:17.279615', 'Darazo', 5),
(96, '2021-12-07 18:57:17.339462', '2021-12-07 18:57:17.340463', 'Dass', 5),
(97, '2021-12-07 18:57:17.384489', '2021-12-07 18:57:17.384489', 'Gamawa', 5),
(98, '2021-12-07 18:57:17.430362', '2021-12-07 18:57:17.430362', 'Ganjuwa', 5),
(99, '2021-12-07 18:57:17.472426', '2021-12-07 18:57:17.472426', 'Giade', 5),
(100, '2021-12-07 18:57:17.516494', '2021-12-07 18:57:17.516494', 'Itas/Gadau', 5),
(101, '2021-12-07 18:57:17.560642', '2021-12-07 18:57:17.560642', 'Jama\'are', 5),
(102, '2021-12-07 18:57:17.592085', '2021-12-07 18:57:17.592085', 'Katagum', 5),
(103, '2021-12-07 18:57:17.625990', '2021-12-07 18:57:17.625990', 'Kirfi', 5),
(104, '2021-12-07 18:57:17.657752', '2021-12-07 18:57:17.657752', 'Misau', 5),
(105, '2021-12-07 18:57:17.755367', '2021-12-07 18:57:17.755367', 'Ningi', 5),
(106, '2021-12-07 18:57:17.870352', '2021-12-07 18:57:17.870352', 'Shira', 5),
(107, '2021-12-07 18:57:17.998292', '2021-12-07 18:57:17.998292', 'Tafawa Balewa', 5),
(108, '2021-12-07 18:57:18.068553', '2021-12-07 18:57:18.068553', 'Toro', 5),
(109, '2021-12-07 18:57:18.131211', '2021-12-07 18:57:18.131211', 'Warji', 5),
(110, '2021-12-07 18:57:18.157440', '2021-12-07 18:57:18.157440', 'Zaki', 5),
(111, '2021-12-07 18:57:18.215439', '2021-12-07 18:57:18.215439', 'Brass', 6),
(112, '2021-12-07 18:57:18.249087', '2021-12-07 18:57:18.249087', 'Ekeremor', 6),
(113, '2021-12-07 18:57:18.307086', '2021-12-07 18:57:18.307086', 'Kolokuma/Opokuma', 6),
(114, '2021-12-07 18:57:18.336267', '2021-12-07 18:57:18.336267', 'Nembe', 6),
(115, '2021-12-07 18:57:18.386564', '2021-12-07 18:57:18.386564', 'Ogbia', 6),
(116, '2021-12-07 18:57:18.413076', '2021-12-07 18:57:18.413076', 'Sagbama', 6),
(117, '2021-12-07 18:57:18.446060', '2021-12-07 18:57:18.446060', 'Southern Ijaw', 6),
(118, '2021-12-07 18:57:18.479792', '2021-12-07 18:57:18.479792', 'Yenagoa', 6),
(119, '2021-12-07 18:57:18.512503', '2021-12-07 18:57:18.512503', 'Agatu', 7),
(120, '2021-12-07 18:57:18.547758', '2021-12-07 18:57:18.547758', 'Apa', 7),
(121, '2021-12-07 18:57:18.579224', '2021-12-07 18:57:18.579224', 'Ado', 7),
(122, '2021-12-07 18:57:18.613406', '2021-12-07 18:57:18.613406', 'Buruku', 7),
(123, '2021-12-07 18:57:18.646118', '2021-12-07 18:57:18.646118', 'Gboko', 7),
(124, '2021-12-07 18:57:18.679859', '2021-12-07 18:57:18.679859', 'Guma', 7),
(125, '2021-12-07 18:57:18.712730', '2021-12-07 18:57:18.712730', 'Gwer East', 7),
(126, '2021-12-07 18:57:18.746761', '2021-12-07 18:57:18.746761', 'Gwer West', 7),
(127, '2021-12-07 18:57:18.779249', '2021-12-07 18:57:18.779249', 'Katsina-Ala', 7),
(128, '2021-12-07 18:57:18.813189', '2021-12-07 18:57:18.813189', 'Konshisha', 7),
(129, '2021-12-07 18:57:18.945719', '2021-12-07 18:57:18.945719', 'Kwande', 7),
(130, '2021-12-07 18:57:19.126736', '2021-12-07 18:57:19.126736', 'Logo', 7),
(131, '2021-12-07 18:57:19.259879', '2021-12-07 18:57:19.259879', 'Makurdi', 7),
(132, '2021-12-07 18:57:19.327315', '2021-12-07 18:57:19.327315', 'Obi', 7),
(133, '2021-12-07 18:57:19.366402', '2021-12-07 18:57:19.367405', 'Ogbadibo', 7),
(134, '2021-12-07 18:57:19.408831', '2021-12-07 18:57:19.408831', 'Ohimini', 7),
(135, '2021-12-07 18:57:19.466736', '2021-12-07 18:57:19.466736', 'Oju', 7),
(136, '2021-12-07 18:57:19.523330', '2021-12-07 18:57:19.524330', 'Okpokwu', 7),
(137, '2021-12-07 18:57:19.553439', '2021-12-07 18:57:19.553439', 'Oturkpo', 7),
(138, '2021-12-07 18:57:19.592764', '2021-12-07 18:57:19.592764', 'Tarka', 7),
(139, '2021-12-07 18:57:19.631452', '2021-12-07 18:57:19.632461', 'Ukum', 7),
(140, '2021-12-07 18:57:19.679293', '2021-12-07 18:57:19.679293', 'Ushongo', 7),
(141, '2021-12-07 18:57:19.715367', '2021-12-07 18:57:19.715367', 'Vandeikya', 7),
(142, '2021-12-07 18:57:19.747384', '2021-12-07 18:57:19.747384', 'Abadam', 8),
(143, '2021-12-07 18:57:19.781779', '2021-12-07 18:57:19.781779', 'Askira/Uba', 8),
(144, '2021-12-07 18:57:19.814804', '2021-12-07 18:57:19.814804', 'Bama', 8),
(145, '2021-12-07 18:57:19.857814', '2021-12-07 18:57:19.857814', 'Bayo', 8),
(146, '2021-12-07 18:57:19.890852', '2021-12-07 18:57:19.890852', 'Biu', 8),
(147, '2021-12-07 18:57:19.917893', '2021-12-07 18:57:19.917893', 'Chibok', 8),
(148, '2021-12-07 18:57:19.959280', '2021-12-07 18:57:19.959280', 'Damboa', 8),
(149, '2021-12-07 18:57:20.178840', '2021-12-07 18:57:20.179825', 'Dikwa', 8),
(150, '2021-12-07 18:57:20.370790', '2021-12-07 18:57:20.370790', 'Gubio', 8),
(151, '2021-12-07 18:57:20.429556', '2021-12-07 18:57:20.429556', 'Guzamala', 8),
(152, '2021-12-07 18:57:20.490130', '2021-12-07 18:57:20.490130', 'Gwoza', 8),
(153, '2021-12-07 18:57:20.557401', '2021-12-07 18:57:20.557401', 'Hawul', 8),
(154, '2021-12-07 18:57:20.625587', '2021-12-07 18:57:20.625587', 'Jere', 8),
(155, '2021-12-07 18:57:20.706822', '2021-12-07 18:57:20.706822', 'Kaga', 8),
(156, '2021-12-07 18:57:20.746907', '2021-12-07 18:57:20.746907', 'Kala/Balge', 8),
(157, '2021-12-07 18:57:20.805760', '2021-12-07 18:57:20.805760', 'Konduga', 8),
(158, '2021-12-07 18:57:20.846713', '2021-12-07 18:57:20.846713', 'Kukawa', 8),
(159, '2021-12-07 18:57:20.905894', '2021-12-07 18:57:20.905894', 'Kwaya Kusar', 8),
(160, '2021-12-07 18:57:20.946761', '2021-12-07 18:57:20.946761', 'Mafa', 8),
(161, '2021-12-07 18:57:21.015104', '2021-12-07 18:57:21.015104', 'Magumeri', 8),
(162, '2021-12-07 18:57:21.047529', '2021-12-07 18:57:21.047529', 'Maiduguri', 8),
(163, '2021-12-07 18:57:21.104124', '2021-12-07 18:57:21.104124', 'Marte', 8),
(164, '2021-12-07 18:57:21.147006', '2021-12-07 18:57:21.147006', 'Mobbar', 8),
(165, '2021-12-07 18:57:21.204241', '2021-12-07 18:57:21.204241', 'Monguno', 8),
(166, '2021-12-07 18:57:21.248939', '2021-12-07 18:57:21.248939', 'Ngala', 8),
(167, '2021-12-07 18:57:21.428238', '2021-12-07 18:57:21.428238', 'Nganzai', 8),
(168, '2021-12-07 18:57:21.535172', '2021-12-07 18:57:21.535172', 'Shani', 8),
(169, '2021-12-07 18:57:21.597135', '2021-12-07 18:57:21.597135', 'Abi', 9),
(170, '2021-12-07 18:57:21.781510', '2021-12-07 18:57:21.781510', 'Akamkpa', 9),
(171, '2021-12-07 18:57:21.836163', '2021-12-07 18:57:21.836163', 'Akpabuyo', 9),
(172, '2021-12-07 18:57:21.890589', '2021-12-07 18:57:21.890589', 'Bakassi', 9),
(173, '2021-12-07 18:57:21.957606', '2021-12-07 18:57:21.957606', 'Bekwarra', 9),
(174, '2021-12-07 18:57:22.006154', '2021-12-07 18:57:22.006154', 'Biase', 9),
(175, '2021-12-07 18:57:22.075313', '2021-12-07 18:57:22.075313', 'Boki', 9),
(176, '2021-12-07 18:57:22.129052', '2021-12-07 18:57:22.129052', 'Calabar Municipal', 9),
(177, '2021-12-07 18:57:22.192112', '2021-12-07 18:57:22.192112', 'Calabar South', 9),
(178, '2021-12-07 18:57:22.266858', '2021-12-07 18:57:22.266858', 'Etung', 9),
(179, '2021-12-07 18:57:22.305880', '2021-12-07 18:57:22.305880', 'Ikom', 9),
(180, '2021-12-07 18:57:22.349166', '2021-12-07 18:57:22.349166', 'Obanliku', 9),
(181, '2021-12-07 18:57:22.446075', '2021-12-07 18:57:22.446075', 'Obubra', 9),
(182, '2021-12-07 18:57:22.579441', '2021-12-07 18:57:22.579441', 'Obudu', 9),
(183, '2021-12-07 18:57:22.672342', '2021-12-07 18:57:22.672342', 'Odukpani', 9),
(184, '2021-12-07 18:57:22.703323', '2021-12-07 18:57:22.703323', 'Ogoja', 9),
(185, '2021-12-07 18:57:22.757290', '2021-12-07 18:57:22.757290', 'Yakuur', 9),
(186, '2021-12-07 18:57:22.791282', '2021-12-07 18:57:22.791282', 'Yala', 9),
(187, '2021-12-07 18:57:22.858515', '2021-12-07 18:57:22.858515', 'Aniocha North', 10),
(188, '2021-12-07 18:57:22.901517', '2021-12-07 18:57:22.901517', 'Aniocha South', 10),
(189, '2021-12-07 18:57:22.959286', '2021-12-07 18:57:22.959286', 'Bomadi', 10),
(190, '2021-12-07 18:57:23.024741', '2021-12-07 18:57:23.024741', 'Burutu', 10),
(191, '2021-12-07 18:57:23.101887', '2021-12-07 18:57:23.101887', 'Ethiope East', 10),
(192, '2021-12-07 18:57:23.168805', '2021-12-07 18:57:23.169804', 'Ethiope West', 10),
(193, '2021-12-07 18:57:23.233023', '2021-12-07 18:57:23.233023', 'Ika North East', 10),
(194, '2021-12-07 18:57:23.302987', '2021-12-07 18:57:23.302987', 'Ika South', 10),
(195, '2021-12-07 18:57:23.369870', '2021-12-07 18:57:23.369870', 'Isoko North', 10),
(196, '2021-12-07 18:57:23.438004', '2021-12-07 18:57:23.438004', 'Isoko South', 10),
(197, '2021-12-07 18:57:23.684312', '2021-12-07 18:57:23.684312', 'Ndokwa East', 10),
(198, '2021-12-07 18:57:23.871871', '2021-12-07 18:57:23.871871', 'Ndokwa West', 10),
(199, '2021-12-07 18:57:24.122194', '2021-12-07 18:57:24.122194', 'Okpe', 10),
(200, '2021-12-07 18:57:24.290789', '2021-12-07 18:57:24.290789', 'Oshimili North', 10),
(201, '2021-12-07 18:57:24.390729', '2021-12-07 18:57:24.390729', 'Oshimili South', 10),
(202, '2021-12-07 18:57:24.446864', '2021-12-07 18:57:24.446864', 'Patani', 10),
(203, '2021-12-07 18:57:24.479635', '2021-12-07 18:57:24.479635', 'Sapele', 10),
(204, '2021-12-07 18:57:24.547139', '2021-12-07 18:57:24.547139', 'Udu', 10),
(205, '2021-12-07 18:57:24.611112', '2021-12-07 18:57:24.611112', 'Ughelli North', 10),
(206, '2021-12-07 18:57:24.705869', '2021-12-07 18:57:24.705869', 'Ughelli South', 10),
(207, '2021-12-07 18:57:24.748937', '2021-12-07 18:57:24.748937', 'Ukwuani', 10),
(208, '2021-12-07 18:57:24.798726', '2021-12-07 18:57:24.798726', 'Uvwie', 10),
(209, '2021-12-07 18:57:24.848981', '2021-12-07 18:57:24.848981', 'Warri North', 10),
(210, '2021-12-07 18:57:24.881902', '2021-12-07 18:57:24.881902', 'Warri South', 10),
(211, '2021-12-07 18:57:24.981319', '2021-12-07 18:57:24.981319', 'Warri South West', 10),
(212, '2021-12-07 18:57:25.046279', '2021-12-07 18:57:25.046279', 'Abakaliki', 11),
(213, '2021-12-07 18:57:25.169829', '2021-12-07 18:57:25.169829', 'Afikpo North', 11),
(214, '2021-12-07 18:57:25.201996', '2021-12-07 18:57:25.201996', 'Afikpo South', 11),
(215, '2021-12-07 18:57:25.277789', '2021-12-07 18:57:25.277789', 'Ebonyi', 11),
(216, '2021-12-07 18:57:25.313226', '2021-12-07 18:57:25.314223', 'Ezza North', 11),
(217, '2021-12-07 18:57:25.347829', '2021-12-07 18:57:25.347829', 'Ezza South', 11),
(218, '2021-12-07 18:57:25.379959', '2021-12-07 18:57:25.379959', 'Ikwo', 11),
(219, '2021-12-07 18:57:25.417212', '2021-12-07 18:57:25.417212', 'Ishielu', 11),
(220, '2021-12-07 18:57:25.507461', '2021-12-07 18:57:25.507461', 'Ivo', 11),
(221, '2021-12-07 18:57:25.550618', '2021-12-07 18:57:25.550618', 'Izzi', 11),
(222, '2021-12-07 18:57:25.599818', '2021-12-07 18:57:25.599818', 'Ohaozara', 11),
(223, '2021-12-07 18:57:25.660243', '2021-12-07 18:57:25.661238', 'Ohaukwu', 11),
(224, '2021-12-07 18:57:25.707973', '2021-12-07 18:57:25.707973', 'Onicha', 11),
(225, '2021-12-07 18:57:25.766794', '2021-12-07 18:57:25.766794', 'Akoko-Edo', 12),
(226, '2021-12-07 18:57:25.807998', '2021-12-07 18:57:25.807998', 'Egor', 12),
(227, '2021-12-07 18:57:25.858262', '2021-12-07 18:57:25.858262', 'Esan Central', 12),
(228, '2021-12-07 18:57:25.908005', '2021-12-07 18:57:25.908005', 'Esan North-East', 12),
(229, '2021-12-07 18:57:25.953449', '2021-12-07 18:57:25.953449', 'Esan South-East', 12),
(230, '2021-12-07 18:57:26.088646', '2021-12-07 18:57:26.089659', 'Esan West', 12),
(231, '2021-12-07 18:57:26.183920', '2021-12-07 18:57:26.183920', 'Etsako Central', 12),
(232, '2021-12-07 18:57:26.223894', '2021-12-07 18:57:26.223894', 'Etsako East', 12),
(233, '2021-12-07 18:57:26.296850', '2021-12-07 18:57:26.296850', 'Etsako West', 12),
(234, '2021-12-07 18:57:26.323834', '2021-12-07 18:57:26.323834', 'Igueben', 12),
(235, '2021-12-07 18:57:26.357812', '2021-12-07 18:57:26.357812', 'Ikpoba Okha', 12),
(236, '2021-12-07 18:57:26.390564', '2021-12-07 18:57:26.390564', 'Orhionmwon', 12),
(237, '2021-12-07 18:57:26.424522', '2021-12-07 18:57:26.424522', 'Oredo', 12),
(238, '2021-12-07 18:57:26.457283', '2021-12-07 18:57:26.457283', 'Ovia North-East', 12),
(239, '2021-12-07 18:57:26.491960', '2021-12-07 18:57:26.491960', 'Ovia South-West', 12),
(240, '2021-12-07 18:57:26.523601', '2021-12-07 18:57:26.523601', 'Owan East', 12),
(241, '2021-12-07 18:57:26.564670', '2021-12-07 18:57:26.564670', 'Owan West', 12),
(242, '2021-12-07 18:57:26.610017', '2021-12-07 18:57:26.610017', 'Uhunmwonde', 12),
(243, '2021-12-07 18:57:26.648031', '2021-12-07 18:57:26.648031', 'Ado Ekiti', 13),
(244, '2021-12-07 18:57:26.680783', '2021-12-07 18:57:26.680783', 'Efon', 13),
(245, '2021-12-07 18:57:26.747238', '2021-12-07 18:57:26.747238', 'Ekiti East', 13),
(246, '2021-12-07 18:57:26.781192', '2021-12-07 18:57:26.781192', 'Ekiti South-West', 13),
(247, '2021-12-07 18:57:26.813912', '2021-12-07 18:57:26.813912', 'Ekiti West', 13),
(248, '2021-12-07 18:57:26.847858', '2021-12-07 18:57:26.847858', 'Emure', 13),
(249, '2021-12-07 18:57:26.881065', '2021-12-07 18:57:26.881065', 'Gbonyin', 13),
(250, '2021-12-07 18:57:26.914532', '2021-12-07 18:57:26.914532', 'Ido Osi', 13),
(251, '2021-12-07 18:57:26.947253', '2021-12-07 18:57:26.947253', 'Ijero', 13),
(252, '2021-12-07 18:57:26.981253', '2021-12-07 18:57:26.981253', 'Ikere', 13),
(253, '2021-12-07 18:57:27.117921', '2021-12-07 18:57:27.117921', 'Ikole', 13),
(254, '2021-12-07 18:57:27.550734', '2021-12-07 18:57:27.550734', 'Ilejemeje', 13),
(255, '2021-12-07 18:57:27.614956', '2021-12-07 18:57:27.614956', 'Irepodun/Ifelodun', 13),
(256, '2021-12-07 18:57:27.669885', '2021-12-07 18:57:27.669885', 'Ise/Orun', 13),
(257, '2021-12-07 18:57:27.724582', '2021-12-07 18:57:27.724582', 'Moba', 13),
(258, '2021-12-07 18:57:27.808235', '2021-12-07 18:57:27.808235', 'Oye', 13),
(259, '2021-12-07 18:57:27.835207', '2021-12-07 18:57:27.835207', 'Aninri', 14),
(260, '2021-12-07 18:57:27.902536', '2021-12-07 18:57:27.902536', 'Awgu', 14),
(261, '2021-12-07 18:57:28.113233', '2021-12-07 18:57:28.113233', 'Enugu East', 14),
(262, '2021-12-07 18:57:28.193532', '2021-12-07 18:57:28.193532', 'Enugu North', 14),
(263, '2021-12-07 18:57:28.224783', '2021-12-07 18:57:28.224783', 'Enugu South', 14),
(264, '2021-12-07 18:57:28.257499', '2021-12-07 18:57:28.257499', 'Ezeagu', 14),
(265, '2021-12-07 18:57:28.291865', '2021-12-07 18:57:28.291865', 'Igbo Etiti', 14),
(266, '2021-12-07 18:57:28.355315', '2021-12-07 18:57:28.355315', 'Igbo Eze North', 14),
(267, '2021-12-07 18:57:28.416685', '2021-12-07 18:57:28.416685', 'Igbo Eze South', 14),
(268, '2021-12-07 18:57:28.473674', '2021-12-07 18:57:28.473674', 'Isi Uzo', 14),
(269, '2021-12-07 18:57:28.628779', '2021-12-07 18:57:28.628779', 'Nkanu East', 14),
(270, '2021-12-07 18:57:28.674745', '2021-12-07 18:57:28.674745', 'Nkanu West', 14),
(271, '2021-12-07 18:57:28.730710', '2021-12-07 18:57:28.730710', 'Nsukka', 14),
(272, '2021-12-07 18:57:28.759695', '2021-12-07 18:57:28.759695', 'Oji River', 14),
(273, '2021-12-07 18:57:28.834713', '2021-12-07 18:57:28.834713', 'Udenu', 14),
(274, '2021-12-07 18:57:28.949396', '2021-12-07 18:57:28.949396', 'Udi', 14),
(275, '2021-12-07 18:57:29.015949', '2021-12-07 18:57:29.015949', 'Uzo-Uwani', 14),
(276, '2021-12-07 18:57:29.072392', '2021-12-07 18:57:29.072392', 'Abaji', 37),
(277, '2021-12-07 18:57:29.115757', '2021-12-07 18:57:29.115757', 'Abuja Municipal Area Council', 37),
(278, '2021-12-07 18:57:29.149810', '2021-12-07 18:57:29.149810', 'Bwari', 37),
(279, '2021-12-07 18:57:29.179921', '2021-12-07 18:57:29.179921', 'Gwagwalada', 37),
(280, '2021-12-07 18:57:29.252869', '2021-12-07 18:57:29.252869', 'Kuje', 37),
(281, '2021-12-07 18:57:29.302204', '2021-12-07 18:57:29.302204', 'Kwali', 37),
(282, '2021-12-07 18:57:29.336117', '2021-12-07 18:57:29.336117', 'Akko', 15),
(283, '2021-12-07 18:57:29.393102', '2021-12-07 18:57:29.393102', 'Balanga', 15),
(284, '2021-12-07 18:57:29.444768', '2021-12-07 18:57:29.444768', 'Billiri', 15),
(285, '2021-12-07 18:57:29.468888', '2021-12-07 18:57:29.468888', 'Dukku', 15),
(286, '2021-12-07 18:57:29.502841', '2021-12-07 18:57:29.502841', 'Funakaye', 15),
(287, '2021-12-07 18:57:29.535558', '2021-12-07 18:57:29.535558', 'Gombe', 15),
(288, '2021-12-07 18:57:29.655872', '2021-12-07 18:57:29.655872', 'Kaltungo', 15),
(289, '2021-12-07 18:57:29.708362', '2021-12-07 18:57:29.708362', 'Kwami', 15),
(290, '2021-12-07 18:57:29.737228', '2021-12-07 18:57:29.737228', 'Nafada', 15),
(291, '2021-12-07 18:57:29.792179', '2021-12-07 18:57:29.792179', 'Shongom', 15),
(292, '2021-12-07 18:57:29.853692', '2021-12-07 18:57:29.853692', 'Yamaltu/Deba', 15),
(293, '2021-12-07 18:57:29.882679', '2021-12-07 18:57:29.882679', 'Aboh Mbaise', 16),
(294, '2021-12-07 18:57:29.941643', '2021-12-07 18:57:29.941643', 'Ahiazu Mbaise', 16),
(295, '2021-12-07 18:57:30.003603', '2021-12-07 18:57:30.004600', 'Ehime Mbano', 16),
(296, '2021-12-07 18:57:30.036580', '2021-12-07 18:57:30.036580', 'Ezinihitte', 16),
(297, '2021-12-07 18:57:30.069637', '2021-12-07 18:57:30.069637', 'Ideato North', 16),
(298, '2021-12-07 18:57:30.103749', '2021-12-07 18:57:30.103749', 'Ideato South', 16),
(299, '2021-12-07 18:57:30.158489', '2021-12-07 18:57:30.158489', 'Ihitte/Uboma', 16),
(300, '2021-12-07 18:57:30.191543', '2021-12-07 18:57:30.191543', 'Ikeduru', 16),
(301, '2021-12-07 18:57:30.225205', '2021-12-07 18:57:30.225205', 'Isiala Mbano', 16),
(302, '2021-12-07 18:57:30.275423', '2021-12-07 18:57:30.275423', 'Isu', 16),
(303, '2021-12-07 18:57:30.330986', '2021-12-07 18:57:30.330986', 'Mbaitoli', 16),
(304, '2021-12-07 18:57:30.380201', '2021-12-07 18:57:30.380201', 'Ngor Okpala', 16),
(305, '2021-12-07 18:57:30.414343', '2021-12-07 18:57:30.414343', 'Njaba', 16),
(306, '2021-12-07 18:57:30.472320', '2021-12-07 18:57:30.473326', 'Nkwerre', 16),
(307, '2021-12-07 18:57:30.539277', '2021-12-07 18:57:30.539277', 'Nwangele', 16),
(308, '2021-12-07 18:57:30.578136', '2021-12-07 18:57:30.578136', 'Obowo', 16),
(309, '2021-12-07 18:57:30.692399', '2021-12-07 18:57:30.692399', 'Oguta', 16),
(310, '2021-12-07 18:57:30.818148', '2021-12-07 18:57:30.819148', 'Ohaji/Egbema', 16),
(311, '2021-12-07 18:57:30.865309', '2021-12-07 18:57:30.865309', 'Okigwe', 16),
(312, '2021-12-07 18:57:30.911347', '2021-12-07 18:57:30.911347', 'Orlu', 16),
(313, '2021-12-07 18:57:30.952627', '2021-12-07 18:57:30.952627', 'Orsu', 16),
(314, '2021-12-07 18:57:31.046751', '2021-12-07 18:57:31.046751', 'Oru East', 16),
(315, '2021-12-07 18:57:31.086718', '2021-12-07 18:57:31.086718', 'Oru West', 16),
(316, '2021-12-07 18:57:31.114703', '2021-12-07 18:57:31.114703', 'Owerri Municipal', 16),
(317, '2021-12-07 18:57:31.146683', '2021-12-07 18:57:31.146683', 'Owerri North', 16),
(318, '2021-12-07 18:57:31.183658', '2021-12-07 18:57:31.183658', 'Owerri West', 16),
(319, '2021-12-07 18:57:31.226633', '2021-12-07 18:57:31.227632', 'Unuimo', 16),
(320, '2021-12-07 18:57:31.260612', '2021-12-07 18:57:31.260612', 'Auyo', 17),
(321, '2021-12-07 18:57:31.292289', '2021-12-07 18:57:31.292289', 'Babura', 17),
(322, '2021-12-07 18:57:31.326787', '2021-12-07 18:57:31.326787', 'Biriniwa', 17),
(323, '2021-12-07 18:57:31.358598', '2021-12-07 18:57:31.358598', 'Birnin Kudu', 17),
(324, '2021-12-07 18:57:31.392510', '2021-12-07 18:57:31.393509', 'Buji', 17),
(325, '2021-12-07 18:57:31.424314', '2021-12-07 18:57:31.424314', 'Dutse', 17),
(326, '2021-12-07 18:57:31.487696', '2021-12-07 18:57:31.487696', 'Gagarawa', 17),
(327, '2021-12-07 18:57:31.554226', '2021-12-07 18:57:31.554226', 'Garki', 17),
(328, '2021-12-07 18:57:31.599051', '2021-12-07 18:57:31.599051', 'Gumel', 17),
(329, '2021-12-07 18:57:31.641224', '2021-12-07 18:57:31.642227', 'Guri', 17),
(330, '2021-12-07 18:57:31.997799', '2021-12-07 18:57:31.998798', 'Gwaram', 17),
(331, '2021-12-07 18:57:32.129270', '2021-12-07 18:57:32.129270', 'Gwiwa', 17),
(332, '2021-12-07 18:57:32.177353', '2021-12-07 18:57:32.177353', 'Hadejia', 17),
(333, '2021-12-07 18:57:32.231218', '2021-12-07 18:57:32.231218', 'Jahun', 17),
(334, '2021-12-07 18:57:32.259086', '2021-12-07 18:57:32.259086', 'Kafin Hausa', 17),
(335, '2021-12-07 18:57:32.313905', '2021-12-07 18:57:32.313905', 'Kazaure', 17),
(336, '2021-12-07 18:57:32.375867', '2021-12-07 18:57:32.375867', 'Kiri Kasama', 17),
(337, '2021-12-07 18:57:32.430830', '2021-12-07 18:57:32.430830', 'Kiyawa', 17),
(338, '2021-12-07 18:57:32.513783', '2021-12-07 18:57:32.514782', 'Kaugama', 17),
(339, '2021-12-07 18:57:32.580048', '2021-12-07 18:57:32.580048', 'Maigatari', 17),
(340, '2021-12-07 18:57:32.617999', '2021-12-07 18:57:32.617999', 'Malam Madori', 17),
(341, '2021-12-07 18:57:32.665973', '2021-12-07 18:57:32.665973', 'Miga', 17),
(342, '2021-12-07 18:57:32.714827', '2021-12-07 18:57:32.714827', 'Ringim', 17),
(343, '2021-12-07 18:57:32.746983', '2021-12-07 18:57:32.746983', 'Roni', 17),
(344, '2021-12-07 18:57:32.780636', '2021-12-07 18:57:32.780636', 'Sule Tankarkar', 17),
(345, '2021-12-07 18:57:32.836662', '2021-12-07 18:57:32.836662', 'Taura', 17),
(346, '2021-12-07 18:57:32.870571', '2021-12-07 18:57:32.871572', 'Yankwashi', 17),
(347, '2021-12-07 18:57:33.179745', '2021-12-07 18:57:33.179745', 'Zaria', 18),
(348, '2021-12-07 18:57:33.236353', '2021-12-07 18:57:33.236353', 'Birnin Gwari', 18),
(349, '2021-12-07 18:57:33.269123', '2021-12-07 18:57:33.269123', 'Chikun', 18),
(350, '2021-12-07 18:57:33.303016', '2021-12-07 18:57:33.303016', 'Giwa', 18),
(351, '2021-12-07 18:57:33.358012', '2021-12-07 18:57:33.358012', 'Igabi', 18),
(352, '2021-12-07 18:57:33.421186', '2021-12-07 18:57:33.421186', 'Ikara', 18),
(353, '2021-12-07 18:57:33.466506', '2021-12-07 18:57:33.466506', 'Jaba', 18),
(354, '2021-12-07 18:57:33.504637', '2021-12-07 18:57:33.504637', 'Jema\'a', 18),
(355, '2021-12-07 18:57:33.536609', '2021-12-07 18:57:33.536609', 'Kachia', 18),
(356, '2021-12-07 18:57:33.569591', '2021-12-07 18:57:33.569591', 'Kaduna North', 18),
(357, '2021-12-07 18:57:33.624559', '2021-12-07 18:57:33.624559', 'Kaduna South', 18),
(358, '2021-12-07 18:57:33.658538', '2021-12-07 18:57:33.658538', 'Kagarko', 18),
(359, '2021-12-07 18:57:33.700808', '2021-12-07 18:57:33.700808', 'Kajuru', 18),
(360, '2021-12-07 18:57:33.742048', '2021-12-07 18:57:33.742048', 'Kaura', 18),
(361, '2021-12-07 18:57:33.786908', '2021-12-07 18:57:33.786908', 'Kauru', 18),
(362, '2021-12-07 18:57:33.837282', '2021-12-07 18:57:33.837282', 'Kubau', 18),
(363, '2021-12-07 18:57:33.869519', '2021-12-07 18:57:33.869519', 'Kudan', 18),
(364, '2021-12-07 18:57:33.903617', '2021-12-07 18:57:33.903617', 'Lere', 18),
(365, '2021-12-07 18:57:33.936809', '2021-12-07 18:57:33.936809', 'Makarfi', 18),
(366, '2021-12-07 18:57:33.971002', '2021-12-07 18:57:33.971002', 'Sabon Gari', 18),
(367, '2021-12-07 18:57:34.004225', '2021-12-07 18:57:34.004225', 'Sanga', 18),
(368, '2021-12-07 18:57:34.460043', '2021-12-07 18:57:34.460043', 'Soba', 18),
(369, '2021-12-07 18:57:34.525969', '2021-12-07 18:57:34.525969', 'Zangon Kataf', 18),
(370, '2021-12-07 18:57:34.614045', '2021-12-07 18:57:34.614045', 'Ajingi', 19),
(371, '2021-12-07 18:57:34.665195', '2021-12-07 18:57:34.665195', 'Albasu', 19),
(372, '2021-12-07 18:57:34.723962', '2021-12-07 18:57:34.723962', 'Bagwai', 19),
(373, '2021-12-07 18:57:34.764936', '2021-12-07 18:57:34.764936', 'Bebeji', 19),
(374, '2021-12-07 18:57:34.794920', '2021-12-07 18:57:34.794920', 'Bichi', 19),
(375, '2021-12-07 18:57:34.845889', '2021-12-07 18:57:34.845889', 'Bunkure', 19),
(376, '2021-12-07 18:57:34.870873', '2021-12-07 18:57:34.870873', 'Dala', 19),
(377, '2021-12-07 18:57:34.902852', '2021-12-07 18:57:34.902852', 'Dambatta', 19),
(378, '2021-12-07 18:57:34.960872', '2021-12-07 18:57:34.960872', 'Dawakin Kudu', 19),
(379, '2021-12-07 18:57:35.015149', '2021-12-07 18:57:35.015149', 'Dawakin Tofa', 19),
(380, '2021-12-07 18:57:35.065491', '2021-12-07 18:57:35.065491', 'Doguwa', 19),
(381, '2021-12-07 18:57:35.094132', '2021-12-07 18:57:35.094132', 'Fagge', 19),
(382, '2021-12-07 18:57:35.161030', '2021-12-07 18:57:35.161030', 'Gabasawa', 19),
(383, '2021-12-07 18:57:35.222202', '2021-12-07 18:57:35.222202', 'Garko', 19),
(384, '2021-12-07 18:57:35.270113', '2021-12-07 18:57:35.270113', 'Garun Mallam', 19),
(385, '2021-12-07 18:57:35.326091', '2021-12-07 18:57:35.326091', 'Gaya', 19),
(386, '2021-12-07 18:57:35.360904', '2021-12-07 18:57:35.360904', 'Gezawa', 19),
(387, '2021-12-07 18:57:35.437003', '2021-12-07 18:57:35.437003', 'Gwale', 19),
(388, '2021-12-07 18:57:35.658918', '2021-12-07 18:57:35.658918', 'Gwarzo', 19),
(389, '2021-12-07 18:57:35.757916', '2021-12-07 18:57:35.757916', 'Kabo', 19),
(390, '2021-12-07 18:57:35.791839', '2021-12-07 18:57:35.791839', 'Kano Municipal', 19),
(391, '2021-12-07 18:57:35.833930', '2021-12-07 18:57:35.834942', 'Karaye', 19),
(392, '2021-12-07 18:57:35.892076', '2021-12-07 18:57:35.892076', 'Kibiya', 19),
(393, '2021-12-07 18:57:35.924756', '2021-12-07 18:57:35.924756', 'Kiru', 19),
(394, '2021-12-07 18:57:35.975616', '2021-12-07 18:57:35.975616', 'Kumbotso', 19),
(395, '2021-12-07 18:57:36.021589', '2021-12-07 18:57:36.021589', 'Kunchi', 19),
(396, '2021-12-07 18:57:36.047571', '2021-12-07 18:57:36.047571', 'Kura', 19),
(397, '2021-12-07 18:57:36.080551', '2021-12-07 18:57:36.080551', 'Madobi', 19),
(398, '2021-12-07 18:57:36.114533', '2021-12-07 18:57:36.114533', 'Makoda', 19),
(399, '2021-12-07 18:57:36.147159', '2021-12-07 18:57:36.147159', 'Minjibir', 19),
(400, '2021-12-07 18:57:36.181057', '2021-12-07 18:57:36.181057', 'Nasarawa', 19),
(401, '2021-12-07 18:57:36.238927', '2021-12-07 18:57:36.238927', 'Rano', 19),
(402, '2021-12-07 18:57:36.291383', '2021-12-07 18:57:36.291383', 'Rimin Gado', 19),
(403, '2021-12-07 18:57:36.325575', '2021-12-07 18:57:36.326575', 'Rogo', 19),
(404, '2021-12-07 18:57:36.395786', '2021-12-07 18:57:36.395786', 'Shanono', 19),
(405, '2021-12-07 18:57:36.433786', '2021-12-07 18:57:36.433786', 'Sumaila', 19),
(406, '2021-12-07 18:57:36.482293', '2021-12-07 18:57:36.482293', 'Takai', 19),
(407, '2021-12-07 18:57:36.516571', '2021-12-07 18:57:36.516571', 'Tarauni', 19),
(408, '2021-12-07 18:57:36.652008', '2021-12-07 18:57:36.652008', 'Tofa', 19),
(409, '2021-12-07 18:57:36.758102', '2021-12-07 18:57:36.758102', 'Tsanyawa', 19),
(410, '2021-12-07 18:57:36.837916', '2021-12-07 18:57:36.837916', 'Tudun Wada', 19),
(411, '2021-12-07 18:57:36.871381', '2021-12-07 18:57:36.872383', 'Ungogo', 19),
(412, '2021-12-07 18:57:36.930480', '2021-12-07 18:57:36.930480', 'Warawa', 19),
(413, '2021-12-07 18:57:36.971884', '2021-12-07 18:57:36.971884', 'Wudil', 19),
(414, '2021-12-07 18:57:37.004642', '2021-12-07 18:57:37.004642', 'Bakori', 20),
(415, '2021-12-07 18:57:37.063975', '2021-12-07 18:57:37.063975', 'Batagarawa', 20),
(416, '2021-12-07 18:57:37.104656', '2021-12-07 18:57:37.104656', 'Batsari', 20),
(417, '2021-12-07 18:57:37.162869', '2021-12-07 18:57:37.162869', 'Baure', 20),
(418, '2021-12-07 18:57:37.211835', '2021-12-07 18:57:37.211835', 'Bindawa', 20),
(419, '2021-12-07 18:57:37.236821', '2021-12-07 18:57:37.236821', 'Charanchi', 20),
(420, '2021-12-07 18:57:37.302778', '2021-12-07 18:57:37.302778', 'Dandume', 20),
(421, '2021-12-07 18:57:37.335762', '2021-12-07 18:57:37.335762', 'Danja', 20),
(422, '2021-12-07 18:57:37.378603', '2021-12-07 18:57:37.378603', 'Dan Musa', 20),
(423, '2021-12-07 18:57:37.402758', '2021-12-07 18:57:37.402758', 'Daura', 20),
(424, '2021-12-07 18:57:37.454099', '2021-12-07 18:57:37.454099', 'Dutsi', 20),
(425, '2021-12-07 18:57:37.516092', '2021-12-07 18:57:37.516092', 'Dutsin Ma', 20),
(426, '2021-12-07 18:57:37.550326', '2021-12-07 18:57:37.550326', 'Faskari', 20),
(427, '2021-12-07 18:57:37.583988', '2021-12-07 18:57:37.583988', 'Funtua', 20),
(428, '2021-12-07 18:57:37.688567', '2021-12-07 18:57:37.688567', 'Ingawa', 20),
(429, '2021-12-07 18:57:37.740832', '2021-12-07 18:57:37.740832', 'Jibia', 20),
(430, '2021-12-07 18:57:37.931186', '2021-12-07 18:57:37.931186', 'Kafur', 20),
(431, '2021-12-07 18:57:37.977236', '2021-12-07 18:57:37.977236', 'Kaita', 20),
(432, '2021-12-07 18:57:38.048267', '2021-12-07 18:57:38.048267', 'Kankara', 20),
(433, '2021-12-07 18:57:38.111515', '2021-12-07 18:57:38.111515', 'Kankia', 20),
(434, '2021-12-07 18:57:38.180374', '2021-12-07 18:57:38.180374', 'Katsina', 20),
(435, '2021-12-07 18:57:38.215117', '2021-12-07 18:57:38.215117', 'Kurfi', 20),
(436, '2021-12-07 18:57:38.248952', '2021-12-07 18:57:38.248952', 'Kusada', 20),
(437, '2021-12-07 18:57:38.306056', '2021-12-07 18:57:38.306056', 'Mai\'Adua', 20),
(438, '2021-12-07 18:57:38.373266', '2021-12-07 18:57:38.373266', 'Malumfashi', 20),
(439, '2021-12-07 18:57:38.481202', '2021-12-07 18:57:38.481202', 'Mani', 20),
(440, '2021-12-07 18:57:38.514182', '2021-12-07 18:57:38.514182', 'Mashi', 20),
(441, '2021-12-07 18:57:38.570914', '2021-12-07 18:57:38.570914', 'Matazu', 20),
(442, '2021-12-07 18:57:38.602583', '2021-12-07 18:57:38.602583', 'Musawa', 20),
(443, '2021-12-07 18:57:38.799507', '2021-12-07 18:57:38.799507', 'Rimi', 20),
(444, '2021-12-07 18:57:38.943550', '2021-12-07 18:57:38.943550', 'Sabuwa', 20),
(445, '2021-12-07 18:57:39.004541', '2021-12-07 18:57:39.004541', 'Safana', 20),
(446, '2021-12-07 18:57:39.038576', '2021-12-07 18:57:39.038576', 'Sandamu', 20),
(447, '2021-12-07 18:57:39.071332', '2021-12-07 18:57:39.071332', 'Zango', 20),
(448, '2021-12-07 18:57:39.105239', '2021-12-07 18:57:39.105239', 'Zuru', 21),
(449, '2021-12-07 18:57:39.138045', '2021-12-07 18:57:39.138045', 'Aleiro', 21),
(450, '2021-12-07 18:57:39.171955', '2021-12-07 18:57:39.171955', 'Arewa Dandi', 21),
(451, '2021-12-07 18:57:39.204715', '2021-12-07 18:57:39.204715', 'Argungu', 21),
(452, '2021-12-07 18:57:39.264289', '2021-12-07 18:57:39.264289', 'Augie', 21),
(453, '2021-12-07 18:57:39.304731', '2021-12-07 18:57:39.304731', 'Bagudo', 21),
(454, '2021-12-07 18:57:39.338634', '2021-12-07 18:57:39.338634', 'Birnin Kebbi', 21),
(455, '2021-12-07 18:57:39.371394', '2021-12-07 18:57:39.371394', 'Bunza', 21),
(456, '2021-12-07 18:57:39.426966', '2021-12-07 18:57:39.426966', 'Dandi', 21),
(457, '2021-12-07 18:57:39.461087', '2021-12-07 18:57:39.461087', 'Fakai', 21),
(458, '2021-12-07 18:57:39.493631', '2021-12-07 18:57:39.493631', 'Gwandu', 21),
(459, '2021-12-07 18:57:39.552571', '2021-12-07 18:57:39.553570', 'Jega', 21),
(460, '2021-12-07 18:57:39.591542', '2021-12-07 18:57:39.591542', 'Kalgo', 21),
(461, '2021-12-07 18:57:39.637514', '2021-12-07 18:57:39.637514', 'Koko/Besse', 21),
(462, '2021-12-07 18:57:39.671492', '2021-12-07 18:57:39.671492', 'Maiyama', 21),
(463, '2021-12-07 18:57:39.726459', '2021-12-07 18:57:39.726459', 'Ngaski', 21),
(464, '2021-12-07 18:57:39.904804', '2021-12-07 18:57:39.905801', 'Sakaba', 21),
(465, '2021-12-07 18:57:40.030382', '2021-12-07 18:57:40.030382', 'Shanga', 21),
(466, '2021-12-07 18:57:40.165038', '2021-12-07 18:57:40.165038', 'Suru', 21),
(467, '2021-12-07 18:57:40.231302', '2021-12-07 18:57:40.231302', 'Wasagu/Danko', 21),
(468, '2021-12-07 18:57:40.280023', '2021-12-07 18:57:40.280023', 'Yauri', 21),
(469, '2021-12-07 18:57:40.314617', '2021-12-07 18:57:40.314617', 'Adavi', 22),
(470, '2021-12-07 18:57:40.372007', '2021-12-07 18:57:40.372007', 'Ajaokuta', 22),
(471, '2021-12-07 18:57:40.410619', '2021-12-07 18:57:40.410619', 'Ankpa', 22),
(472, '2021-12-07 18:57:40.444161', '2021-12-07 18:57:40.444161', 'Bassa', 22),
(473, '2021-12-07 18:57:40.476429', '2021-12-07 18:57:40.476429', 'Dekina', 22),
(474, '2021-12-07 18:57:40.510334', '2021-12-07 18:57:40.510334', 'Ibaji', 22),
(475, '2021-12-07 18:57:40.572245', '2021-12-07 18:57:40.572245', 'Idah', 22),
(476, '2021-12-07 18:57:40.611324', '2021-12-07 18:57:40.612320', 'Igalamela Odolu', 22),
(477, '2021-12-07 18:57:40.656501', '2021-12-07 18:57:40.656501', 'Ijumu', 22),
(478, '2021-12-07 18:57:40.680827', '2021-12-07 18:57:40.680827', 'Kabba/Bunu', 22),
(479, '2021-12-07 18:57:40.715005', '2021-12-07 18:57:40.715005', 'Kogi', 22),
(480, '2021-12-07 18:57:40.747882', '2021-12-07 18:57:40.747882', 'Lokoja', 22),
(481, '2021-12-07 18:57:40.783091', '2021-12-07 18:57:40.783091', 'Mopa Muro', 22),
(482, '2021-12-07 18:57:40.814072', '2021-12-07 18:57:40.814072', 'Ofu', 22),
(483, '2021-12-07 18:57:40.848050', '2021-12-07 18:57:40.848050', 'Ogori/Magongo', 22),
(484, '2021-12-07 18:57:40.881031', '2021-12-07 18:57:40.881031', 'Okehi', 22),
(485, '2021-12-07 18:57:40.915010', '2021-12-07 18:57:40.915010', 'Okene', 22),
(486, '2021-12-07 18:57:40.948991', '2021-12-07 18:57:40.948991', 'Olamaboro', 22),
(487, '2021-12-07 18:57:41.003168', '2021-12-07 18:57:41.003168', 'Omala', 22),
(488, '2021-12-07 18:57:41.169933', '2021-12-07 18:57:41.170934', 'Yagba East', 22),
(489, '2021-12-07 18:57:41.473988', '2021-12-07 18:57:41.473988', 'Yagba West', 22),
(490, '2021-12-07 18:57:41.655021', '2021-12-07 18:57:41.655021', 'Asa', 23),
(491, '2021-12-07 18:57:41.720224', '2021-12-07 18:57:41.720224', 'Baruten', 23),
(492, '2021-12-07 18:57:41.773439', '2021-12-07 18:57:41.773439', 'Edu', 23),
(493, '2021-12-07 18:57:41.822988', '2021-12-07 18:57:41.822988', 'Ekiti', 23),
(494, '2021-12-07 18:57:41.851764', '2021-12-07 18:57:41.851764', 'Ifelodun', 23),
(495, '2021-12-07 18:57:41.909106', '2021-12-07 18:57:41.910101', 'Ilorin East', 23),
(496, '2021-12-07 18:57:41.941870', '2021-12-07 18:57:41.941870', 'Ilorin South', 23),
(497, '2021-12-07 18:57:41.986941', '2021-12-07 18:57:41.986941', 'Ilorin West', 23),
(498, '2021-12-07 18:57:42.039105', '2021-12-07 18:57:42.039105', 'Irepodun', 23),
(499, '2021-12-07 18:57:42.077084', '2021-12-07 18:57:42.077084', 'Isin', 23),
(500, '2021-12-07 18:57:42.106063', '2021-12-07 18:57:42.106063', 'Kaiama', 23),
(501, '2021-12-07 18:57:42.144041', '2021-12-07 18:57:42.144041', 'Moro', 23),
(502, '2021-12-07 18:57:42.173039', '2021-12-07 18:57:42.173039', 'Offa', 23),
(503, '2021-12-07 18:57:42.224057', '2021-12-07 18:57:42.224057', 'Oke Ero', 23),
(504, '2021-12-07 18:57:42.247833', '2021-12-07 18:57:42.247833', 'Oyun', 23),
(505, '2021-12-07 18:57:42.281785', '2021-12-07 18:57:42.281785', 'Pategi', 23),
(506, '2021-12-07 18:57:42.316194', '2021-12-07 18:57:42.316194', 'Agege', 24),
(507, '2021-12-07 18:57:42.373627', '2021-12-07 18:57:42.373627', 'Ajeromi-Ifelodun', 24),
(508, '2021-12-07 18:57:42.438958', '2021-12-07 18:57:42.438958', 'Alimosho', 24),
(509, '2021-12-07 18:57:42.590102', '2021-12-07 18:57:42.590102', 'Amuwo-Odofin', 24),
(510, '2021-12-07 18:57:42.761064', '2021-12-07 18:57:42.761064', 'Apapa', 24),
(511, '2021-12-07 18:57:42.812410', '2021-12-07 18:57:42.812410', 'Badagry', 24),
(512, '2021-12-07 18:57:42.865905', '2021-12-07 18:57:42.865905', 'Epe', 24),
(513, '2021-12-07 18:57:42.912977', '2021-12-07 18:57:42.912977', 'Eti Osa', 24),
(514, '2021-12-07 18:57:42.954998', '2021-12-07 18:57:42.954998', 'Ibeju-Lekki', 24),
(515, '2021-12-07 18:57:43.018262', '2021-12-07 18:57:43.018262', 'Ifako-Ijaiye', 24),
(516, '2021-12-07 18:57:43.118419', '2021-12-07 18:57:43.118419', 'Ikeja', 24),
(517, '2021-12-07 18:57:43.171420', '2021-12-07 18:57:43.171420', 'Ikorodu', 24),
(518, '2021-12-07 18:57:43.208509', '2021-12-07 18:57:43.208509', 'Kosofe', 24),
(519, '2021-12-07 18:57:43.250471', '2021-12-07 18:57:43.250471', 'Lagos Island', 24),
(520, '2021-12-07 18:57:43.303436', '2021-12-07 18:57:43.303436', 'Lagos Mainland', 24),
(521, '2021-12-07 18:57:43.358406', '2021-12-07 18:57:43.358406', 'Mushin', 24),
(522, '2021-12-07 18:57:43.417368', '2021-12-07 18:57:43.417368', 'Ojo', 24),
(523, '2021-12-07 18:57:43.468488', '2021-12-07 18:57:43.468488', 'Oshodi-Isolo', 24),
(524, '2021-12-07 18:57:43.552897', '2021-12-07 18:57:43.552897', 'Shomolu', 24),
(525, '2021-12-07 18:57:43.603203', '2021-12-07 18:57:43.603203', 'Surulere', 24),
(526, '2021-12-07 18:57:43.637605', '2021-12-07 18:57:43.637605', 'Akwanga', 25),
(527, '2021-12-07 18:57:43.672559', '2021-12-07 18:57:43.673558', 'Awe', 25),
(528, '2021-12-07 18:57:43.705551', '2021-12-07 18:57:43.705551', 'Doma', 25),
(529, '2021-12-07 18:57:43.805398', '2021-12-07 18:57:43.805398', 'Karu', 25),
(530, '2021-12-07 18:57:43.871926', '2021-12-07 18:57:43.872925', 'Keana', 25),
(531, '2021-12-07 18:57:43.905129', '2021-12-07 18:57:43.905129', 'Keffi', 25),
(532, '2021-12-07 18:57:43.963360', '2021-12-07 18:57:43.963360', 'Kokona', 25),
(533, '2021-12-07 18:57:44.011435', '2021-12-07 18:57:44.011435', 'Lafia', 25),
(534, '2021-12-07 18:57:44.061697', '2021-12-07 18:57:44.062704', 'Nasarawa', 25),
(535, '2021-12-07 18:57:44.097700', '2021-12-07 18:57:44.097700', 'Nasarawa Egon', 25),
(536, '2021-12-07 18:57:44.145440', '2021-12-07 18:57:44.145440', 'Obi', 25),
(537, '2021-12-07 18:57:44.208693', '2021-12-07 18:57:44.208693', 'Toto', 25),
(538, '2021-12-07 18:57:44.249586', '2021-12-07 18:57:44.249586', 'Wamba', 25),
(539, '2021-12-07 18:57:44.283739', '2021-12-07 18:57:44.283739', 'Agaie', 26),
(540, '2021-12-07 18:57:44.316302', '2021-12-07 18:57:44.316302', 'Agwara', 26),
(541, '2021-12-07 18:57:44.349576', '2021-12-07 18:57:44.349576', 'Bida', 26),
(542, '2021-12-07 18:57:44.382671', '2021-12-07 18:57:44.382671', 'Borgu', 26),
(543, '2021-12-07 18:57:44.416887', '2021-12-07 18:57:44.416887', 'Bosso', 26),
(544, '2021-12-07 18:57:44.448960', '2021-12-07 18:57:44.448960', 'Chanchaga', 26),
(545, '2021-12-07 18:57:44.482942', '2021-12-07 18:57:44.482942', 'Edati', 26),
(546, '2021-12-07 18:57:44.513921', '2021-12-07 18:57:44.513921', 'Gbako', 26),
(547, '2021-12-07 18:57:44.574885', '2021-12-07 18:57:44.574885', 'Gurara', 26),
(548, '2021-12-07 18:57:44.772778', '2021-12-07 18:57:44.772778', 'Katcha', 26),
(549, '2021-12-07 18:57:44.878800', '2021-12-07 18:57:44.878800', 'Kontagora', 26),
(550, '2021-12-07 18:57:44.971043', '2021-12-07 18:57:44.971043', 'Lapai', 26),
(551, '2021-12-07 18:57:45.038286', '2021-12-07 18:57:45.038286', 'Lavun', 26),
(552, '2021-12-07 18:57:45.101289', '2021-12-07 18:57:45.101289', 'Magama', 26),
(553, '2021-12-07 18:57:45.170524', '2021-12-07 18:57:45.170524', 'Mariga', 26),
(554, '2021-12-07 18:57:45.210598', '2021-12-07 18:57:45.211603', 'Mashegu', 26),
(555, '2021-12-07 18:57:45.276606', '2021-12-07 18:57:45.276606', 'Mokwa', 26),
(556, '2021-12-07 18:57:45.324609', '2021-12-07 18:57:45.324609', 'Moya', 26),
(557, '2021-12-07 18:57:45.371615', '2021-12-07 18:57:45.371615', 'Paikoro', 26),
(558, '2021-12-07 18:57:45.407118', '2021-12-07 18:57:45.407118', 'Rafi', 26),
(559, '2021-12-07 18:57:45.647078', '2021-12-07 18:57:45.647078', 'Rijau', 26),
(560, '2021-12-07 18:57:45.682099', '2021-12-07 18:57:45.682099', 'Shiroro', 26),
(561, '2021-12-07 18:57:45.717072', '2021-12-07 18:57:45.717072', 'Suleja', 26),
(562, '2021-12-07 18:57:45.748052', '2021-12-07 18:57:45.748052', 'Tafa', 26),
(563, '2021-12-07 18:57:45.806020', '2021-12-07 18:57:45.806020', 'Wushishi', 26),
(564, '2021-12-07 18:57:45.838998', '2021-12-07 18:57:45.838998', 'Abeokuta North', 27),
(565, '2021-12-07 18:57:46.098023', '2021-12-07 18:57:46.098023', 'Abeokuta South', 27),
(566, '2021-12-07 18:57:46.378865', '2021-12-07 18:57:46.378865', 'Ado-Odo/Ota', 27),
(567, '2021-12-07 18:57:46.462514', '2021-12-07 18:57:46.462514', 'Yewa North', 27),
(568, '2021-12-07 18:57:46.530443', '2021-12-07 18:57:46.530443', 'Yewa South', 27),
(569, '2021-12-07 18:57:46.563608', '2021-12-07 18:57:46.563608', 'Ewekoro', 27),
(570, '2021-12-07 18:57:46.597794', '2021-12-07 18:57:46.597794', 'Ifo', 27),
(571, '2021-12-07 18:57:46.649600', '2021-12-07 18:57:46.649600', 'Ijebu East', 27),
(572, '2021-12-07 18:57:46.683577', '2021-12-07 18:57:46.683577', 'Ijebu North', 27),
(573, '2021-12-07 18:57:46.750537', '2021-12-07 18:57:46.750537', 'Ijebu North East', 27),
(574, '2021-12-07 18:57:46.804208', '2021-12-07 18:57:46.804208', 'Ijebu Ode', 27),
(575, '2021-12-07 18:57:46.862099', '2021-12-07 18:57:46.862099', 'Ikenne', 27),
(576, '2021-12-07 18:57:46.916013', '2021-12-07 18:57:46.916013', 'Imeko Afon', 27),
(577, '2021-12-07 18:57:46.969980', '2021-12-07 18:57:46.969980', 'Ipokia', 27),
(578, '2021-12-07 18:57:47.003958', '2021-12-07 18:57:47.003958', 'Obafemi Owode', 27),
(579, '2021-12-07 18:57:47.070418', '2021-12-07 18:57:47.070418', 'Odeda', 27),
(580, '2021-12-07 18:57:47.133940', '2021-12-07 18:57:47.133940', 'Odogbolu', 27),
(581, '2021-12-07 18:57:47.192652', '2021-12-07 18:57:47.193649', 'Ogun Waterside', 27),
(582, '2021-12-07 18:57:47.372829', '2021-12-07 18:57:47.372829', 'Remo North', 27),
(583, '2021-12-07 18:57:47.503714', '2021-12-07 18:57:47.503714', 'Shagamu', 27),
(584, '2021-12-07 18:57:47.563108', '2021-12-07 18:57:47.564106', 'Akoko North-East', 28),
(585, '2021-12-07 18:57:47.619938', '2021-12-07 18:57:47.619938', 'Akoko North-West', 28),
(586, '2021-12-07 18:57:47.685997', '2021-12-07 18:57:47.685997', 'Akoko South-West', 28),
(587, '2021-12-07 18:57:47.719914', '2021-12-07 18:57:47.719914', 'Akoko South-East', 28),
(588, '2021-12-07 18:57:47.751932', '2021-12-07 18:57:47.752926', 'Akure North', 28),
(589, '2021-12-07 18:57:47.811045', '2021-12-07 18:57:47.811045', 'Akure South', 28),
(590, '2021-12-07 18:57:47.849022', '2021-12-07 18:57:47.849022', 'Ese Odo', 28),
(591, '2021-12-07 18:57:47.906985', '2021-12-07 18:57:47.907985', 'Idanre', 28),
(592, '2021-12-07 18:57:47.939965', '2021-12-07 18:57:47.939965', 'Ifedore', 28),
(593, '2021-12-07 18:57:47.992329', '2021-12-07 18:57:47.992329', 'Ilaje', 28),
(594, '2021-12-07 18:57:48.025605', '2021-12-07 18:57:48.025605', 'Ile Oluji/Okeigbo', 28),
(595, '2021-12-07 18:57:48.059513', '2021-12-07 18:57:48.059513', 'Irele', 28),
(596, '2021-12-07 18:57:48.092025', '2021-12-07 18:57:48.092025', 'Odigbo', 28),
(597, '2021-12-07 18:57:48.147993', '2021-12-07 18:57:48.147993', 'Okitipupa', 28),
(598, '2021-12-07 18:57:48.214952', '2021-12-07 18:57:48.214952', 'Ondo East', 28),
(599, '2021-12-07 18:57:48.248929', '2021-12-07 18:57:48.248929', 'Ondo West', 28),
(600, '2021-12-07 18:57:48.494685', '2021-12-07 18:57:48.494685', 'Ose', 28),
(601, '2021-12-07 18:57:48.669342', '2021-12-07 18:57:48.669342', 'Owo', 28),
(602, '2021-12-07 18:57:48.734125', '2021-12-07 18:57:48.734125', 'Atakunmosa East', 29),
(603, '2021-12-07 18:57:48.792814', '2021-12-07 18:57:48.792814', 'Atakunmosa West', 29),
(604, '2021-12-07 18:57:48.828461', '2021-12-07 18:57:48.828461', 'Aiyedaade', 29),
(605, '2021-12-07 18:57:48.861224', '2021-12-07 18:57:48.861224', 'Aiyedire', 29),
(606, '2021-12-07 18:57:48.915780', '2021-12-07 18:57:48.915780', 'Boluwaduro', 29),
(607, '2021-12-07 18:57:48.948829', '2021-12-07 18:57:48.948829', 'Boripe', 29),
(608, '2021-12-07 18:57:48.984114', '2021-12-07 18:57:48.984114', 'Ede North', 29),
(609, '2021-12-07 18:57:49.018091', '2021-12-07 18:57:49.018091', 'Ede South', 29),
(610, '2021-12-07 18:57:49.052071', '2021-12-07 18:57:49.052071', 'Ife Central', 29),
(611, '2021-12-07 18:57:49.085049', '2021-12-07 18:57:49.085049', 'Ife East', 29),
(612, '2021-12-07 18:57:49.137584', '2021-12-07 18:57:49.137584', 'Ife North', 29),
(613, '2021-12-07 18:57:49.178770', '2021-12-07 18:57:49.178770', 'Ife South', 29),
(614, '2021-12-07 18:57:49.271407', '2021-12-07 18:57:49.271407', 'Egbedore', 29),
(615, '2021-12-07 18:57:49.311382', '2021-12-07 18:57:49.311382', 'Ejigbo', 29),
(616, '2021-12-07 18:57:49.337365', '2021-12-07 18:57:49.337365', 'Ifedayo', 29),
(617, '2021-12-07 18:57:49.372347', '2021-12-07 18:57:49.372347', 'Ifelodun', 29),
(618, '2021-12-07 18:57:49.422316', '2021-12-07 18:57:49.422316', 'Ila', 29),
(619, '2021-12-07 18:57:49.469287', '2021-12-07 18:57:49.469287', 'Ilesa East', 29),
(620, '2021-12-07 18:57:49.639339', '2021-12-07 18:57:49.639339', 'Ilesa West', 29),
(621, '2021-12-07 18:57:49.810258', '2021-12-07 18:57:49.810258', 'Irepodun', 29),
(622, '2021-12-07 18:57:49.899927', '2021-12-07 18:57:49.899927', 'Irewole', 29),
(623, '2021-12-07 18:57:49.959082', '2021-12-07 18:57:49.959082', 'Isokan', 29);
INSERT INTO `lga` (`id`, `created_at`, `updated_at`, `title`, `state_id`) VALUES
(624, '2021-12-07 18:57:50.040652', '2021-12-07 18:57:50.040652', 'Iwo', 29),
(625, '2021-12-07 18:57:50.093408', '2021-12-07 18:57:50.093408', 'Obokun', 29),
(626, '2021-12-07 18:57:50.127633', '2021-12-07 18:57:50.127633', 'Odo Otin', 29),
(627, '2021-12-07 18:57:50.168605', '2021-12-07 18:57:50.168605', 'Ola Oluwa', 29),
(628, '2021-12-07 18:57:50.195588', '2021-12-07 18:57:50.195588', 'Olorunda', 29),
(629, '2021-12-07 18:57:50.228569', '2021-12-07 18:57:50.228569', 'Oriade', 29),
(630, '2021-12-07 18:57:50.262549', '2021-12-07 18:57:50.262549', 'Orolu', 29),
(631, '2021-12-07 18:57:50.295527', '2021-12-07 18:57:50.295527', 'Osogbo', 29),
(632, '2021-12-07 18:57:50.348261', '2021-12-07 18:57:50.348261', 'Afijio', 30),
(633, '2021-12-07 18:57:50.418444', '2021-12-07 18:57:50.418444', 'Akinyele', 30),
(634, '2021-12-07 18:57:50.461323', '2021-12-07 18:57:50.461323', 'Atiba', 30),
(635, '2021-12-07 18:57:50.495295', '2021-12-07 18:57:50.495295', 'Atisbo', 30),
(636, '2021-12-07 18:57:50.528275', '2021-12-07 18:57:50.528275', 'Egbeda', 30),
(637, '2021-12-07 18:57:50.582246', '2021-12-07 18:57:50.582246', 'Ibadan North', 30),
(638, '2021-12-07 18:57:50.615221', '2021-12-07 18:57:50.615221', 'Ibadan North-East', 30),
(639, '2021-12-07 18:57:50.649203', '2021-12-07 18:57:50.649203', 'Ibadan North-West', 30),
(640, '2021-12-07 18:57:50.875347', '2021-12-07 18:57:50.875347', 'Ibadan South-East', 30),
(641, '2021-12-07 18:57:50.999562', '2021-12-07 18:57:50.999562', 'Ibadan South-West', 30),
(642, '2021-12-07 18:57:51.176106', '2021-12-07 18:57:51.176106', 'Ibarapa Central', 30),
(643, '2021-12-07 18:57:51.242632', '2021-12-07 18:57:51.242632', 'Ibarapa East', 30),
(644, '2021-12-07 18:57:51.276276', '2021-12-07 18:57:51.276276', 'Ibarapa North', 30),
(645, '2021-12-07 18:57:51.327694', '2021-12-07 18:57:51.327694', 'Ido', 30),
(646, '2021-12-07 18:57:51.376932', '2021-12-07 18:57:51.376932', 'Irepo', 30),
(647, '2021-12-07 18:57:51.422948', '2021-12-07 18:57:51.422948', 'Iseyin', 30),
(648, '2021-12-07 18:57:51.461631', '2021-12-07 18:57:51.461631', 'Itesiwaju', 30),
(649, '2021-12-07 18:57:51.506785', '2021-12-07 18:57:51.506785', 'Iwajowa', 30),
(650, '2021-12-07 18:57:51.552524', '2021-12-07 18:57:51.553522', 'Kajola', 30),
(651, '2021-12-07 18:57:51.595592', '2021-12-07 18:57:51.595592', 'Lagelu', 30),
(652, '2021-12-07 18:57:51.674749', '2021-12-07 18:57:51.674749', 'Ogbomosho North', 30),
(653, '2021-12-07 18:57:51.721509', '2021-12-07 18:57:51.721509', 'Ogbomosho South', 30),
(654, '2021-12-07 18:57:51.759484', '2021-12-07 18:57:51.759484', 'Ogo Oluwa', 30),
(655, '2021-12-07 18:57:51.806458', '2021-12-07 18:57:51.806458', 'Olorunsogo', 30),
(656, '2021-12-07 18:57:51.839438', '2021-12-07 18:57:51.839438', 'Oluyole', 30),
(657, '2021-12-07 18:57:51.873418', '2021-12-07 18:57:51.873418', 'Ona Ara', 30),
(658, '2021-12-07 18:57:51.906397', '2021-12-07 18:57:51.906397', 'Orelope', 30),
(659, '2021-12-07 18:57:52.106133', '2021-12-07 18:57:52.106133', 'Ori Ire', 30),
(660, '2021-12-07 18:57:52.217913', '2021-12-07 18:57:52.217913', 'Oyo West', 30),
(661, '2021-12-07 18:57:52.449374', '2021-12-07 18:57:52.449374', 'Oyo East', 30),
(662, '2021-12-07 18:57:52.531898', '2021-12-07 18:57:52.531898', 'Saki East', 30),
(663, '2021-12-07 18:57:52.585129', '2021-12-07 18:57:52.585129', 'Saki West', 30),
(664, '2021-12-07 18:57:52.651202', '2021-12-07 18:57:52.651202', 'Surulere', 30),
(665, '2021-12-07 18:57:52.685270', '2021-12-07 18:57:52.685270', 'Bokkos', 31),
(666, '2021-12-07 18:57:52.739080', '2021-12-07 18:57:52.739080', 'Barkin Ladi', 31),
(667, '2021-12-07 18:57:52.791141', '2021-12-07 18:57:52.791141', 'Bassa', 31),
(668, '2021-12-07 18:57:52.830325', '2021-12-07 18:57:52.830325', 'Jos East', 31),
(669, '2021-12-07 18:57:52.883230', '2021-12-07 18:57:52.883230', 'Jos North', 31),
(670, '2021-12-07 18:57:52.919409', '2021-12-07 18:57:52.919409', 'Jos South', 31),
(671, '2021-12-07 18:57:52.953388', '2021-12-07 18:57:52.953388', 'Kanam', 31),
(672, '2021-12-07 18:57:52.983364', '2021-12-07 18:57:52.983364', 'Kanke', 31),
(673, '2021-12-07 18:57:53.038333', '2021-12-07 18:57:53.038333', 'Langtang South', 31),
(674, '2021-12-07 18:57:53.071312', '2021-12-07 18:57:53.071312', 'Langtang North', 31),
(675, '2021-12-07 18:57:53.150000', '2021-12-07 18:57:53.150000', 'Mangu', 31),
(676, '2021-12-07 18:57:53.202167', '2021-12-07 18:57:53.202167', 'Mikang', 31),
(677, '2021-12-07 18:57:53.271594', '2021-12-07 18:57:53.271594', 'Pankshin', 31),
(678, '2021-12-07 18:57:53.408245', '2021-12-07 18:57:53.408245', 'Qua\'an Pan', 31),
(679, '2021-12-07 18:57:53.529012', '2021-12-07 18:57:53.529012', 'Riyom', 31),
(680, '2021-12-07 18:57:53.607991', '2021-12-07 18:57:53.607991', 'Shendam', 31),
(681, '2021-12-07 18:57:53.661930', '2021-12-07 18:57:53.661930', 'Wase', 31),
(682, '2021-12-07 18:57:53.694712', '2021-12-07 18:57:53.694712', 'Abua/Odual', 32),
(683, '2021-12-07 18:57:53.747317', '2021-12-07 18:57:53.747317', 'Ahoada East', 32),
(684, '2021-12-07 18:57:53.816157', '2021-12-07 18:57:53.817156', 'Ahoada West', 32),
(685, '2021-12-07 18:57:53.861994', '2021-12-07 18:57:53.861994', 'Akuku-Toru', 32),
(686, '2021-12-07 18:57:53.909018', '2021-12-07 18:57:53.909018', 'Andoni', 32),
(687, '2021-12-07 18:57:53.960223', '2021-12-07 18:57:53.960223', 'Asari-Toru', 32),
(688, '2021-12-07 18:57:53.993061', '2021-12-07 18:57:53.993061', 'Bonny', 32),
(689, '2021-12-07 18:57:54.029152', '2021-12-07 18:57:54.029152', 'Degema', 32),
(690, '2021-12-07 18:57:54.061582', '2021-12-07 18:57:54.061582', 'Eleme', 32),
(691, '2021-12-07 18:57:54.117059', '2021-12-07 18:57:54.117059', 'Emuoha', 32),
(692, '2021-12-07 18:57:54.150373', '2021-12-07 18:57:54.150373', 'Etche', 32),
(693, '2021-12-07 18:57:54.200342', '2021-12-07 18:57:54.200342', 'Gokana', 32),
(694, '2021-12-07 18:57:54.227325', '2021-12-07 18:57:54.227325', 'Ikwerre', 32),
(695, '2021-12-07 18:57:54.261304', '2021-12-07 18:57:54.261304', 'Khana', 32),
(696, '2021-12-07 18:57:54.294284', '2021-12-07 18:57:54.294284', 'Obio/Akpor', 32),
(697, '2021-12-07 18:57:54.329263', '2021-12-07 18:57:54.329263', 'Ogba/Egbema/Ndoni', 32),
(698, '2021-12-07 18:57:54.363073', '2021-12-07 18:57:54.363073', 'Ogu/Bolo', 32),
(699, '2021-12-07 18:57:54.505249', '2021-12-07 18:57:54.505249', 'Okrika', 32),
(700, '2021-12-07 18:57:54.582295', '2021-12-07 18:57:54.582295', 'Omuma', 32),
(701, '2021-12-07 18:57:54.704882', '2021-12-07 18:57:54.704882', 'Opobo/Nkoro', 32),
(702, '2021-12-07 18:57:54.737407', '2021-12-07 18:57:54.737407', 'Oyigbo', 32),
(703, '2021-12-07 18:57:54.795731', '2021-12-07 18:57:54.795731', 'Port Harcourt', 32),
(704, '2021-12-07 18:57:54.861628', '2021-12-07 18:57:54.861628', 'Tai', 32),
(705, '2021-12-07 18:57:54.895592', '2021-12-07 18:57:54.895592', 'Binji', 33),
(706, '2021-12-07 18:57:54.926264', '2021-12-07 18:57:54.926264', 'Bodinga', 33),
(707, '2021-12-07 18:57:54.960217', '2021-12-07 18:57:54.960217', 'Dange Shuni', 33),
(708, '2021-12-07 18:57:55.018217', '2021-12-07 18:57:55.018217', 'Gada', 33),
(709, '2021-12-07 18:57:55.051016', '2021-12-07 18:57:55.051016', 'Goronyo', 33),
(710, '2021-12-07 18:57:55.085046', '2021-12-07 18:57:55.085046', 'Gudu', 33),
(711, '2021-12-07 18:57:55.117684', '2021-12-07 18:57:55.117684', 'Gwadabawa', 33),
(712, '2021-12-07 18:57:55.152123', '2021-12-07 18:57:55.152123', 'Illela', 33),
(713, '2021-12-07 18:57:55.184546', '2021-12-07 18:57:55.184546', 'Isa', 33),
(714, '2021-12-07 18:57:55.217481', '2021-12-07 18:57:55.217481', 'Kebbe', 33),
(715, '2021-12-07 18:57:55.251209', '2021-12-07 18:57:55.252209', 'Kware', 33),
(716, '2021-12-07 18:57:55.284923', '2021-12-07 18:57:55.284923', 'Rabah', 33),
(717, '2021-12-07 18:57:55.318322', '2021-12-07 18:57:55.318322', 'Sabon Birni', 33),
(718, '2021-12-07 18:57:55.351646', '2021-12-07 18:57:55.351646', 'Shagari', 33),
(719, '2021-12-07 18:57:55.384628', '2021-12-07 18:57:55.384628', 'Silame', 33),
(720, '2021-12-07 18:57:55.417609', '2021-12-07 18:57:55.417609', 'Sokoto North', 33),
(721, '2021-12-07 18:57:55.565313', '2021-12-07 18:57:55.565313', 'Sokoto South', 33),
(722, '2021-12-07 18:57:55.683464', '2021-12-07 18:57:55.683464', 'Tambuwal', 33),
(723, '2021-12-07 18:57:55.883555', '2021-12-07 18:57:55.883555', 'Tangaza', 33),
(724, '2021-12-07 18:57:55.916455', '2021-12-07 18:57:55.916455', 'Tureta', 33),
(725, '2021-12-07 18:57:55.951161', '2021-12-07 18:57:55.951161', 'Wamako', 33),
(726, '2021-12-07 18:57:55.983126', '2021-12-07 18:57:55.983126', 'Wurno', 33),
(727, '2021-12-07 18:57:56.017026', '2021-12-07 18:57:56.017026', 'Yabo', 33),
(728, '2021-12-07 18:57:56.049797', '2021-12-07 18:57:56.049797', 'Zing', 34),
(729, '2021-12-07 18:57:56.085030', '2021-12-07 18:57:56.085030', 'Ardo Kola', 34),
(730, '2021-12-07 18:57:56.248813', '2021-12-07 18:57:56.248813', 'Bali', 34),
(731, '2021-12-07 18:57:56.471561', '2021-12-07 18:57:56.471561', 'Donga', 34),
(732, '2021-12-07 18:57:56.505582', '2021-12-07 18:57:56.505582', 'Gashaka', 34),
(733, '2021-12-07 18:57:56.538261', '2021-12-07 18:57:56.539261', 'Gassol', 34),
(734, '2021-12-07 18:57:56.573241', '2021-12-07 18:57:56.573241', 'Ibi', 34),
(735, '2021-12-07 18:57:56.605220', '2021-12-07 18:57:56.605220', 'Jalingo', 34),
(736, '2021-12-07 18:57:56.704156', '2021-12-07 18:57:56.704156', 'Karim Lamido', 34),
(737, '2021-12-07 18:57:56.764137', '2021-12-07 18:57:56.764137', 'Kumi', 34),
(738, '2021-12-07 18:57:56.917157', '2021-12-07 18:57:56.917157', 'Lau', 34),
(739, '2021-12-07 18:57:56.959461', '2021-12-07 18:57:56.959461', 'Sardauna', 34),
(740, '2021-12-07 18:57:56.993402', '2021-12-07 18:57:56.993402', 'Takum', 34),
(741, '2021-12-07 18:57:57.026197', '2021-12-07 18:57:57.026197', 'Ussa', 34),
(742, '2021-12-07 18:57:57.060110', '2021-12-07 18:57:57.060110', 'Wukari', 34),
(743, '2021-12-07 18:57:57.093084', '2021-12-07 18:57:57.093084', 'Yorro', 34),
(744, '2021-12-07 18:57:57.127034', '2021-12-07 18:57:57.127034', 'Bade', 35),
(745, '2021-12-07 18:57:57.159587', '2021-12-07 18:57:57.159587', 'Bursari', 35),
(746, '2021-12-07 18:57:57.193521', '2021-12-07 18:57:57.193521', 'Damaturu', 35),
(747, '2021-12-07 18:57:57.232261', '2021-12-07 18:57:57.233255', 'Fika', 35),
(748, '2021-12-07 18:57:57.277321', '2021-12-07 18:57:57.277321', 'Fune', 35),
(749, '2021-12-07 18:57:57.324475', '2021-12-07 18:57:57.324475', 'Geidam', 35),
(750, '2021-12-07 18:57:57.361497', '2021-12-07 18:57:57.361497', 'Gujba', 35),
(751, '2021-12-07 18:57:57.397505', '2021-12-07 18:57:57.397505', 'Gulani', 35),
(752, '2021-12-07 18:57:57.437298', '2021-12-07 18:57:57.437298', 'Jakusko', 35),
(753, '2021-12-07 18:57:57.480271', '2021-12-07 18:57:57.480271', 'Karasuwa', 35),
(754, '2021-12-07 18:57:57.531242', '2021-12-07 18:57:57.531242', 'Machina', 35),
(755, '2021-12-07 18:57:57.587207', '2021-12-07 18:57:57.587207', 'Nangere', 35),
(756, '2021-12-07 18:57:57.623186', '2021-12-07 18:57:57.623186', 'Nguru', 35),
(757, '2021-12-07 18:57:57.753464', '2021-12-07 18:57:57.753464', 'Potiskum', 35),
(758, '2021-12-07 18:57:58.084077', '2021-12-07 18:57:58.084077', 'Tarmuwa', 35),
(759, '2021-12-07 18:57:58.240406', '2021-12-07 18:57:58.240406', 'Yunusari', 35),
(760, '2021-12-07 18:57:58.296652', '2021-12-07 18:57:58.297648', 'Yusufari', 35),
(761, '2021-12-07 18:57:58.350779', '2021-12-07 18:57:58.350779', 'Zurmi', 36),
(762, '2021-12-07 18:57:58.414208', '2021-12-07 18:57:58.414208', 'Anka', 36),
(763, '2021-12-07 18:57:58.439717', '2021-12-07 18:57:58.440716', 'Bakura', 36),
(764, '2021-12-07 18:57:58.498717', '2021-12-07 18:57:58.498717', 'Birnin Magaji/Kiyaw', 36),
(765, '2021-12-07 18:57:58.528966', '2021-12-07 18:57:58.528966', 'Bukkuyum', 36),
(766, '2021-12-07 18:57:58.560857', '2021-12-07 18:57:58.560857', 'Bungudu', 36),
(767, '2021-12-07 18:57:58.595631', '2021-12-07 18:57:58.596635', 'Gummi', 36),
(768, '2021-12-07 18:57:58.651687', '2021-12-07 18:57:58.651687', 'Gusau', 36),
(769, '2021-12-07 18:57:58.705907', '2021-12-07 18:57:58.705907', 'Kaura Namoda', 36),
(770, '2021-12-07 18:57:58.763066', '2021-12-07 18:57:58.763066', 'Maradun', 36),
(771, '2021-12-07 18:57:58.795953', '2021-12-07 18:57:58.796954', 'Maru', 36),
(772, '2021-12-07 18:57:58.860190', '2021-12-07 18:57:58.860190', 'Shinkafi', 36),
(773, '2021-12-07 18:57:58.892996', '2021-12-07 18:57:58.892996', 'Talata Mafara', 36),
(774, '2021-12-07 18:57:58.935162', '2021-12-07 18:57:58.935162', 'Chafe', 36);

-- --------------------------------------------------------

--
-- Table structure for table `loanbased_savings`
--

CREATE TABLE `loanbased_savings` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `savings_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loanbased_savings`
--

INSERT INTO `loanbased_savings` (`id`, `created_at`, `updated_at`, `savings_id`) VALUES
(2, '2021-12-16 13:08:05.328029', '2021-12-16 13:08:05.328029', 3);

-- --------------------------------------------------------

--
-- Table structure for table `loans_cleared`
--

CREATE TABLE `loans_cleared` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `loan_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `loans_disbursed`
--

CREATE TABLE `loans_disbursed` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `loan_number` varchar(255) NOT NULL,
  `loan_amount` decimal(20,2) NOT NULL,
  `repayment` decimal(20,2) NOT NULL,
  `amount_paid` decimal(20,2) NOT NULL,
  `balance` decimal(20,2) NOT NULL,
  `duration` int(11) NOT NULL,
  `interest_rate` int(11) NOT NULL,
  `interest_deduction` varchar(255) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `stop_date` date DEFAULT NULL,
  `merge_account_number` varchar(255) DEFAULT NULL,
  `loan_merge_status_id` int(11) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `schedule_status_id` int(11) NOT NULL,
  `status_id` int(11) DEFAULT NULL,
  `transaction_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loans_disbursed`
--

INSERT INTO `loans_disbursed` (`id`, `created_at`, `updated_at`, `loan_number`, `loan_amount`, `repayment`, `amount_paid`, `balance`, `duration`, `interest_rate`, `interest_deduction`, `start_date`, `stop_date`, `merge_account_number`, `loan_merge_status_id`, `member_id`, `processed_by_id`, `schedule_status_id`, `status_id`, `transaction_id`) VALUES
(1, '2021-12-13 15:42:44.060854', '2021-12-13 15:42:44.060854', '2010000120211213164200001', '105000.00', '35000.00', '70798.00', '-34202.00', 3, 5, 'SPREAD', '2021-11-01', '2022-02-01', NULL, 1, 151, 9, 1, 1, 8),
(2, '2021-12-13 16:22:58.467739', '2021-12-13 16:22:58.468746', '2020000120211213172200002', '500000.00', '50000.00', '50000.00', '-450000.00', 3, 5, 'SOURCE', '2021-11-01', '2022-02-01', NULL, 1, 151, 9, 1, 1, 9);

-- --------------------------------------------------------

--
-- Table structure for table `loans_repayment_base`
--

CREATE TABLE `loans_repayment_base` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `loan_number` varchar(255) NOT NULL,
  `loan_amount` decimal(20,2) NOT NULL,
  `repayment` decimal(20,2) NOT NULL,
  `amount_paid` decimal(20,2) NOT NULL,
  `balance` decimal(20,2) NOT NULL,
  `start_date` date DEFAULT NULL,
  `stop_date` date DEFAULT NULL,
  `merged_loans` varchar(255) DEFAULT NULL,
  `loan_merge_status_id` int(11) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL,
  `transaction_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loans_repayment_base`
--

INSERT INTO `loans_repayment_base` (`id`, `created_at`, `updated_at`, `loan_number`, `loan_amount`, `repayment`, `amount_paid`, `balance`, `start_date`, `stop_date`, `merged_loans`, `loan_merge_status_id`, `member_id`, `processed_by_id`, `status_id`, `transaction_id`) VALUES
(1, '2021-12-13 15:42:44.033867', '2021-12-15 02:57:24.620762', '2010000120211213164200001', '105000.00', '35000.00', '62899.00', '-42101.00', '2021-11-01', '2022-02-01', NULL, 1, 151, 9, 1, 8),
(2, '2021-12-13 16:22:58.394457', '2021-12-13 16:22:58.394457', '2020000120211213172200002', '500000.00', '50000.00', '50000.00', '-450000.00', '2021-11-01', '2022-02-01', NULL, 1, 151, 9, 1, 9);

-- --------------------------------------------------------

--
-- Table structure for table `loans_uploaded`
--

CREATE TABLE `loans_uploaded` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `particulars` varchar(255) NOT NULL,
  `loan_amount` decimal(20,2) NOT NULL,
  `amount_paid` decimal(20,2) NOT NULL,
  `balance` decimal(20,2) NOT NULL,
  `repayment` decimal(20,2) NOT NULL,
  `duration` int(11) NOT NULL,
  `interest_rate` int(11) NOT NULL,
  `interest_deduction` varchar(255) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `stop_date` date DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL,
  `transaction_id` int(11) DEFAULT NULL,
  `transaction_period_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loans_uploaded`
--

INSERT INTO `loans_uploaded` (`id`, `created_at`, `updated_at`, `particulars`, `loan_amount`, `amount_paid`, `balance`, `repayment`, `duration`, `interest_rate`, `interest_deduction`, `start_date`, `stop_date`, `member_id`, `processed_by_id`, `status_id`, `transaction_id`, `transaction_period_id`) VALUES
(1, '2021-12-13 15:17:43.766172', '2021-12-13 15:42:44.143800', 'Balance Brought Forward as at 12/08/2021', '105000.00', '35000.00', '70000.00', '35000.00', 3, 5, 'SPREAD', '2021-11-01', '2022-02-01', 151, 9, 2, 8, 1),
(3, '2021-12-13 16:18:02.391122', '2021-12-13 16:22:58.657693', 'Balance Brought Forward as at 12/08/2021', '500000.00', '50000.00', '450000.00', '50000.00', 3, 5, 'SOURCE', '2021-11-01', '2022-02-01', 151, 9, 2, 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `loan_application`
--

CREATE TABLE `loan_application` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `loan_amount` decimal(20,2) NOT NULL,
  `approved_amount` decimal(20,2) DEFAULT NULL,
  `comment` longtext DEFAULT NULL,
  `certification_comment` longtext DEFAULT NULL,
  `certification_date` date DEFAULT NULL,
  `approval_comment` longtext DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `applicant_id` int(11) DEFAULT NULL,
  `approval_officer_id` int(11) DEFAULT NULL,
  `approval_status_id` int(11) NOT NULL,
  `bank_account_id` int(11) DEFAULT NULL,
  `certification_officer_id` int(11) DEFAULT NULL,
  `certification_status_id` int(11) NOT NULL,
  `nok_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `submission_status_id` int(11) NOT NULL,
  `transaction_status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `loan_application_guarnators`
--

CREATE TABLE `loan_application_guarnators` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `applicant_id` int(11) DEFAULT NULL,
  `guarantor_id` int(11) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `loan_application_settings`
--

CREATE TABLE `loan_application_settings` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `description` varchar(255) NOT NULL,
  `value` varchar(255) NOT NULL,
  `category` varchar(255) DEFAULT NULL,
  `applicant_id` int(11) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `loan_category`
--

CREATE TABLE `loan_category` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loan_category`
--

INSERT INTO `loan_category` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'MONETARY', '2021-12-07 19:06:56.784479', '2021-12-07 19:06:56.784479'),
(2, 'NON-MONETARY', '2021-12-07 19:06:56.836529', '2021-12-07 19:06:56.836529');

-- --------------------------------------------------------

--
-- Table structure for table `loan_form_issuance`
--

CREATE TABLE `loan_form_issuance` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `receipt` varchar(255) NOT NULL,
  `admin_charge` decimal(20,2) NOT NULL,
  `applicant_id` int(11) DEFAULT NULL,
  `processing_status_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `loan_guarantors`
--

CREATE TABLE `loan_guarantors` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `applicant_id` int(11) DEFAULT NULL,
  `guarantor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `loan_merge_status`
--

CREATE TABLE `loan_merge_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loan_merge_status`
--

INSERT INTO `loan_merge_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'NORMINAL', '2021-12-07 19:09:38.864869', '2021-12-07 19:09:38.864869'),
(2, 'MERGED', '2021-12-07 19:09:38.914044', '2021-12-07 19:09:38.914044');

-- --------------------------------------------------------

--
-- Table structure for table `loan_number`
--

CREATE TABLE `loan_number` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `code` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loan_number`
--

INSERT INTO `loan_number` (`id`, `created_at`, `updated_at`, `code`) VALUES
(1, '2021-12-13 15:38:23.230298', '2021-12-13 16:22:58.298337', 3);

-- --------------------------------------------------------

--
-- Table structure for table `loan_request`
--

CREATE TABLE `loan_request` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `loan_amount` decimal(20,2) NOT NULL,
  `approved_amount` decimal(20,2) DEFAULT NULL,
  `comment` longtext DEFAULT NULL,
  `certification_comment` longtext DEFAULT NULL,
  `certification_date` date DEFAULT NULL,
  `approval_comment` longtext DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_officer_id` int(11) DEFAULT NULL,
  `approval_status_id` int(11) NOT NULL,
  `certification_officer_id` int(11) DEFAULT NULL,
  `certification_status_id` int(11) NOT NULL,
  `loan_id` int(11) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `submission_status_id` int(11) NOT NULL,
  `transaction_status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loan_request`
--

INSERT INTO `loan_request` (`id`, `created_at`, `updated_at`, `loan_amount`, `approved_amount`, `comment`, `certification_comment`, `certification_date`, `approval_comment`, `approval_date`, `approval_officer_id`, `approval_status_id`, `certification_officer_id`, `certification_status_id`, `loan_id`, `member_id`, `processed_by_id`, `submission_status_id`, `transaction_status_id`) VALUES
(1, '2021-12-16 10:58:44.176434', '2021-12-16 10:58:44.176434', '50000.00', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, 1, 8, 152, 9, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `loan_request_attachments`
--

CREATE TABLE `loan_request_attachments` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `description` varchar(255) NOT NULL,
  `image` varchar(100) NOT NULL,
  `applicant_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loan_request_attachments`
--

INSERT INTO `loan_request_attachments` (`id`, `created_at`, `updated_at`, `description`, `image`, `applicant_id`, `processed_by_id`, `status_id`) VALUES
(1, '2021-12-16 12:57:59.578505', '2021-12-16 12:57:59.578505', 'Payslip nov 2021', '/media/icons_9oX5Oa9.png', 1, 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `loan_request_settings`
--

CREATE TABLE `loan_request_settings` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `description` varchar(255) NOT NULL,
  `value` varchar(255) NOT NULL,
  `category` varchar(255) DEFAULT NULL,
  `applicant_id` int(11) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `loan_schedule_status`
--

CREATE TABLE `loan_schedule_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loan_schedule_status`
--

INSERT INTO `loan_schedule_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'UNSCHEDULED', '2021-12-07 19:05:50.947712', '2021-12-07 19:05:50.947712'),
(2, 'SCHEDULED', '2021-12-07 19:05:50.993591', '2021-12-07 19:05:50.994590');

-- --------------------------------------------------------

--
-- Table structure for table `loan_upload_status`
--

CREATE TABLE `loan_upload_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loan_upload_status`
--

INSERT INTO `loan_upload_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'PENDING', '2021-12-07 19:06:23.953983', '2021-12-07 19:06:23.953983'),
(2, 'UPLOADED', '2021-12-07 19:06:23.997778', '2021-12-07 19:06:23.997778'),
(3, 'VERIFIED', '2021-12-07 19:06:24.130740', '2021-12-07 19:06:24.130740');

-- --------------------------------------------------------

--
-- Table structure for table `locations`
--

CREATE TABLE `locations` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `locations`
--

INSERT INTO `locations` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'FETHA', '2021-12-07 19:01:34.040297', '2021-12-07 19:01:34.040297'),
(2, 'EBSU', '2021-12-07 19:01:34.083187', '2021-12-07 19:01:34.083187'),
(3, 'FISTULA', '2021-12-07 19:01:34.230301', '2021-12-07 19:01:34.230301');

-- --------------------------------------------------------

--
-- Table structure for table `locked_status`
--

CREATE TABLE `locked_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `locked_status`
--

INSERT INTO `locked_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'OPEN', '2021-12-07 19:05:17.364608', '2021-12-07 19:05:17.364608'),
(2, 'LOCKED', '2021-12-07 19:05:17.424711', '2021-12-07 19:05:17.425711');

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `member_id` varchar(255) NOT NULL,
  `middle_name` varchar(255) DEFAULT NULL,
  `full_name` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) NOT NULL,
  `profile_pic` varchar(100) DEFAULT NULL,
  `residential_address` longtext DEFAULT NULL,
  `permanent_home_address` longtext DEFAULT NULL,
  `file_no` varchar(255) NOT NULL,
  `ippis_no` varchar(255) NOT NULL,
  `gross_pay` decimal(20,2) NOT NULL,
  `gross_pay_as_at` varchar(255) DEFAULT NULL,
  `shares` int(11) NOT NULL,
  `date_joined` date DEFAULT NULL,
  `admin_id` bigint(20) DEFAULT NULL,
  `applicant_id` int(11) DEFAULT NULL,
  `date_joined_status_id` int(11) NOT NULL,
  `department_id` int(11) DEFAULT NULL,
  `exclusive_status_id` int(11) NOT NULL,
  `gender_id` int(11) DEFAULT NULL,
  `gross_pay_status_id` int(11) NOT NULL,
  `lga_id` int(11) DEFAULT NULL,
  `loan_status_id` int(11) NOT NULL,
  `salary_institution_id` int(11) DEFAULT NULL,
  `savings_status_id` int(11) NOT NULL,
  `shares_status_id` int(11) NOT NULL,
  `state_id` int(11) DEFAULT NULL,
  `status_id` int(11) NOT NULL,
  `title_id` int(11) DEFAULT NULL,
  `welfare_status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`id`, `created_at`, `updated_at`, `member_id`, `middle_name`, `full_name`, `phone_number`, `profile_pic`, `residential_address`, `permanent_home_address`, `file_no`, `ippis_no`, `gross_pay`, `gross_pay_as_at`, `shares`, `date_joined`, `admin_id`, `applicant_id`, `date_joined_status_id`, `department_id`, `exclusive_status_id`, `gender_id`, `gross_pay_status_id`, `lga_id`, `loan_status_id`, `salary_institution_id`, `savings_status_id`, `shares_status_id`, `state_id`, `status_id`, `title_id`, `welfare_status_id`) VALUES
(151, '2021-12-07 21:04:28.778306', '2021-12-31 07:47:55.222933', 'FETHAII/2010/00001', 'MAUREEN', 'BEN IDAKA MAUREEN', '08064004355', '', 'Abakaliki', 'Idembia', '00001', '00001', '250000.00', 'Salary as at 12/16/2021', 0, '2020-01-01', 167, 352, 1, 1, 1, 2, 2, NULL, 2, 1, 2, 3, NULL, 1, 2, 3),
(152, '2021-12-07 21:04:30.179870', '2022-01-10 14:39:17.122877', 'FETHAII/2011/00002', 'OBIA', 'UCHENNA OKOLI OBIA', '08064004356', '', '', '', '00002', '00002', '158000.00', 'Salary as at 01/10/2022', 0, '2020-01-01', 168, 353, 1, 1, 1, NULL, 2, NULL, 1, 1, 2, 3, NULL, 1, NULL, 3),
(153, '2021-12-07 21:04:30.878929', '2021-12-16 11:03:24.896170', 'FETHAII/2012/00003', 'E', 'NKONYELU OKONKWO E', '08064004357', '', '', '', '00003', '00003', '190000.00', 'Salary as at 12/16/2021', 0, '2020-01-01', 169, 354, 1, NULL, 1, NULL, 2, NULL, 1, 1, 1, 3, NULL, 1, NULL, 1),
(154, '2021-12-07 21:04:31.628875', '2022-01-10 14:53:34.820748', 'FETHAII/2013/00004', 'CHIB', 'OPHELIA AMADI CHIB', '08064004358', '', '', '', '00004', '00004', '158000.00', 'Salary as at 01/10/2022', 0, '2020-01-01', 170, 355, 1, NULL, 1, NULL, 2, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(155, '2021-12-07 21:04:32.330190', '2022-01-10 18:45:14.948229', 'FETHAII/2014/00005', 'IJEM', 'IKWUO NNACHI IJEM', '08064004359', '', '', '', '00005', '00005', '200000.00', 'Salary as at 01/10/2022', 0, '2020-01-01', 171, 356, 1, NULL, 1, NULL, 2, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(156, '2021-12-07 21:04:32.917815', '2022-01-10 14:45:05.297590', 'FETHAII/2015/00006', 'MARY', 'IFEOMA AGBOWO MARY', '08064004360', '', '', '', '00006', '00006', '190000.00', 'Salary as at 01/10/2022', 0, '2020-01-01', 172, 357, 1, NULL, 1, NULL, 2, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(157, '2021-12-07 21:04:33.585676', '2021-12-07 21:04:33.659120', 'FETHAII/2016/00007', 'OKUTA J', 'DR NWANKWO OKUTA J', '08064004361', '', '', '', '00007', '00007', '0.00', NULL, 0, '2020-01-01', 173, 358, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(158, '2021-12-07 21:04:34.483294', '2021-12-07 21:04:34.583147', 'FETHAII/2017/00008', '', 'EMMANUEL ABAA ', '08064004362', '', '', '', '00008', '00008', '0.00', NULL, 0, '2020-01-01', 174, 359, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(159, '2021-12-07 21:04:35.469113', '2021-12-07 21:04:35.583399', 'FETHAII/2018/00009', 'AGNES', 'UGO ABAGHA AGNES', '08064004363', '', '', '', '00009', '00009', '0.00', NULL, 0, '2020-01-01', 175, 360, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(160, '2021-12-07 21:04:36.106691', '2021-12-07 21:04:36.331501', 'FETHAII/2019/00010', '', 'CHIGOZI ABAGHAUGWU ', '08064004364', '', '', '', '00010', '00010', '0.00', NULL, 0, '2020-01-01', 176, 361, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(161, '2021-12-07 21:04:37.006502', '2021-12-07 21:04:37.105675', 'FETHAII/2020/00011', '', 'NWACHINAME ABANIFI ', '08064004365', '', '', '', '00011', '00011', '0.00', NULL, 0, '2020-01-01', 177, 362, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(162, '2021-12-07 21:04:37.653192', '2021-12-07 21:04:37.715240', 'FETHAII/2021/00012', 'P', 'NNENWAOGO ABARA P', '08064004366', '', '', '', '00012', '00012', '0.00', NULL, 0, '2020-01-01', 178, 363, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(163, '2021-12-07 21:04:38.532958', '2021-12-07 21:04:38.763592', 'FETHAII/2010/00013', 'CHI', 'LAWRENCE ABARA CHI', '08064004367', '', '', '', '00013', '00013', '0.00', NULL, 0, '2020-01-01', 179, 364, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(164, '2021-12-07 21:04:39.374579', '2021-12-07 21:04:39.488758', 'FETHAII/2011/00014', 'EUC', 'NWAKAEGO ABARA EUC', '08064004368', '', '', '', '00014', '00014', '0.00', NULL, 0, '2020-01-01', 180, 365, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(165, '2021-12-07 21:04:40.370419', '2021-12-07 21:04:40.451364', 'FETHAII/2012/00015', 'DORCAS', 'OBASI ABBA DORCAS', '08064004369', '', '', '', '00015', '00015', '0.00', NULL, 0, '2020-01-01', 181, 366, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(166, '2021-12-07 21:04:40.942450', '2021-12-07 21:04:40.983089', 'FETHAII/2013/00016', 'ANIET', 'EFFIONG ABIA ANIET', '08064004370', '', '', '', '00016', '00016', '0.00', NULL, 0, '2020-01-01', 182, 367, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(167, '2021-12-07 21:04:41.497046', '2021-12-07 21:04:41.561632', 'FETHAII/2014/00017', 'NDON', 'NKIRUKA ABIA NDON', '08064004371', '', '', '', '00017', '00017', '0.00', NULL, 0, '2020-01-01', 183, 368, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(168, '2021-12-07 21:04:42.105763', '2021-12-07 21:04:42.215456', 'FETHAII/2015/00018', 'EFFIONG NDO', 'DR ABIA EFFIONG NDO', '08064004372', '', '', '', '00018', '00018', '0.00', NULL, 0, '2020-01-01', 184, 369, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(169, '2021-12-07 21:04:42.742450', '2021-12-07 21:04:42.928571', 'FETHAII/2016/00019', 'GLORIA', 'UGOCHI ABII GLORIA', '08064004373', '', '', '', '00019', '00019', '0.00', NULL, 0, '2020-01-01', 185, 370, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(170, '2021-12-07 21:04:43.450302', '2021-12-07 21:04:43.687229', 'FETHAII/2017/00020', 'ZULAY', 'ABEKE ABIOLA ZULAY', '08064004374', '', '', '', '00020', '00020', '0.00', NULL, 0, '2020-01-01', 186, 371, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(171, '2021-12-07 21:04:44.289093', '2021-12-07 21:04:44.398736', 'FETHAII/2018/00021', 'CLARA', 'CHIOMA ABIRI CLARA', '08064004375', '', '', '', '00021', '00021', '0.00', NULL, 0, '2020-01-01', 187, 372, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(172, '2021-12-07 21:04:45.037950', '2021-12-07 21:04:45.463884', 'FETHAII/2019/00022', 'AD', 'OLADELE ABOKEDE AD', '08064004376', '', '', '', '00022', '00022', '0.00', NULL, 0, '2020-01-01', 188, 373, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(173, '2021-12-07 21:04:46.205080', '2021-12-07 21:04:46.271041', 'FETHAII/2020/00023', 'AD', 'OMOLARA ABOKEDE AD', '08064004377', '', '', '', '00023', '00023', '0.00', NULL, 0, '2020-01-01', 189, 374, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(174, '2021-12-07 21:04:47.073720', '2021-12-07 21:04:47.176613', 'FETHAII/2021/00024', '', 'LEONARD ABOR ', '08064004378', '', '', '', '00024', '00024', '0.00', NULL, 0, '2020-01-01', 190, 375, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(175, '2021-12-07 21:04:48.081609', '2021-12-07 21:04:48.374008', 'FETHAII/2010/00025', 'AUGUSTIN', 'MOMOH ABU AUGUSTIN', '08064004379', '', '', '', '00025', '00025', '0.00', NULL, 0, '2020-01-01', 191, 376, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(176, '2021-12-07 21:04:49.192905', '2021-12-07 21:04:49.729293', 'FETHAII/2011/00026', '', 'MMADUABUCHI ABUWA ', '08064004380', '', '', '', '00026', '00026', '0.00', NULL, 0, '2020-01-01', 192, 377, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(177, '2021-12-07 21:04:50.358862', '2021-12-07 21:04:50.430566', 'FETHAII/2012/00027', 'NGWU', 'MAXWELL ACHI NGWU', '08064004381', '', '', '', '00027', '00027', '0.00', NULL, 0, '2020-01-01', 193, 378, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(178, '2021-12-07 21:04:50.921721', '2021-12-07 21:04:50.985687', 'FETHAII/2013/00028', 'UC', 'EZEKIEL ACHONWA UC', '08064004382', '', '', '', '00028', '00028', '0.00', NULL, 0, '2020-01-01', 194, 379, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(179, '2021-12-07 21:04:51.656145', '2021-12-07 21:04:51.767013', 'FETHAII/2014/00029', '', 'UDOCHRIS ACHUGONYE ', '08064004383', '', '', '', '00029', '00029', '0.00', NULL, 0, '2020-01-01', 195, 380, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(180, '2021-12-07 21:04:52.493867', '2021-12-07 21:04:52.640236', 'FETHAII/2015/00030', 'SIMO', 'MATTHEW ADAMA SIMO', '08064004384', '', '', '', '00030', '00030', '0.00', NULL, 0, '2020-01-01', 196, 381, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(181, '2021-12-07 21:04:53.458087', '2021-12-07 21:04:53.643570', 'FETHAII/2016/00031', '', 'BEATRI ADAMSOKORIE ', '08064004385', '', '', '', '00031', '00031', '0.00', NULL, 0, '2020-01-01', 197, 382, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(182, '2021-12-07 21:04:54.187751', '2021-12-07 21:04:54.784583', 'FETHAII/2017/00032', 'MODES', 'IFEOMA ADANI MODES', '08064004386', '', '', '', '00032', '00032', '0.00', NULL, 0, '2020-01-01', 198, 383, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(183, '2021-12-07 21:04:55.476409', '2021-12-07 21:04:55.552359', 'FETHAII/2018/00033', 'NGOZ', 'IBUKUN ADEOLU NGOZ', '08064004387', '', '', '', '00033', '00033', '0.00', NULL, 0, '2020-01-01', 199, 384, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(184, '2021-12-07 21:04:56.011273', '2021-12-07 21:04:56.113272', 'FETHAII/2019/00034', 'JULIAN', 'KUSS ADEOYE JULIAN', '08064004388', '', '', '', '00034', '00034', '0.00', NULL, 0, '2020-01-01', 200, 385, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(185, '2021-12-07 21:04:56.595980', '2021-12-07 21:04:56.708319', 'FETHAII/2020/00035', 'OLU', 'SAMSON ADEYEMI OLU', '08064004389', '', '', '', '00035', '00035', '0.00', NULL, 0, '2020-01-01', 201, 386, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(186, '2021-12-07 21:04:57.308801', '2021-12-16 00:07:47.357758', 'FETHAII/2021/00036', 'AME', 'EMMANUEL ADIDU AME', '08064004390', '', '', '', '00036', '00036', '0.00', NULL, 0, '2020-01-01', 202, 387, 1, NULL, 1, NULL, 1, NULL, 1, 1, 2, 1, NULL, 1, NULL, 1),
(187, '2021-12-07 21:04:58.102307', '2021-12-07 21:04:58.206512', 'FETHAII/2010/00037', 'N', 'NWANYIEZE ADIELE N', '08064004391', '', '', '', '00037', '00037', '0.00', NULL, 0, '2020-01-01', 203, 388, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(188, '2021-12-07 21:04:58.734040', '2021-12-07 21:04:58.843433', 'FETHAII/2011/00038', 'IF', 'EMMANUEL ADIGWE IF', '08064004392', '', '', '', '00038', '00038', '0.00', NULL, 0, '2020-01-01', 204, 389, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(189, '2021-12-07 21:04:59.673771', '2021-12-07 21:04:59.777799', 'FETHAII/2012/00039', 'NGO', 'JULIANA ADIKWU NGO', '08064004393', '', '', '', '00039', '00039', '0.00', NULL, 0, '2020-01-01', 205, 390, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(190, '2021-12-07 21:05:00.397637', '2021-12-07 21:05:00.512712', 'FETHAII/2013/00040', '', 'CAROLINE ADIMORAH ', '08064004394', '', '', '', '00040', '00040', '0.00', NULL, 0, '2020-01-01', 206, 391, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(191, '2021-12-07 21:05:01.352282', '2021-12-07 21:05:01.461194', 'FETHAII/2014/00041', 'HA', 'ORAEKI ADIMORAH HA', '08064004395', '', '', '', '00041', '00041', '0.00', NULL, 0, '2020-01-01', 207, 392, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(192, '2021-12-07 21:05:01.922522', '2021-12-07 21:05:01.996135', 'FETHAII/2015/00042', '', 'IFEYINWA ADOGU ', '08064004396', '', '', '', '00042', '00042', '0.00', NULL, 0, '2020-01-01', 208, 393, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(193, '2021-12-07 21:05:02.474177', '2021-12-07 21:05:02.561181', 'FETHAII/2016/00043', '', 'OGHENEOCHUKO ADOKA ', '08064004397', '', '', '', '00043', '00043', '0.00', NULL, 0, '2020-01-01', 209, 394, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(194, '2021-12-07 21:05:03.019273', '2021-12-07 21:05:03.109420', 'FETHAII/2017/00044', 'JOHN', 'NWOVA ADOKE JOHN', '08064004398', '', '', '', '00044', '00044', '0.00', NULL, 0, '2020-01-01', 210, 395, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(195, '2021-12-07 21:05:03.608681', '2021-12-07 21:05:03.705383', 'FETHAII/2018/00045', 'ELDA', 'EDACHE ADOKWU ELDA', '08064004399', '', '', '', '00045', '00045', '0.00', NULL, 0, '2020-01-01', 211, 396, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(196, '2021-12-07 21:05:04.174988', '2021-12-07 21:05:04.270349', 'FETHAII/2019/00046', 'BENJA', 'OBINNA ADONU BENJA', '08064004400', '', '', '', '00046', '00046', '0.00', NULL, 0, '2020-01-01', 212, 397, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(197, '2021-12-07 21:05:04.945655', '2021-12-07 21:05:05.028132', 'FETHAII/2020/00047', 'UKAMA', 'LINDA ADUAKA UKAMA', '08064004401', '', '', '', '00047', '00047', '0.00', NULL, 0, '2020-01-01', 213, 398, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(198, '2021-12-07 21:05:05.539143', '2021-12-07 21:05:05.792605', 'FETHAII/2021/00048', 'ELIZA', 'NGOZI ADUAKA ELIZA', '08064004402', '', '', '', '00048', '00048', '0.00', NULL, 0, '2020-01-01', 214, 399, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(199, '2021-12-07 21:05:06.294739', '2021-12-07 21:05:06.398963', 'FETHAII/2010/00049', 'ONYI', 'VIVIAN ADUAKA ONYI', '08064004403', '', '', '', '00049', '00049', '0.00', NULL, 0, '2020-01-01', 215, 400, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(200, '2021-12-07 21:05:06.841428', '2021-12-07 21:05:06.969147', 'FETHAII/2011/00050', 'PATRI', 'ADAGBA ADUWA PATRI', '08064004404', '', '', '', '00050', '00050', '0.00', NULL, 0, '2020-01-01', 216, 401, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1),
(209, '2021-12-16 10:06:52.749052', '2021-12-16 10:06:52.879813', 'FETHAII/2021/05005', 'EDET', 'FRED EKPE EDET', '08598574455', '', '', '', '67766767', '67766767', '0.00', NULL, 0, '2021-12-16', 227, 402, 1, 17, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 7, 1);

-- --------------------------------------------------------

--
-- Table structure for table `membership_form_sales_record`
--

CREATE TABLE `membership_form_sales_record` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `payment_reference` varchar(255) DEFAULT NULL,
  `receipt` varchar(255) NOT NULL,
  `admin_charge` decimal(20,2) DEFAULT NULL,
  `shares` int(11) NOT NULL,
  `share_amount` decimal(20,2) DEFAULT NULL,
  `welfare_amount` decimal(20,2) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `applicant_id` int(11) DEFAULT NULL,
  `bank_ccount_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `membership_form_sales_record`
--

INSERT INTO `membership_form_sales_record` (`id`, `created_at`, `updated_at`, `payment_reference`, `receipt`, `admin_charge`, `shares`, `share_amount`, `welfare_amount`, `image`, `applicant_id`, `bank_ccount_id`, `processed_by_id`, `status_id`) VALUES
(352, '2021-12-07 21:04:18.681299', '2021-12-07 21:04:29.113579', NULL, 'C-00201', NULL, 0, NULL, NULL, '', 351, NULL, 9, 2),
(353, '2021-12-07 21:04:18.880683', '2021-12-07 21:04:30.314438', NULL, 'C-00202', NULL, 0, NULL, NULL, '', 352, NULL, 9, 2),
(354, '2021-12-07 21:04:19.729405', '2021-12-07 21:04:31.145350', NULL, 'C-00203', NULL, 0, NULL, NULL, '', 353, NULL, 9, 2),
(355, '2021-12-07 21:04:20.050574', '2021-12-07 21:04:31.826153', NULL, 'C-00204', NULL, 0, NULL, NULL, '', 354, NULL, 9, 2),
(356, '2021-12-07 21:04:20.183123', '2021-12-07 21:04:32.447166', NULL, 'C-00205', NULL, 0, NULL, NULL, '', 355, NULL, 9, 2),
(357, '2021-12-07 21:04:20.306518', '2021-12-07 21:04:33.081980', NULL, 'C-00206', NULL, 0, NULL, NULL, '', 356, NULL, 9, 2),
(358, '2021-12-07 21:04:20.521571', '2021-12-07 21:04:33.701984', NULL, 'C-00207', NULL, 0, NULL, NULL, '', 357, NULL, 9, 2),
(359, '2021-12-07 21:04:20.714125', '2021-12-07 21:04:34.624125', NULL, 'C-00208', NULL, 0, NULL, NULL, '', 358, NULL, 9, 2),
(360, '2021-12-07 21:04:20.848571', '2021-12-07 21:04:35.637246', NULL, 'C-00209', NULL, 0, NULL, NULL, '', 359, NULL, 9, 2),
(361, '2021-12-07 21:04:20.982058', '2021-12-07 21:04:36.358126', NULL, 'C-00210', NULL, 0, NULL, NULL, '', 360, NULL, 9, 2),
(362, '2021-12-07 21:04:21.161165', '2021-12-07 21:04:37.149241', NULL, 'C-00211', NULL, 0, NULL, NULL, '', 361, NULL, 9, 2),
(363, '2021-12-07 21:04:21.304462', '2021-12-07 21:04:37.757097', NULL, 'C-00212', NULL, 0, NULL, NULL, '', 362, NULL, 9, 2),
(364, '2021-12-07 21:04:21.417071', '2021-12-07 21:04:38.858041', NULL, 'C-00213', NULL, 0, NULL, NULL, '', 363, NULL, 9, 2),
(365, '2021-12-07 21:04:21.516998', '2021-12-07 21:04:39.548057', NULL, 'C-00214', NULL, 0, NULL, NULL, '', 364, NULL, 9, 2),
(366, '2021-12-07 21:04:21.605067', '2021-12-07 21:04:40.504331', NULL, 'C-00215', NULL, 0, NULL, NULL, '', 365, NULL, 9, 2),
(367, '2021-12-07 21:04:21.682726', '2021-12-07 21:04:41.027371', NULL, 'C-00216', NULL, 0, NULL, NULL, '', 366, NULL, 9, 2),
(368, '2021-12-07 21:04:22.784854', '2021-12-07 21:04:41.604609', NULL, 'C-00217', NULL, 0, NULL, NULL, '', 367, NULL, 9, 2),
(369, '2021-12-07 21:04:23.002788', '2021-12-07 21:04:42.259777', NULL, 'C-00218', NULL, 0, NULL, NULL, '', 368, NULL, 9, 2),
(370, '2021-12-07 21:04:23.162791', '2021-12-07 21:04:42.946586', NULL, 'C-00219', NULL, 0, NULL, NULL, '', 369, NULL, 9, 2),
(371, '2021-12-07 21:04:23.327813', '2021-12-07 21:04:43.739150', NULL, 'C-00220', NULL, 0, NULL, NULL, '', 370, NULL, 9, 2),
(372, '2021-12-07 21:04:23.606581', '2021-12-07 21:04:44.449216', NULL, 'C-00221', NULL, 0, NULL, NULL, '', 371, NULL, 9, 2),
(373, '2021-12-07 21:04:23.759740', '2021-12-07 21:04:45.515722', NULL, 'C-00222', NULL, 0, NULL, NULL, '', 372, NULL, 9, 2),
(374, '2021-12-07 21:04:23.849926', '2021-12-07 21:04:46.363664', NULL, 'C-00223', NULL, 0, NULL, NULL, '', 373, NULL, 9, 2),
(375, '2021-12-07 21:04:24.016418', '2021-12-07 21:04:47.228020', NULL, 'C-00224', NULL, 0, NULL, NULL, '', 374, NULL, 9, 2),
(376, '2021-12-07 21:04:24.158590', '2021-12-07 21:04:48.416451', NULL, 'C-00225', NULL, 0, NULL, NULL, '', 375, NULL, 9, 2),
(377, '2021-12-07 21:04:24.329451', '2021-12-07 21:04:49.792254', NULL, 'C-00226', NULL, 0, NULL, NULL, '', 376, NULL, 9, 2),
(378, '2021-12-07 21:04:24.568262', '2021-12-07 21:04:50.470453', NULL, 'C-00227', NULL, 0, NULL, NULL, '', 377, NULL, 9, 2),
(379, '2021-12-07 21:04:24.772529', '2021-12-07 21:04:51.102369', NULL, 'C-00228', NULL, 0, NULL, NULL, '', 378, NULL, 9, 2),
(380, '2021-12-07 21:04:24.903388', '2021-12-07 21:04:51.815421', NULL, 'C-00229', NULL, 0, NULL, NULL, '', 379, NULL, 9, 2),
(381, '2021-12-07 21:04:25.005788', '2021-12-07 21:04:52.725121', NULL, 'C-00230', NULL, 0, NULL, NULL, '', 380, NULL, 9, 2),
(382, '2021-12-07 21:04:25.136008', '2021-12-07 21:04:53.704255', NULL, 'C-00231', NULL, 0, NULL, NULL, '', 381, NULL, 9, 2),
(383, '2021-12-07 21:04:25.282970', '2021-12-07 21:04:54.929382', NULL, 'C-00232', NULL, 0, NULL, NULL, '', 382, NULL, 9, 2),
(384, '2021-12-07 21:04:25.358924', '2021-12-07 21:04:55.569347', NULL, 'C-00233', NULL, 0, NULL, NULL, '', 383, NULL, 9, 2),
(385, '2021-12-07 21:04:25.481299', '2021-12-07 21:04:56.172955', NULL, 'C-00234', NULL, 0, NULL, NULL, '', 384, NULL, 9, 2),
(386, '2021-12-07 21:04:25.618510', '2021-12-07 21:04:56.803717', NULL, 'C-00235', NULL, 0, NULL, NULL, '', 385, NULL, 9, 2),
(387, '2021-12-07 21:04:25.806992', '2021-12-07 21:04:57.414915', NULL, 'C-00236', NULL, 0, NULL, NULL, '', 386, NULL, 9, 2),
(388, '2021-12-07 21:04:25.937302', '2021-12-07 21:04:58.251036', NULL, 'C-00237', NULL, 0, NULL, NULL, '', 387, NULL, 9, 2),
(389, '2021-12-07 21:04:26.005551', '2021-12-07 21:04:58.881736', NULL, 'C-00238', NULL, 0, NULL, NULL, '', 388, NULL, 9, 2),
(390, '2021-12-07 21:04:26.106123', '2021-12-07 21:04:59.829274', NULL, 'C-00239', NULL, 0, NULL, NULL, '', 389, NULL, 9, 2),
(391, '2021-12-07 21:04:26.192464', '2021-12-07 21:05:00.570960', NULL, 'C-00240', NULL, 0, NULL, NULL, '', 390, NULL, 9, 2),
(392, '2021-12-07 21:04:26.258709', '2021-12-07 21:05:01.503170', NULL, 'C-00241', NULL, 0, NULL, NULL, '', 391, NULL, 9, 2),
(393, '2021-12-07 21:04:26.326625', '2021-12-07 21:05:02.036763', NULL, 'C-00242', NULL, 0, NULL, NULL, '', 392, NULL, 9, 2),
(394, '2021-12-07 21:04:26.425645', '2021-12-07 21:05:02.604156', NULL, 'C-00243', NULL, 0, NULL, NULL, '', 393, NULL, 9, 2),
(395, '2021-12-07 21:04:26.536576', '2021-12-07 21:05:03.152238', NULL, 'C-00244', NULL, 0, NULL, NULL, '', 394, NULL, 9, 2),
(396, '2021-12-07 21:04:26.991630', '2021-12-07 21:05:03.727371', NULL, 'C-00245', NULL, 0, NULL, NULL, '', 395, NULL, 9, 2),
(397, '2021-12-07 21:04:27.151701', '2021-12-07 21:05:04.331143', NULL, 'C-00246', NULL, 0, NULL, NULL, '', 396, NULL, 9, 2),
(398, '2021-12-07 21:04:27.293176', '2021-12-07 21:05:05.074302', NULL, 'C-00247', NULL, 0, NULL, NULL, '', 397, NULL, 9, 2),
(399, '2021-12-07 21:04:27.437132', '2021-12-07 21:05:05.826225', NULL, 'C-00248', NULL, 0, NULL, NULL, '', 398, NULL, 9, 2),
(400, '2021-12-07 21:04:27.502724', '2021-12-07 21:05:06.414669', NULL, 'C-00249', NULL, 0, NULL, NULL, '', 399, NULL, 9, 2),
(401, '2021-12-07 21:04:27.591954', '2021-12-07 21:05:07.020286', NULL, 'C-00250', NULL, 0, NULL, NULL, '', 400, NULL, 9, 2),
(402, '2021-12-16 07:57:07.339636', '2021-12-16 10:06:53.899807', NULL, 'C-00270', '2000.00', 1, '10000.00', '3600.00', '/media/avatar3_nNQfcxr.png', 401, 1, 9, 2),
(403, '2021-12-16 09:09:56.459706', '2021-12-16 09:10:42.112349', NULL, 'C-00271', '2000.00', 1, '10000.00', '3600.00', '', 402, 1, 9, 1),
(404, '2021-12-16 09:29:46.384079', '2021-12-16 09:29:46.384079', NULL, 'C-00272', '2000.00', 2, '20000.00', '3600.00', '/media/avatar_ugWZWXq.png', 403, 1, 9, 1),
(405, '2021-12-16 09:39:48.264501', '2021-12-16 09:41:06.175172', NULL, 'C-00273', '2000.00', 2, '20000.00', '3600.00', '', 404, 1, 9, 1),
(406, '2021-12-16 09:49:49.089608', '2021-12-16 09:49:49.089608', NULL, 'C-00274', '2000.00', 2, '20000.00', '3600.00', '/media/boxed-bg.jpg', 405, 1, 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `membership_request`
--

CREATE TABLE `membership_request` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `middle_name` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) NOT NULL,
  `certified_date` date DEFAULT NULL,
  `approval_comment` longtext DEFAULT NULL,
  `approved_date` date DEFAULT NULL,
  `file_no` varchar(255) DEFAULT NULL,
  `ippis_no` varchar(255) DEFAULT NULL,
  `year` varchar(255) DEFAULT NULL,
  `member_id` varchar(255) DEFAULT NULL,
  `approval_officer_id` int(11) DEFAULT NULL,
  `approval_status_id` int(11) NOT NULL,
  `certification_officer_id` int(11) DEFAULT NULL,
  `certification_status_id` int(11) NOT NULL,
  `department_id` int(11) DEFAULT NULL,
  `gender_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `salary_institution_id` int(11) DEFAULT NULL,
  `submission_status_id` int(11) NOT NULL,
  `title_id` int(11) DEFAULT NULL,
  `transaction_status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `membership_request`
--

INSERT INTO `membership_request` (`id`, `created_at`, `updated_at`, `first_name`, `last_name`, `middle_name`, `phone_number`, `certified_date`, `approval_comment`, `approved_date`, `file_no`, `ippis_no`, `year`, `member_id`, `approval_officer_id`, `approval_status_id`, `certification_officer_id`, `certification_status_id`, `department_id`, `gender_id`, `processed_by_id`, `salary_institution_id`, `submission_status_id`, `title_id`, `transaction_status_id`) VALUES
(1, '2021-12-07 19:57:33.846414', '2021-12-07 20:27:03.659500', 'BEN', 'IDAKA', 'MAUREEN', '08064004355', NULL, NULL, NULL, '00001', '00001', '2010', 'FETHAII/2010/00001', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(2, '2021-12-07 19:57:34.137983', '2021-12-07 20:27:03.885639', 'UCHENNA', 'OKOLI', 'OBIA', '08064004356', NULL, NULL, NULL, '00002', '00002', '2011', 'FETHAII/2011/00002', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(3, '2021-12-07 19:57:34.379531', '2021-12-07 20:27:04.067026', 'NKONYELU', 'OKONKWO', 'E', '08064004357', NULL, NULL, NULL, '00003', '00003', '2012', 'FETHAII/2012/00003', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(4, '2021-12-07 19:57:34.446613', '2021-12-07 20:27:04.203510', 'OPHELIA', 'AMADI', 'CHIB', '08064004358', NULL, NULL, NULL, '00004', '00004', '2013', 'FETHAII/2013/00004', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(5, '2021-12-07 19:57:34.538384', '2021-12-07 20:27:04.322692', 'IKWUO', 'NNACHI', 'IJEM', '08064004359', NULL, NULL, NULL, '00005', '00005', '2014', 'FETHAII/2014/00005', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(6, '2021-12-07 19:57:34.630163', '2021-12-07 20:27:04.435723', 'IFEOMA', 'AGBOWO', 'MARY', '08064004360', NULL, NULL, NULL, '00006', '00006', '2015', 'FETHAII/2015/00006', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(7, '2021-12-07 19:57:34.694113', '2021-12-07 20:27:04.533953', 'DR', 'NWANKWO', 'OKUTA J', '08064004361', NULL, NULL, NULL, '00007', '00007', '2016', 'FETHAII/2016/00007', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(8, '2021-12-07 19:57:34.759076', '2021-12-07 20:27:04.801688', 'EMMANUEL', 'ABAA', '', '08064004362', NULL, NULL, NULL, '00008', '00008', '2017', 'FETHAII/2017/00008', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(9, '2021-12-07 19:57:34.904000', '2021-12-07 20:27:04.956990', 'UGO', 'ABAGHA', 'AGNES', '08064004363', NULL, NULL, NULL, '00009', '00009', '2018', 'FETHAII/2018/00009', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(10, '2021-12-07 19:57:34.996893', '2021-12-07 20:27:05.125096', 'CHIGOZI', 'ABAGHAUGWU', '', '08064004364', NULL, NULL, NULL, '00010', '00010', '2019', 'FETHAII/2019/00010', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(11, '2021-12-07 19:57:35.060923', '2021-12-07 20:27:05.292208', 'NWACHINAME', 'ABANIFI', '', '08064004365', NULL, NULL, NULL, '00011', '00011', '2020', 'FETHAII/2020/00011', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(12, '2021-12-07 19:57:35.193841', '2021-12-07 20:27:05.401753', 'NNENWAOGO', 'ABARA', 'P', '08064004366', NULL, NULL, NULL, '00012', '00012', '2021', 'FETHAII/2021/00012', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(13, '2021-12-07 19:57:35.315766', '2021-12-07 20:27:05.468998', 'LAWRENCE', 'ABARA', 'CHI', '08064004367', NULL, NULL, NULL, '00013', '00013', '2010', 'FETHAII/2010/00013', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(14, '2021-12-07 19:57:35.382478', '2021-12-07 20:27:05.603905', 'NWAKAEGO', 'ABARA', 'EUC', '08064004368', NULL, NULL, NULL, '00014', '00014', '2011', 'FETHAII/2011/00014', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(15, '2021-12-07 19:57:35.449137', '2021-12-07 20:27:05.725791', 'OBASI', 'ABBA', 'DORCAS', '08064004369', NULL, NULL, NULL, '00015', '00015', '2012', 'FETHAII/2012/00015', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(16, '2021-12-07 19:57:35.529676', '2021-12-07 20:27:06.113967', 'EFFIONG', 'ABIA', 'ANIET', '08064004370', NULL, NULL, NULL, '00016', '00016', '2013', 'FETHAII/2013/00016', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(17, '2021-12-07 19:57:35.608744', '2021-12-07 20:27:06.358179', 'NKIRUKA', 'ABIA', 'NDON', '08064004371', NULL, NULL, NULL, '00017', '00017', '2014', 'FETHAII/2014/00017', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(18, '2021-12-07 19:57:35.677422', '2021-12-07 20:27:06.447175', 'DR', 'ABIA', 'EFFIONG NDO', '08064004372', NULL, NULL, NULL, '00018', '00018', '2015', 'FETHAII/2015/00018', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(19, '2021-12-07 19:57:35.772449', '2021-12-07 20:27:06.615048', 'UGOCHI', 'ABII', 'GLORIA', '08064004373', NULL, NULL, NULL, '00019', '00019', '2016', 'FETHAII/2016/00019', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(20, '2021-12-07 19:57:35.843152', '2021-12-07 20:27:06.702353', 'ABEKE', 'ABIOLA', 'ZULAY', '08064004374', NULL, NULL, NULL, '00020', '00020', '2017', 'FETHAII/2017/00020', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(21, '2021-12-07 19:57:36.103844', '2021-12-07 20:27:06.833835', 'CHIOMA', 'ABIRI', 'CLARA', '08064004375', NULL, NULL, NULL, '00021', '00021', '2018', 'FETHAII/2018/00021', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(22, '2021-12-07 19:57:36.207117', '2021-12-07 20:27:06.901040', 'OLADELE', 'ABOKEDE', 'AD', '08064004376', NULL, NULL, NULL, '00022', '00022', '2019', 'FETHAII/2019/00022', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(23, '2021-12-07 19:57:36.279072', '2021-12-07 20:27:07.024960', 'OMOLARA', 'ABOKEDE', 'AD', '08064004377', NULL, NULL, NULL, '00023', '00023', '2020', 'FETHAII/2020/00023', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(24, '2021-12-07 19:57:36.361022', '2021-12-07 20:27:07.202667', 'LEONARD', 'ABOR', '', '08064004378', NULL, NULL, NULL, '00024', '00024', '2021', 'FETHAII/2021/00024', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(25, '2021-12-07 19:57:36.437675', '2021-12-07 20:27:07.403816', 'MOMOH', 'ABU', 'AUGUSTIN', '08064004379', NULL, NULL, NULL, '00025', '00025', '2010', 'FETHAII/2010/00025', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(26, '2021-12-07 19:57:36.515679', '2021-12-07 20:27:07.559715', 'MMADUABUCHI', 'ABUWA', '', '08064004380', NULL, NULL, NULL, '00026', '00026', '2011', 'FETHAII/2011/00026', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(27, '2021-12-07 19:57:36.607604', '2021-12-07 20:27:07.682301', 'MAXWELL', 'ACHI', 'NGWU', '08064004381', NULL, NULL, NULL, '00027', '00027', '2012', 'FETHAII/2012/00027', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(28, '2021-12-07 19:57:36.673848', '2021-12-07 20:27:07.767368', 'EZEKIEL', 'ACHONWA', 'UC', '08064004382', NULL, NULL, NULL, '00028', '00028', '2013', 'FETHAII/2013/00028', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(29, '2021-12-07 19:57:36.738381', '2021-12-07 20:27:07.858135', 'UDOCHRIS', 'ACHUGONYE', '', '08064004383', NULL, NULL, NULL, '00029', '00029', '2014', 'FETHAII/2014/00029', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(30, '2021-12-07 19:57:36.804928', '2021-12-07 20:27:07.935553', 'MATTHEW', 'ADAMA', 'SIMO', '08064004384', NULL, NULL, NULL, '00030', '00030', '2015', 'FETHAII/2015/00030', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(31, '2021-12-07 19:57:36.871569', '2021-12-07 20:27:08.001450', 'BEATRI', 'ADAMSOKORIE', '', '08064004385', NULL, NULL, NULL, '00031', '00031', '2016', 'FETHAII/2016/00031', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(32, '2021-12-07 19:57:36.974430', '2021-12-07 20:27:08.079870', 'IFEOMA', 'ADANI', 'MODES', '08064004386', NULL, NULL, NULL, '00032', '00032', '2017', 'FETHAII/2017/00032', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(33, '2021-12-07 19:57:37.083701', '2021-12-07 20:27:08.178806', 'IBUKUN', 'ADEOLU', 'NGOZ', '08064004387', NULL, NULL, NULL, '00033', '00033', '2018', 'FETHAII/2018/00033', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(34, '2021-12-07 19:57:37.248598', '2021-12-07 20:27:08.894797', 'KUSS', 'ADEOYE', 'JULIAN', '08064004388', NULL, NULL, NULL, '00034', '00034', '2019', 'FETHAII/2019/00034', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(35, '2021-12-07 19:57:37.315166', '2021-12-07 20:27:09.002052', 'SAMSON', 'ADEYEMI', 'OLU', '08064004389', NULL, NULL, NULL, '00035', '00035', '2020', 'FETHAII/2020/00035', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(36, '2021-12-07 19:57:37.387916', '2021-12-07 20:27:09.105325', 'EMMANUEL', 'ADIDU', 'AME', '08064004390', NULL, NULL, NULL, '00036', '00036', '2021', 'FETHAII/2021/00036', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(37, '2021-12-07 19:57:37.471860', '2021-12-07 20:27:09.245587', 'NWANYIEZE', 'ADIELE', 'N', '08064004391', NULL, NULL, NULL, '00037', '00037', '2010', 'FETHAII/2010/00037', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(38, '2021-12-07 19:57:37.538819', '2021-12-07 20:27:09.378192', 'EMMANUEL', 'ADIGWE', 'IF', '08064004392', NULL, NULL, NULL, '00038', '00038', '2011', 'FETHAII/2011/00038', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(39, '2021-12-07 19:57:37.605068', '2021-12-07 20:27:09.523605', 'JULIANA', 'ADIKWU', 'NGO', '08064004393', NULL, NULL, NULL, '00039', '00039', '2012', 'FETHAII/2012/00039', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(40, '2021-12-07 19:57:37.673787', '2021-12-07 20:27:09.622866', 'CAROLINE', 'ADIMORAH', '', '08064004394', NULL, NULL, NULL, '00040', '00040', '2013', 'FETHAII/2013/00040', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(41, '2021-12-07 19:57:37.740712', '2021-12-07 20:27:09.928073', 'ORAEKI', 'ADIMORAH', 'HA', '08064004395', NULL, NULL, NULL, '00041', '00041', '2014', 'FETHAII/2014/00041', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(42, '2021-12-07 19:57:37.828798', '2021-12-07 20:27:10.083366', 'IFEYINWA', 'ADOGU', '', '08064004396', NULL, NULL, NULL, '00042', '00042', '2015', 'FETHAII/2015/00042', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(43, '2021-12-07 19:57:37.895048', '2021-12-07 20:27:10.226920', 'OGHENEOCHUKO', 'ADOKA', '', '08064004397', NULL, NULL, NULL, '00043', '00043', '2016', 'FETHAII/2016/00043', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(44, '2021-12-07 19:57:37.973106', '2021-12-07 20:27:10.346806', 'NWOVA', 'ADOKE', 'JOHN', '08064004398', NULL, NULL, NULL, '00044', '00044', '2017', 'FETHAII/2017/00044', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(45, '2021-12-07 19:57:38.064159', '2021-12-07 20:27:10.434399', 'EDACHE', 'ADOKWU', 'ELDA', '08064004399', NULL, NULL, NULL, '00045', '00045', '2018', 'FETHAII/2018/00045', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(46, '2021-12-07 19:57:38.131406', '2021-12-07 20:27:10.501914', 'OBINNA', 'ADONU', 'BENJA', '08064004400', NULL, NULL, NULL, '00046', '00046', '2019', 'FETHAII/2019/00046', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(47, '2021-12-07 19:57:38.283257', '2021-12-07 20:27:10.615844', 'LINDA', 'ADUAKA', 'UKAMA', '08064004401', NULL, NULL, NULL, '00047', '00047', '2020', 'FETHAII/2020/00047', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(48, '2021-12-07 19:57:38.360206', '2021-12-07 20:27:10.678804', 'NGOZI', 'ADUAKA', 'ELIZA', '08064004402', NULL, NULL, NULL, '00048', '00048', '2021', 'FETHAII/2021/00048', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(49, '2021-12-07 19:57:38.427167', '2021-12-07 20:27:10.768622', 'VIVIAN', 'ADUAKA', 'ONYI', '08064004403', NULL, NULL, NULL, '00049', '00049', '2010', 'FETHAII/2010/00049', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(50, '2021-12-07 19:57:38.493562', '2021-12-07 20:27:11.357011', 'ADAGBA', 'ADUWA', 'PATRI', '08064004404', NULL, NULL, NULL, '00050', '00050', '2011', 'FETHAII/2011/00050', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(51, '2021-12-07 20:26:57.088927', '2021-12-07 20:27:11.669320', 'BEN', 'IDAKA', 'MAUREEN', '08064004355', NULL, NULL, NULL, '00001', '00001', '2010', 'FETHAII/2010/00001', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(52, '2021-12-07 20:26:57.373438', '2021-12-07 20:27:11.796891', 'UCHENNA', 'OKOLI', 'OBIA', '08064004356', NULL, NULL, NULL, '00002', '00002', '2011', 'FETHAII/2011/00002', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(53, '2021-12-07 20:26:57.762024', '2021-12-07 20:27:11.912773', 'NKONYELU', 'OKONKWO', 'E', '08064004357', NULL, NULL, NULL, '00003', '00003', '2012', 'FETHAII/2012/00003', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(54, '2021-12-07 20:26:57.840087', '2021-12-07 20:27:12.023401', 'OPHELIA', 'AMADI', 'CHIB', '08064004358', NULL, NULL, NULL, '00004', '00004', '2013', 'FETHAII/2013/00004', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(55, '2021-12-07 20:26:57.929956', '2021-12-07 20:27:12.113689', 'IKWUO', 'NNACHI', 'IJEM', '08064004359', NULL, NULL, NULL, '00005', '00005', '2014', 'FETHAII/2014/00005', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(56, '2021-12-07 20:26:58.005213', '2021-12-07 20:27:12.179896', 'IFEOMA', 'AGBOWO', 'MARY', '08064004360', NULL, NULL, NULL, '00006', '00006', '2015', 'FETHAII/2015/00006', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(57, '2021-12-07 20:26:58.079669', '2021-12-07 20:27:12.347869', 'DR', 'NWANKWO', 'OKUTA J', '08064004361', NULL, NULL, NULL, '00007', '00007', '2016', 'FETHAII/2016/00007', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(58, '2021-12-07 20:26:58.348231', '2021-12-07 20:27:12.584224', 'EMMANUEL', 'ABAA', '', '08064004362', NULL, NULL, NULL, '00008', '00008', '2017', 'FETHAII/2017/00008', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(59, '2021-12-07 20:26:58.597575', '2021-12-07 20:27:12.691084', 'UGO', 'ABAGHA', 'AGNES', '08064004363', NULL, NULL, NULL, '00009', '00009', '2018', 'FETHAII/2018/00009', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(60, '2021-12-07 20:26:58.825077', '2021-12-07 20:27:12.779136', 'CHIGOZI', 'ABAGHAUGWU', '', '08064004364', NULL, NULL, NULL, '00010', '00010', '2019', 'FETHAII/2019/00010', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(61, '2021-12-07 20:26:58.917969', '2021-12-07 20:27:13.071694', 'NWACHINAME', 'ABANIFI', '', '08064004365', NULL, NULL, NULL, '00011', '00011', '2020', 'FETHAII/2020/00011', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(62, '2021-12-07 20:26:58.995068', '2021-12-07 20:27:13.195422', 'NNENWAOGO', 'ABARA', 'P', '08064004366', NULL, NULL, NULL, '00012', '00012', '2021', 'FETHAII/2021/00012', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(63, '2021-12-07 20:26:59.073241', '2021-12-07 20:27:13.346202', 'LAWRENCE', 'ABARA', 'CHI', '08064004367', NULL, NULL, NULL, '00013', '00013', '2010', 'FETHAII/2010/00013', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(64, '2021-12-07 20:26:59.159161', '2021-12-07 20:27:13.434256', 'NWAKAEGO', 'ABARA', 'EUC', '08064004368', NULL, NULL, NULL, '00014', '00014', '2011', 'FETHAII/2011/00014', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(65, '2021-12-07 20:26:59.237255', '2021-12-07 20:27:13.617695', 'OBASI', 'ABBA', 'DORCAS', '08064004369', NULL, NULL, NULL, '00015', '00015', '2012', 'FETHAII/2012/00015', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(66, '2021-12-07 20:26:59.308194', '2021-12-07 20:27:14.183096', 'EFFIONG', 'ABIA', 'ANIET', '08064004370', NULL, NULL, NULL, '00016', '00016', '2013', 'FETHAII/2013/00016', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(67, '2021-12-07 20:26:59.381157', '2021-12-07 20:27:14.368354', 'NKIRUKA', 'ABIA', 'NDON', '08064004371', NULL, NULL, NULL, '00017', '00017', '2014', 'FETHAII/2014/00017', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(68, '2021-12-07 20:26:59.462767', '2021-12-07 20:27:14.445618', 'DR', 'ABIA', 'EFFIONG NDO', '08064004372', NULL, NULL, NULL, '00018', '00018', '2015', 'FETHAII/2015/00018', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(69, '2021-12-07 20:26:59.516214', '2021-12-07 20:27:14.513893', 'UGOCHI', 'ABII', 'GLORIA', '08064004373', NULL, NULL, NULL, '00019', '00019', '2016', 'FETHAII/2016/00019', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(70, '2021-12-07 20:26:59.570898', '2021-12-07 20:27:14.579006', 'ABEKE', 'ABIOLA', 'ZULAY', '08064004374', NULL, NULL, NULL, '00020', '00020', '2017', 'FETHAII/2017/00020', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(71, '2021-12-07 20:27:00.331045', '2021-12-07 20:27:14.646251', 'CHIOMA', 'ABIRI', 'CLARA', '08064004375', NULL, NULL, NULL, '00021', '00021', '2018', 'FETHAII/2018/00021', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(72, '2021-12-07 20:27:00.507072', '2021-12-07 20:27:14.712351', 'OLADELE', 'ABOKEDE', 'AD', '08064004376', NULL, NULL, NULL, '00022', '00022', '2019', 'FETHAII/2019/00022', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(73, '2021-12-07 20:27:00.550674', '2021-12-07 20:27:15.183378', 'OMOLARA', 'ABOKEDE', 'AD', '08064004377', NULL, NULL, NULL, '00023', '00023', '2020', 'FETHAII/2020/00023', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(74, '2021-12-07 20:27:00.717092', '2021-12-07 20:27:15.338857', 'LEONARD', 'ABOR', '', '08064004378', NULL, NULL, NULL, '00024', '00024', '2021', 'FETHAII/2021/00024', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(75, '2021-12-07 20:27:00.805656', '2021-12-07 20:27:15.456538', 'MOMOH', 'ABU', 'AUGUSTIN', '08064004379', NULL, NULL, NULL, '00025', '00025', '2010', 'FETHAII/2010/00025', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(76, '2021-12-07 20:27:00.872880', '2021-12-07 20:27:15.568279', 'MMADUABUCHI', 'ABUWA', '', '08064004380', NULL, NULL, NULL, '00026', '00026', '2011', 'FETHAII/2011/00026', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(77, '2021-12-07 20:27:00.948580', '2021-12-07 20:27:15.656628', 'MAXWELL', 'ACHI', 'NGWU', '08064004381', NULL, NULL, NULL, '00027', '00027', '2012', 'FETHAII/2012/00027', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(78, '2021-12-07 20:27:00.991548', '2021-12-07 20:27:15.723854', 'EZEKIEL', 'ACHONWA', 'UC', '08064004382', NULL, NULL, NULL, '00028', '00028', '2013', 'FETHAII/2013/00028', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(79, '2021-12-07 20:27:01.058509', '2021-12-07 20:27:15.813548', 'UDOCHRIS', 'ACHUGONYE', '', '08064004383', NULL, NULL, NULL, '00029', '00029', '2014', 'FETHAII/2014/00029', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(80, '2021-12-07 20:27:01.192822', '2021-12-07 20:27:15.923328', 'MATTHEW', 'ADAMA', 'SIMO', '08064004384', NULL, NULL, NULL, '00030', '00030', '2015', 'FETHAII/2015/00030', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(81, '2021-12-07 20:27:01.281698', '2021-12-07 20:27:16.073217', 'BEATRI', 'ADAMSOKORIE', '', '08064004385', NULL, NULL, NULL, '00031', '00031', '2016', 'FETHAII/2016/00031', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(82, '2021-12-07 20:27:01.427673', '2021-12-07 20:27:17.135204', 'IFEOMA', 'ADANI', 'MODES', '08064004386', NULL, NULL, NULL, '00032', '00032', '2017', 'FETHAII/2017/00032', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(83, '2021-12-07 20:27:01.526546', '2021-12-07 20:27:17.547491', 'IBUKUN', 'ADEOLU', 'NGOZ', '08064004387', NULL, NULL, NULL, '00033', '00033', '2018', 'FETHAII/2018/00033', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(84, '2021-12-07 20:27:01.581971', '2021-12-07 20:27:17.797744', 'KUSS', 'ADEOYE', 'JULIAN', '08064004388', NULL, NULL, NULL, '00034', '00034', '2019', 'FETHAII/2019/00034', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(85, '2021-12-07 20:27:01.762887', '2021-12-07 20:27:18.073558', 'SAMSON', 'ADEYEMI', 'OLU', '08064004389', NULL, NULL, NULL, '00035', '00035', '2020', 'FETHAII/2020/00035', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(86, '2021-12-07 20:27:01.850934', '2021-12-07 20:27:18.255555', 'EMMANUEL', 'ADIDU', 'AME', '08064004390', NULL, NULL, NULL, '00036', '00036', '2021', 'FETHAII/2021/00036', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(87, '2021-12-07 20:27:01.938004', '2021-12-07 20:27:18.606583', 'NWANYIEZE', 'ADIELE', 'N', '08064004391', NULL, NULL, NULL, '00037', '00037', '2010', 'FETHAII/2010/00037', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(88, '2021-12-07 20:27:01.994587', '2021-12-07 20:27:18.792506', 'EMMANUEL', 'ADIGWE', 'IF', '08064004392', NULL, NULL, NULL, '00038', '00038', '2011', 'FETHAII/2011/00038', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(89, '2021-12-07 20:27:02.071477', '2021-12-07 20:27:18.925110', 'JULIANA', 'ADIKWU', 'NGO', '08064004393', NULL, NULL, NULL, '00039', '00039', '2012', 'FETHAII/2012/00039', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(90, '2021-12-07 20:27:02.125707', '2021-12-07 20:27:19.194926', 'CAROLINE', 'ADIMORAH', '', '08064004394', NULL, NULL, NULL, '00040', '00040', '2013', 'FETHAII/2013/00040', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(91, '2021-12-07 20:27:02.202663', '2021-12-07 20:27:19.317203', 'ORAEKI', 'ADIMORAH', 'HA', '08064004395', NULL, NULL, NULL, '00041', '00041', '2014', 'FETHAII/2014/00041', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(92, '2021-12-07 20:27:02.248632', '2021-12-07 20:27:19.380547', 'IFEYINWA', 'ADOGU', '', '08064004396', NULL, NULL, NULL, '00042', '00042', '2015', 'FETHAII/2015/00042', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(93, '2021-12-07 20:27:02.302603', '2021-12-07 20:27:19.691339', 'OGHENEOCHUKO', 'ADOKA', '', '08064004397', NULL, NULL, NULL, '00043', '00043', '2016', 'FETHAII/2016/00043', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(94, '2021-12-07 20:27:02.531645', '2021-12-07 20:27:19.757743', 'NWOVA', 'ADOKE', 'JOHN', '08064004398', NULL, NULL, NULL, '00044', '00044', '2017', 'FETHAII/2017/00044', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(95, '2021-12-07 20:27:02.604130', '2021-12-07 20:27:19.835795', 'EDACHE', 'ADOKWU', 'ELDA', '08064004399', NULL, NULL, NULL, '00045', '00045', '2018', 'FETHAII/2018/00045', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(96, '2021-12-07 20:27:02.681918', '2021-12-07 20:27:19.901438', 'OBINNA', 'ADONU', 'BENJA', '08064004400', NULL, NULL, NULL, '00046', '00046', '2019', 'FETHAII/2019/00046', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(97, '2021-12-07 20:27:02.873416', '2021-12-07 20:27:19.968760', 'LINDA', 'ADUAKA', 'UKAMA', '08064004401', NULL, NULL, NULL, '00047', '00047', '2020', 'FETHAII/2020/00047', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(98, '2021-12-07 20:27:02.961471', '2021-12-07 20:27:20.235260', 'NGOZI', 'ADUAKA', 'ELIZA', '08064004402', NULL, NULL, NULL, '00048', '00048', '2021', 'FETHAII/2021/00048', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(99, '2021-12-07 20:27:03.041545', '2021-12-07 20:27:20.314405', 'VIVIAN', 'ADUAKA', 'ONYI', '08064004403', NULL, NULL, NULL, '00049', '00049', '2010', 'FETHAII/2010/00049', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(100, '2021-12-07 20:27:03.141160', '2021-12-07 20:27:20.412705', 'ADAGBA', 'ADUWA', 'PATRI', '08064004404', NULL, NULL, NULL, '00050', '00050', '2011', 'FETHAII/2011/00050', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(101, '2021-12-07 20:35:58.255734', '2021-12-07 20:36:04.691508', 'BEN', 'IDAKA', 'MAUREEN', '08064004355', NULL, NULL, NULL, '00001', '00001', '2010', 'FETHAII/2010/00001', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(102, '2021-12-07 20:35:58.510585', '2021-12-07 20:36:04.874431', 'UCHENNA', 'OKOLI', 'OBIA', '08064004356', NULL, NULL, NULL, '00002', '00002', '2011', 'FETHAII/2011/00002', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(103, '2021-12-07 20:35:58.614523', '2021-12-07 20:36:05.014049', 'NKONYELU', 'OKONKWO', 'E', '08064004357', NULL, NULL, NULL, '00003', '00003', '2012', 'FETHAII/2012/00003', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(104, '2021-12-07 20:35:58.697471', '2021-12-07 20:36:05.244233', 'OPHELIA', 'AMADI', 'CHIB', '08064004358', NULL, NULL, NULL, '00004', '00004', '2013', 'FETHAII/2013/00004', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(105, '2021-12-07 20:35:58.781438', '2021-12-07 20:36:05.509186', 'IKWUO', 'NNACHI', 'IJEM', '08064004359', NULL, NULL, NULL, '00005', '00005', '2014', 'FETHAII/2014/00005', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(106, '2021-12-07 20:35:58.876056', '2021-12-07 20:36:05.741128', 'IFEOMA', 'AGBOWO', 'MARY', '08064004360', NULL, NULL, NULL, '00006', '00006', '2015', 'FETHAII/2015/00006', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(107, '2021-12-07 20:35:58.996684', '2021-12-07 20:36:05.852004', 'DR', 'NWANKWO', 'OKUTA J', '08064004361', NULL, NULL, NULL, '00007', '00007', '2016', 'FETHAII/2016/00007', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(108, '2021-12-07 20:35:59.065566', '2021-12-07 20:36:05.975009', 'EMMANUEL', 'ABAA', '', '08064004362', NULL, NULL, NULL, '00008', '00008', '2017', 'FETHAII/2017/00008', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(109, '2021-12-07 20:35:59.210102', '2021-12-07 20:36:06.096526', 'UGO', 'ABAGHA', 'AGNES', '08064004363', NULL, NULL, NULL, '00009', '00009', '2018', 'FETHAII/2018/00009', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(110, '2021-12-07 20:35:59.310964', '2021-12-07 20:36:06.197248', 'CHIGOZI', 'ABAGHAUGWU', '', '08064004364', NULL, NULL, NULL, '00010', '00010', '2019', 'FETHAII/2019/00010', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(111, '2021-12-07 20:35:59.416360', '2021-12-07 20:36:06.297693', 'NWACHINAME', 'ABANIFI', '', '08064004365', NULL, NULL, NULL, '00011', '00011', '2020', 'FETHAII/2020/00011', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(112, '2021-12-07 20:35:59.499068', '2021-12-07 20:36:06.475485', 'NNENWAOGO', 'ABARA', 'P', '08064004366', NULL, NULL, NULL, '00012', '00012', '2021', 'FETHAII/2021/00012', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(113, '2021-12-07 20:35:59.566129', '2021-12-07 20:36:06.608979', 'LAWRENCE', 'ABARA', 'CHI', '08064004367', NULL, NULL, NULL, '00013', '00013', '2010', 'FETHAII/2010/00013', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(114, '2021-12-07 20:35:59.654881', '2021-12-07 20:36:07.042017', 'NWAKAEGO', 'ABARA', 'EUC', '08064004368', NULL, NULL, NULL, '00014', '00014', '2011', 'FETHAII/2011/00014', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(115, '2021-12-07 20:35:59.765536', '2021-12-07 20:36:07.154041', 'OBASI', 'ABBA', 'DORCAS', '08064004369', NULL, NULL, NULL, '00015', '00015', '2012', 'FETHAII/2012/00015', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(116, '2021-12-07 20:35:59.859478', '2021-12-07 20:36:07.320043', 'EFFIONG', 'ABIA', 'ANIET', '08064004370', NULL, NULL, NULL, '00016', '00016', '2013', 'FETHAII/2013/00016', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(117, '2021-12-07 20:35:59.965595', '2021-12-07 20:36:07.632451', 'NKIRUKA', 'ABIA', 'NDON', '08064004371', NULL, NULL, NULL, '00017', '00017', '2014', 'FETHAII/2014/00017', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(118, '2021-12-07 20:36:00.072465', '2021-12-07 20:36:07.841997', 'DR', 'ABIA', 'EFFIONG NDO', '08064004372', NULL, NULL, NULL, '00018', '00018', '2015', 'FETHAII/2015/00018', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(119, '2021-12-07 20:36:00.236887', '2021-12-07 20:36:07.963726', 'UGOCHI', 'ABII', 'GLORIA', '08064004373', NULL, NULL, NULL, '00019', '00019', '2016', 'FETHAII/2016/00019', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(120, '2021-12-07 20:36:00.337090', '2021-12-07 20:36:08.086714', 'ABEKE', 'ABIOLA', 'ZULAY', '08064004374', NULL, NULL, NULL, '00020', '00020', '2017', 'FETHAII/2017/00020', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(121, '2021-12-07 20:36:00.512550', '2021-12-07 20:36:08.185647', 'CHIOMA', 'ABIRI', 'CLARA', '08064004375', NULL, NULL, NULL, '00021', '00021', '2018', 'FETHAII/2018/00021', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(122, '2021-12-07 20:36:00.608762', '2021-12-07 20:36:08.297603', 'OLADELE', 'ABOKEDE', 'AD', '08064004376', NULL, NULL, NULL, '00022', '00022', '2019', 'FETHAII/2019/00022', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(123, '2021-12-07 20:36:00.734131', '2021-12-07 20:36:08.397200', 'OMOLARA', 'ABOKEDE', 'AD', '08064004377', NULL, NULL, NULL, '00023', '00023', '2020', 'FETHAII/2020/00023', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(124, '2021-12-07 20:36:00.799289', '2021-12-07 20:36:08.503627', 'LEONARD', 'ABOR', '', '08064004378', NULL, NULL, NULL, '00024', '00024', '2021', 'FETHAII/2021/00024', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(125, '2021-12-07 20:36:00.866023', '2021-12-07 20:36:09.131642', 'MOMOH', 'ABU', 'AUGUSTIN', '08064004379', NULL, NULL, NULL, '00025', '00025', '2010', 'FETHAII/2010/00025', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(126, '2021-12-07 20:36:00.953461', '2021-12-07 20:36:09.296752', 'MMADUABUCHI', 'ABUWA', '', '08064004380', NULL, NULL, NULL, '00026', '00026', '2011', 'FETHAII/2011/00026', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(127, '2021-12-07 20:36:01.043403', '2021-12-07 20:36:09.419676', 'MAXWELL', 'ACHI', 'NGWU', '08064004381', NULL, NULL, NULL, '00027', '00027', '2012', 'FETHAII/2012/00027', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(128, '2021-12-07 20:36:01.108750', '2021-12-07 20:36:09.520464', 'EZEKIEL', 'ACHONWA', 'UC', '08064004382', NULL, NULL, NULL, '00028', '00028', '2013', 'FETHAII/2013/00028', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(129, '2021-12-07 20:36:01.181002', '2021-12-07 20:36:09.648778', 'UDOCHRIS', 'ACHUGONYE', '', '08064004383', NULL, NULL, NULL, '00029', '00029', '2014', 'FETHAII/2014/00029', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(130, '2021-12-07 20:36:01.357003', '2021-12-07 20:36:09.827106', 'MATTHEW', 'ADAMA', 'SIMO', '08064004384', NULL, NULL, NULL, '00030', '00030', '2015', 'FETHAII/2015/00030', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(131, '2021-12-07 20:36:01.489956', '2021-12-07 20:36:10.252978', 'BEATRI', 'ADAMSOKORIE', '', '08064004385', NULL, NULL, NULL, '00031', '00031', '2016', 'FETHAII/2016/00031', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(132, '2021-12-07 20:36:01.568653', '2021-12-07 20:36:10.397483', 'IFEOMA', 'ADANI', 'MODES', '08064004386', NULL, NULL, NULL, '00032', '00032', '2017', 'FETHAII/2017/00032', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(133, '2021-12-07 20:36:01.662712', '2021-12-07 20:36:10.518653', 'IBUKUN', 'ADEOLU', 'NGOZ', '08064004387', NULL, NULL, NULL, '00033', '00033', '2018', 'FETHAII/2018/00033', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(134, '2021-12-07 20:36:01.754533', '2021-12-07 20:36:10.619592', 'KUSS', 'ADEOYE', 'JULIAN', '08064004388', NULL, NULL, NULL, '00034', '00034', '2019', 'FETHAII/2019/00034', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(135, '2021-12-07 20:36:01.821254', '2021-12-07 20:36:10.730297', 'SAMSON', 'ADEYEMI', 'OLU', '08064004389', NULL, NULL, NULL, '00035', '00035', '2020', 'FETHAII/2020/00035', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(136, '2021-12-07 20:36:01.892077', '2021-12-07 20:36:10.842369', 'EMMANUEL', 'ADIDU', 'AME', '08064004390', NULL, NULL, NULL, '00036', '00036', '2021', 'FETHAII/2021/00036', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(137, '2021-12-07 20:36:01.955252', '2021-12-07 20:36:11.054205', 'NWANYIEZE', 'ADIELE', 'N', '08064004391', NULL, NULL, NULL, '00037', '00037', '2010', 'FETHAII/2010/00037', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(138, '2021-12-07 20:36:02.046766', '2021-12-07 20:36:11.285959', 'EMMANUEL', 'ADIGWE', 'IF', '08064004392', NULL, NULL, NULL, '00038', '00038', '2011', 'FETHAII/2011/00038', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(139, '2021-12-07 20:36:02.132799', '2021-12-07 20:36:11.398132', 'JULIANA', 'ADIKWU', 'NGO', '08064004393', NULL, NULL, NULL, '00039', '00039', '2012', 'FETHAII/2012/00039', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(140, '2021-12-07 20:36:02.226741', '2021-12-07 20:36:11.552743', 'CAROLINE', 'ADIMORAH', '', '08064004394', NULL, NULL, NULL, '00040', '00040', '2013', 'FETHAII/2013/00040', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(141, '2021-12-07 20:36:02.811612', '2021-12-07 20:36:11.675466', 'ORAEKI', 'ADIMORAH', 'HA', '08064004395', NULL, NULL, NULL, '00041', '00041', '2014', 'FETHAII/2014/00041', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(142, '2021-12-07 20:36:03.208935', '2021-12-07 20:36:11.786393', 'IFEYINWA', 'ADOGU', '', '08064004396', NULL, NULL, NULL, '00042', '00042', '2015', 'FETHAII/2015/00042', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(143, '2021-12-07 20:36:03.471260', '2021-12-07 20:36:11.886654', 'OGHENEOCHUKO', 'ADOKA', '', '08064004397', NULL, NULL, NULL, '00043', '00043', '2016', 'FETHAII/2016/00043', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(144, '2021-12-07 20:36:03.600789', '2021-12-07 20:36:12.008383', 'NWOVA', 'ADOKE', 'JOHN', '08064004398', NULL, NULL, NULL, '00044', '00044', '2017', 'FETHAII/2017/00044', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(145, '2021-12-07 20:36:03.706609', '2021-12-07 20:36:12.436300', 'EDACHE', 'ADOKWU', 'ELDA', '08064004399', NULL, NULL, NULL, '00045', '00045', '2018', 'FETHAII/2018/00045', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(146, '2021-12-07 20:36:03.800524', '2021-12-07 20:36:12.651215', 'OBINNA', 'ADONU', 'BENJA', '08064004400', NULL, NULL, NULL, '00046', '00046', '2019', 'FETHAII/2019/00046', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(147, '2021-12-07 20:36:03.914095', '2021-12-07 20:36:12.942873', 'LINDA', 'ADUAKA', 'UKAMA', '08064004401', NULL, NULL, NULL, '00047', '00047', '2020', 'FETHAII/2020/00047', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(148, '2021-12-07 20:36:03.991461', '2021-12-07 20:36:13.106089', 'NGOZI', 'ADUAKA', 'ELIZA', '08064004402', NULL, NULL, NULL, '00048', '00048', '2021', 'FETHAII/2021/00048', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(149, '2021-12-07 20:36:04.209989', '2021-12-07 20:36:13.333171', 'VIVIAN', 'ADUAKA', 'ONYI', '08064004403', NULL, NULL, NULL, '00049', '00049', '2010', 'FETHAII/2010/00049', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(150, '2021-12-07 20:36:04.276276', '2021-12-07 20:36:14.060168', 'ADAGBA', 'ADUWA', 'PATRI', '08064004404', NULL, NULL, NULL, '00050', '00050', '2011', 'FETHAII/2011/00050', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(151, '2021-12-07 20:41:48.166900', '2021-12-07 20:45:14.557595', 'BEN', 'IDAKA', 'MAUREEN', '08064004355', NULL, NULL, NULL, '00001', '00001', '2010', 'FETHAII/2010/00001', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(152, '2021-12-07 20:41:48.379785', '2021-12-07 20:45:14.746042', 'UCHENNA', 'OKOLI', 'OBIA', '08064004356', NULL, NULL, NULL, '00002', '00002', '2011', 'FETHAII/2011/00002', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(153, '2021-12-07 20:41:48.476448', '2021-12-07 20:45:15.353005', 'NKONYELU', 'OKONKWO', 'E', '08064004357', NULL, NULL, NULL, '00003', '00003', '2012', 'FETHAII/2012/00003', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(154, '2021-12-07 20:41:48.549343', '2021-12-07 20:45:15.568816', 'OPHELIA', 'AMADI', 'CHIB', '08064004358', NULL, NULL, NULL, '00004', '00004', '2013', 'FETHAII/2013/00004', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(155, '2021-12-07 20:41:48.638401', '2021-12-07 20:45:15.739802', 'IKWUO', 'NNACHI', 'IJEM', '08064004359', NULL, NULL, NULL, '00005', '00005', '2014', 'FETHAII/2014/00005', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(156, '2021-12-07 20:41:48.894479', '2021-12-07 20:45:15.859936', 'IFEOMA', 'AGBOWO', 'MARY', '08064004360', NULL, NULL, NULL, '00006', '00006', '2015', 'FETHAII/2015/00006', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(157, '2021-12-07 20:41:49.083071', '2021-12-07 20:45:15.972641', 'DR', 'NWANKWO', 'OKUTA J', '08064004361', NULL, NULL, NULL, '00007', '00007', '2016', 'FETHAII/2016/00007', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(158, '2021-12-07 20:41:49.234119', '2021-12-07 20:45:16.161168', 'EMMANUEL', 'ABAA', '', '08064004362', NULL, NULL, NULL, '00008', '00008', '2017', 'FETHAII/2017/00008', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(159, '2021-12-07 20:41:49.339907', '2021-12-07 20:45:16.417331', 'UGO', 'ABAGHA', 'AGNES', '08064004363', NULL, NULL, NULL, '00009', '00009', '2018', 'FETHAII/2018/00009', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(160, '2021-12-07 20:41:49.482656', '2021-12-07 20:45:16.658612', 'CHIGOZI', 'ABAGHAUGWU', '', '08064004364', NULL, NULL, NULL, '00010', '00010', '2019', 'FETHAII/2019/00010', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(161, '2021-12-07 20:41:49.593823', '2021-12-07 20:45:16.816376', 'NWACHINAME', 'ABANIFI', '', '08064004365', NULL, NULL, NULL, '00011', '00011', '2020', 'FETHAII/2020/00011', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(162, '2021-12-07 20:41:49.697504', '2021-12-07 20:45:16.950291', 'NNENWAOGO', 'ABARA', 'P', '08064004366', NULL, NULL, NULL, '00012', '00012', '2021', 'FETHAII/2021/00012', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(163, '2021-12-07 20:41:49.821108', '2021-12-07 20:45:17.061406', 'LAWRENCE', 'ABARA', 'CHI', '08064004367', NULL, NULL, NULL, '00013', '00013', '2010', 'FETHAII/2010/00013', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(164, '2021-12-07 20:41:49.974802', '2021-12-07 20:45:17.284362', 'NWAKAEGO', 'ABARA', 'EUC', '08064004368', NULL, NULL, NULL, '00014', '00014', '2011', 'FETHAII/2011/00014', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(165, '2021-12-07 20:41:50.137750', '2021-12-07 20:45:17.597105', 'OBASI', 'ABBA', 'DORCAS', '08064004369', NULL, NULL, NULL, '00015', '00015', '2012', 'FETHAII/2012/00015', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(166, '2021-12-07 20:41:50.205711', '2021-12-07 20:45:17.717491', 'EFFIONG', 'ABIA', 'ANIET', '08064004370', NULL, NULL, NULL, '00016', '00016', '2013', 'FETHAII/2013/00016', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(167, '2021-12-07 20:41:50.269671', '2021-12-07 20:45:17.894364', 'NKIRUKA', 'ABIA', 'NDON', '08064004371', NULL, NULL, NULL, '00017', '00017', '2014', 'FETHAII/2014/00017', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(168, '2021-12-07 20:41:50.335732', '2021-12-07 20:45:18.015915', 'DR', 'ABIA', 'EFFIONG NDO', '08064004372', NULL, NULL, NULL, '00018', '00018', '2015', 'FETHAII/2015/00018', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(169, '2021-12-07 20:41:50.380424', '2021-12-07 20:45:18.161687', 'UGOCHI', 'ABII', 'GLORIA', '08064004373', NULL, NULL, NULL, '00019', '00019', '2016', 'FETHAII/2016/00019', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(170, '2021-12-07 20:41:50.425864', '2021-12-07 20:45:18.279363', 'ABEKE', 'ABIOLA', 'ZULAY', '08064004374', NULL, NULL, NULL, '00020', '00020', '2017', 'FETHAII/2017/00020', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(171, '2021-12-07 20:41:50.469789', '2021-12-07 20:45:18.406093', 'CHIOMA', 'ABIRI', 'CLARA', '08064004375', NULL, NULL, NULL, '00021', '00021', '2018', 'FETHAII/2018/00021', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(172, '2021-12-07 20:41:50.514761', '2021-12-07 20:45:18.523751', 'OLADELE', 'ABOKEDE', 'AD', '08064004376', NULL, NULL, NULL, '00022', '00022', '2019', 'FETHAII/2019/00022', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(173, '2021-12-07 20:41:50.605705', '2021-12-07 20:45:18.634906', 'OMOLARA', 'ABOKEDE', 'AD', '08064004377', NULL, NULL, NULL, '00023', '00023', '2020', 'FETHAII/2020/00023', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(174, '2021-12-07 20:41:50.646668', '2021-12-07 20:45:18.835345', 'LEONARD', 'ABOR', '', '08064004378', NULL, NULL, NULL, '00024', '00024', '2021', 'FETHAII/2021/00024', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(175, '2021-12-07 20:41:50.716487', '2021-12-07 20:45:18.979966', 'MOMOH', 'ABU', 'AUGUSTIN', '08064004379', NULL, NULL, NULL, '00025', '00025', '2010', 'FETHAII/2010/00025', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(176, '2021-12-07 20:41:50.816838', '2021-12-07 20:45:19.127336', 'MMADUABUCHI', 'ABUWA', '', '08064004380', NULL, NULL, NULL, '00026', '00026', '2011', 'FETHAII/2011/00026', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(177, '2021-12-07 20:41:50.891077', '2021-12-07 20:45:19.262317', 'MAXWELL', 'ACHI', 'NGWU', '08064004381', NULL, NULL, NULL, '00027', '00027', '2012', 'FETHAII/2012/00027', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(178, '2021-12-07 20:41:51.446259', '2021-12-07 20:45:19.361151', 'EZEKIEL', 'ACHONWA', 'UC', '08064004382', NULL, NULL, NULL, '00028', '00028', '2013', 'FETHAII/2013/00028', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(179, '2021-12-07 20:41:51.837257', '2021-12-07 20:45:20.291071', 'UDOCHRIS', 'ACHUGONYE', '', '08064004383', NULL, NULL, NULL, '00029', '00029', '2014', 'FETHAII/2014/00029', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(180, '2021-12-07 20:41:51.986118', '2021-12-07 20:45:20.649806', 'MATTHEW', 'ADAMA', 'SIMO', '08064004384', NULL, NULL, NULL, '00030', '00030', '2015', 'FETHAII/2015/00030', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(181, '2021-12-07 20:41:52.348874', '2021-12-07 20:45:20.771453', 'BEATRI', 'ADAMSOKORIE', '', '08064004385', NULL, NULL, NULL, '00031', '00031', '2016', 'FETHAII/2016/00031', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(182, '2021-12-07 20:41:52.437774', '2021-12-07 20:45:20.916706', 'IFEOMA', 'ADANI', 'MODES', '08064004386', NULL, NULL, NULL, '00032', '00032', '2017', 'FETHAII/2017/00032', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(183, '2021-12-07 20:41:52.549903', '2021-12-07 20:45:21.427919', 'IBUKUN', 'ADEOLU', 'NGOZ', '08064004387', NULL, NULL, NULL, '00033', '00033', '2018', 'FETHAII/2018/00033', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(184, '2021-12-07 20:41:52.772908', '2021-12-07 20:45:21.549466', 'KUSS', 'ADEOYE', 'JULIAN', '08064004388', NULL, NULL, NULL, '00034', '00034', '2019', 'FETHAII/2019/00034', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(185, '2021-12-07 20:41:52.826524', '2021-12-07 20:45:21.673165', 'SAMSON', 'ADEYEMI', 'OLU', '08064004389', NULL, NULL, NULL, '00035', '00035', '2020', 'FETHAII/2020/00035', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(186, '2021-12-07 20:41:52.926460', '2021-12-07 20:45:21.828502', 'EMMANUEL', 'ADIDU', 'AME', '08064004390', NULL, NULL, NULL, '00036', '00036', '2021', 'FETHAII/2021/00036', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(187, '2021-12-07 20:41:53.053700', '2021-12-07 20:45:21.949503', 'NWANYIEZE', 'ADIELE', 'N', '08064004391', NULL, NULL, NULL, '00037', '00037', '2010', 'FETHAII/2010/00037', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(188, '2021-12-07 20:41:53.119956', '2021-12-07 20:45:22.295214', 'EMMANUEL', 'ADIGWE', 'IF', '08064004392', NULL, NULL, NULL, '00038', '00038', '2011', 'FETHAII/2011/00038', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(189, '2021-12-07 20:41:53.161583', '2021-12-07 20:45:22.524107', 'JULIANA', 'ADIKWU', 'NGO', '08064004393', NULL, NULL, NULL, '00039', '00039', '2012', 'FETHAII/2012/00039', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(190, '2021-12-07 20:41:53.306511', '2021-12-07 20:45:22.617049', 'CAROLINE', 'ADIMORAH', '', '08064004394', NULL, NULL, NULL, '00040', '00040', '2013', 'FETHAII/2013/00040', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(191, '2021-12-07 20:41:53.348361', '2021-12-07 20:45:22.738272', 'ORAEKI', 'ADIMORAH', 'HA', '08064004395', NULL, NULL, NULL, '00041', '00041', '2014', 'FETHAII/2014/00041', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(192, '2021-12-07 20:41:53.426185', '2021-12-07 20:45:22.839080', 'IFEYINWA', 'ADOGU', '', '08064004396', NULL, NULL, NULL, '00042', '00042', '2015', 'FETHAII/2015/00042', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(193, '2021-12-07 20:41:53.470981', '2021-12-07 20:45:22.960731', 'OGHENEOCHUKO', 'ADOKA', '', '08064004397', NULL, NULL, NULL, '00043', '00043', '2016', 'FETHAII/2016/00043', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(194, '2021-12-07 20:41:53.541222', '2021-12-07 20:45:23.127410', 'NWOVA', 'ADOKE', 'JOHN', '08064004398', NULL, NULL, NULL, '00044', '00044', '2017', 'FETHAII/2017/00044', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(195, '2021-12-07 20:41:53.584800', '2021-12-07 20:45:23.516986', 'EDACHE', 'ADOKWU', 'ELDA', '08064004399', NULL, NULL, NULL, '00045', '00045', '2018', 'FETHAII/2018/00045', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(196, '2021-12-07 20:41:53.714533', '2021-12-07 20:45:23.627544', 'OBINNA', 'ADONU', 'BENJA', '08064004400', NULL, NULL, NULL, '00046', '00046', '2019', 'FETHAII/2019/00046', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(197, '2021-12-07 20:41:53.827441', '2021-12-07 20:45:23.750174', 'LINDA', 'ADUAKA', 'UKAMA', '08064004401', NULL, NULL, NULL, '00047', '00047', '2020', 'FETHAII/2020/00047', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(198, '2021-12-07 20:41:53.927856', '2021-12-07 20:45:23.872042', 'NGOZI', 'ADUAKA', 'ELIZA', '08064004402', NULL, NULL, NULL, '00048', '00048', '2021', 'FETHAII/2021/00048', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(199, '2021-12-07 20:41:54.059261', '2021-12-07 20:45:23.983735', 'VIVIAN', 'ADUAKA', 'ONYI', '08064004403', NULL, NULL, NULL, '00049', '00049', '2010', 'FETHAII/2010/00049', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(200, '2021-12-07 20:41:54.126218', '2021-12-07 20:45:24.129620', 'ADAGBA', 'ADUWA', 'PATRI', '08064004404', NULL, NULL, NULL, '00050', '00050', '2011', 'FETHAII/2011/00050', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(201, '2021-12-07 20:45:07.915459', '2021-12-07 20:45:24.251297', 'BEN', 'IDAKA', 'MAUREEN', '08064004355', NULL, NULL, NULL, '00001', '00001', '2010', 'FETHAII/2010/00001', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(202, '2021-12-07 20:45:08.404939', '2021-12-07 20:45:24.695451', 'UCHENNA', 'OKOLI', 'OBIA', '08064004356', NULL, NULL, NULL, '00002', '00002', '2011', 'FETHAII/2011/00002', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(203, '2021-12-07 20:45:08.525786', '2021-12-07 20:45:24.905463', 'NKONYELU', 'OKONKWO', 'E', '08064004357', NULL, NULL, NULL, '00003', '00003', '2012', 'FETHAII/2012/00003', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(204, '2021-12-07 20:45:08.617726', '2021-12-07 20:45:25.050372', 'OPHELIA', 'AMADI', 'CHIB', '08064004358', NULL, NULL, NULL, '00004', '00004', '2013', 'FETHAII/2013/00004', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(205, '2021-12-07 20:45:08.706151', '2021-12-07 20:45:25.183674', 'IKWUO', 'NNACHI', 'IJEM', '08064004359', NULL, NULL, NULL, '00005', '00005', '2014', 'FETHAII/2014/00005', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(206, '2021-12-07 20:45:08.795442', '2021-12-07 20:45:25.328167', 'IFEOMA', 'AGBOWO', 'MARY', '08064004360', NULL, NULL, NULL, '00006', '00006', '2015', 'FETHAII/2015/00006', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(207, '2021-12-07 20:45:08.862769', '2021-12-07 20:45:25.461142', 'DR', 'NWANKWO', 'OKUTA J', '08064004361', NULL, NULL, NULL, '00007', '00007', '2016', 'FETHAII/2016/00007', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(208, '2021-12-07 20:45:08.954214', '2021-12-07 20:45:26.069887', 'EMMANUEL', 'ABAA', '', '08064004362', NULL, NULL, NULL, '00008', '00008', '2017', 'FETHAII/2017/00008', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(209, '2021-12-07 20:45:09.074141', '2021-12-07 20:45:26.295026', 'UGO', 'ABAGHA', 'AGNES', '08064004363', NULL, NULL, NULL, '00009', '00009', '2018', 'FETHAII/2018/00009', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(210, '2021-12-07 20:45:09.166848', '2021-12-07 20:45:26.439915', 'CHIGOZI', 'ABAGHAUGWU', '', '08064004364', NULL, NULL, NULL, '00010', '00010', '2019', 'FETHAII/2019/00010', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(211, '2021-12-07 20:45:09.462014', '2021-12-07 20:45:26.594781', 'NWACHINAME', 'ABANIFI', '', '08064004365', NULL, NULL, NULL, '00011', '00011', '2020', 'FETHAII/2020/00011', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(212, '2021-12-07 20:45:09.632253', '2021-12-07 20:45:26.705284', 'NNENWAOGO', 'ABARA', 'P', '08064004366', NULL, NULL, NULL, '00012', '00012', '2021', 'FETHAII/2021/00012', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(213, '2021-12-07 20:45:09.698071', '2021-12-07 20:45:26.829369', 'LAWRENCE', 'ABARA', 'CHI', '08064004367', NULL, NULL, NULL, '00013', '00013', '2010', 'FETHAII/2010/00013', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(214, '2021-12-07 20:45:09.763032', '2021-12-07 20:45:27.043461', 'NWAKAEGO', 'ABARA', 'EUC', '08064004368', NULL, NULL, NULL, '00014', '00014', '2011', 'FETHAII/2011/00014', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(215, '2021-12-07 20:45:09.862582', '2021-12-07 20:45:27.283258', 'OBASI', 'ABBA', 'DORCAS', '08064004369', NULL, NULL, NULL, '00015', '00015', '2012', 'FETHAII/2012/00015', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(216, '2021-12-07 20:45:09.951523', '2021-12-07 20:45:27.414178', 'EFFIONG', 'ABIA', 'ANIET', '08064004370', NULL, NULL, NULL, '00016', '00016', '2013', 'FETHAII/2013/00016', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(217, '2021-12-07 20:45:10.021197', '2021-12-07 20:45:27.571883', 'NKIRUKA', 'ABIA', 'NDON', '08064004371', NULL, NULL, NULL, '00017', '00017', '2014', 'FETHAII/2014/00017', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(218, '2021-12-07 20:45:10.133984', '2021-12-07 20:45:27.717835', 'DR', 'ABIA', 'EFFIONG NDO', '08064004372', NULL, NULL, NULL, '00018', '00018', '2015', 'FETHAII/2015/00018', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(219, '2021-12-07 20:45:10.200984', '2021-12-07 20:45:27.850864', 'UGOCHI', 'ABII', 'GLORIA', '08064004373', NULL, NULL, NULL, '00019', '00019', '2016', 'FETHAII/2016/00019', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(220, '2021-12-07 20:45:10.263477', '2021-12-07 20:45:28.128663', 'ABEKE', 'ABIOLA', 'ZULAY', '08064004374', NULL, NULL, NULL, '00020', '00020', '2017', 'FETHAII/2017/00020', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2);
INSERT INTO `membership_request` (`id`, `created_at`, `updated_at`, `first_name`, `last_name`, `middle_name`, `phone_number`, `certified_date`, `approval_comment`, `approved_date`, `file_no`, `ippis_no`, `year`, `member_id`, `approval_officer_id`, `approval_status_id`, `certification_officer_id`, `certification_status_id`, `department_id`, `gender_id`, `processed_by_id`, `salary_institution_id`, `submission_status_id`, `title_id`, `transaction_status_id`) VALUES
(221, '2021-12-07 20:45:10.361740', '2021-12-07 20:45:28.440271', 'CHIOMA', 'ABIRI', 'CLARA', '08064004375', NULL, NULL, NULL, '00021', '00021', '2018', 'FETHAII/2018/00021', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(222, '2021-12-07 20:45:10.433589', '2021-12-07 20:45:28.558999', 'OLADELE', 'ABOKEDE', 'AD', '08064004376', NULL, NULL, NULL, '00022', '00022', '2019', 'FETHAII/2019/00022', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(223, '2021-12-07 20:45:11.109478', '2021-12-07 20:45:28.638949', 'OMOLARA', 'ABOKEDE', 'AD', '08064004377', NULL, NULL, NULL, '00023', '00023', '2020', 'FETHAII/2020/00023', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(224, '2021-12-07 20:45:11.220994', '2021-12-07 20:45:28.763115', 'LEONARD', 'ABOR', '', '08064004378', NULL, NULL, NULL, '00024', '00024', '2021', 'FETHAII/2021/00024', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(225, '2021-12-07 20:45:11.314405', '2021-12-07 20:45:28.929276', 'MOMOH', 'ABU', 'AUGUSTIN', '08064004379', NULL, NULL, NULL, '00025', '00025', '2010', 'FETHAII/2010/00025', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(226, '2021-12-07 20:45:11.407627', '2021-12-07 20:45:29.073079', 'MMADUABUCHI', 'ABUWA', '', '08064004380', NULL, NULL, NULL, '00026', '00026', '2011', 'FETHAII/2011/00026', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(227, '2021-12-07 20:45:11.623353', '2021-12-07 20:45:29.172946', 'MAXWELL', 'ACHI', 'NGWU', '08064004381', NULL, NULL, NULL, '00027', '00027', '2012', 'FETHAII/2012/00027', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(228, '2021-12-07 20:45:11.727812', '2021-12-07 20:45:29.739651', 'EZEKIEL', 'ACHONWA', 'UC', '08064004382', NULL, NULL, NULL, '00028', '00028', '2013', 'FETHAII/2013/00028', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(229, '2021-12-07 20:45:11.817757', '2021-12-07 20:45:29.861196', 'UDOCHRIS', 'ACHUGONYE', '', '08064004383', NULL, NULL, NULL, '00029', '00029', '2014', 'FETHAII/2014/00029', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(230, '2021-12-07 20:45:11.895505', '2021-12-07 20:45:30.051069', 'MATTHEW', 'ADAMA', 'SIMO', '08064004384', NULL, NULL, NULL, '00030', '00030', '2015', 'FETHAII/2015/00030', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(231, '2021-12-07 20:45:11.984492', '2021-12-07 20:45:30.217230', 'BEATRI', 'ADAMSOKORIE', '', '08064004385', NULL, NULL, NULL, '00031', '00031', '2016', 'FETHAII/2016/00031', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(232, '2021-12-07 20:45:12.147782', '2021-12-07 20:45:30.372935', 'IFEOMA', 'ADANI', 'MODES', '08064004386', NULL, NULL, NULL, '00032', '00032', '2017', 'FETHAII/2017/00032', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(233, '2021-12-07 20:45:12.206719', '2021-12-07 20:45:30.484164', 'IBUKUN', 'ADEOLU', 'NGOZ', '08064004387', NULL, NULL, NULL, '00033', '00033', '2018', 'FETHAII/2018/00033', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(234, '2021-12-07 20:45:12.295619', '2021-12-07 20:45:30.661087', 'KUSS', 'ADEOYE', 'JULIAN', '08064004388', NULL, NULL, NULL, '00034', '00034', '2019', 'FETHAII/2019/00034', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(235, '2021-12-07 20:45:12.387674', '2021-12-07 20:45:30.906067', 'SAMSON', 'ADEYEMI', 'OLU', '08064004389', NULL, NULL, NULL, '00035', '00035', '2020', 'FETHAII/2020/00035', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(236, '2021-12-07 20:45:12.451279', '2021-12-07 20:45:31.038978', 'EMMANUEL', 'ADIDU', 'AME', '08064004390', NULL, NULL, NULL, '00036', '00036', '2021', 'FETHAII/2021/00036', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(237, '2021-12-07 20:45:12.544189', '2021-12-07 20:45:31.151222', 'NWANYIEZE', 'ADIELE', 'N', '08064004391', NULL, NULL, NULL, '00037', '00037', '2010', 'FETHAII/2010/00037', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(238, '2021-12-07 20:45:12.864463', '2021-12-07 20:45:31.283501', 'EMMANUEL', 'ADIGWE', 'IF', '08064004392', NULL, NULL, NULL, '00038', '00038', '2011', 'FETHAII/2011/00038', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(239, '2021-12-07 20:45:12.930917', '2021-12-07 20:45:31.395186', 'JULIANA', 'ADIKWU', 'NGO', '08064004393', NULL, NULL, NULL, '00039', '00039', '2012', 'FETHAII/2012/00039', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(240, '2021-12-07 20:45:13.028854', '2021-12-07 20:45:31.517685', 'CAROLINE', 'ADIMORAH', '', '08064004394', NULL, NULL, NULL, '00040', '00040', '2013', 'FETHAII/2013/00040', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(241, '2021-12-07 20:45:13.204003', '2021-12-07 20:45:32.484898', 'ORAEKI', 'ADIMORAH', 'HA', '08064004395', NULL, NULL, NULL, '00041', '00041', '2014', 'FETHAII/2014/00041', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(242, '2021-12-07 20:45:13.319930', '2021-12-07 20:45:32.884401', 'IFEYINWA', 'ADOGU', '', '08064004396', NULL, NULL, NULL, '00042', '00042', '2015', 'FETHAII/2015/00042', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(243, '2021-12-07 20:45:13.395972', '2021-12-07 20:45:33.128674', 'OGHENEOCHUKO', 'ADOKA', '', '08064004397', NULL, NULL, NULL, '00043', '00043', '2016', 'FETHAII/2016/00043', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(244, '2021-12-07 20:45:13.548269', '2021-12-07 20:45:33.418611', 'NWOVA', 'ADOKE', 'JOHN', '08064004398', NULL, NULL, NULL, '00044', '00044', '2017', 'FETHAII/2017/00044', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(245, '2021-12-07 20:45:13.643501', '2021-12-07 20:45:33.842325', 'EDACHE', 'ADOKWU', 'ELDA', '08064004399', NULL, NULL, NULL, '00045', '00045', '2018', 'FETHAII/2018/00045', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(246, '2021-12-07 20:45:13.751899', '2021-12-07 20:45:34.317131', 'OBINNA', 'ADONU', 'BENJA', '08064004400', NULL, NULL, NULL, '00046', '00046', '2019', 'FETHAII/2019/00046', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(247, '2021-12-07 20:45:13.920689', '2021-12-07 20:45:34.595291', 'LINDA', 'ADUAKA', 'UKAMA', '08064004401', NULL, NULL, NULL, '00047', '00047', '2020', 'FETHAII/2020/00047', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(248, '2021-12-07 20:45:13.987334', '2021-12-07 20:45:34.694861', 'NGOZI', 'ADUAKA', 'ELIZA', '08064004402', NULL, NULL, NULL, '00048', '00048', '2021', 'FETHAII/2021/00048', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(249, '2021-12-07 20:45:14.051616', '2021-12-07 20:45:34.907519', 'VIVIAN', 'ADUAKA', 'ONYI', '08064004403', NULL, NULL, NULL, '00049', '00049', '2010', 'FETHAII/2010/00049', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(250, '2021-12-07 20:45:14.118346', '2021-12-07 20:45:35.162685', 'ADAGBA', 'ADUWA', 'PATRI', '08064004404', NULL, NULL, NULL, '00050', '00050', '2011', 'FETHAII/2011/00050', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(251, '2021-12-07 20:52:22.857533', '2021-12-07 20:52:29.645322', 'BEN', 'IDAKA', 'MAUREEN', '08064004355', NULL, NULL, NULL, '00001', '00001', '2010', 'FETHAII/2010/00001', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(252, '2021-12-07 20:52:23.123571', '2021-12-07 20:52:29.922353', 'UCHENNA', 'OKOLI', 'OBIA', '08064004356', NULL, NULL, NULL, '00002', '00002', '2011', 'FETHAII/2011/00002', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(253, '2021-12-07 20:52:23.353509', '2021-12-07 20:52:30.249611', 'NKONYELU', 'OKONKWO', 'E', '08064004357', NULL, NULL, NULL, '00003', '00003', '2012', 'FETHAII/2012/00003', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(254, '2021-12-07 20:52:23.452003', '2021-12-07 20:52:30.371542', 'OPHELIA', 'AMADI', 'CHIB', '08064004358', NULL, NULL, NULL, '00004', '00004', '2013', 'FETHAII/2013/00004', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(255, '2021-12-07 20:52:23.561253', '2021-12-07 20:52:30.738960', 'IKWUO', 'NNACHI', 'IJEM', '08064004359', NULL, NULL, NULL, '00005', '00005', '2014', 'FETHAII/2014/00005', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(256, '2021-12-07 20:52:23.635298', '2021-12-07 20:52:30.894687', 'IFEOMA', 'AGBOWO', 'MARY', '08064004360', NULL, NULL, NULL, '00006', '00006', '2015', 'FETHAII/2015/00006', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(257, '2021-12-07 20:52:23.688687', '2021-12-07 20:52:31.026935', 'DR', 'NWANKWO', 'OKUTA J', '08064004361', NULL, NULL, NULL, '00007', '00007', '2016', 'FETHAII/2016/00007', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(258, '2021-12-07 20:52:23.904098', '2021-12-07 20:52:31.159913', 'EMMANUEL', 'ABAA', '', '08064004362', NULL, NULL, NULL, '00008', '00008', '2017', 'FETHAII/2017/00008', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(259, '2021-12-07 20:52:23.984051', '2021-12-07 20:52:31.259461', 'UGO', 'ABAGHA', 'AGNES', '08064004363', NULL, NULL, NULL, '00009', '00009', '2018', 'FETHAII/2018/00009', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(260, '2021-12-07 20:52:24.039015', '2021-12-07 20:52:31.404348', 'CHIGOZI', 'ABAGHAUGWU', '', '08064004364', NULL, NULL, NULL, '00010', '00010', '2019', 'FETHAII/2019/00010', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(261, '2021-12-07 20:52:24.110545', '2021-12-07 20:52:31.503828', 'NWACHINAME', 'ABANIFI', '', '08064004365', NULL, NULL, NULL, '00011', '00011', '2020', 'FETHAII/2020/00011', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(262, '2021-12-07 20:52:24.198060', '2021-12-07 20:52:31.727799', 'NNENWAOGO', 'ABARA', 'P', '08064004366', NULL, NULL, NULL, '00012', '00012', '2021', 'FETHAII/2021/00012', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(263, '2021-12-07 20:52:24.518308', '2021-12-07 20:52:31.915826', 'LAWRENCE', 'ABARA', 'CHI', '08064004367', NULL, NULL, NULL, '00013', '00013', '2010', 'FETHAII/2010/00013', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(264, '2021-12-07 20:52:24.599527', '2021-12-07 20:52:32.049390', 'NWAKAEGO', 'ABARA', 'EUC', '08064004368', NULL, NULL, NULL, '00014', '00014', '2011', 'FETHAII/2011/00014', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(265, '2021-12-07 20:52:24.662558', '2021-12-07 20:52:32.183350', 'OBASI', 'ABBA', 'DORCAS', '08064004369', NULL, NULL, NULL, '00015', '00015', '2012', 'FETHAII/2012/00015', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(266, '2021-12-07 20:52:24.756269', '2021-12-07 20:52:32.311349', 'EFFIONG', 'ABIA', 'ANIET', '08064004370', NULL, NULL, NULL, '00016', '00016', '2013', 'FETHAII/2013/00016', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(267, '2021-12-07 20:52:24.818462', '2021-12-07 20:52:32.404289', 'NKIRUKA', 'ABIA', 'NDON', '08064004371', NULL, NULL, NULL, '00017', '00017', '2014', 'FETHAII/2014/00017', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(268, '2021-12-07 20:52:24.885324', '2021-12-07 20:52:32.559983', 'DR', 'ABIA', 'EFFIONG NDO', '08064004372', NULL, NULL, NULL, '00018', '00018', '2015', 'FETHAII/2015/00018', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(269, '2021-12-07 20:52:24.985138', '2021-12-07 20:52:32.722790', 'UGOCHI', 'ABII', 'GLORIA', '08064004373', NULL, NULL, NULL, '00019', '00019', '2016', 'FETHAII/2016/00019', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(270, '2021-12-07 20:52:25.063241', '2021-12-07 20:52:33.711797', 'ABEKE', 'ABIOLA', 'ZULAY', '08064004374', NULL, NULL, NULL, '00020', '00020', '2017', 'FETHAII/2017/00020', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(271, '2021-12-07 20:52:25.151008', '2021-12-07 20:52:33.893472', 'CHIOMA', 'ABIRI', 'CLARA', '08064004375', NULL, NULL, NULL, '00021', '00021', '2018', 'FETHAII/2018/00021', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(272, '2021-12-07 20:52:25.239950', '2021-12-07 20:52:34.015131', 'OLADELE', 'ABOKEDE', 'AD', '08064004376', NULL, NULL, NULL, '00022', '00022', '2019', 'FETHAII/2019/00022', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(273, '2021-12-07 20:52:25.617136', '2021-12-07 20:52:34.168036', 'OMOLARA', 'ABOKEDE', 'AD', '08064004377', NULL, NULL, NULL, '00023', '00023', '2020', 'FETHAII/2020/00023', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(274, '2021-12-07 20:52:25.709076', '2021-12-07 20:52:34.549705', 'LEONARD', 'ABOR', '', '08064004378', NULL, NULL, NULL, '00024', '00024', '2021', 'FETHAII/2021/00024', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(275, '2021-12-07 20:52:25.784652', '2021-12-07 20:52:34.715514', 'MOMOH', 'ABU', 'AUGUSTIN', '08064004379', NULL, NULL, NULL, '00025', '00025', '2010', 'FETHAII/2010/00025', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(276, '2021-12-07 20:52:25.888800', '2021-12-07 20:52:34.848617', 'MMADUABUCHI', 'ABUWA', '', '08064004380', NULL, NULL, NULL, '00026', '00026', '2011', 'FETHAII/2011/00026', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(277, '2021-12-07 20:52:25.991846', '2021-12-07 20:52:34.982777', 'MAXWELL', 'ACHI', 'NGWU', '08064004381', NULL, NULL, NULL, '00027', '00027', '2012', 'FETHAII/2012/00027', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(278, '2021-12-07 20:52:26.099742', '2021-12-07 20:52:35.117394', 'EZEKIEL', 'ACHONWA', 'UC', '08064004382', NULL, NULL, NULL, '00028', '00028', '2013', 'FETHAII/2013/00028', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(279, '2021-12-07 20:52:26.203762', '2021-12-07 20:52:35.337980', 'UDOCHRIS', 'ACHUGONYE', '', '08064004383', NULL, NULL, NULL, '00029', '00029', '2014', 'FETHAII/2014/00029', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(280, '2021-12-07 20:52:26.262586', '2021-12-07 20:52:35.672933', 'MATTHEW', 'ADAMA', 'SIMO', '08064004384', NULL, NULL, NULL, '00030', '00030', '2015', 'FETHAII/2015/00030', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(281, '2021-12-07 20:52:26.373558', '2021-12-07 20:52:35.805521', 'BEATRI', 'ADAMSOKORIE', '', '08064004385', NULL, NULL, NULL, '00031', '00031', '2016', 'FETHAII/2016/00031', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(282, '2021-12-07 20:52:26.477540', '2021-12-07 20:52:35.937861', 'IFEOMA', 'ADANI', 'MODES', '08064004386', NULL, NULL, NULL, '00032', '00032', '2017', 'FETHAII/2017/00032', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(283, '2021-12-07 20:52:27.217058', '2021-12-07 20:52:36.082876', 'IBUKUN', 'ADEOLU', 'NGOZ', '08064004387', NULL, NULL, NULL, '00033', '00033', '2018', 'FETHAII/2018/00033', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(284, '2021-12-07 20:52:27.434600', '2021-12-07 20:52:36.327262', 'KUSS', 'ADEOYE', 'JULIAN', '08064004388', NULL, NULL, NULL, '00034', '00034', '2019', 'FETHAII/2019/00034', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(285, '2021-12-07 20:52:27.728220', '2021-12-07 20:52:36.749951', 'SAMSON', 'ADEYEMI', 'OLU', '08064004389', NULL, NULL, NULL, '00035', '00035', '2020', 'FETHAII/2020/00035', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(286, '2021-12-07 20:52:27.910309', '2021-12-07 20:52:37.159811', 'EMMANUEL', 'ADIDU', 'AME', '08064004390', NULL, NULL, NULL, '00036', '00036', '2021', 'FETHAII/2021/00036', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(287, '2021-12-07 20:52:28.095471', '2021-12-07 20:52:37.294363', 'NWANYIEZE', 'ADIELE', 'N', '08064004391', NULL, NULL, NULL, '00037', '00037', '2010', 'FETHAII/2010/00037', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(288, '2021-12-07 20:52:28.198116', '2021-12-07 20:52:37.427190', 'EMMANUEL', 'ADIGWE', 'IF', '08064004392', NULL, NULL, NULL, '00038', '00038', '2011', 'FETHAII/2011/00038', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(289, '2021-12-07 20:52:28.254133', '2021-12-07 20:52:37.749684', 'JULIANA', 'ADIKWU', 'NGO', '08064004393', NULL, NULL, NULL, '00039', '00039', '2012', 'FETHAII/2012/00039', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(290, '2021-12-07 20:52:28.445271', '2021-12-07 20:52:37.902230', 'CAROLINE', 'ADIMORAH', '', '08064004394', NULL, NULL, NULL, '00040', '00040', '2013', 'FETHAII/2013/00040', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(291, '2021-12-07 20:52:28.567732', '2021-12-07 20:52:38.038397', 'ORAEKI', 'ADIMORAH', 'HA', '08064004395', NULL, NULL, NULL, '00041', '00041', '2014', 'FETHAII/2014/00041', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(292, '2021-12-07 20:52:28.705782', '2021-12-07 20:52:38.149972', 'IFEYINWA', 'ADOGU', '', '08064004396', NULL, NULL, NULL, '00042', '00042', '2015', 'FETHAII/2015/00042', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(293, '2021-12-07 20:52:28.788732', '2021-12-07 20:52:38.261459', 'OGHENEOCHUKO', 'ADOKA', '', '08064004397', NULL, NULL, NULL, '00043', '00043', '2016', 'FETHAII/2016/00043', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(294, '2021-12-07 20:52:28.861547', '2021-12-07 20:52:38.382376', 'NWOVA', 'ADOKE', 'JOHN', '08064004398', NULL, NULL, NULL, '00044', '00044', '2017', 'FETHAII/2017/00044', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(295, '2021-12-07 20:52:28.917471', '2021-12-07 20:52:38.505253', 'EDACHE', 'ADOKWU', 'ELDA', '08064004399', NULL, NULL, NULL, '00045', '00045', '2018', 'FETHAII/2018/00045', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(296, '2021-12-07 20:52:29.003040', '2021-12-07 20:52:38.927703', 'OBINNA', 'ADONU', 'BENJA', '08064004400', NULL, NULL, NULL, '00046', '00046', '2019', 'FETHAII/2019/00046', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(297, '2021-12-07 20:52:29.051050', '2021-12-07 20:52:39.061323', 'LINDA', 'ADUAKA', 'UKAMA', '08064004401', NULL, NULL, NULL, '00047', '00047', '2020', 'FETHAII/2020/00047', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(298, '2021-12-07 20:52:29.107419', '2021-12-07 20:52:39.259821', 'NGOZI', 'ADUAKA', 'ELIZA', '08064004402', NULL, NULL, NULL, '00048', '00048', '2021', 'FETHAII/2021/00048', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(299, '2021-12-07 20:52:29.220576', '2021-12-07 20:52:39.405168', 'VIVIAN', 'ADUAKA', 'ONYI', '08064004403', NULL, NULL, NULL, '00049', '00049', '2010', 'FETHAII/2010/00049', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(300, '2021-12-07 20:52:29.309648', '2021-12-07 20:52:39.538471', 'ADAGBA', 'ADUWA', 'PATRI', '08064004404', NULL, NULL, NULL, '00050', '00050', '2011', 'FETHAII/2011/00050', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(301, '2021-12-07 20:52:12.262945', '2021-12-07 20:52:18.081556', 'BEN', 'IDAKA', 'MAUREEN', '08064004355', NULL, NULL, NULL, '00001', '00001', '2010', 'FETHAII/2010/00001', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(302, '2021-12-07 20:52:12.662417', '2021-12-07 20:52:18.248730', 'UCHENNA', 'OKOLI', 'OBIA', '08064004356', NULL, NULL, NULL, '00002', '00002', '2011', 'FETHAII/2011/00002', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(303, '2021-12-07 20:52:12.751738', '2021-12-07 20:52:19.172266', 'NKONYELU', 'OKONKWO', 'E', '08064004357', NULL, NULL, NULL, '00003', '00003', '2012', 'FETHAII/2012/00003', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(304, '2021-12-07 20:52:12.844370', '2021-12-07 20:52:19.326762', 'OPHELIA', 'AMADI', 'CHIB', '08064004358', NULL, NULL, NULL, '00004', '00004', '2013', 'FETHAII/2013/00004', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(305, '2021-12-07 20:52:12.931350', '2021-12-07 20:52:19.438683', 'IKWUO', 'NNACHI', 'IJEM', '08064004359', NULL, NULL, NULL, '00005', '00005', '2014', 'FETHAII/2014/00005', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(306, '2021-12-07 20:52:13.018121', '2021-12-07 20:52:19.595505', 'IFEOMA', 'AGBOWO', 'MARY', '08064004360', NULL, NULL, NULL, '00006', '00006', '2015', 'FETHAII/2015/00006', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(307, '2021-12-07 20:52:13.107413', '2021-12-07 20:52:19.728544', 'DR', 'NWANKWO', 'OKUTA J', '08064004361', NULL, NULL, NULL, '00007', '00007', '2016', 'FETHAII/2016/00007', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(308, '2021-12-07 20:52:13.317366', '2021-12-07 20:52:19.849365', 'EMMANUEL', 'ABAA', '', '08064004362', NULL, NULL, NULL, '00008', '00008', '2017', 'FETHAII/2017/00008', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(309, '2021-12-07 20:52:13.409013', '2021-12-07 20:52:20.050492', 'UGO', 'ABAGHA', 'AGNES', '08064004363', NULL, NULL, NULL, '00009', '00009', '2018', 'FETHAII/2018/00009', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(310, '2021-12-07 20:52:13.537993', '2021-12-07 20:52:20.171931', 'CHIGOZI', 'ABAGHAUGWU', '', '08064004364', NULL, NULL, NULL, '00010', '00010', '2019', 'FETHAII/2019/00010', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(311, '2021-12-07 20:52:13.662573', '2021-12-07 20:52:20.294762', 'NWACHINAME', 'ABANIFI', '', '08064004365', NULL, NULL, NULL, '00011', '00011', '2020', 'FETHAII/2020/00011', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(312, '2021-12-07 20:52:13.797004', '2021-12-07 20:52:20.493700', 'NNENWAOGO', 'ABARA', 'P', '08064004366', NULL, NULL, NULL, '00012', '00012', '2021', 'FETHAII/2021/00012', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(313, '2021-12-07 20:52:13.974674', '2021-12-07 20:52:20.672794', 'LAWRENCE', 'ABARA', 'CHI', '08064004367', NULL, NULL, NULL, '00013', '00013', '2010', 'FETHAII/2010/00013', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(314, '2021-12-07 20:52:14.129468', '2021-12-07 20:52:20.772431', 'NWAKAEGO', 'ABARA', 'EUC', '08064004368', NULL, NULL, NULL, '00014', '00014', '2011', 'FETHAII/2011/00014', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(315, '2021-12-07 20:52:14.232840', '2021-12-07 20:52:20.906224', 'OBASI', 'ABBA', 'DORCAS', '08064004369', NULL, NULL, NULL, '00015', '00015', '2012', 'FETHAII/2012/00015', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(316, '2021-12-07 20:52:14.332723', '2021-12-07 20:52:21.401134', 'EFFIONG', 'ABIA', 'ANIET', '08064004370', NULL, NULL, NULL, '00016', '00016', '2013', 'FETHAII/2013/00016', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(317, '2021-12-07 20:52:14.431570', '2021-12-07 20:52:21.771160', 'NKIRUKA', 'ABIA', 'NDON', '08064004371', NULL, NULL, NULL, '00017', '00017', '2014', 'FETHAII/2014/00017', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(318, '2021-12-07 20:52:14.495813', '2021-12-07 20:52:21.894199', 'DR', 'ABIA', 'EFFIONG NDO', '08064004372', NULL, NULL, NULL, '00018', '00018', '2015', 'FETHAII/2015/00018', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(319, '2021-12-07 20:52:14.565055', '2021-12-07 20:52:22.161794', 'UGOCHI', 'ABII', 'GLORIA', '08064004373', NULL, NULL, NULL, '00019', '00019', '2016', 'FETHAII/2016/00019', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(320, '2021-12-07 20:52:14.631653', '2021-12-07 20:52:22.404920', 'ABEKE', 'ABIOLA', 'ZULAY', '08064004374', NULL, NULL, NULL, '00020', '00020', '2017', 'FETHAII/2017/00020', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(321, '2021-12-07 20:52:14.694782', '2021-12-07 20:52:22.774069', 'CHIOMA', 'ABIRI', 'CLARA', '08064004375', NULL, NULL, NULL, '00021', '00021', '2018', 'FETHAII/2018/00021', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(322, '2021-12-07 20:52:14.770735', '2021-12-07 20:52:22.959276', 'OLADELE', 'ABOKEDE', 'AD', '08064004376', NULL, NULL, NULL, '00022', '00022', '2019', 'FETHAII/2019/00022', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(323, '2021-12-07 20:52:14.957974', '2021-12-07 20:52:23.299776', 'OMOLARA', 'ABOKEDE', 'AD', '08064004377', NULL, NULL, NULL, '00023', '00023', '2020', 'FETHAII/2020/00023', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(324, '2021-12-07 20:52:15.066393', '2021-12-07 20:52:23.438371', 'LEONARD', 'ABOR', '', '08064004378', NULL, NULL, NULL, '00024', '00024', '2021', 'FETHAII/2021/00024', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(325, '2021-12-07 20:52:15.207859', '2021-12-07 20:52:23.639000', 'MOMOH', 'ABU', 'AUGUSTIN', '08064004379', NULL, NULL, NULL, '00025', '00025', '2010', 'FETHAII/2010/00025', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(326, '2021-12-07 20:52:15.274533', '2021-12-07 20:52:23.884054', 'MMADUABUCHI', 'ABUWA', '', '08064004380', NULL, NULL, NULL, '00026', '00026', '2011', 'FETHAII/2011/00026', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(327, '2021-12-07 20:52:15.402371', '2021-12-07 20:52:24.006838', 'MAXWELL', 'ACHI', 'NGWU', '08064004381', NULL, NULL, NULL, '00027', '00027', '2012', 'FETHAII/2012/00027', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(328, '2021-12-07 20:52:15.468053', '2021-12-07 20:52:24.194008', 'EZEKIEL', 'ACHONWA', 'UC', '08064004382', NULL, NULL, NULL, '00028', '00028', '2013', 'FETHAII/2013/00028', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(329, '2021-12-07 20:52:15.534726', '2021-12-07 20:52:24.306390', 'UDOCHRIS', 'ACHUGONYE', '', '08064004383', NULL, NULL, NULL, '00029', '00029', '2014', 'FETHAII/2014/00029', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(330, '2021-12-07 20:52:15.664311', '2021-12-07 20:52:24.438156', 'MATTHEW', 'ADAMA', 'SIMO', '08064004384', NULL, NULL, NULL, '00030', '00030', '2015', 'FETHAII/2015/00030', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(331, '2021-12-07 20:52:15.755637', '2021-12-07 20:52:24.640589', 'BEATRI', 'ADAMSOKORIE', '', '08064004385', NULL, NULL, NULL, '00031', '00031', '2016', 'FETHAII/2016/00031', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(332, '2021-12-07 20:52:15.853264', '2021-12-07 20:52:24.805670', 'IFEOMA', 'ADANI', 'MODES', '08064004386', NULL, NULL, NULL, '00032', '00032', '2017', 'FETHAII/2017/00032', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(333, '2021-12-07 20:52:15.952203', '2021-12-07 20:52:24.929448', 'IBUKUN', 'ADEOLU', 'NGOZ', '08064004387', NULL, NULL, NULL, '00033', '00033', '2018', 'FETHAII/2018/00033', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(334, '2021-12-07 20:52:16.007620', '2021-12-07 20:52:25.039409', 'KUSS', 'ADEOYE', 'JULIAN', '08064004388', NULL, NULL, NULL, '00034', '00034', '2019', 'FETHAII/2019/00034', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(335, '2021-12-07 20:52:16.091628', '2021-12-07 20:52:25.206369', 'SAMSON', 'ADEYEMI', 'OLU', '08064004389', NULL, NULL, NULL, '00035', '00035', '2020', 'FETHAII/2020/00035', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(336, '2021-12-07 20:52:16.265981', '2021-12-07 20:52:25.305772', 'EMMANUEL', 'ADIDU', 'AME', '08064004390', NULL, NULL, NULL, '00036', '00036', '2021', 'FETHAII/2021/00036', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(337, '2021-12-07 20:52:16.564571', '2021-12-07 20:52:25.383723', 'NWANYIEZE', 'ADIELE', 'N', '08064004391', NULL, NULL, NULL, '00037', '00037', '2010', 'FETHAII/2010/00037', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(338, '2021-12-07 20:52:16.678235', '2021-12-07 20:52:25.472863', 'EMMANUEL', 'ADIGWE', 'IF', '08064004392', NULL, NULL, NULL, '00038', '00038', '2011', 'FETHAII/2011/00038', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(339, '2021-12-07 20:52:16.741951', '2021-12-07 20:52:25.736371', 'JULIANA', 'ADIKWU', 'NGO', '08064004393', NULL, NULL, NULL, '00039', '00039', '2012', 'FETHAII/2012/00039', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(340, '2021-12-07 20:52:16.808831', '2021-12-07 20:52:26.084784', 'CAROLINE', 'ADIMORAH', '', '08064004394', NULL, NULL, NULL, '00040', '00040', '2013', 'FETHAII/2013/00040', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(341, '2021-12-07 20:52:16.874500', '2021-12-07 20:52:26.404238', 'ORAEKI', 'ADIMORAH', 'HA', '08064004395', NULL, NULL, NULL, '00041', '00041', '2014', 'FETHAII/2014/00041', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(342, '2021-12-07 20:52:16.943959', '2021-12-07 20:52:26.593338', 'IFEYINWA', 'ADOGU', '', '08064004396', NULL, NULL, NULL, '00042', '00042', '2015', 'FETHAII/2015/00042', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(343, '2021-12-07 20:52:17.005916', '2021-12-07 20:52:26.739681', 'OGHENEOCHUKO', 'ADOKA', '', '08064004397', NULL, NULL, NULL, '00043', '00043', '2016', 'FETHAII/2016/00043', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(344, '2021-12-07 20:52:17.062884', '2021-12-07 20:52:26.984387', 'NWOVA', 'ADOKE', 'JOHN', '08064004398', NULL, NULL, NULL, '00044', '00044', '2017', 'FETHAII/2017/00044', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(345, '2021-12-07 20:52:17.140833', '2021-12-07 20:52:27.128227', 'EDACHE', 'ADOKWU', 'ELDA', '08064004399', NULL, NULL, NULL, '00045', '00045', '2018', 'FETHAII/2018/00045', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(346, '2021-12-07 20:52:17.285449', '2021-12-07 20:52:27.239559', 'OBINNA', 'ADONU', 'BENJA', '08064004400', NULL, NULL, NULL, '00046', '00046', '2019', 'FETHAII/2019/00046', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(347, '2021-12-07 20:52:17.522794', '2021-12-07 20:52:27.372733', 'LINDA', 'ADUAKA', 'UKAMA', '08064004401', NULL, NULL, NULL, '00047', '00047', '2020', 'FETHAII/2020/00047', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(348, '2021-12-07 20:52:17.657828', '2021-12-07 20:52:27.572773', 'NGOZI', 'ADUAKA', 'ELIZA', '08064004402', NULL, NULL, NULL, '00048', '00048', '2021', 'FETHAII/2021/00048', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(349, '2021-12-07 20:52:17.740945', '2021-12-07 20:52:27.673170', 'VIVIAN', 'ADUAKA', 'ONYI', '08064004403', NULL, NULL, NULL, '00049', '00049', '2010', 'FETHAII/2010/00049', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(350, '2021-12-07 20:52:17.806688', '2021-12-07 20:52:27.750122', 'ADAGBA', 'ADUWA', 'PATRI', '08064004404', NULL, NULL, NULL, '00050', '00050', '2011', 'FETHAII/2011/00050', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(351, '2021-12-07 21:04:13.677877', '2021-12-07 21:04:18.779028', 'BEN', 'IDAKA', 'MAUREEN', '08064004355', NULL, NULL, NULL, '00001', '00001', '2010', 'FETHAII/2010/00001', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(352, '2021-12-07 21:04:13.953006', '2021-12-07 21:04:18.933983', 'UCHENNA', 'OKOLI', 'OBIA', '08064004356', NULL, NULL, NULL, '00002', '00002', '2011', 'FETHAII/2011/00002', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(353, '2021-12-07 21:04:14.040120', '2021-12-07 21:04:19.858805', 'NKONYELU', 'OKONKWO', 'E', '08064004357', NULL, NULL, NULL, '00003', '00003', '2012', 'FETHAII/2012/00003', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(354, '2021-12-07 21:04:14.148151', '2021-12-07 21:04:20.112968', 'OPHELIA', 'AMADI', 'CHIB', '08064004358', NULL, NULL, NULL, '00004', '00004', '2013', 'FETHAII/2013/00004', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(355, '2021-12-07 21:04:14.224999', '2021-12-07 21:04:20.234744', 'IKWUO', 'NNACHI', 'IJEM', '08064004359', NULL, NULL, NULL, '00005', '00005', '2014', 'FETHAII/2014/00005', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(356, '2021-12-07 21:04:14.313490', '2021-12-07 21:04:20.357053', 'IFEOMA', 'AGBOWO', 'MARY', '08064004360', NULL, NULL, NULL, '00006', '00006', '2015', 'FETHAII/2015/00006', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(357, '2021-12-07 21:04:14.370138', '2021-12-07 21:04:20.578952', 'DR', 'NWANKWO', 'OKUTA J', '08064004361', NULL, NULL, NULL, '00007', '00007', '2016', 'FETHAII/2016/00007', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(358, '2021-12-07 21:04:14.461393', '2021-12-07 21:04:20.757516', 'EMMANUEL', 'ABAA', '', '08064004362', NULL, NULL, NULL, '00008', '00008', '2017', 'FETHAII/2017/00008', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(359, '2021-12-07 21:04:14.529633', '2021-12-07 21:04:20.889762', 'UGO', 'ABAGHA', 'AGNES', '08064004363', NULL, NULL, NULL, '00009', '00009', '2018', 'FETHAII/2018/00009', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(360, '2021-12-07 21:04:14.847265', '2021-12-07 21:04:21.078923', 'CHIGOZI', 'ABAGHAUGWU', '', '08064004364', NULL, NULL, NULL, '00010', '00010', '2019', 'FETHAII/2019/00010', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(361, '2021-12-07 21:04:14.939115', '2021-12-07 21:04:21.212416', 'NWACHINAME', 'ABANIFI', '', '08064004365', NULL, NULL, NULL, '00011', '00011', '2020', 'FETHAII/2020/00011', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(362, '2021-12-07 21:04:15.037157', '2021-12-07 21:04:21.331089', 'NNENWAOGO', 'ABARA', 'P', '08064004366', NULL, NULL, NULL, '00012', '00012', '2021', 'FETHAII/2021/00012', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(363, '2021-12-07 21:04:15.135073', '2021-12-07 21:04:21.468583', 'LAWRENCE', 'ABARA', 'CHI', '08064004367', NULL, NULL, NULL, '00013', '00013', '2010', 'FETHAII/2010/00013', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(364, '2021-12-07 21:04:15.180252', '2021-12-07 21:04:21.545814', 'NWAKAEGO', 'ABARA', 'EUC', '08064004368', NULL, NULL, NULL, '00014', '00014', '2011', 'FETHAII/2011/00014', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(365, '2021-12-07 21:04:15.226105', '2021-12-07 21:04:21.634691', 'OBASI', 'ABBA', 'DORCAS', '08064004369', NULL, NULL, NULL, '00015', '00015', '2012', 'FETHAII/2012/00015', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(366, '2021-12-07 21:04:15.296821', '2021-12-07 21:04:22.623460', 'EFFIONG', 'ABIA', 'ANIET', '08064004370', NULL, NULL, NULL, '00016', '00016', '2013', 'FETHAII/2013/00016', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(367, '2021-12-07 21:04:15.373200', '2021-12-07 21:04:22.901848', 'NKIRUKA', 'ABIA', 'NDON', '08064004371', NULL, NULL, NULL, '00017', '00017', '2014', 'FETHAII/2014/00017', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(368, '2021-12-07 21:04:15.473072', '2021-12-07 21:04:23.056719', 'DR', 'ABIA', 'EFFIONG NDO', '08064004372', NULL, NULL, NULL, '00018', '00018', '2015', 'FETHAII/2015/00018', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(369, '2021-12-07 21:04:15.561746', '2021-12-07 21:04:23.212923', 'UGOCHI', 'ABII', 'GLORIA', '08064004373', NULL, NULL, NULL, '00019', '00019', '2016', 'FETHAII/2016/00019', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(370, '2021-12-07 21:04:15.663969', '2021-12-07 21:04:23.380971', 'ABEKE', 'ABIOLA', 'ZULAY', '08064004374', NULL, NULL, NULL, '00020', '00020', '2017', 'FETHAII/2017/00020', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(371, '2021-12-07 21:04:15.793473', '2021-12-07 21:04:23.657014', 'CHIOMA', 'ABIRI', 'CLARA', '08064004375', NULL, NULL, NULL, '00021', '00021', '2018', 'FETHAII/2018/00021', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(372, '2021-12-07 21:04:15.990170', '2021-12-07 21:04:23.801303', 'OLADELE', 'ABOKEDE', 'AD', '08064004376', NULL, NULL, NULL, '00022', '00022', '2019', 'FETHAII/2019/00022', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(373, '2021-12-07 21:04:16.116313', '2021-12-07 21:04:23.913731', 'OMOLARA', 'ABOKEDE', 'AD', '08064004377', NULL, NULL, NULL, '00023', '00023', '2020', 'FETHAII/2020/00023', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(374, '2021-12-07 21:04:16.191283', '2021-12-07 21:04:24.057658', 'LEONARD', 'ABOR', '', '08064004378', NULL, NULL, NULL, '00024', '00024', '2021', 'FETHAII/2021/00024', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(375, '2021-12-07 21:04:16.269691', '2021-12-07 21:04:24.201562', 'MOMOH', 'ABU', 'AUGUSTIN', '08064004379', NULL, NULL, NULL, '00025', '00025', '2010', 'FETHAII/2010/00025', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(376, '2021-12-07 21:04:16.433291', '2021-12-07 21:04:24.412499', 'MMADUABUCHI', 'ABUWA', '', '08064004380', NULL, NULL, NULL, '00026', '00026', '2011', 'FETHAII/2011/00026', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(377, '2021-12-07 21:04:16.507036', '2021-12-07 21:04:24.677703', 'MAXWELL', 'ACHI', 'NGWU', '08064004381', NULL, NULL, NULL, '00027', '00027', '2012', 'FETHAII/2012/00027', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(378, '2021-12-07 21:04:16.572717', '2021-12-07 21:04:24.823810', 'EZEKIEL', 'ACHONWA', 'UC', '08064004382', NULL, NULL, NULL, '00028', '00028', '2013', 'FETHAII/2013/00028', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(379, '2021-12-07 21:04:16.647547', '2021-12-07 21:04:24.956919', 'UDOCHRIS', 'ACHUGONYE', '', '08064004383', NULL, NULL, NULL, '00029', '00029', '2014', 'FETHAII/2014/00029', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(380, '2021-12-07 21:04:16.692254', '2021-12-07 21:04:25.058323', 'MATTHEW', 'ADAMA', 'SIMO', '08064004384', NULL, NULL, NULL, '00030', '00030', '2015', 'FETHAII/2015/00030', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(381, '2021-12-07 21:04:16.770395', '2021-12-07 21:04:25.168042', 'BEATRI', 'ADAMSOKORIE', '', '08064004385', NULL, NULL, NULL, '00031', '00031', '2016', 'FETHAII/2016/00031', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(382, '2021-12-07 21:04:16.850390', '2021-12-07 21:04:25.312952', 'IFEOMA', 'ADANI', 'MODES', '08064004386', NULL, NULL, NULL, '00032', '00032', '2017', 'FETHAII/2017/00032', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(383, '2021-12-07 21:04:17.102611', '2021-12-07 21:04:25.378911', 'IBUKUN', 'ADEOLU', 'NGOZ', '08064004387', NULL, NULL, NULL, '00033', '00033', '2018', 'FETHAII/2018/00033', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(384, '2021-12-07 21:04:17.180561', '2021-12-07 21:04:25.501004', 'KUSS', 'ADEOYE', 'JULIAN', '08064004388', NULL, NULL, NULL, '00034', '00034', '2019', 'FETHAII/2019/00034', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(385, '2021-12-07 21:04:17.281640', '2021-12-07 21:04:25.669325', 'SAMSON', 'ADEYEMI', 'OLU', '08064004389', NULL, NULL, NULL, '00035', '00035', '2020', 'FETHAII/2020/00035', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(386, '2021-12-07 21:04:17.347881', '2021-12-07 21:04:25.834411', 'EMMANUEL', 'ADIDU', 'AME', '08064004390', NULL, NULL, NULL, '00036', '00036', '2021', 'FETHAII/2021/00036', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(387, '2021-12-07 21:04:17.436192', '2021-12-07 21:04:25.957396', 'NWANYIEZE', 'ADIELE', 'N', '08064004391', NULL, NULL, NULL, '00037', '00037', '2010', 'FETHAII/2010/00037', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(388, '2021-12-07 21:04:17.491749', '2021-12-07 21:04:26.057978', 'EMMANUEL', 'ADIGWE', 'IF', '08064004392', NULL, NULL, NULL, '00038', '00038', '2011', 'FETHAII/2011/00038', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(389, '2021-12-07 21:04:17.548360', '2021-12-07 21:04:26.147071', 'JULIANA', 'ADIKWU', 'NGO', '08064004393', NULL, NULL, NULL, '00039', '00039', '2012', 'FETHAII/2012/00039', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(390, '2021-12-07 21:04:17.625141', '2021-12-07 21:04:26.212234', 'CAROLINE', 'ADIMORAH', '', '08064004394', NULL, NULL, NULL, '00040', '00040', '2013', 'FETHAII/2013/00040', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(391, '2021-12-07 21:04:17.687326', '2021-12-07 21:04:26.279522', 'ORAEKI', 'ADIMORAH', 'HA', '08064004395', NULL, NULL, NULL, '00041', '00041', '2014', 'FETHAII/2014/00041', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(392, '2021-12-07 21:04:17.893198', '2021-12-07 21:04:26.345623', 'IFEYINWA', 'ADOGU', '', '08064004396', NULL, NULL, NULL, '00042', '00042', '2015', 'FETHAII/2015/00042', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(393, '2021-12-07 21:04:18.026469', '2021-12-07 21:04:26.468620', 'OGHENEOCHUKO', 'ADOKA', '', '08064004397', NULL, NULL, NULL, '00043', '00043', '2016', 'FETHAII/2016/00043', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(394, '2021-12-07 21:04:18.258570', '2021-12-07 21:04:26.660182', 'NWOVA', 'ADOKE', 'JOHN', '08064004398', NULL, NULL, NULL, '00044', '00044', '2017', 'FETHAII/2017/00044', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(395, '2021-12-07 21:04:18.324529', '2021-12-07 21:04:27.045828', 'EDACHE', 'ADOKWU', 'ELDA', '08064004399', NULL, NULL, NULL, '00045', '00045', '2018', 'FETHAII/2018/00045', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(396, '2021-12-07 21:04:18.369497', '2021-12-07 21:04:27.218936', 'OBINNA', 'ADONU', 'BENJA', '08064004400', NULL, NULL, NULL, '00046', '00046', '2019', 'FETHAII/2019/00046', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(397, '2021-12-07 21:04:18.413700', '2021-12-07 21:04:27.335347', 'LINDA', 'ADUAKA', 'UKAMA', '08064004401', NULL, NULL, NULL, '00047', '00047', '2020', 'FETHAII/2020/00047', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(398, '2021-12-07 21:04:18.458403', '2021-12-07 21:04:27.457026', 'NGOZI', 'ADUAKA', 'ELIZA', '08064004402', NULL, NULL, NULL, '00048', '00048', '2021', 'FETHAII/2021/00048', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(399, '2021-12-07 21:04:18.513746', '2021-12-07 21:04:27.523125', 'VIVIAN', 'ADUAKA', 'ONYI', '08064004403', NULL, NULL, NULL, '00049', '00049', '2010', 'FETHAII/2010/00049', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(400, '2021-12-07 21:04:18.569297', '2021-12-07 21:04:27.611942', 'ADAGBA', 'ADUWA', 'PATRI', '08064004404', NULL, NULL, NULL, '00050', '00050', '2011', 'FETHAII/2011/00050', NULL, 2, NULL, 2, NULL, NULL, NULL, 1, 2, NULL, 2),
(401, '2021-12-16 07:42:00.391862', '2021-12-16 07:57:07.533430', 'FRED', 'EKPE', 'EDET', '08598574455', '2021-12-16', NULL, '2021-12-16', NULL, NULL, NULL, NULL, 7, 2, 2, 2, 17, 1, 9, NULL, 2, 7, 2),
(402, '2021-12-16 09:08:13.936840', '2021-12-16 09:09:56.598706', 'PHILIP', 'ALOKE', 'SUNDAY', '08075544443', '2021-12-16', NULL, '2021-12-16', NULL, NULL, NULL, NULL, 7, 2, 2, 2, 6, 1, 9, NULL, 2, 8, 2),
(403, '2021-12-16 09:27:41.712497', '2021-12-16 09:29:46.534985', 'EMEKA', 'NJOKU', 'NJOKU', '08608686445', '2021-12-16', NULL, '2021-12-16', NULL, NULL, NULL, NULL, 7, 2, 2, 2, 1, 1, 9, NULL, 2, 4, 2),
(404, '2021-12-16 09:35:44.889608', '2021-12-16 09:39:48.391995', 'CHINYERE', 'IGWE', 'SONIA', '08145674655', '2021-12-16', NULL, '2021-12-16', NULL, NULL, NULL, NULL, 7, 2, 2, 2, 26, 2, 9, NULL, 2, 2, 2),
(405, '2021-12-16 09:48:39.429963', '2021-12-16 09:49:49.200783', 'EMMANUEL', 'ONWE', 'CHIKE', '08039555648', '2021-12-16', NULL, '2021-12-16', NULL, NULL, NULL, NULL, 7, 2, 2, 2, 14, 1, 9, NULL, 2, 8, 2),
(406, '2022-01-01 08:43:48.387405', '2022-01-01 08:45:34.512585', 'NWEKE', 'AGU', '', '09505857445', '2022-01-01', NULL, '2022-01-01', NULL, NULL, NULL, NULL, 7, 2, 2, 2, 1, 1, 9, NULL, 2, 7, 1);

-- --------------------------------------------------------

--
-- Table structure for table `membership_request_additional_attachment`
--

CREATE TABLE `membership_request_additional_attachment` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `caption` varchar(255) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `applicant_id` int(11) DEFAULT NULL,
  `officer_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `membership_request_additional_attachment`
--

INSERT INTO `membership_request_additional_attachment` (`id`, `created_at`, `updated_at`, `caption`, `image`, `applicant_id`, `officer_id`) VALUES
(1, '2021-12-16 07:42:25.014907', '2021-12-16 07:42:25.014907', 'September 2021 Payslip', '/media/avatar2_AII1SA4.png', 401, 9),
(2, '2021-12-16 07:44:39.224938', '2021-12-16 07:44:39.224938', 'Evidience', '/media/avatar5_DSdpXHG.png', 401, 4),
(3, '2021-12-16 09:08:28.314167', '2021-12-16 09:08:28.314167', 'September 2021 Payslip', '/media/photo1_jmUzRuB.png', 402, 9),
(4, '2021-12-16 09:27:56.126722', '2021-12-16 09:27:56.127723', 'September 2021 Payslip', '/media/default-150x150_cjBhnT6.png', 403, 9);

-- --------------------------------------------------------

--
-- Table structure for table `membership_request_additional_info`
--

CREATE TABLE `membership_request_additional_info` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `comment` longtext DEFAULT NULL,
  `applicant_id` int(11) DEFAULT NULL,
  `officer_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `membership_request_additional_info`
--

INSERT INTO `membership_request_additional_info` (`id`, `created_at`, `updated_at`, `comment`, `applicant_id`, `officer_id`) VALUES
(1, '2021-12-16 07:42:07.371074', '2021-12-16 07:42:07.371074', 'ok', 401, 9),
(2, '2021-12-16 07:44:26.392096', '2021-12-16 07:44:26.392096', 'ok', 401, 4),
(3, '2021-12-16 07:45:04.410286', '2021-12-16 07:45:04.411285', 'ok', 401, 2),
(4, '2021-12-16 09:08:17.677357', '2021-12-16 09:08:17.677357', 'ok', 402, 9),
(5, '2021-12-16 09:08:55.737647', '2021-12-16 09:08:55.737647', 'ok', 402, 4),
(6, '2021-12-16 09:09:20.743382', '2021-12-16 09:09:20.743382', 'ok', 402, 2),
(7, '2021-12-16 09:27:45.749000', '2021-12-16 09:27:45.749000', 'ok', 403, 9),
(8, '2021-12-16 09:28:22.292629', '2021-12-16 09:28:22.292629', 'ok', 403, 4),
(9, '2021-12-16 09:28:43.538805', '2021-12-16 09:28:43.538805', 'ok', 403, 2),
(10, '2021-12-16 09:36:11.977286', '2021-12-16 09:36:11.977286', 'ok', 404, 4),
(11, '2021-12-16 09:39:28.730765', '2021-12-16 09:39:28.730765', 'ok', 404, 2);

-- --------------------------------------------------------

--
-- Table structure for table `membership_status`
--

CREATE TABLE `membership_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `membership_status`
--

INSERT INTO `membership_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'ACTIVE', '2021-12-07 18:58:37.362762', '2021-12-07 18:58:37.362762'),
(2, 'INACTIVE', '2021-12-07 18:58:37.472306', '2021-12-07 18:58:37.473306');

-- --------------------------------------------------------

--
-- Table structure for table `members_accounts_domain`
--

CREATE TABLE `members_accounts_domain` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `account_number` varchar(255) NOT NULL,
  `member_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL,
  `transaction_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members_accounts_domain`
--

INSERT INTO `members_accounts_domain` (`id`, `created_at`, `updated_at`, `account_number`, `member_id`, `status_id`, `transaction_id`) VALUES
(351, '2021-12-07 21:05:46.029098', '2021-12-07 21:05:46.029098', '10100001', 151, 1, 2),
(352, '2021-12-07 21:05:46.102265', '2021-12-07 21:05:46.102265', '10200001', 151, 1, 3),
(353, '2021-12-07 21:05:46.267666', '2021-12-07 21:05:46.267666', '10300001', 151, 1, 4),
(354, '2021-12-07 21:05:46.297424', '2021-12-07 21:05:46.297424', '10400001', 151, 1, 5),
(355, '2021-12-07 21:05:46.343441', '2021-12-07 21:05:46.343441', '10500001', 151, 1, 6),
(356, '2021-12-07 21:05:46.364022', '2021-12-07 21:05:46.364022', '70000001', 151, 1, 15),
(357, '2021-12-07 21:05:46.421226', '2021-12-13 17:04:25.884535', '80000001', 151, 1, 17),
(358, '2021-12-07 21:05:46.443802', '2021-12-07 21:05:46.443802', '10100002', 152, 1, 2),
(359, '2021-12-07 21:05:46.465957', '2021-12-07 21:05:46.465957', '10200002', 152, 1, 3),
(360, '2021-12-07 21:05:46.510390', '2021-12-07 21:05:46.510390', '10300002', 152, 1, 4),
(361, '2021-12-07 21:05:46.531375', '2021-12-07 21:05:46.531375', '10400002', 152, 1, 5),
(362, '2021-12-07 21:05:46.580345', '2021-12-07 21:05:46.580345', '10500002', 152, 1, 6),
(363, '2021-12-07 21:05:46.620319', '2021-12-07 21:05:46.620319', '70000002', 152, 1, 15),
(364, '2021-12-07 21:05:46.669091', '2021-12-07 21:05:46.669091', '80000002', 152, 1, 17),
(365, '2021-12-07 21:05:46.724803', '2021-12-07 21:05:46.724803', '10100003', 153, 1, 2),
(366, '2021-12-07 21:05:46.756806', '2021-12-07 21:05:46.756806', '10200003', 153, 1, 3),
(367, '2021-12-07 21:05:46.803231', '2021-12-07 21:05:46.803231', '10300003', 153, 1, 4),
(368, '2021-12-07 21:05:47.212305', '2021-12-07 21:05:47.212305', '10400003', 153, 1, 5),
(369, '2021-12-07 21:05:47.273948', '2021-12-07 21:05:47.273948', '10500003', 153, 1, 6),
(370, '2021-12-07 21:05:47.342177', '2021-12-07 21:05:47.343177', '70000003', 153, 1, 15),
(371, '2021-12-07 21:05:47.366983', '2021-12-07 21:05:47.366983', '80000003', 153, 1, 17),
(372, '2021-12-07 21:05:47.398625', '2021-12-07 21:05:47.398625', '10100004', 154, 1, 2),
(373, '2021-12-07 21:05:47.422060', '2021-12-07 21:05:47.422060', '10200004', 154, 1, 3),
(374, '2021-12-07 21:05:47.484379', '2021-12-07 21:05:47.484379', '10300004', 154, 1, 4),
(375, '2021-12-07 21:05:47.502349', '2021-12-07 21:05:47.503348', '10400004', 154, 1, 5),
(376, '2021-12-07 21:05:47.546186', '2021-12-07 21:05:47.546186', '10500004', 154, 1, 6),
(377, '2021-12-07 21:05:47.568752', '2021-12-07 21:05:47.568752', '70000004', 154, 1, 15),
(378, '2021-12-07 21:05:47.609402', '2021-12-07 21:05:47.609402', '80000004', 154, 1, 17),
(379, '2021-12-07 21:05:47.632476', '2021-12-07 21:05:47.632476', '10100005', 155, 1, 2),
(380, '2021-12-07 21:05:47.667235', '2021-12-07 21:05:47.667235', '10200005', 155, 1, 3),
(381, '2021-12-07 21:05:47.710210', '2021-12-07 21:05:47.710210', '10300005', 155, 1, 4),
(382, '2021-12-07 21:05:47.743185', '2021-12-07 21:05:47.743185', '10400005', 155, 1, 5),
(383, '2021-12-07 21:05:47.765171', '2021-12-07 21:05:47.766175', '10500005', 155, 1, 6),
(384, '2021-12-07 21:05:47.831132', '2021-12-07 21:05:47.831132', '70000005', 155, 1, 15),
(385, '2021-12-07 21:05:47.876100', '2021-12-07 21:05:47.876100', '80000005', 155, 1, 17),
(386, '2021-12-07 21:05:47.908724', '2021-12-07 21:05:47.908724', '10100006', 156, 1, 2),
(387, '2021-12-07 21:05:47.946753', '2021-12-07 21:05:47.946753', '10200006', 156, 1, 3),
(388, '2021-12-07 21:05:47.995803', '2021-12-07 21:05:47.996802', '10300006', 156, 1, 4),
(389, '2021-12-07 21:05:48.035904', '2021-12-07 21:05:48.035904', '10400006', 156, 1, 5),
(390, '2021-12-07 21:05:48.068404', '2021-12-07 21:05:48.068404', '10500006', 156, 1, 6),
(391, '2021-12-07 21:05:48.235090', '2021-12-07 21:05:48.235090', '70000006', 156, 1, 15),
(392, '2021-12-07 21:05:48.282195', '2021-12-07 21:05:48.282195', '80000006', 156, 1, 17),
(393, '2021-12-07 21:05:48.340089', '2021-12-07 21:05:48.340089', '10100007', 157, 1, 2),
(394, '2021-12-07 21:05:48.391298', '2021-12-07 21:05:48.391298', '10200007', 157, 1, 3),
(395, '2021-12-07 21:05:48.434911', '2021-12-07 21:05:48.434911', '10300007', 157, 1, 4),
(396, '2021-12-07 21:05:48.482198', '2021-12-07 21:05:48.482198', '10400007', 157, 1, 5),
(397, '2021-12-07 21:05:48.534768', '2021-12-07 21:05:48.534768', '10500007', 157, 1, 6),
(398, '2021-12-07 21:05:48.596651', '2021-12-07 21:05:48.596651', '70000007', 157, 1, 15),
(399, '2021-12-07 21:05:48.638805', '2021-12-07 21:05:48.638805', '80000007', 157, 1, 17),
(400, '2021-12-07 21:05:48.693570', '2021-12-07 21:05:48.693570', '10100008', 158, 1, 2),
(401, '2021-12-07 21:05:48.710978', '2021-12-07 21:05:48.710978', '10200008', 158, 1, 3),
(402, '2021-12-07 21:05:48.733477', '2021-12-07 21:05:48.733477', '10300008', 158, 1, 4),
(403, '2021-12-07 21:05:48.795693', '2021-12-07 21:05:48.796701', '10400008', 158, 1, 5),
(404, '2021-12-07 21:05:48.846977', '2021-12-07 21:05:48.846977', '10500008', 158, 1, 6),
(405, '2021-12-07 21:05:48.871779', '2021-12-07 21:05:48.871779', '70000008', 158, 1, 15),
(406, '2021-12-07 21:05:48.926730', '2021-12-07 21:05:48.926730', '80000008', 158, 1, 17),
(407, '2021-12-07 21:05:48.999678', '2021-12-07 21:05:48.999678', '10100009', 159, 1, 2),
(408, '2021-12-07 21:05:49.019665', '2021-12-07 21:05:49.019665', '10200009', 159, 1, 3),
(409, '2021-12-07 21:05:49.042653', '2021-12-07 21:05:49.042653', '10300009', 159, 1, 4),
(410, '2021-12-07 21:05:49.064640', '2021-12-07 21:05:49.064640', '10400009', 159, 1, 5),
(411, '2021-12-07 21:05:49.113916', '2021-12-07 21:05:49.113916', '10500009', 159, 1, 6),
(412, '2021-12-07 21:05:49.183840', '2021-12-07 21:05:49.183840', '70000009', 159, 1, 15),
(413, '2021-12-07 21:05:49.302644', '2021-12-07 21:05:49.302644', '80000009', 159, 1, 17),
(414, '2021-12-07 21:05:49.446553', '2021-12-07 21:05:49.446553', '10100010', 160, 1, 2),
(415, '2021-12-07 21:05:49.492413', '2021-12-07 21:05:49.492413', '10200010', 160, 1, 3),
(416, '2021-12-07 21:05:49.526241', '2021-12-07 21:05:49.526241', '10300010', 160, 1, 4),
(417, '2021-12-07 21:05:49.580052', '2021-12-07 21:05:49.580052', '10400010', 160, 1, 5),
(418, '2021-12-07 21:05:49.629145', '2021-12-07 21:05:49.629145', '10500010', 160, 1, 6),
(419, '2021-12-07 21:05:49.699749', '2021-12-07 21:05:49.699749', '70000010', 160, 1, 15),
(420, '2021-12-07 21:05:49.751387', '2021-12-07 21:05:49.751387', '80000010', 160, 1, 17),
(421, '2021-12-07 21:05:49.795586', '2021-12-07 21:05:49.795586', '10100011', 161, 1, 2),
(422, '2021-12-07 21:05:49.835202', '2021-12-07 21:05:49.835202', '10200011', 161, 1, 3),
(423, '2021-12-07 21:05:49.868712', '2021-12-07 21:05:49.868712', '10300011', 161, 1, 4),
(424, '2021-12-07 21:05:49.892990', '2021-12-07 21:05:49.892990', '10400011', 161, 1, 5),
(425, '2021-12-07 21:05:49.931871', '2021-12-07 21:05:49.931871', '10500011', 161, 1, 6),
(426, '2021-12-07 21:05:49.954713', '2021-12-07 21:05:49.954713', '70000011', 161, 1, 15),
(427, '2021-12-07 21:05:50.014145', '2021-12-07 21:05:50.014145', '80000011', 161, 1, 17),
(428, '2021-12-07 21:05:50.109513', '2021-12-07 21:05:50.109513', '10100012', 162, 1, 2),
(429, '2021-12-07 21:05:50.131496', '2021-12-07 21:05:50.131496', '10200012', 162, 1, 3),
(430, '2021-12-07 21:05:50.186462', '2021-12-07 21:05:50.186462', '10300012', 162, 1, 4),
(431, '2021-12-07 21:05:50.236338', '2021-12-07 21:05:50.236338', '10400012', 162, 1, 5),
(432, '2021-12-07 21:05:50.357615', '2021-12-07 21:05:50.357615', '10500012', 162, 1, 6),
(433, '2021-12-07 21:05:50.391116', '2021-12-07 21:05:50.391116', '70000012', 162, 1, 15),
(434, '2021-12-07 21:05:50.515228', '2021-12-07 21:05:50.515228', '80000012', 162, 1, 17),
(435, '2021-12-07 21:05:50.627252', '2021-12-07 21:05:50.627252', '10100013', 163, 1, 2),
(436, '2021-12-07 21:05:50.676377', '2021-12-07 21:05:50.676377', '10200013', 163, 1, 3),
(437, '2021-12-07 21:05:50.704382', '2021-12-07 21:05:50.704382', '10300013', 163, 1, 4),
(438, '2021-12-07 21:05:50.757346', '2021-12-07 21:05:50.757346', '10400013', 163, 1, 5),
(439, '2021-12-07 21:05:50.781091', '2021-12-07 21:05:50.781091', '10500013', 163, 1, 6),
(440, '2021-12-07 21:05:50.824006', '2021-12-07 21:05:50.824006', '70000013', 163, 1, 15),
(441, '2021-12-07 21:05:50.882964', '2021-12-07 21:05:50.882964', '80000013', 163, 1, 17),
(442, '2021-12-07 21:05:50.934884', '2021-12-07 21:05:50.934884', '10100014', 164, 1, 2),
(443, '2021-12-07 21:05:50.954511', '2021-12-07 21:05:50.954511', '10200014', 164, 1, 3),
(444, '2021-12-07 21:05:50.987168', '2021-12-07 21:05:50.988164', '10300014', 164, 1, 4),
(445, '2021-12-07 21:05:51.013456', '2021-12-07 21:05:51.013456', '10400014', 164, 1, 5),
(446, '2021-12-07 21:05:51.046281', '2021-12-07 21:05:51.046281', '10500014', 164, 1, 6),
(447, '2021-12-07 21:05:51.123638', '2021-12-07 21:05:51.123638', '70000014', 164, 1, 15),
(448, '2021-12-07 21:05:51.146888', '2021-12-07 21:05:51.146888', '80000014', 164, 1, 17),
(449, '2021-12-07 21:05:51.207697', '2021-12-07 21:05:51.207697', '10100015', 165, 1, 2),
(450, '2021-12-07 21:05:51.224495', '2021-12-07 21:05:51.225491', '10200015', 165, 1, 3),
(451, '2021-12-07 21:05:51.258944', '2021-12-07 21:05:51.258944', '10300015', 165, 1, 4),
(452, '2021-12-07 21:05:51.290903', '2021-12-07 21:05:51.290903', '10400015', 165, 1, 5),
(453, '2021-12-07 21:05:51.492861', '2021-12-07 21:05:51.493842', '10500015', 165, 1, 6),
(454, '2021-12-07 21:05:51.763436', '2021-12-07 21:05:51.763436', '70000015', 165, 1, 15),
(455, '2021-12-07 21:05:51.915782', '2021-12-07 21:05:51.915782', '80000015', 165, 1, 17),
(456, '2021-12-07 21:05:52.064954', '2021-12-07 21:05:52.064954', '10100016', 166, 1, 2),
(457, '2021-12-07 21:05:52.231951', '2021-12-07 21:05:52.231951', '10200016', 166, 1, 3),
(458, '2021-12-07 21:05:52.290519', '2021-12-07 21:05:52.291516', '10300016', 166, 1, 4),
(459, '2021-12-07 21:05:52.324236', '2021-12-07 21:05:52.324236', '10400016', 166, 1, 5),
(460, '2021-12-07 21:05:52.369309', '2021-12-07 21:05:52.369309', '10500016', 166, 1, 6),
(461, '2021-12-07 21:05:52.554039', '2021-12-07 21:05:52.554039', '70000016', 166, 1, 15),
(462, '2021-12-07 21:05:52.577024', '2021-12-07 21:05:52.577024', '80000016', 166, 1, 17),
(463, '2021-12-07 21:05:52.698862', '2021-12-07 21:05:52.698862', '10100017', 167, 1, 2),
(464, '2021-12-07 21:05:52.776645', '2021-12-07 21:05:52.776645', '10200017', 167, 1, 3),
(465, '2021-12-07 21:05:52.825526', '2021-12-07 21:05:52.825526', '10300017', 167, 1, 4),
(466, '2021-12-07 21:05:52.875991', '2021-12-07 21:05:52.875991', '10400017', 167, 1, 5),
(467, '2021-12-07 21:05:53.046722', '2021-12-07 21:05:53.046722', '10500017', 167, 1, 6),
(468, '2021-12-07 21:05:53.079515', '2021-12-07 21:05:53.079515', '70000017', 167, 1, 15),
(469, '2021-12-07 21:05:53.130176', '2021-12-07 21:05:53.130176', '80000017', 167, 1, 17),
(470, '2021-12-07 21:05:53.194403', '2021-12-07 21:05:53.194403', '10100018', 168, 1, 2),
(471, '2021-12-07 21:05:53.323706', '2021-12-07 21:05:53.323706', '10200018', 168, 1, 3),
(472, '2021-12-07 21:05:53.403462', '2021-12-07 21:05:53.403462', '10300018', 168, 1, 4),
(473, '2021-12-07 21:05:53.518230', '2021-12-07 21:05:53.518230', '10400018', 168, 1, 5),
(474, '2021-12-07 21:05:53.664629', '2021-12-07 21:05:53.664629', '10500018', 168, 1, 6),
(475, '2021-12-07 21:05:53.709602', '2021-12-07 21:05:53.709602', '70000018', 168, 1, 15),
(476, '2021-12-07 21:05:53.764567', '2021-12-07 21:05:53.764567', '80000018', 168, 1, 17),
(477, '2021-12-07 21:05:53.809413', '2021-12-07 21:05:53.809413', '10100019', 169, 1, 2),
(478, '2021-12-07 21:05:53.864456', '2021-12-07 21:05:53.864456', '10200019', 169, 1, 3),
(479, '2021-12-07 21:05:53.887213', '2021-12-07 21:05:53.887213', '10300019', 169, 1, 4),
(480, '2021-12-07 21:05:53.945900', '2021-12-07 21:05:53.945900', '10400019', 169, 1, 5),
(481, '2021-12-07 21:05:54.064159', '2021-12-07 21:05:54.064159', '10500019', 169, 1, 6),
(482, '2021-12-07 21:05:54.115193', '2021-12-07 21:05:54.115193', '70000019', 169, 1, 15),
(483, '2021-12-07 21:05:54.157916', '2021-12-07 21:05:54.157916', '80000019', 169, 1, 17),
(484, '2021-12-07 21:05:54.216052', '2021-12-07 21:05:54.216052', '10100020', 170, 1, 2),
(485, '2021-12-07 21:05:54.266312', '2021-12-07 21:05:54.266312', '10200020', 170, 1, 3),
(486, '2021-12-07 21:05:54.298932', '2021-12-07 21:05:54.299932', '10300020', 170, 1, 4),
(487, '2021-12-07 21:05:54.321714', '2021-12-07 21:05:54.321714', '10400020', 170, 1, 5),
(488, '2021-12-07 21:05:54.354545', '2021-12-07 21:05:54.354545', '10500020', 170, 1, 6),
(489, '2021-12-07 21:05:54.388470', '2021-12-07 21:05:54.388470', '70000020', 170, 1, 15),
(490, '2021-12-07 21:05:54.474186', '2021-12-07 21:05:54.474186', '80000020', 170, 1, 17),
(491, '2021-12-07 21:05:54.502688', '2021-12-07 21:05:54.502688', '10100021', 171, 1, 2),
(492, '2021-12-07 21:05:54.564084', '2021-12-07 21:05:54.564084', '10200021', 171, 1, 3),
(493, '2021-12-07 21:05:54.842960', '2021-12-07 21:05:54.842960', '10300021', 171, 1, 4),
(494, '2021-12-07 21:05:54.887932', '2021-12-07 21:05:54.887932', '10400021', 171, 1, 5),
(495, '2021-12-07 21:05:54.919911', '2021-12-07 21:05:54.919911', '10500021', 171, 1, 6),
(496, '2021-12-07 21:05:54.965218', '2021-12-07 21:05:54.965218', '70000021', 171, 1, 15),
(497, '2021-12-07 21:05:55.179133', '2021-12-07 21:05:55.180132', '80000021', 171, 1, 17),
(498, '2021-12-07 21:05:55.237466', '2021-12-07 21:05:55.237466', '10100022', 172, 1, 2),
(499, '2021-12-07 21:05:55.276720', '2021-12-07 21:05:55.276720', '10200022', 172, 1, 3),
(500, '2021-12-07 21:05:55.313587', '2021-12-07 21:05:55.313587', '10300022', 172, 1, 4),
(501, '2021-12-07 21:05:55.346421', '2021-12-07 21:05:55.346421', '10400022', 172, 1, 5),
(502, '2021-12-07 21:05:55.396664', '2021-12-07 21:05:55.396664', '10500022', 172, 1, 6),
(503, '2021-12-07 21:05:55.452087', '2021-12-07 21:05:55.452087', '70000022', 172, 1, 15),
(504, '2021-12-07 21:05:55.546934', '2021-12-07 21:05:55.546934', '80000022', 172, 1, 17),
(505, '2021-12-07 21:05:55.580373', '2021-12-07 21:05:55.580373', '10100023', 173, 1, 2),
(506, '2021-12-07 21:05:55.642034', '2021-12-07 21:05:55.643033', '10200023', 173, 1, 3),
(507, '2021-12-07 21:05:55.702617', '2021-12-07 21:05:55.702617', '10300023', 173, 1, 4),
(508, '2021-12-07 21:05:55.735597', '2021-12-07 21:05:55.735597', '10400023', 173, 1, 5),
(509, '2021-12-07 21:05:55.765895', '2021-12-07 21:05:55.765895', '10500023', 173, 1, 6),
(510, '2021-12-07 21:05:55.799024', '2021-12-07 21:05:55.799024', '70000023', 173, 1, 15),
(511, '2021-12-07 21:05:55.902248', '2021-12-07 21:05:55.902248', '80000023', 173, 1, 17),
(512, '2021-12-07 21:05:56.032214', '2021-12-07 21:05:56.032214', '10100024', 174, 1, 2),
(513, '2021-12-07 21:05:56.198695', '2021-12-07 21:05:56.198695', '10200024', 174, 1, 3),
(514, '2021-12-07 21:05:56.249189', '2021-12-07 21:05:56.249189', '10300024', 174, 1, 4),
(515, '2021-12-07 21:05:56.291239', '2021-12-07 21:05:56.291239', '10400024', 174, 1, 5),
(516, '2021-12-07 21:05:56.353870', '2021-12-07 21:05:56.353870', '10500024', 174, 1, 6),
(517, '2021-12-07 21:05:56.574544', '2021-12-07 21:05:56.574544', '70000024', 174, 1, 15),
(518, '2021-12-07 21:05:56.610805', '2021-12-07 21:05:56.610805', '80000024', 174, 1, 17),
(519, '2021-12-07 21:05:56.646849', '2021-12-07 21:05:56.646849', '10100025', 175, 1, 2),
(520, '2021-12-07 21:05:56.680601', '2021-12-07 21:05:56.681609', '10200025', 175, 1, 3),
(521, '2021-12-07 21:05:56.713389', '2021-12-07 21:05:56.713389', '10300025', 175, 1, 4),
(522, '2021-12-07 21:05:56.747386', '2021-12-07 21:05:56.748387', '10400025', 175, 1, 5),
(523, '2021-12-07 21:05:56.779369', '2021-12-07 21:05:56.779369', '10500025', 175, 1, 6),
(524, '2021-12-07 21:05:56.810864', '2021-12-07 21:05:56.810864', '70000025', 175, 1, 15),
(525, '2021-12-07 21:05:56.844721', '2021-12-07 21:05:56.844721', '80000025', 175, 1, 17),
(526, '2021-12-07 21:05:56.880661', '2021-12-07 21:05:56.880661', '10100026', 176, 1, 2),
(527, '2021-12-07 21:05:56.913408', '2021-12-07 21:05:56.913408', '10200026', 176, 1, 3),
(528, '2021-12-07 21:05:56.936186', '2021-12-07 21:05:56.936186', '10300026', 176, 1, 4),
(529, '2021-12-07 21:05:56.970204', '2021-12-07 21:05:56.970204', '10400026', 176, 1, 5),
(530, '2021-12-07 21:05:57.468605', '2021-12-07 21:05:57.468605', '10500026', 176, 1, 6),
(531, '2021-12-07 21:05:57.517413', '2021-12-07 21:05:57.517413', '70000026', 176, 1, 15),
(532, '2021-12-07 21:05:57.576266', '2021-12-07 21:05:57.576266', '80000026', 176, 1, 17),
(533, '2021-12-07 21:05:57.626167', '2021-12-07 21:05:57.626167', '10100027', 177, 1, 2),
(534, '2021-12-07 21:05:57.685793', '2021-12-07 21:05:57.685793', '10200027', 177, 1, 3),
(535, '2021-12-07 21:05:57.702411', '2021-12-07 21:05:57.702411', '10300027', 177, 1, 4),
(536, '2021-12-07 21:05:57.735647', '2021-12-07 21:05:57.735647', '10400027', 177, 1, 5),
(537, '2021-12-07 21:05:57.784026', '2021-12-07 21:05:57.784026', '10500027', 177, 1, 6),
(538, '2021-12-07 21:05:57.811399', '2021-12-07 21:05:57.812398', '70000027', 177, 1, 15),
(539, '2021-12-07 21:05:57.859449', '2021-12-07 21:05:57.859449', '80000027', 177, 1, 17),
(540, '2021-12-07 21:05:57.915203', '2021-12-07 21:05:57.915203', '10100028', 178, 1, 2),
(541, '2021-12-07 21:05:57.949881', '2021-12-07 21:05:57.949881', '10200028', 178, 1, 3),
(542, '2021-12-07 21:05:57.991501', '2021-12-07 21:05:57.991501', '10300028', 178, 1, 4),
(543, '2021-12-07 21:05:58.025467', '2021-12-07 21:05:58.026468', '10400028', 178, 1, 5),
(544, '2021-12-07 21:05:58.058217', '2021-12-07 21:05:58.058217', '10500028', 178, 1, 6),
(545, '2021-12-07 21:05:58.092149', '2021-12-07 21:05:58.092149', '70000028', 178, 1, 15),
(546, '2021-12-07 21:05:58.124741', '2021-12-07 21:05:58.124741', '80000028', 178, 1, 17),
(547, '2021-12-07 21:05:58.158653', '2021-12-07 21:05:58.158653', '10100029', 179, 1, 2),
(548, '2021-12-07 21:05:58.191632', '2021-12-07 21:05:58.191632', '10200029', 179, 1, 3),
(549, '2021-12-07 21:05:58.255485', '2021-12-07 21:05:58.256483', '10300029', 179, 1, 4),
(550, '2021-12-07 21:05:58.324822', '2021-12-07 21:05:58.324822', '10400029', 179, 1, 5),
(551, '2021-12-07 21:05:58.432552', '2021-12-07 21:05:58.432552', '10500029', 179, 1, 6),
(552, '2021-12-07 21:05:58.582736', '2021-12-07 21:05:58.582736', '70000029', 179, 1, 15),
(553, '2021-12-07 21:05:58.633171', '2021-12-07 21:05:58.633171', '80000029', 179, 1, 17),
(554, '2021-12-07 21:05:58.686049', '2021-12-07 21:05:58.687046', '10100030', 180, 1, 2),
(555, '2021-12-07 21:05:58.730389', '2021-12-07 21:05:58.730389', '10200030', 180, 1, 3),
(556, '2021-12-07 21:05:58.776098', '2021-12-07 21:05:58.777099', '10300030', 180, 1, 4),
(557, '2021-12-07 21:05:58.811326', '2021-12-07 21:05:58.811326', '10400030', 180, 1, 5),
(558, '2021-12-07 21:05:58.855676', '2021-12-07 21:05:58.855676', '10500030', 180, 1, 6),
(559, '2021-12-07 21:05:58.892355', '2021-12-07 21:05:58.892355', '70000030', 180, 1, 15),
(560, '2021-12-07 21:05:58.937015', '2021-12-07 21:05:58.937015', '80000030', 180, 1, 17),
(561, '2021-12-07 21:05:58.958579', '2021-12-07 21:05:58.958579', '10100031', 181, 1, 2),
(562, '2021-12-07 21:05:58.992202', '2021-12-07 21:05:58.992202', '10200031', 181, 1, 3),
(563, '2021-12-07 21:05:59.025817', '2021-12-07 21:05:59.025817', '10300031', 181, 1, 4),
(564, '2021-12-07 21:05:59.057468', '2021-12-07 21:05:59.057468', '10400031', 181, 1, 5),
(565, '2021-12-07 21:05:59.092089', '2021-12-07 21:05:59.092089', '10500031', 181, 1, 6),
(566, '2021-12-07 21:05:59.124917', '2021-12-07 21:05:59.124917', '70000031', 181, 1, 15),
(567, '2021-12-07 21:05:59.159318', '2021-12-07 21:05:59.159318', '80000031', 181, 1, 17),
(568, '2021-12-07 21:05:59.192944', '2021-12-07 21:05:59.192944', '10100032', 182, 1, 2),
(569, '2021-12-07 21:05:59.226741', '2021-12-07 21:05:59.226741', '10200032', 182, 1, 3),
(570, '2021-12-07 21:05:59.255764', '2021-12-07 21:05:59.255764', '10300032', 182, 1, 4),
(571, '2021-12-07 21:05:59.289674', '2021-12-07 21:05:59.289674', '10400032', 182, 1, 5),
(572, '2021-12-07 21:05:59.322446', '2021-12-07 21:05:59.323446', '10500032', 182, 1, 6),
(573, '2021-12-07 21:05:59.359344', '2021-12-07 21:05:59.360343', '70000032', 182, 1, 15),
(574, '2021-12-07 21:05:59.513335', '2021-12-07 21:05:59.513335', '80000032', 182, 1, 17),
(575, '2021-12-07 21:05:59.654288', '2021-12-07 21:05:59.654288', '10100033', 183, 1, 2),
(576, '2021-12-07 21:05:59.766398', '2021-12-07 21:05:59.766398', '10200033', 183, 1, 3),
(577, '2021-12-07 21:05:59.832124', '2021-12-07 21:05:59.832124', '10300033', 183, 1, 4),
(578, '2021-12-07 21:05:59.891149', '2021-12-07 21:05:59.892163', '10400033', 183, 1, 5),
(579, '2021-12-07 21:05:59.948287', '2021-12-07 21:05:59.948287', '10500033', 183, 1, 6),
(580, '2021-12-07 21:05:59.982083', '2021-12-07 21:05:59.982083', '70000033', 183, 1, 15),
(581, '2021-12-07 21:06:00.038666', '2021-12-07 21:06:00.038666', '80000033', 183, 1, 17),
(582, '2021-12-07 21:06:00.065907', '2021-12-07 21:06:00.065907', '10100034', 184, 1, 2),
(583, '2021-12-07 21:06:00.102873', '2021-12-07 21:06:00.102873', '10200034', 184, 1, 3),
(584, '2021-12-07 21:06:00.153157', '2021-12-07 21:06:00.153157', '10300034', 184, 1, 4),
(585, '2021-12-07 21:06:00.182895', '2021-12-07 21:06:00.182895', '10400034', 184, 1, 5),
(586, '2021-12-07 21:06:00.236216', '2021-12-07 21:06:00.236216', '10500034', 184, 1, 6),
(587, '2021-12-07 21:06:00.270834', '2021-12-07 21:06:00.270834', '70000034', 184, 1, 15),
(588, '2021-12-07 21:06:00.300812', '2021-12-07 21:06:00.300812', '80000034', 184, 1, 17),
(589, '2021-12-07 21:06:00.333385', '2021-12-07 21:06:00.333385', '10100035', 185, 1, 2),
(590, '2021-12-07 21:06:00.372079', '2021-12-07 21:06:00.372079', '10200035', 185, 1, 3),
(591, '2021-12-07 21:06:00.427654', '2021-12-07 21:06:00.427654', '10300035', 185, 1, 4),
(592, '2021-12-07 21:06:00.481338', '2021-12-07 21:06:00.481338', '10400035', 185, 1, 5),
(593, '2021-12-07 21:06:00.541834', '2021-12-07 21:06:00.541834', '10500035', 185, 1, 6),
(594, '2021-12-07 21:06:00.613856', '2021-12-07 21:06:00.614851', '70000035', 185, 1, 15),
(595, '2021-12-07 21:06:00.936280', '2021-12-07 21:06:00.936280', '80000035', 185, 1, 17),
(596, '2021-12-07 21:06:01.114346', '2021-12-07 21:06:01.114346', '10100036', 186, 1, 2),
(597, '2021-12-07 21:06:01.159816', '2021-12-07 21:06:01.159816', '10200036', 186, 1, 3),
(598, '2021-12-07 21:06:01.220650', '2021-12-07 21:06:01.220650', '10300036', 186, 1, 4),
(599, '2021-12-07 21:06:01.259228', '2021-12-07 21:06:01.259228', '10400036', 186, 1, 5),
(600, '2021-12-07 21:06:01.314294', '2021-12-07 21:06:01.314294', '10500036', 186, 1, 6),
(601, '2021-12-07 21:06:01.344051', '2021-12-07 21:06:01.344051', '70000036', 186, 1, 15),
(602, '2021-12-07 21:06:01.378364', '2021-12-07 21:06:01.378364', '80000036', 186, 1, 17),
(603, '2021-12-07 21:06:01.435408', '2021-12-07 21:06:01.436406', '10100037', 187, 1, 2),
(604, '2021-12-07 21:06:01.494048', '2021-12-07 21:06:01.494048', '10200037', 187, 1, 3),
(605, '2021-12-07 21:06:01.552932', '2021-12-07 21:06:01.552932', '10300037', 187, 1, 4),
(606, '2021-12-07 21:06:01.614718', '2021-12-07 21:06:01.614718', '10400037', 187, 1, 5),
(607, '2021-12-07 21:06:01.697788', '2021-12-07 21:06:01.697788', '10500037', 187, 1, 6),
(608, '2021-12-07 21:06:01.906426', '2021-12-07 21:06:01.907425', '70000037', 187, 1, 15),
(609, '2021-12-07 21:06:01.977382', '2021-12-07 21:06:01.977382', '80000037', 187, 1, 17),
(610, '2021-12-07 21:06:02.032346', '2021-12-07 21:06:02.032346', '10100038', 188, 1, 2),
(611, '2021-12-07 21:06:02.213885', '2021-12-07 21:06:02.213885', '10200038', 188, 1, 3),
(612, '2021-12-07 21:06:02.416131', '2021-12-07 21:06:02.416131', '10300038', 188, 1, 4),
(613, '2021-12-07 21:06:02.491812', '2021-12-07 21:06:02.491812', '10400038', 188, 1, 5),
(614, '2021-12-07 21:06:02.548952', '2021-12-07 21:06:02.548952', '10500038', 188, 1, 6),
(615, '2021-12-07 21:06:02.580704', '2021-12-07 21:06:02.580704', '70000038', 188, 1, 15),
(616, '2021-12-07 21:06:02.611655', '2021-12-07 21:06:02.611655', '80000038', 188, 1, 17),
(617, '2021-12-07 21:06:02.644379', '2021-12-07 21:06:02.644379', '10100039', 189, 1, 2),
(618, '2021-12-07 21:06:02.696790', '2021-12-07 21:06:02.696790', '10200039', 189, 1, 3),
(619, '2021-12-07 21:06:02.742356', '2021-12-07 21:06:02.742356', '10300039', 189, 1, 4),
(620, '2021-12-07 21:06:02.772222', '2021-12-07 21:06:02.772222', '10400039', 189, 1, 5),
(621, '2021-12-07 21:06:02.839101', '2021-12-07 21:06:02.840100', '10500039', 189, 1, 6),
(622, '2021-12-07 21:06:02.965608', '2021-12-07 21:06:02.965608', '70000039', 189, 1, 15),
(623, '2021-12-07 21:06:03.012538', '2021-12-07 21:06:03.012538', '80000039', 189, 1, 17),
(624, '2021-12-07 21:06:03.047466', '2021-12-07 21:06:03.047466', '10100040', 190, 1, 2),
(625, '2021-12-07 21:06:03.080247', '2021-12-07 21:06:03.080247', '10200040', 190, 1, 3),
(626, '2021-12-07 21:06:03.133056', '2021-12-07 21:06:03.133056', '10300040', 190, 1, 4),
(627, '2021-12-07 21:06:03.165035', '2021-12-07 21:06:03.165035', '10400040', 190, 1, 5),
(628, '2021-12-07 21:06:03.199014', '2021-12-07 21:06:03.199014', '10500040', 190, 1, 6),
(629, '2021-12-07 21:06:03.254982', '2021-12-07 21:06:03.254982', '70000040', 190, 1, 15),
(630, '2021-12-07 21:06:03.299282', '2021-12-07 21:06:03.299282', '80000040', 190, 1, 17),
(631, '2021-12-07 21:06:03.331912', '2021-12-07 21:06:03.331912', '10100041', 191, 1, 2),
(632, '2021-12-07 21:06:03.369009', '2021-12-07 21:06:03.369009', '10200041', 191, 1, 3),
(633, '2021-12-07 21:06:04.293683', '2021-12-07 21:06:04.293683', '10300041', 191, 1, 4),
(634, '2021-12-07 21:06:04.477023', '2021-12-07 21:06:04.477023', '10400041', 191, 1, 5),
(635, '2021-12-07 21:06:04.533005', '2021-12-07 21:06:04.533005', '10500041', 191, 1, 6),
(636, '2021-12-07 21:06:04.594280', '2021-12-07 21:06:04.594280', '70000041', 191, 1, 15),
(637, '2021-12-07 21:06:04.658847', '2021-12-07 21:06:04.658847', '80000041', 191, 1, 17),
(638, '2021-12-07 21:06:04.708943', '2021-12-07 21:06:04.708943', '10100042', 192, 1, 2),
(639, '2021-12-07 21:06:04.764753', '2021-12-07 21:06:04.764753', '10200042', 192, 1, 3),
(640, '2021-12-07 21:06:04.826019', '2021-12-07 21:06:04.826019', '10300042', 192, 1, 4),
(641, '2021-12-07 21:06:04.859542', '2021-12-07 21:06:04.859542', '10400042', 192, 1, 5),
(642, '2021-12-07 21:06:05.014536', '2021-12-07 21:06:05.014536', '10500042', 192, 1, 6),
(643, '2021-12-07 21:06:05.064962', '2021-12-07 21:06:05.064962', '70000042', 192, 1, 15),
(644, '2021-12-07 21:06:05.092352', '2021-12-07 21:06:05.092352', '80000042', 192, 1, 17),
(645, '2021-12-07 21:06:05.128016', '2021-12-07 21:06:05.128016', '10100043', 193, 1, 2),
(646, '2021-12-07 21:06:05.181200', '2021-12-07 21:06:05.181200', '10200043', 193, 1, 3),
(647, '2021-12-07 21:06:05.232084', '2021-12-07 21:06:05.233092', '10300043', 193, 1, 4),
(648, '2021-12-07 21:06:05.299291', '2021-12-07 21:06:05.299291', '10400043', 193, 1, 5),
(649, '2021-12-07 21:06:05.336381', '2021-12-07 21:06:05.336381', '10500043', 193, 1, 6),
(650, '2021-12-07 21:06:05.423317', '2021-12-07 21:06:05.423317', '70000043', 193, 1, 15),
(651, '2021-12-07 21:06:05.587425', '2021-12-07 21:06:05.587425', '80000043', 193, 1, 17),
(652, '2021-12-07 21:06:05.632751', '2021-12-07 21:06:05.632751', '10100044', 194, 1, 2),
(653, '2021-12-07 21:06:05.699546', '2021-12-07 21:06:05.699546', '10200044', 194, 1, 3),
(654, '2021-12-07 21:06:05.736263', '2021-12-07 21:06:05.736263', '10300044', 194, 1, 4),
(655, '2021-12-07 21:06:05.770212', '2021-12-07 21:06:05.770212', '10400044', 194, 1, 5),
(656, '2021-12-07 21:06:05.802927', '2021-12-07 21:06:05.802927', '10500044', 194, 1, 6),
(657, '2021-12-07 21:06:05.837279', '2021-12-07 21:06:05.837279', '70000044', 194, 1, 15),
(658, '2021-12-07 21:06:05.900315', '2021-12-07 21:06:05.900315', '80000044', 194, 1, 17),
(659, '2021-12-07 21:06:06.049213', '2021-12-07 21:06:06.050217', '10100045', 195, 1, 2),
(660, '2021-12-07 21:06:06.099300', '2021-12-07 21:06:06.099300', '10200045', 195, 1, 3),
(661, '2021-12-07 21:06:06.136875', '2021-12-07 21:06:06.136875', '10300045', 195, 1, 4),
(662, '2021-12-07 21:06:06.189902', '2021-12-07 21:06:06.189902', '10400045', 195, 1, 5),
(663, '2021-12-07 21:06:06.265839', '2021-12-07 21:06:06.265839', '10500045', 195, 1, 6),
(664, '2021-12-07 21:06:06.332545', '2021-12-07 21:06:06.332545', '70000045', 195, 1, 15),
(665, '2021-12-07 21:06:06.394539', '2021-12-07 21:06:06.394539', '80000045', 195, 1, 17),
(666, '2021-12-07 21:06:06.470828', '2021-12-07 21:06:06.471826', '10100046', 196, 1, 2),
(667, '2021-12-07 21:06:06.677318', '2021-12-07 21:06:06.677318', '10200046', 196, 1, 3),
(668, '2021-12-07 21:06:06.743275', '2021-12-07 21:06:06.743275', '10300046', 196, 1, 4),
(669, '2021-12-07 21:06:06.794245', '2021-12-07 21:06:06.794245', '10400046', 196, 1, 5),
(670, '2021-12-07 21:06:06.843970', '2021-12-07 21:06:06.843970', '10500046', 196, 1, 6),
(671, '2021-12-07 21:06:06.909856', '2021-12-07 21:06:06.909856', '70000046', 196, 1, 15),
(672, '2021-12-07 21:06:06.954798', '2021-12-07 21:06:06.954798', '80000046', 196, 1, 17),
(673, '2021-12-07 21:06:07.126690', '2021-12-07 21:06:07.126690', '10100047', 197, 1, 2),
(674, '2021-12-07 21:06:07.206814', '2021-12-07 21:06:07.206814', '10200047', 197, 1, 3),
(675, '2021-12-07 21:06:07.248379', '2021-12-07 21:06:07.248379', '10300047', 197, 1, 4),
(676, '2021-12-07 21:06:07.302822', '2021-12-07 21:06:07.302822', '10400047', 197, 1, 5),
(677, '2021-12-07 21:06:07.360158', '2021-12-07 21:06:07.361156', '10500047', 197, 1, 6),
(678, '2021-12-07 21:06:07.392673', '2021-12-07 21:06:07.393673', '70000047', 197, 1, 15),
(679, '2021-12-07 21:06:07.427633', '2021-12-07 21:06:07.427633', '80000047', 197, 1, 17),
(680, '2021-12-07 21:06:07.480749', '2021-12-07 21:06:07.480749', '10100048', 198, 1, 2),
(681, '2021-12-07 21:06:07.538185', '2021-12-07 21:06:07.538185', '10200048', 198, 1, 3),
(682, '2021-12-07 21:06:07.660187', '2021-12-07 21:06:07.661185', '10300048', 198, 1, 4),
(683, '2021-12-07 21:06:07.703454', '2021-12-07 21:06:07.703454', '10400048', 198, 1, 5),
(684, '2021-12-07 21:06:07.897922', '2021-12-07 21:06:07.897922', '10500048', 198, 1, 6),
(685, '2021-12-07 21:06:07.931901', '2021-12-07 21:06:07.931901', '70000048', 198, 1, 15),
(686, '2021-12-07 21:06:07.965878', '2021-12-07 21:06:07.965878', '80000048', 198, 1, 17),
(687, '2021-12-07 21:06:07.998938', '2021-12-07 21:06:07.998938', '10100049', 199, 1, 2),
(688, '2021-12-07 21:06:08.204626', '2021-12-07 21:06:08.204626', '10200049', 199, 1, 3),
(689, '2021-12-07 21:06:08.347469', '2021-12-07 21:06:08.347469', '10300049', 199, 1, 4),
(690, '2021-12-07 21:06:08.407537', '2021-12-07 21:06:08.407537', '10400049', 199, 1, 5),
(691, '2021-12-07 21:06:08.446539', '2021-12-07 21:06:08.446539', '10500049', 199, 1, 6),
(692, '2021-12-07 21:06:08.481405', '2021-12-07 21:06:08.481405', '70000049', 199, 1, 15),
(693, '2021-12-07 21:06:08.514187', '2021-12-07 21:06:08.514187', '80000049', 199, 1, 17),
(694, '2021-12-07 21:06:08.548329', '2021-12-07 21:06:08.548329', '10100050', 200, 1, 2),
(695, '2021-12-07 21:06:08.578912', '2021-12-07 21:06:08.578912', '10200050', 200, 1, 3),
(696, '2021-12-07 21:06:08.771580', '2021-12-07 21:06:08.772581', '10300050', 200, 1, 4),
(697, '2021-12-07 21:06:08.848137', '2021-12-07 21:06:08.848137', '10400050', 200, 1, 5),
(698, '2021-12-07 21:06:08.881055', '2021-12-07 21:06:08.881055', '10500050', 200, 1, 6),
(699, '2021-12-07 21:06:08.937286', '2021-12-07 21:06:08.938285', '70000050', 200, 1, 15),
(700, '2021-12-07 21:06:08.992755', '2021-12-07 21:06:08.992755', '80000050', 200, 1, 17),
(702, '2021-12-16 08:55:16.656079', '2021-12-16 08:55:16.657089', '70005000', 203, 1, 15),
(703, '2021-12-16 08:55:16.907924', '2021-12-16 08:55:16.907924', '80005000', 203, 1, 17),
(704, '2021-12-16 09:10:41.490318', '2021-12-16 09:10:41.490318', '70005001', 204, 1, 15),
(705, '2021-12-16 09:10:41.968083', '2021-12-16 09:10:41.968083', '80005001', 204, 1, 17),
(706, '2021-12-16 09:33:16.318948', '2021-12-16 09:33:16.318948', '70005002', 205, 1, 15),
(707, '2021-12-16 09:41:05.240627', '2021-12-16 09:41:05.241628', '70005003', 206, 1, 15),
(708, '2021-12-16 09:41:05.707959', '2021-12-16 09:41:05.707959', '80005003', 206, 1, 17),
(709, '2021-12-16 09:50:24.227328', '2021-12-16 09:50:24.227328', '70005004', 207, 1, 15),
(710, '2021-12-16 10:06:53.144936', '2021-12-16 10:06:53.144936', '70005005', 209, 1, 15),
(711, '2021-12-16 10:06:53.466945', '2021-12-16 10:06:53.466945', '80005005', 209, 1, 17),
(713, '2021-12-31 11:40:50.727133', '2021-12-31 11:40:50.727133', '60000001', 151, 1, 14),
(714, '2022-01-10 17:21:59.970211', '2022-01-10 17:21:59.970211', '60000004', 154, 1, 14),
(715, '2022-01-10 18:56:22.285632', '2022-01-10 18:56:22.285632', '60000005', 155, 1, 14),
(716, '2022-01-17 04:03:15.853524', '2022-01-17 04:03:15.853524', '60000002', 152, 1, 14);

-- --------------------------------------------------------

--
-- Table structure for table `members_bank_accounts`
--

CREATE TABLE `members_bank_accounts` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `account_name` varchar(255) NOT NULL,
  `account_number` varchar(255) NOT NULL,
  `account_type_id` int(11) DEFAULT NULL,
  `bank_id` int(11) DEFAULT NULL,
  `lock_status_id` int(11) NOT NULL,
  `member_id_id` int(11) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `members_cash_deposits`
--

CREATE TABLE `members_cash_deposits` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `payment_reference` varchar(255) NOT NULL,
  `purpose` longtext NOT NULL,
  `payment_evidience` varchar(100) DEFAULT NULL,
  `payment_date` date NOT NULL,
  `bank_accounts_id` int(11) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL,
  `receipt` varchar(255) DEFAULT NULL,
  `account_number` varchar(255) DEFAULT NULL,
  `transaction_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members_cash_deposits`
--

INSERT INTO `members_cash_deposits` (`id`, `created_at`, `updated_at`, `amount`, `payment_reference`, `purpose`, `payment_evidience`, `payment_date`, `bank_accounts_id`, `member_id`, `processed_by_id`, `status_id`, `receipt`, `account_number`, `transaction_id`) VALUES
(16, '2021-12-15 03:37:04.354161', '2021-12-15 03:37:04.355161', '3600.00', 'tttrrrr', 'rttrtrtr', '/media/avatar2_tBNcWrS.png', '2021-12-15', 1, 151, 9, 1, '00001', '80000001', 17),
(17, '2021-12-15 04:29:50.031630', '2021-12-15 04:29:50.031630', '190000.00', '666656544', 'ok', '/media/photo1_GZU0MnQ.png', '2021-12-15', 1, 151, 9, 1, '00006', '70000001', 17),
(18, '2021-12-15 04:52:04.715359', '2021-12-15 04:52:04.715359', '50000.00', 'fgfg', 'yttyty', '/media/avatar5_ljXmDcM.png', '2021-12-15', 1, 151, 9, 1, 'C-00269', '70000001', 15),
(21, '2021-12-16 10:56:30.739991', '2021-12-16 10:56:30.739991', '50000.00', '5656565656', '5 share(s) at a unit cost 10000.00', '/media/photo2_9odETzV.png', '2021-12-16', 1, 152, 9, 1, 'C-00281', '70000002', 15);

-- --------------------------------------------------------

--
-- Table structure for table `members_cash_sales_selected`
--

CREATE TABLE `members_cash_sales_selected` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `ticket` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `unit_selling_price` decimal(20,2) NOT NULL,
  `total` decimal(20,2) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members_cash_sales_selected`
--

INSERT INTO `members_cash_sales_selected` (`id`, `created_at`, `updated_at`, `ticket`, `quantity`, `unit_selling_price`, `total`, `member_id`, `processed_by_id`, `product_id`, `status_id`) VALUES
(1, '2022-01-10 21:20:29.545354', '2022-01-10 21:20:29.545354', '2022110222029', 2, '2300.00', '4600.00', 176, 12, 917, 2),
(2, '2022-01-10 21:20:48.049507', '2022-01-10 21:20:48.049507', '2022110222029', 5, '700.00', '3500.00', 176, 12, 971, 2),
(3, '2022-01-10 21:21:02.221466', '2022-01-10 21:21:02.221466', '2022110222029', 5, '2100.00', '10500.00', 176, 12, 986, 2),
(4, '2022-01-17 03:51:41.932234', '2022-01-17 03:51:41.932234', '202211745141', 5, '2300.00', '11500.00', 151, 13, 917, 2);

-- --------------------------------------------------------

--
-- Table structure for table `members_cash_withdrawals`
--

CREATE TABLE `members_cash_withdrawals` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `ledger_balance` decimal(20,2) NOT NULL,
  `narration` longtext NOT NULL,
  `approved_amount` decimal(20,2) NOT NULL,
  `approval_comment` longtext DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `maturity_date` date DEFAULT NULL,
  `approval_officer_id` int(11) DEFAULT NULL,
  `approval_status_id` int(11) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `members_cash_withdrawals_application`
--

CREATE TABLE `members_cash_withdrawals_application` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `ledger_balance` decimal(20,2) NOT NULL,
  `narration` longtext NOT NULL,
  `approved_amount` decimal(20,2) NOT NULL,
  `approval_comment` longtext DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `maturity_date` date DEFAULT NULL,
  `approval_officer_id` int(11) DEFAULT NULL,
  `approval_status_id` int(11) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL,
  `certification_officer_id` int(11) DEFAULT NULL,
  `certification_status_id` int(11) NOT NULL,
  `certification_comment` longtext DEFAULT NULL,
  `certification_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members_cash_withdrawals_application`
--

INSERT INTO `members_cash_withdrawals_application` (`id`, `created_at`, `updated_at`, `amount`, `ledger_balance`, `narration`, `approved_amount`, `approval_comment`, `approval_date`, `maturity_date`, `approval_officer_id`, `approval_status_id`, `member_id`, `processed_by_id`, `status_id`, `certification_officer_id`, `certification_status_id`, `certification_comment`, `certification_date`) VALUES
(2, '2021-12-15 04:54:35.113214', '2021-12-15 21:15:16.314518', '200000.00', '500000.00', 'for your consideration', '200000.00', 'Please Process', NULL, '2022-01-15', 4, 2, 355, 9, 2, 1, 2, NULL, '2021-12-15');

-- --------------------------------------------------------

--
-- Table structure for table `members_cash_withdrawals_main`
--

CREATE TABLE `members_cash_withdrawals_main` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `payment_date` date DEFAULT NULL,
  `cheque_number` varchar(255) DEFAULT NULL,
  `disbursement_date` date DEFAULT NULL,
  `channel_id` int(11) DEFAULT NULL,
  `coop_account_id` int(11) DEFAULT NULL,
  `disbursement_officer_id` int(11) DEFAULT NULL,
  `disbursement_status_id` int(11) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `member_account_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members_cash_withdrawals_main`
--

INSERT INTO `members_cash_withdrawals_main` (`id`, `created_at`, `updated_at`, `payment_date`, `cheque_number`, `disbursement_date`, `channel_id`, `coop_account_id`, `disbursement_officer_id`, `disbursement_status_id`, `member_id`, `member_account_id`, `processed_by_id`, `status_id`) VALUES
(4, '2021-12-15 21:15:16.247911', '2021-12-15 21:15:16.247911', '2021-12-15', '5654545454545454', NULL, 2, 1, 1, 1, 2, NULL, 7, 1);

-- --------------------------------------------------------

--
-- Table structure for table `members_credit_purchase_analysis`
--

CREATE TABLE `members_credit_purchase_analysis` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `particulars` varchar(255) DEFAULT NULL,
  `debit` decimal(20,2) NOT NULL,
  `credit` decimal(20,2) NOT NULL,
  `status_id` int(11) DEFAULT NULL,
  `trans_code_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members_credit_purchase_analysis`
--

INSERT INTO `members_credit_purchase_analysis` (`id`, `created_at`, `updated_at`, `particulars`, `debit`, `credit`, `status_id`, `trans_code_id`) VALUES
(34, '2022-01-06 07:25:02.859395', '2022-01-06 07:25:02.859395', 'Salary as at 12/16/2021', '0.00', '250000.00', 1, 4),
(35, '2022-01-06 07:25:02.926413', '2022-01-06 07:25:02.926413', 'ORDINARY SAVINGS', '15000.00', '0.00', 1, 4),
(36, '2022-01-06 07:25:03.092353', '2022-01-06 07:25:03.092353', 'PROJECT SAVINGS', '15000.00', '0.00', 1, 4),
(37, '2022-01-06 07:25:03.146386', '2022-01-06 07:25:03.146386', 'XMAS SAVINGS', '5000.00', '0.00', 1, 4),
(38, '2022-01-06 07:25:03.200446', '2022-01-06 07:25:03.200446', 'SHORT TERM LOAN', '35000.00', '0.00', 1, 4),
(39, '2022-01-06 07:25:03.266436', '2022-01-06 07:25:03.266436', 'LONG TERM LOAN', '50000.00', '0.00', 1, 4),
(40, '2022-01-10 17:20:10.275029', '2022-01-10 17:20:10.275029', 'Salary as at 01/10/2022', '0.00', '158000.00', 1, 7),
(41, '2022-01-10 17:20:10.389607', '2022-01-10 17:20:10.389607', 'ORDINARY SAVINGS', '10000.00', '0.00', 1, 7),
(42, '2022-01-10 18:45:59.017090', '2022-01-10 18:45:59.017090', 'Salary as at 01/10/2022', '0.00', '200000.00', 1, 9),
(43, '2022-01-10 18:45:59.109496', '2022-01-10 18:45:59.109496', 'ORDINARY SAVINGS', '8000.00', '0.00', 1, 9),
(44, '2022-01-17 04:01:21.504791', '2022-01-17 04:01:21.504791', 'Salary as at 01/10/2022', '0.00', '158000.00', 1, 12),
(45, '2022-01-17 04:01:21.577780', '2022-01-17 04:01:21.577780', 'ORDINARY SAVINGS', '20000.00', '0.00', 1, 12),
(46, '2022-01-17 04:01:21.642660', '2022-01-17 04:01:21.642660', 'PROJECT SAVINGS', '10000.00', '0.00', 1, 12),
(47, '2022-01-17 04:01:21.815050', '2022-01-17 04:01:21.815050', 'XMAS SAVINGS', '30000.00', '0.00', 1, 12),
(48, '2022-01-17 04:01:21.861991', '2022-01-17 04:01:21.861991', 'LAND SAVINGS', '3000.00', '0.00', 1, 12);

-- --------------------------------------------------------

--
-- Table structure for table `members_credit_purchase_summary`
--

CREATE TABLE `members_credit_purchase_summary` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `debit` decimal(20,2) NOT NULL,
  `credit` decimal(20,2) NOT NULL,
  `balance` decimal(20,2) NOT NULL,
  `approval_comment` longtext NOT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_officer_id` int(11) DEFAULT NULL,
  `approval_status_id` int(11) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL,
  `trans_code_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members_credit_purchase_summary`
--

INSERT INTO `members_credit_purchase_summary` (`id`, `created_at`, `updated_at`, `debit`, `credit`, `balance`, `approval_comment`, `approval_date`, `approval_officer_id`, `approval_status_id`, `status_id`, `trans_code_id`) VALUES
(5, '2022-01-06 07:25:02.822394', '2022-01-06 07:34:18.872668', '142700.00', '250000.00', '107300.00', 'ok', NULL, 11, 2, 2, 4),
(6, '2022-01-10 17:20:10.170283', '2022-01-10 17:22:10.269896', '26000.00', '158000.00', '132000.00', 'ok', NULL, 11, 2, 2, 7),
(7, '2022-01-10 18:45:58.965667', '2022-01-10 18:56:28.576353', '21800.00', '200000.00', '178200.00', 'ok', NULL, 11, 2, 2, 9),
(8, '2022-01-17 04:01:21.441779', '2022-01-17 04:03:23.536792', '104250.00', '158000.00', '53750.00', 'ok', NULL, 11, 2, 2, 12);

-- --------------------------------------------------------

--
-- Table structure for table `members_credit_sales_external_fascilities`
--

CREATE TABLE `members_credit_sales_external_fascilities` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `description` varchar(255) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `status_id` int(11) DEFAULT NULL,
  `trans_code_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `members_credit_sales_selected`
--

CREATE TABLE `members_credit_sales_selected` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `ticket` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `unit_selling_price` decimal(20,2) NOT NULL,
  `total` decimal(20,2) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members_credit_sales_selected`
--

INSERT INTO `members_credit_sales_selected` (`id`, `created_at`, `updated_at`, `ticket`, `quantity`, `unit_selling_price`, `total`, `member_id`, `processed_by_id`, `product_id`, `status_id`) VALUES
(4, '2022-01-06 07:11:19.021304', '2022-01-06 07:16:57.280664', '20221681119', 5, '2300.00', '11500.00', 151, 12, 917, 2),
(5, '2022-01-06 07:14:52.101648', '2022-01-06 07:14:52.101648', '20221681119', 10, '700.00', '7000.00', 151, 12, 971, 2),
(6, '2022-01-06 07:17:07.968074', '2022-01-06 07:17:07.968074', '20221681119', 2, '2100.00', '4200.00', 151, 12, 986, 2),
(7, '2022-01-10 12:37:19.855868', '2022-01-10 12:37:19.855868', '2022110133719', 10, '700.00', '7000.00', 154, 12, 971, 2),
(8, '2022-01-10 12:37:27.540377', '2022-01-10 12:37:27.540377', '2022110133719', 5, '1800.00', '9000.00', 154, 12, 1017, 2),
(9, '2022-01-10 18:44:19.066453', '2022-01-10 18:44:19.066453', '2022110194419', 3, '2300.00', '6900.00', 155, 12, 917, 2),
(10, '2022-01-10 18:44:23.784565', '2022-01-10 18:44:23.784565', '2022110194419', 3, '2100.00', '6300.00', 155, 12, 986, 2),
(11, '2022-01-10 18:44:28.906644', '2022-01-10 18:44:28.906644', '2022110194419', 4, '150.00', '600.00', 155, 12, 1024, 2),
(12, '2022-01-17 03:54:01.006321', '2022-01-17 03:54:01.006321', '20221174540', 5, '950.00', '4750.00', 152, 13, 924, 2),
(13, '2022-01-17 03:54:09.303449', '2022-01-17 03:54:09.303449', '20221174540', 5, '1200.00', '6000.00', 152, 13, 918, 2),
(14, '2022-01-17 03:54:18.339028', '2022-01-17 03:54:18.339028', '20221174540', 5, '700.00', '3500.00', 152, 13, 971, 2),
(15, '2022-01-17 03:56:12.722129', '2022-01-17 03:56:12.722129', '20221174540', 10, '2700.00', '27000.00', 152, 13, 955, 2);

-- --------------------------------------------------------

--
-- Table structure for table `members_exclusiveness`
--

CREATE TABLE `members_exclusiveness` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `approval_comment` longtext DEFAULT NULL,
  `approved_at` date DEFAULT NULL,
  `approval_officer_id` int(11) DEFAULT NULL,
  `approval_status_id` int(11) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `status_id` int(11) NOT NULL,
  `transaction_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `members_id_manager`
--

CREATE TABLE `members_id_manager` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `prefix_title` varchar(255) NOT NULL,
  `prefix_year` varchar(255) NOT NULL,
  `member_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members_id_manager`
--

INSERT INTO `members_id_manager` (`id`, `created_at`, `updated_at`, `prefix_title`, `prefix_year`, `member_id`) VALUES
(1, '2021-12-07 19:57:26.406767', '2021-12-16 10:06:52.943943', 'FETHAII', '2021', 5006);

-- --------------------------------------------------------

--
-- Table structure for table `members_next_of_kins`
--

CREATE TABLE `members_next_of_kins` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` longtext DEFAULT NULL,
  `phone_number` varchar(255) NOT NULL,
  `lock_status_id` int(11) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `relationships_id` int(11) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `members_salary_update_request`
--

CREATE TABLE `members_salary_update_request` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `description` varchar(255) NOT NULL,
  `approved_at` date DEFAULT NULL,
  `approval_comment` longtext DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `approved_officer_id` int(11) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `processing_status_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members_salary_update_request`
--

INSERT INTO `members_salary_update_request` (`id`, `created_at`, `updated_at`, `amount`, `description`, `approved_at`, `approval_comment`, `image`, `approved_officer_id`, `member_id`, `processing_status_id`, `status_id`) VALUES
(1, '2021-12-31 07:47:26.307480', '2021-12-31 07:47:55.142144', '250000.00', 'payslip for ecember 2021', '2021-12-31', 'ok', '', 12, 151, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `members_share_accounts`
--

CREATE TABLE `members_share_accounts` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `shares` int(11) NOT NULL,
  `unit_cost` decimal(20,2) NOT NULL,
  `total_cost` decimal(20,2) NOT NULL,
  `effective_date` date DEFAULT NULL,
  `year` int(11) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members_share_accounts`
--

INSERT INTO `members_share_accounts` (`id`, `created_at`, `updated_at`, `shares`, `unit_cost`, `total_cost`, `effective_date`, `year`, `member_id`, `processed_by_id`, `status_id`) VALUES
(1, '2021-12-13 17:22:30.243244', '2021-12-15 04:52:04.660531', 25, '10000.00', '250000.00', '2021-12-01', 2021, 356, 9, 1),
(2, '2021-12-13 17:23:17.842386', '2021-12-16 10:56:30.870051', 8, '10000.00', '130000.00', '2020-12-31', 2020, 363, 9, 1),
(3, '2021-12-13 17:28:45.826026', '2021-12-13 17:28:45.826026', 1, '10000.00', '10000.00', '2021-12-13', 2021, 370, 9, 1),
(6, '2021-12-14 19:24:28.614554', '2021-12-14 19:24:28.614554', 5, '10000.00', '50000.00', '2021-12-14', 2021, 370, 9, 1),
(11, '2021-12-16 10:06:53.311553', '2021-12-16 10:06:53.311553', 1, '10000.00', '10000.00', '2021-12-16', 2021, 710, 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `members_share_accounts_main`
--

CREATE TABLE `members_share_accounts_main` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `account_number` int(11) NOT NULL,
  `shares` int(11) NOT NULL,
  `unit_cost` decimal(20,2) NOT NULL,
  `total_cost` decimal(20,2) NOT NULL,
  `effective_date` date DEFAULT NULL,
  `year` int(11) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `members_share_configurations`
--

CREATE TABLE `members_share_configurations` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `unit_cost` decimal(20,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members_share_configurations`
--

INSERT INTO `members_share_configurations` (`id`, `created_at`, `updated_at`, `unit_cost`) VALUES
(1, '2021-12-13 17:41:38.710842', '2021-12-13 17:41:38.710842', '10000.00');

-- --------------------------------------------------------

--
-- Table structure for table `members_share_initial_update_request`
--

CREATE TABLE `members_share_initial_update_request` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `approval_comment` longtext DEFAULT NULL,
  `approved_at` date DEFAULT NULL,
  `approval_officer_id` int(11) DEFAULT NULL,
  `approval_status_id` int(11) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL,
  `transaction_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members_share_initial_update_request`
--

INSERT INTO `members_share_initial_update_request` (`id`, `created_at`, `updated_at`, `amount`, `approval_comment`, `approved_at`, `approval_officer_id`, `approval_status_id`, `member_id`, `processed_by_id`, `status_id`, `transaction_id`) VALUES
(2, '2021-12-13 17:58:36.221298', '2021-12-13 18:58:51.177716', '10000.00', 'ok', '2021-12-13', 1, 2, 3, 9, 2, 3);

-- --------------------------------------------------------

--
-- Table structure for table `members_share_purchase_request`
--

CREATE TABLE `members_share_purchase_request` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `units` int(11) NOT NULL,
  `approval_comment` longtext DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_officer_id` int(11) DEFAULT NULL,
  `approval_status_id` int(11) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members_share_purchase_request`
--

INSERT INTO `members_share_purchase_request` (`id`, `created_at`, `updated_at`, `units`, `approval_comment`, `approval_date`, `approval_officer_id`, `approval_status_id`, `member_id`, `status_id`) VALUES
(3, '2021-12-14 01:03:16.622353', '2021-12-14 02:23:10.695272', 4, 'ok', '2021-12-14', 2, 2, 363, 2),
(4, '2021-12-14 04:28:12.652390', '2021-12-14 19:24:29.280989', 5, 'ok', '2021-12-14', 2, 2, 370, 2),
(5, '2021-12-16 10:26:08.355636', '2021-12-16 10:56:31.015849', 5, 'ok', '2021-12-16', 2, 2, 363, 2);

-- --------------------------------------------------------

--
-- Table structure for table `members_welfare`
--

CREATE TABLE `members_welfare` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `amount` decimal(20,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members_welfare`
--

INSERT INTO `members_welfare` (`id`, `created_at`, `updated_at`, `amount`) VALUES
(1, '2021-12-16 07:49:03.545260', '2021-12-16 07:49:03.545260', '3600.00');

-- --------------------------------------------------------

--
-- Table structure for table `members_welfare_accounts`
--

CREATE TABLE `members_welfare_accounts` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `year` int(11) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members_welfare_accounts`
--

INSERT INTO `members_welfare_accounts` (`id`, `created_at`, `updated_at`, `amount`, `year`, `member_id`, `processed_by_id`, `status_id`) VALUES
(3, '2021-12-13 17:06:46.057815', '2021-12-13 17:06:46.057815', '60000.00', 0, 357, 9, 1),
(4, '2021-12-13 17:08:20.026238', '2021-12-13 17:08:20.026238', '80000.00', 0, 364, 9, 1),
(6, '2021-12-15 03:37:04.470058', '2021-12-15 03:37:04.470058', '3600.00', 2022, 357, 9, 1),
(10, '2021-12-16 10:06:53.691368', '2021-12-16 10:06:53.691368', '3600.00', 2021, 711, NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `monthly_deduction_list`
--

CREATE TABLE `monthly_deduction_list` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `account_number` varchar(255) DEFAULT NULL,
  `amount` decimal(20,2) NOT NULL,
  `amount_deducted` decimal(20,2) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `transaction_id` int(11) DEFAULT NULL,
  `transaction_period_id` int(11) NOT NULL,
  `transaction_status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `monthly_deduction_list`
--

INSERT INTO `monthly_deduction_list` (`id`, `created_at`, `updated_at`, `account_number`, `amount`, `amount_deducted`, `member_id`, `transaction_id`, `transaction_period_id`, `transaction_status_id`) VALUES
(6, '2022-01-10 21:05:04.850462', '2022-01-10 21:05:04.850462', '60000001', '22700.00', '0.00', 151, 14, 2, 2),
(7, '2022-01-10 21:05:05.051806', '2022-01-10 21:05:05.051806', '60000004', '16000.00', '0.00', 154, 14, 2, 2),
(8, '2022-01-10 21:05:05.123823', '2022-01-10 21:05:05.123823', '60000005', '13800.00', '0.00', 155, 14, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `monthly_deduction_list_generated`
--

CREATE TABLE `monthly_deduction_list_generated` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `amount_deducted` decimal(20,2) NOT NULL,
  `balance` decimal(20,2) NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `salary_institution_id` int(11) NOT NULL,
  `transaction_period_id` int(11) NOT NULL,
  `transaction_status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `monthly_deduction_list_generated`
--

INSERT INTO `monthly_deduction_list_generated` (`id`, `created_at`, `updated_at`, `amount`, `amount_deducted`, `balance`, `member_id`, `salary_institution_id`, `transaction_period_id`, `transaction_status_id`) VALUES
(1, '2022-01-11 14:06:49.981794', '2022-01-11 14:06:49.981794', '22700.00', '0.00', '0.00', 151, 1, 2, 1),
(2, '2022-01-11 14:06:50.100916', '2022-01-11 14:06:50.100916', '16000.00', '0.00', '0.00', 154, 1, 2, 1),
(3, '2022-01-11 14:06:50.221841', '2022-01-11 14:06:50.221841', '13800.00', '0.00', '0.00', 155, 1, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `monthly_generated_transactions`
--

CREATE TABLE `monthly_generated_transactions` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `transaction_id` int(11) NOT NULL,
  `transaction_period_id` int(11) NOT NULL,
  `transaction_status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `monthly_generated_transactions`
--

INSERT INTO `monthly_generated_transactions` (`id`, `created_at`, `updated_at`, `processed_by_id`, `transaction_id`, `transaction_period_id`, `transaction_status_id`) VALUES
(1, '2021-12-31 12:04:03.859657', '2021-12-31 12:04:03.859657', 12, 14, 2, 2),
(2, '2022-01-10 21:05:05.193677', '2022-01-10 21:05:05.193677', 12, 14, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `monthly_group_generated_transactions`
--

CREATE TABLE `monthly_group_generated_transactions` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `salary_institution_id` int(11) NOT NULL,
  `transaction_period_id` int(11) NOT NULL,
  `transaction_status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `multiple_loan_status`
--

CREATE TABLE `multiple_loan_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `multiple_loan_status`
--

INSERT INTO `multiple_loan_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'NOT ALLOWED', '2021-12-07 19:09:27.109949', '2021-12-07 19:09:27.109949'),
(2, 'ALLOWED', '2021-12-07 19:09:27.146682', '2021-12-07 19:09:27.146682');

-- --------------------------------------------------------

--
-- Table structure for table `next_of_kins_maximun`
--

CREATE TABLE `next_of_kins_maximun` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `maximun` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `nok_relationships`
--

CREATE TABLE `nok_relationships` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `nok_relationships`
--

INSERT INTO `nok_relationships` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'FATHER', '2021-12-07 19:03:51.187065', '2021-12-07 19:03:51.187065'),
(2, 'MOTHER', '2021-12-07 19:03:51.243070', '2021-12-07 19:03:51.243070'),
(3, 'SPOUSE', '2021-12-07 19:03:51.417014', '2021-12-07 19:03:51.417014'),
(4, 'BROTHER', '2021-12-07 19:03:51.462541', '2021-12-07 19:03:51.462541'),
(5, 'SISTER', '2021-12-07 19:03:51.496759', '2021-12-07 19:03:51.496759'),
(6, 'SON', '2021-12-07 19:03:51.596475', '2021-12-07 19:03:51.596475'),
(7, 'DUAGHTER', '2021-12-07 19:03:51.752649', '2021-12-07 19:03:51.752649'),
(8, 'UNCLE', '2021-12-07 19:03:51.834161', '2021-12-07 19:03:51.834161'),
(10, 'NICE', '2022-01-13 20:41:43.692243', '2022-01-13 20:41:43.693228');

-- --------------------------------------------------------

--
-- Table structure for table `non_member_account_deductions`
--

CREATE TABLE `non_member_account_deductions` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `ippis_no` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `salary_institution_id` int(11) NOT NULL,
  `transaction_period_id` int(11) NOT NULL,
  `transaction_status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `norminal_roll`
--

CREATE TABLE `norminal_roll` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `member_id` varchar(255) NOT NULL,
  `file_no` varchar(255) NOT NULL,
  `ippis_no` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `middle_name` varchar(255) DEFAULT NULL,
  `phone_no` varchar(255) NOT NULL,
  `year` varchar(255) NOT NULL,
  `salary_institution` varchar(255) NOT NULL,
  `transaction_status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `norminal_roll`
--

INSERT INTO `norminal_roll` (`id`, `created_at`, `updated_at`, `member_id`, `file_no`, `ippis_no`, `last_name`, `first_name`, `middle_name`, `phone_no`, `year`, `salary_institution`, `transaction_status_id`) VALUES
(301, '2021-12-07 20:40:53.807951', '2021-12-07 20:52:12.587014', '1', '1', '1', 'IDAKA', 'BEN', 'MAUREEN', '8064004355', '2010', '1', 2),
(302, '2021-12-07 20:40:53.876997', '2021-12-07 20:52:12.694038', '2', '2', '2', 'OKOLI', 'UCHENNA', 'OBIA', '8064004356', '2011', '1', 2),
(303, '2021-12-07 20:40:53.932173', '2021-12-07 20:52:12.805048', '3', '3', '3', 'OKONKWO', 'NKONYELU', 'E', '8064004357', '2012', '1', 2),
(304, '2021-12-07 20:40:53.972007', '2021-12-07 20:52:12.872108', '4', '4', '4', 'AMADI', 'OPHELIA', 'CHIB', '8064004358', '2013', '1', 2),
(305, '2021-12-07 20:40:54.055220', '2021-12-07 20:52:12.960568', '5', '5', '5', 'NNACHI', 'IKWUO', 'IJEM', '8064004359', '2014', '1', 2),
(306, '2021-12-07 20:40:54.121477', '2021-12-07 20:52:13.049332', '6', '6', '6', 'AGBOWO', 'IFEOMA', 'MARY', '8064004360', '2015', '1', 2),
(307, '2021-12-07 20:40:54.163090', '2021-12-07 20:52:13.138304', '7', '7', '7', 'NWANKWO', 'DR', 'OKUTA J', '8064004361', '2016', '1', 2),
(308, '2021-12-07 20:40:54.187220', '2021-12-07 20:52:13.359921', '8', '8', '8', 'ABAA', 'EMMANUEL', '', '8064004362', '2017', '1', 2),
(309, '2021-12-07 20:40:54.233077', '2021-12-07 20:52:13.483030', '9', '9', '9', 'ABAGHA', 'UGO', 'AGNES', '8064004363', '2018', '1', 2),
(310, '2021-12-07 20:40:54.288237', '2021-12-07 20:52:13.581966', '10', '10', '10', 'ABAGHAUGWU', 'CHIGOZI', '', '8064004364', '2019', '1', 2),
(311, '2021-12-07 20:40:54.328663', '2021-12-07 20:52:13.727709', '11', '11', '11', 'ABANIFI', 'NWACHINAME', '', '8064004365', '2020', '1', 2),
(312, '2021-12-07 20:40:54.355828', '2021-12-07 20:52:13.892919', '12', '12', '12', 'ABARA', 'NNENWAOGO', 'P', '8064004366', '2021', '1', 2),
(313, '2021-12-07 20:40:54.400265', '2021-12-07 20:52:14.095360', '13', '13', '13', 'ABARA', 'LAWRENCE', 'CHI', '8064004367', '2010', '1', 2),
(314, '2021-12-07 20:40:54.444050', '2021-12-07 20:52:14.171831', '14', '14', '14', 'ABARA', 'NWAKAEGO', 'EUC', '8064004368', '2011', '1', 2),
(315, '2021-12-07 20:40:54.489333', '2021-12-07 20:52:14.261459', '15', '15', '15', 'ABBA', 'OBASI', 'DORCAS', '8064004369', '2012', '1', 2),
(316, '2021-12-07 20:40:54.533746', '2021-12-07 20:52:14.384085', '16', '16', '16', 'ABIA', 'EFFIONG', 'ANIET', '8064004370', '2013', '1', 2),
(317, '2021-12-07 20:40:54.595325', '2021-12-07 20:52:14.461196', '17', '17', '17', 'ABIA', 'NKIRUKA', 'NDON', '8064004371', '2014', '1', 2),
(318, '2021-12-07 20:40:54.645788', '2021-12-07 20:52:14.528435', '18', '18', '18', 'ABIA', 'DR', 'EFFIONG NDO', '8064004372', '2015', '1', 2),
(319, '2021-12-07 20:40:54.676766', '2021-12-07 20:52:14.595686', '19', '19', '19', 'ABII', 'UGOCHI', 'GLORIA', '8064004373', '2016', '1', 2),
(320, '2021-12-07 20:40:54.709747', '2021-12-07 20:52:14.660804', '20', '20', '20', 'ABIOLA', 'ABEKE', 'ZULAY', '8064004374', '2017', '1', 2),
(321, '2021-12-07 20:40:54.743728', '2021-12-07 20:52:14.727762', '21', '21', '21', 'ABIRI', 'CHIOMA', 'CLARA', '8064004375', '2018', '1', 2),
(322, '2021-12-07 20:40:54.776705', '2021-12-07 20:52:14.866488', '22', '22', '22', 'ABOKEDE', 'OLADELE', 'AD', '8064004376', '2019', '1', 2),
(323, '2021-12-07 20:40:54.810684', '2021-12-07 20:52:15.005357', '23', '23', '23', 'ABOKEDE', 'OMOLARA', 'AD', '8064004377', '2020', '1', 2),
(324, '2021-12-07 20:40:55.036549', '2021-12-07 20:52:15.171464', '24', '24', '24', 'ABOR', 'LEONARD', '', '8064004378', '2021', '1', 2),
(325, '2021-12-07 20:40:55.188380', '2021-12-07 20:52:15.239496', '25', '25', '25', 'ABU', 'MOMOH', 'AUGUSTIN', '8064004379', '2010', '1', 2),
(326, '2021-12-07 20:40:55.322344', '2021-12-07 20:52:15.316912', '26', '26', '26', 'ABUWA', 'MMADUABUCHI', '', '8064004380', '2011', '1', 2),
(327, '2021-12-07 20:40:55.355373', '2021-12-07 20:52:15.428160', '27', '27', '27', 'ACHI', 'MAXWELL', 'NGWU', '8064004381', '2012', '1', 2),
(328, '2021-12-07 20:40:55.400189', '2021-12-07 20:52:15.494840', '28', '28', '28', 'ACHONWA', 'EZEKIEL', 'UC', '8064004382', '2013', '1', 2),
(329, '2021-12-07 20:40:55.439872', '2021-12-07 20:52:15.605345', '29', '29', '29', 'ACHUGONYE', 'UDOCHRIS', '', '8064004383', '2014', '1', 2),
(330, '2021-12-07 20:40:55.484332', '2021-12-07 20:52:15.706206', '30', '30', '30', 'ADAMA', 'MATTHEW', 'SIMO', '8064004384', '2015', '1', 2),
(331, '2021-12-07 20:40:55.510786', '2021-12-07 20:52:15.805294', '31', '31', '31', 'ADAMSOKORIE', 'BEATRI', '', '8064004385', '2016', '1', 2),
(332, '2021-12-07 20:40:55.544407', '2021-12-07 20:52:15.905237', '32', '32', '32', 'ADANI', 'IFEOMA', 'MODES', '8064004386', '2017', '1', 2),
(333, '2021-12-07 20:40:55.599619', '2021-12-07 20:52:15.982777', '33', '33', '33', 'ADEOLU', 'IBUKUN', 'NGOZ', '8064004387', '2018', '1', 2),
(334, '2021-12-07 20:40:55.645273', '2021-12-07 20:52:16.038385', '34', '34', '34', 'ADEOYE', 'KUSS', 'JULIAN', '8064004388', '2019', '1', 2),
(335, '2021-12-07 20:40:55.677897', '2021-12-07 20:52:16.127659', '35', '35', '35', 'ADEYEMI', 'SAMSON', 'OLU', '8064004389', '2020', '1', 2),
(336, '2021-12-07 20:40:55.711151', '2021-12-07 20:52:16.439891', '36', '36', '36', 'ADIDU', 'EMMANUEL', 'AME', '8064004390', '2021', '1', 2),
(337, '2021-12-07 20:40:55.766360', '2021-12-07 20:52:16.606127', '37', '37', '37', 'ADIELE', 'NWANYIEZE', 'N', '8064004391', '2010', '1', 2),
(338, '2021-12-07 20:40:55.806622', '2021-12-07 20:52:16.705175', '38', '38', '38', 'ADIGWE', 'EMMANUEL', 'IF', '8064004392', '2011', '1', 2),
(339, '2021-12-07 20:40:55.855248', '2021-12-07 20:52:16.771854', '39', '39', '39', 'ADIKWU', 'JULIANA', 'NGO', '8064004393', '2012', '1', 2),
(340, '2021-12-07 20:40:55.889200', '2021-12-07 20:52:16.838709', '40', '40', '40', 'ADIMORAH', 'CAROLINE', '', '8064004394', '2013', '1', 2),
(341, '2021-12-07 20:40:56.028396', '2021-12-07 20:52:16.905453', '41', '41', '41', 'ADIMORAH', 'ORAEKI', 'HA', '8064004395', '2014', '1', 2),
(342, '2021-12-07 20:40:56.235262', '2021-12-07 20:52:16.972937', '42', '42', '42', 'ADOGU', 'IFEYINWA', '', '8064004396', '2015', '1', 2),
(343, '2021-12-07 20:40:56.288292', '2021-12-07 20:52:17.038896', '43', '43', '43', 'ADOKA', 'OGHENEOCHUKO', '', '8064004397', '2016', '1', 2),
(344, '2021-12-07 20:40:56.321722', '2021-12-07 20:52:17.093865', '44', '44', '44', 'ADOKE', 'NWOVA', 'JOHN', '8064004398', '2017', '1', 2),
(345, '2021-12-07 20:40:56.361186', '2021-12-07 20:52:17.181570', '45', '45', '45', 'ADOKWU', 'EDACHE', 'ELDA', '8064004399', '2018', '1', 2),
(346, '2021-12-07 20:40:56.409917', '2021-12-07 20:52:17.484174', '46', '46', '46', 'ADONU', 'OBINNA', 'BENJA', '8064004400', '2019', '1', 2),
(347, '2021-12-07 20:40:56.443860', '2021-12-07 20:52:17.595105', '47', '47', '47', 'ADUAKA', 'LINDA', 'UKAMA', '8064004401', '2020', '1', 2),
(348, '2021-12-07 20:40:56.487690', '2021-12-07 20:52:17.682908', '48', '48', '48', 'ADUAKA', 'NGOZI', 'ELIZA', '8064004402', '2021', '1', 2),
(349, '2021-12-07 20:40:56.533261', '2021-12-07 20:52:17.771922', '49', '49', '49', 'ADUAKA', 'VIVIAN', 'ONYI', '8064004403', '2010', '1', 2),
(350, '2021-12-07 20:40:56.566748', '2021-12-07 20:52:17.839162', '50', '50', '50', 'ADUWA', 'ADAGBA', 'PATRI', '8064004404', '2011', '1', 2),
(351, '2021-12-07 20:58:54.348290', '2021-12-07 21:04:13.844158', '1', '1', '1', 'IDAKA', 'BEN', 'MAUREEN', '8064004355', '2010', '1', 2),
(352, '2021-12-07 20:58:54.411581', '2021-12-07 21:04:14.001306', '2', '2', '2', 'OKOLI', 'UCHENNA', 'OBIA', '8064004356', '2011', '1', 2),
(353, '2021-12-07 20:58:54.456531', '2021-12-07 21:04:14.088548', '3', '3', '3', 'OKONKWO', 'NKONYELU', 'E', '8064004357', '2012', '1', 2),
(354, '2021-12-07 20:58:54.511482', '2021-12-07 21:04:14.201016', '4', '4', '4', 'AMADI', 'OPHELIA', 'CHIB', '8064004358', '2013', '1', 2),
(355, '2021-12-07 20:58:54.556789', '2021-12-07 21:04:14.266700', '5', '5', '5', 'NNACHI', 'IKWUO', 'IJEM', '8064004359', '2014', '1', 2),
(356, '2021-12-07 20:58:54.634733', '2021-12-07 21:04:14.344215', '6', '6', '6', 'AGBOWO', 'IFEOMA', 'MARY', '8064004360', '2015', '1', 2),
(357, '2021-12-07 20:58:54.690594', '2021-12-07 21:04:14.422781', '7', '7', '7', 'NWANKWO', 'DR', 'OKUTA J', '8064004361', '2016', '1', 2),
(358, '2021-12-07 20:58:54.711227', '2021-12-07 21:04:14.489852', '8', '8', '8', 'ABAA', 'EMMANUEL', '', '8064004362', '2017', '1', 2),
(359, '2021-12-07 20:58:54.855845', '2021-12-07 21:04:14.623505', '9', '9', '9', 'ABAGHA', 'UGO', 'AGNES', '8064004363', '2018', '1', 2),
(360, '2021-12-07 20:58:54.901142', '2021-12-07 21:04:14.901225', '10', '10', '10', 'ABAGHAUGWU', 'CHIGOZI', '', '8064004364', '2019', '1', 2),
(361, '2021-12-07 20:58:54.923126', '2021-12-07 21:04:14.967721', '11', '11', '11', 'ABANIFI', 'NWACHINAME', '', '8064004365', '2020', '1', 2),
(362, '2021-12-07 20:58:54.978091', '2021-12-07 21:04:15.066910', '12', '12', '12', 'ABARA', 'NNENWAOGO', 'P', '8064004366', '2021', '1', 2),
(363, '2021-12-07 20:58:55.023063', '2021-12-07 21:04:15.156043', '13', '13', '13', 'ABARA', 'LAWRENCE', 'CHI', '8064004367', '2010', '1', 2),
(364, '2021-12-07 20:58:55.079029', '2021-12-07 21:04:15.200300', '14', '14', '14', 'ABARA', 'NWAKAEGO', 'EUC', '8064004368', '2011', '1', 2),
(365, '2021-12-07 20:58:55.101015', '2021-12-07 21:04:15.256890', '15', '15', '15', 'ABBA', 'OBASI', 'DORCAS', '8064004369', '2012', '1', 2),
(366, '2021-12-07 20:58:55.156556', '2021-12-07 21:04:15.323604', '16', '16', '16', 'ABIA', 'EFFIONG', 'ANIET', '8064004370', '2013', '1', 2),
(367, '2021-12-07 20:58:55.178542', '2021-12-07 21:04:15.412625', '17', '17', '17', 'ABIA', 'NKIRUKA', 'NDON', '8064004371', '2014', '1', 2),
(368, '2021-12-07 20:58:55.199531', '2021-12-07 21:04:15.512560', '18', '18', '18', 'ABIA', 'DR', 'EFFIONG NDO', '8064004372', '2015', '1', 2),
(369, '2021-12-07 20:58:55.222515', '2021-12-07 21:04:15.623357', '19', '19', '19', 'ABII', 'UGOCHI', 'GLORIA', '8064004373', '2016', '1', 2),
(370, '2021-12-07 20:58:55.267488', '2021-12-07 21:04:15.700358', '20', '20', '20', 'ABIOLA', 'ABEKE', 'ZULAY', '8064004374', '2017', '1', 2),
(371, '2021-12-07 20:58:55.289473', '2021-12-07 21:04:15.923209', '21', '21', '21', 'ABIRI', 'CHIOMA', 'CLARA', '8064004375', '2018', '1', 2),
(372, '2021-12-07 20:58:55.311461', '2021-12-07 21:04:16.056288', '22', '22', '22', 'ABOKEDE', 'OLADELE', 'AD', '8064004376', '2019', '1', 2),
(373, '2021-12-07 20:58:55.356432', '2021-12-07 21:04:16.146233', '23', '23', '23', 'ABOKEDE', 'OMOLARA', 'AD', '8064004377', '2020', '1', 2),
(374, '2021-12-07 20:58:55.377578', '2021-12-07 21:04:16.211655', '24', '24', '24', 'ABOR', 'LEONARD', '', '8064004378', '2021', '1', 2),
(375, '2021-12-07 20:58:55.400474', '2021-12-07 21:04:16.323412', '25', '25', '25', 'ABU', 'MOMOH', 'AUGUSTIN', '8064004379', '2010', '1', 2),
(376, '2021-12-07 20:58:55.444971', '2021-12-07 21:04:16.468338', '26', '26', '26', 'ABUWA', 'MMADUABUCHI', '', '8064004380', '2011', '1', 2),
(377, '2021-12-07 20:58:55.467719', '2021-12-07 21:04:16.535016', '27', '27', '27', 'ACHI', 'MAXWELL', 'NGWU', '8064004381', '2012', '1', 2),
(378, '2021-12-07 20:58:55.488744', '2021-12-07 21:04:16.601399', '28', '28', '28', 'ACHONWA', 'EZEKIEL', 'UC', '8064004382', '2013', '1', 2),
(379, '2021-12-07 20:58:55.595896', '2021-12-07 21:04:16.667977', '29', '29', '29', 'ACHUGONYE', 'UDOCHRIS', '', '8064004383', '2014', '1', 2),
(380, '2021-12-07 20:58:55.722842', '2021-12-07 21:04:16.723876', '30', '30', '30', 'ADAMA', 'MATTHEW', 'SIMO', '8064004384', '2015', '1', 2),
(381, '2021-12-07 20:58:55.944578', '2021-12-07 21:04:16.800146', '31', '31', '31', 'ADAMSOKORIE', 'BEATRI', '', '8064004385', '2016', '1', 2),
(382, '2021-12-07 20:58:56.002619', '2021-12-07 21:04:17.055642', '32', '32', '32', 'ADANI', 'IFEOMA', 'MODES', '8064004386', '2017', '1', 2),
(383, '2021-12-07 20:58:56.046369', '2021-12-07 21:04:17.122598', '33', '33', '33', 'ADEOLU', 'IBUKUN', 'NGOZ', '8064004387', '2018', '1', 2),
(384, '2021-12-07 20:58:56.101650', '2021-12-07 21:04:17.233850', '34', '34', '34', 'ADEOYE', 'KUSS', 'JULIAN', '8064004388', '2019', '1', 2),
(385, '2021-12-07 20:58:56.124361', '2021-12-07 21:04:17.322493', '35', '35', '35', 'ADEYEMI', 'SAMSON', 'OLU', '8064004389', '2020', '1', 2),
(386, '2021-12-07 20:58:56.145492', '2021-12-07 21:04:17.378508', '36', '36', '36', 'ADIDU', 'EMMANUEL', 'AME', '8064004390', '2021', '1', 2),
(387, '2021-12-07 20:58:56.168287', '2021-12-07 21:04:17.466954', '37', '37', '37', 'ADIELE', 'NWANYIEZE', 'N', '8064004391', '2010', '1', 2),
(388, '2021-12-07 20:58:56.212922', '2021-12-07 21:04:17.522549', '38', '38', '38', 'ADIGWE', 'EMMANUEL', 'IF', '8064004392', '2011', '1', 2),
(389, '2021-12-07 20:58:56.267250', '2021-12-07 21:04:17.601061', '39', '39', '39', 'ADIKWU', 'JULIANA', 'NGO', '8064004393', '2012', '1', 2),
(390, '2021-12-07 20:58:56.289458', '2021-12-07 21:04:17.655891', '40', '40', '40', 'ADIMORAH', 'CAROLINE', '', '8064004394', '2013', '1', 2),
(391, '2021-12-07 20:58:56.333967', '2021-12-07 21:04:17.733487', '41', '41', '41', 'ADIMORAH', 'ORAEKI', 'HA', '8064004395', '2014', '1', 2),
(392, '2021-12-07 20:58:56.357701', '2021-12-07 21:04:17.967843', '42', '42', '42', 'ADOGU', 'IFEYINWA', '', '8064004396', '2015', '1', 2),
(393, '2021-12-07 20:58:56.385514', '2021-12-07 21:04:18.234585', '43', '43', '43', 'ADOKA', 'OGHENEOCHUKO', '', '8064004397', '2016', '1', 2),
(394, '2021-12-07 20:58:56.411495', '2021-12-07 21:04:18.278557', '44', '44', '44', 'ADOKE', 'NWOVA', 'JOHN', '8064004398', '2017', '1', 2),
(395, '2021-12-07 20:58:56.456467', '2021-12-07 21:04:18.345516', '45', '45', '45', 'ADOKWU', 'EDACHE', 'ELDA', '8064004399', '2018', '1', 2),
(396, '2021-12-07 20:58:56.478455', '2021-12-07 21:04:18.390164', '46', '46', '46', 'ADONU', 'OBINNA', 'BENJA', '8064004400', '2019', '1', 2),
(397, '2021-12-07 20:58:56.522427', '2021-12-07 21:04:18.434742', '47', '47', '47', 'ADUAKA', 'LINDA', 'UKAMA', '8064004401', '2020', '1', 2),
(398, '2021-12-07 20:58:56.545410', '2021-12-07 21:04:18.490032', '48', '48', '48', 'ADUAKA', 'NGOZI', 'ELIZA', '8064004402', '2021', '1', 2),
(399, '2021-12-07 20:58:56.600304', '2021-12-07 21:04:18.545620', '49', '49', '49', 'ADUAKA', 'VIVIAN', 'ONYI', '8064004403', '2010', '1', 2),
(400, '2021-12-07 20:58:56.624181', '2021-12-07 21:04:18.601201', '50', '50', '50', 'ADUWA', 'ADAGBA', 'PATRI', '8064004404', '2011', '1', 2);

-- --------------------------------------------------------

--
-- Table structure for table `payment_channels`
--

CREATE TABLE `payment_channels` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payment_channels`
--

INSERT INTO `payment_channels` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'CASH', '2021-12-07 19:01:19.658905', '2021-12-07 19:01:19.658905'),
(3, 'TRANSFER', '2021-12-07 19:01:19.850131', '2021-12-07 19:01:19.850131');

-- --------------------------------------------------------

--
-- Table structure for table `personal_ledger`
--

CREATE TABLE `personal_ledger` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `account_number` varchar(255) NOT NULL,
  `particulars` varchar(255) NOT NULL,
  `debit` decimal(20,2) NOT NULL,
  `credit` decimal(20,2) NOT NULL,
  `balance` decimal(20,2) NOT NULL,
  `transaction_period` date NOT NULL,
  `member_id` int(11) DEFAULT NULL,
  `status_id` int(11) NOT NULL,
  `transaction_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `personal_ledger`
--

INSERT INTO `personal_ledger` (`id`, `created_at`, `updated_at`, `account_number`, `particulars`, `debit`, `credit`, `balance`, `transaction_period`, `member_id`, `status_id`, `transaction_id`) VALUES
(7, '2021-12-13 14:50:47.634825', '2021-12-13 14:50:47.634825', '10100001', 'Balance Brought Forward as at 12/08/2021', '0.00', '120000.00', '120000.00', '2021-12-08', 151, 1, 2),
(8, '2021-12-13 14:50:48.036141', '2021-12-13 14:50:48.037138', '10300001', 'Balance Brought Forward as at 12/08/2021', '0.00', '150000.00', '150000.00', '2021-12-08', 151, 1, 4),
(11, '2021-12-13 15:15:43.580636', '2021-12-13 15:15:43.580636', '10200001', 'Balance Brought Forward as at 12/08/2021', '0.00', '250000.00', '250000.00', '2021-12-08', 151, 1, 3),
(12, '2021-12-13 15:42:43.855978', '2021-12-13 15:42:43.856979', '2010000120211213164200001', 'Balance Brought Forward as at 12/08/2021', '70000.00', '0.00', '-70000.00', '2021-12-08', 151, 1, 8),
(13, '2021-12-13 16:22:58.350642', '2021-12-13 16:22:58.351643', '2020000120211213172200002', 'Balance Brought Forward as at 12/08/2021', '450000.00', '0.00', '-450000.00', '2021-12-08', 151, 1, 9),
(14, '2021-12-13 17:22:30.289661', '2021-12-13 17:22:30.289661', '70000001', 'Balance Broght Forward as at 2021-12-08 with shares of 2', '0.00', '20000.00', '20000.00', '2021-12-08', 151, 1, 15),
(15, '2021-12-13 17:23:17.908165', '2021-12-13 17:23:17.908165', '70000002', 'Balance Broght Forward as at 2021-12-08 with shares of 3', '0.00', '30000.00', '30000.00', '2021-12-08', 152, 1, 15),
(16, '2021-12-13 17:28:45.870879', '2021-12-13 17:28:45.870879', '70000003', 'Balance Broght Forward as at 2021-12-08 with shares of 1', '0.00', '10000.00', '10000.00', '2021-12-08', 153, 1, 15),
(19, '2021-12-13 18:58:51.110316', '2021-12-13 18:58:51.110316', '70000003', 'Initial Share Balance update as at 2021-12-08 with shares: 1 Deducted from PROJECT SAVINGS', '0.00', '10000.00', '20000.00', '2021-12-08', 153, 1, 15),
(22, '2021-12-14 02:23:10.648071', '2021-12-14 02:23:10.648071', '70000002', '4 Unit(s) Share Purchase, at unit cost of 10000.00 as at 2021-12-14 03:22:51.861132', '0.00', '40000.00', '70000.00', '2021-12-14', 152, 1, 15),
(23, '2021-12-14 02:33:15.304125', '2021-12-14 02:33:15.304125', '10100001', 'update', '0.00', '50000.00', '170000.00', '2021-12-14', 151, 1, 2),
(24, '2021-12-14 02:34:40.302039', '2021-12-14 02:34:40.302039', '2010000120211213164200001', 'bep up', '0.00', '20000.00', '-50000.00', '2021-12-14', 151, 1, 8),
(25, '2021-12-14 19:24:29.167046', '2021-12-14 19:24:29.167046', '70000003', '5 Unit(s) Share Purchase, at unit cost of 10000.00 as at 2021-12-14 20:24:15.346587', '0.00', '50000.00', '70000.00', '2021-12-14', 153, 1, 15),
(26, '2021-12-14 20:55:44.697553', '2021-12-14 20:55:44.697553', '10100001', '5445454', '0.00', '45000.00', '215000.00', '2021-12-14', 151, 1, 2),
(27, '2021-12-14 20:59:28.230559', '2021-12-14 20:59:28.230559', '10200001', '5665656', '0.00', '34000.00', '284000.00', '2021-12-14', 151, 1, 3),
(28, '2021-12-14 21:00:33.813099', '2021-12-14 21:00:33.813099', '10200001', '56545656', '0.00', '60000.00', '344000.00', '2021-12-14', 151, 1, 3),
(29, '2021-12-14 21:01:28.577048', '2021-12-14 21:01:28.577048', '10200001', '565456567777', '0.00', '60000.00', '404000.00', '2021-12-14', 151, 1, 3),
(30, '2021-12-14 21:02:21.980417', '2021-12-14 21:02:21.980417', '10200001', '5654565677773', '0.00', '54000.00', '458000.00', '2021-12-14', 151, 1, 3),
(31, '2021-12-15 02:57:24.967587', '2021-12-15 02:57:24.967587', '2010000120211213164200001', 'uyyuyuyu', '0.00', '7899.00', '-42101.00', '2021-12-15', 151, 1, 8),
(32, '2021-12-15 03:03:31.534011', '2021-12-15 03:03:31.534011', '10100001', 'hgghgh', '0.00', '6000.00', '221000.00', '2021-12-15', 151, 1, 2),
(33, '2021-12-15 04:46:44.140199', '2021-12-15 04:46:44.140199', '70000001', '3 Unit(s) Share Payment, at unit cost of 10000.00 as at 2021-12-15 05:44:53.827489', '0.00', '30000.00', '50000.00', '2021-12-15', 151, 1, 17),
(34, '2021-12-15 04:52:04.828024', '2021-12-15 04:52:04.828024', '70000001', '5 Unit(s) Share Payment, at unit cost of 10000.00 as at 2021-12-15 05:51:38.409672', '0.00', '50000.00', '100000.00', '2021-12-15', 151, 1, 15),
(35, '2021-12-15 05:02:26.580163', '2021-12-15 05:02:26.580163', '10500001', 'Balance Brought Forward as at 12/08/2021', '0.00', '500000.00', '500000.00', '2021-12-08', 151, 1, 6),
(38, '2021-12-16 00:07:47.143112', '2021-12-16 00:07:47.143112', '10100036', 'Balance Brought Forward as at 12/08/2021', '0.00', '200000.00', '200000.00', '2021-12-08', 186, 1, 2),
(43, '2021-12-16 10:06:53.379876', '2021-12-16 10:06:53.379876', '70005005', 'SHARES INITIAL PURCHASE OF 1 BY 10000.0 PER A UNIT', '0.00', '10000.00', '10000.00', '2021-12-16', 209, 1, 15),
(44, '2021-12-16 10:56:30.953431', '2021-12-16 10:56:30.953431', '70000002', '5 Unit(s) Share Purchase, at unit cost of 10000.00 as at 2021-12-16 11:56:16.386004', '0.00', '50000.00', '120000.00', '2021-12-16', 152, 1, 15),
(45, '2021-12-16 12:53:24.627655', '2021-12-16 12:53:24.627655', '10100002', 'Balance Brought Forward as at 12/08/2021', '0.00', '200000.00', '200000.00', '2021-12-08', 152, 1, 2),
(46, '2021-12-16 12:53:24.969363', '2021-12-16 12:53:24.969363', '10200002', 'Balance Brought Forward as at 12/08/2021', '0.00', '150000.00', '150000.00', '2021-12-08', 152, 1, 3),
(47, '2021-12-16 12:53:25.190123', '2021-12-16 12:53:25.190123', '10300002', 'Balance Brought Forward as at 12/08/2021', '0.00', '200000.00', '200000.00', '2021-12-08', 152, 1, 4),
(48, '2021-12-16 12:53:25.363312', '2021-12-16 12:53:25.363312', '10400002', 'Balance Brought Forward as at 12/08/2021', '0.00', '120000.00', '120000.00', '2021-12-08', 152, 1, 5);

-- --------------------------------------------------------

--
-- Table structure for table `processing_status`
--

CREATE TABLE `processing_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `processing_status`
--

INSERT INTO `processing_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'UNPROCESSED', '2021-12-07 18:58:48.250361', '2021-12-07 18:58:48.250361'),
(2, 'PROCESSED', '2021-12-07 18:58:48.351664', '2021-12-07 18:58:48.351664');

-- --------------------------------------------------------

--
-- Table structure for table `product_category`
--

CREATE TABLE `product_category` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `code` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product_category`
--

INSERT INTO `product_category` (`id`, `title`, `created_at`, `updated_at`, `code`) VALUES
(56, 'A', '2021-12-23 01:12:18.781105', '2021-12-23 01:12:18.782103', '1'),
(57, 'B', '2021-12-23 01:12:18.851059', '2021-12-23 01:12:18.851059', '2'),
(58, 'C', '2021-12-23 01:12:19.003516', '2021-12-23 01:12:19.003516', '3'),
(59, 'D', '2021-12-23 01:12:19.060451', '2021-12-23 01:12:19.061451', '4'),
(60, 'E', '2021-12-23 01:12:19.138565', '2021-12-23 01:12:19.138565', '5'),
(61, 'F', '2021-12-23 01:12:19.210464', '2021-12-23 01:12:19.210464', '6'),
(62, 'G', '2021-12-23 01:12:19.376088', '2021-12-23 01:12:19.376088', '7'),
(63, 'H', '2021-12-23 01:12:19.455980', '2021-12-23 01:12:19.456966', '8'),
(64, 'I', '2021-12-23 01:12:19.509048', '2021-12-23 01:12:19.509048', '9'),
(65, 'J', '2021-12-23 01:12:19.578404', '2021-12-23 01:12:19.578404', '10'),
(66, 'K', '2021-12-23 01:12:19.640672', '2021-12-23 01:12:19.640672', '11'),
(67, 'L', '2021-12-23 01:12:19.708651', '2021-12-23 01:12:19.708651', '12'),
(68, 'M', '2021-12-23 01:12:19.776348', '2021-12-23 01:12:19.776348', '13'),
(69, 'N', '2021-12-23 01:12:19.854825', '2021-12-23 01:12:19.855845', '14'),
(70, 'O', '2021-12-23 01:12:19.915787', '2021-12-23 01:12:19.915787', '15'),
(71, 'P', '2021-12-23 01:12:19.949767', '2021-12-23 01:12:19.949767', '16'),
(72, 'Q', '2021-12-23 01:12:20.093675', '2021-12-23 01:12:20.093675', '17'),
(73, 'R', '2021-12-23 01:12:20.159634', '2021-12-23 01:12:20.159634', '18'),
(74, 'S', '2021-12-23 01:12:20.261574', '2021-12-23 01:12:20.261574', '19'),
(75, 'T', '2021-12-23 01:12:20.304545', '2021-12-23 01:12:20.304545', '20'),
(76, 'U', '2021-12-23 01:12:20.450373', '2021-12-23 01:12:20.450373', '21'),
(77, 'V', '2021-12-23 01:12:20.744841', '2021-12-23 01:12:20.744841', '22'),
(78, 'W', '2021-12-23 01:12:20.900112', '2021-12-23 01:12:20.900112', '23'),
(79, 'X', '2021-12-23 01:12:20.966609', '2021-12-23 01:12:20.966609', '24'),
(80, 'Y', '2021-12-23 01:12:21.034851', '2021-12-23 01:12:21.034851', '25'),
(81, 'Z', '2021-12-23 01:12:21.111490', '2021-12-23 01:12:21.111490', '26');

-- --------------------------------------------------------

--
-- Table structure for table `purchases`
--

CREATE TABLE `purchases` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `quantity` int(11) NOT NULL,
  `cost_price` decimal(20,2) NOT NULL,
  `total_cost` decimal(20,2) NOT NULL,
  `selling_price` decimal(20,2) NOT NULL,
  `product_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL,
  `purchase_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `purchases`
--

INSERT INTO `purchases` (`id`, `created_at`, `updated_at`, `quantity`, `cost_price`, `total_cost`, `selling_price`, `product_id`, `status_id`, `purchase_id`) VALUES
(19, '2022-01-14 11:11:52.807432', '2022-01-14 11:11:52.807432', 20, '2200.00', '44000.00', '2300.00', 917, 1, 2),
(20, '2022-01-14 11:11:52.914293', '2022-01-14 11:11:52.914293', 25, '1000.00', '25000.00', '1200.00', 918, 1, 2),
(21, '2022-01-14 11:11:53.282161', '2022-01-14 11:11:53.282161', 10, '1000.00', '10000.00', '1500.00', 1167, 1, 2),
(22, '2022-01-14 11:11:53.384627', '2022-01-14 11:11:53.384627', 5, '3000.00', '15000.00', '3500.00', 922, 1, 2),
(23, '2022-01-14 11:11:53.451580', '2022-01-14 11:11:53.452580', 10, '150.00', '1500.00', '200.00', 1170, 1, 2),
(24, '2022-01-14 11:11:53.537528', '2022-01-14 11:11:53.537528', 5, '7000.00', '35000.00', '8000.00', 1171, 1, 2),
(25, '2022-01-16 15:01:29.648643', '2022-01-16 15:01:29.648643', 34, '2000.00', '68000.00', '2700.00', 935, 1, 3),
(26, '2022-01-16 15:01:29.984493', '2022-01-16 15:01:29.985493', 50, '250.00', '12500.00', '350.00', 946, 1, 3),
(27, '2022-01-16 15:01:30.337781', '2022-01-16 15:01:30.337781', 20, '900.00', '18000.00', '1050.00', 966, 1, 3),
(28, '2022-01-16 15:43:29.537351', '2022-01-16 15:43:29.537351', 50, '3000.00', '150000.00', '3500.00', 922, 1, 5),
(29, '2022-01-16 15:43:29.764967', '2022-01-16 15:43:29.764967', 20, '800.00', '16000.00', '950.00', 924, 1, 5),
(30, '2022-01-16 15:43:30.190569', '2022-01-16 15:43:30.190569', 50, '1350.00', '67500.00', '1450.00', 936, 1, 5),
(31, '2022-01-16 15:43:30.258527', '2022-01-16 15:43:30.258527', 30, '2500.00', '75000.00', '2700.00', 955, 1, 5);

-- --------------------------------------------------------

--
-- Table structure for table `purchase_header`
--

CREATE TABLE `purchase_header` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `total_amount` decimal(20,2) NOT NULL,
  `invoice` varchar(255) NOT NULL,
  `invoice_date` date NOT NULL,
  `branch_id` int(11) NOT NULL,
  `personnel_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) NOT NULL,
  `status_id` int(11) NOT NULL,
  `certification_status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `purchase_header`
--

INSERT INTO `purchase_header` (`id`, `created_at`, `updated_at`, `total_amount`, `invoice`, `invoice_date`, `branch_id`, `personnel_id`, `processed_by_id`, `status_id`, `certification_status_id`) VALUES
(2, '2022-01-12 16:07:34.110241', '2022-01-14 11:11:53.732406', '79000.00', 'MST-00001', '2022-01-12', 3, 5, 13, 2, 2),
(3, '2022-01-16 14:59:15.970696', '2022-01-16 15:01:30.522428', '98500.00', 'HTBC-777777', '2022-01-16', 5, 6, 12, 2, 2),
(5, '2022-01-16 15:31:22.792594', '2022-01-16 15:43:30.408463', '308500.00', 'HTBC-45678', '2022-01-16', 5, 6, 12, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `purchase_temp`
--

CREATE TABLE `purchase_temp` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `quantity` int(11) NOT NULL,
  `cost_price` decimal(20,2) NOT NULL,
  `total_cost` decimal(20,2) NOT NULL,
  `selling_price` decimal(20,2) NOT NULL,
  `product_id` int(11) NOT NULL,
  `purchase_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `receipts`
--

CREATE TABLE `receipts` (
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `id` int(11) NOT NULL,
  `receipt` varchar(255) NOT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `receipts`
--

INSERT INTO `receipts` (`created_at`, `updated_at`, `id`, `receipt`, `status_id`) VALUES
('2021-12-07 19:58:05.182278', '2021-12-15 03:37:04.217892', 1, '00001', 2),
('2021-12-07 19:58:05.294732', '2021-12-15 04:12:49.206360', 2, '00002', 2),
('2021-12-07 19:58:05.346519', '2021-12-15 04:25:22.511701', 3, '00003', 2),
('2021-12-07 19:58:05.504739', '2021-12-14 01:53:02.825822', 4, '00004', 1),
('2021-12-07 19:58:05.570802', '2021-12-15 04:28:39.129371', 5, '00005', 2),
('2021-12-07 19:58:05.604749', '2021-12-15 04:29:49.851801', 6, '00006', 2),
('2021-12-07 19:58:05.649242', '2021-12-15 04:38:43.249492', 7, '00007', 2),
('2021-12-07 19:58:05.682268', '2021-12-15 04:44:31.892675', 8, '00008', 2),
('2021-12-07 19:58:05.775285', '2021-12-15 04:46:44.014275', 9, '00009', 2),
('2021-12-07 19:58:05.838969', '2021-12-14 02:11:01.312015', 10, '00010', 1),
('2021-12-07 19:58:05.879854', '2021-12-14 02:12:33.159115', 11, '00011', 1),
('2021-12-07 19:58:05.926824', '2021-12-14 02:13:57.307123', 12, '00012', 1),
('2021-12-07 19:58:05.959803', '2021-12-07 19:58:05.959803', 13, '00013', 1),
('2021-12-07 19:58:06.083789', '2021-12-07 19:58:06.083789', 14, '00014', 1),
('2021-12-07 19:58:06.204748', '2021-12-07 19:58:06.204748', 15, '00015', 1),
('2021-12-07 19:58:06.249412', '2021-12-14 02:15:19.042746', 16, '00016', 1),
('2021-12-07 19:58:06.293696', '2021-12-07 19:58:06.293696', 17, '00017', 1),
('2021-12-07 19:58:06.348675', '2021-12-14 02:16:48.614596', 18, '00018', 1),
('2021-12-07 19:58:06.405948', '2021-12-07 19:58:06.405948', 19, '00019', 1),
('2021-12-07 19:58:06.471117', '2021-12-14 02:19:13.042232', 20, '00020', 1),
('2021-12-07 19:58:06.516223', '2021-12-14 02:21:27.221399', 21, '00021', 1),
('2021-12-07 19:58:06.548932', '2021-12-14 02:23:10.088583', 22, '00022', 1),
('2021-12-07 19:58:06.640601', '2021-12-14 19:23:20.699364', 23, '00023', 1),
('2021-12-07 19:58:06.679342', '2021-12-14 19:24:28.332253', 24, '00024', 1),
('2021-12-07 19:58:06.727525', '2021-12-07 19:58:06.727525', 25, '00025', 1),
('2021-12-07 19:58:06.772727', '2021-12-07 19:58:06.772727', 26, '00026', 1),
('2021-12-07 19:58:06.942432', '2021-12-07 19:58:06.942432', 27, '00027', 1),
('2021-12-07 19:58:06.970991', '2021-12-07 19:58:06.970991', 28, '00028', 1),
('2021-12-07 19:58:07.017086', '2021-12-07 19:58:07.017086', 29, '00029', 1),
('2021-12-07 19:58:07.182684', '2021-12-07 19:58:07.182684', 30, '00030', 1),
('2021-12-07 19:58:07.315748', '2021-12-14 20:44:55.570946', 31, '00031', 1),
('2021-12-07 19:58:07.362061', '2021-12-14 20:45:54.598030', 32, '00032', 1),
('2021-12-07 19:58:07.394276', '2021-12-07 19:58:07.394276', 33, '00033', 1),
('2021-12-07 19:58:07.427478', '2021-12-07 19:58:07.428477', 34, '00034', 1),
('2021-12-07 19:58:07.460759', '2021-12-15 03:19:43.413169', 35, '00035', 1),
('2021-12-07 19:58:07.494776', '2021-12-07 19:58:07.494776', 36, '00036', 1),
('2021-12-07 19:58:07.534977', '2021-12-15 03:21:25.442354', 37, '00037', 1),
('2021-12-07 19:58:07.561130', '2021-12-07 19:58:07.561130', 38, '00038', 1),
('2021-12-07 19:58:07.593761', '2021-12-07 19:58:07.593761', 39, '00039', 1),
('2021-12-07 19:58:07.635010', '2021-12-15 03:27:17.052943', 40, '00040', 1),
('2021-12-07 19:58:07.693518', '2021-12-15 03:30:26.890934', 41, '00041', 1),
('2021-12-07 19:58:07.717598', '2021-12-07 19:58:07.717598', 42, '00042', 1),
('2021-12-07 19:58:07.760382', '2021-12-07 19:58:07.760382', 43, '00043', 1),
('2021-12-07 19:58:07.801950', '2021-12-07 19:58:07.801950', 44, '00044', 1),
('2021-12-07 19:58:07.850231', '2021-12-07 19:58:07.850231', 45, '00045', 1),
('2021-12-07 19:58:07.905473', '2021-12-07 19:58:07.905473', 46, '00046', 1),
('2021-12-07 19:58:07.938271', '2021-12-07 19:58:07.938271', 47, '00047', 1),
('2021-12-07 19:58:07.990852', '2021-12-07 19:58:07.990852', 48, '00048', 1),
('2021-12-07 19:58:08.016818', '2021-12-07 19:58:08.016818', 49, '00049', 1),
('2021-12-07 19:58:08.051792', '2021-12-07 19:58:08.051792', 50, '00050', 1),
('2021-12-07 19:58:08.083771', '2021-12-07 19:58:08.083771', 51, '00051', 1),
('2021-12-07 19:58:08.117750', '2021-12-07 19:58:08.117750', 52, '00052', 1),
('2021-12-07 19:58:08.184709', '2021-12-07 19:58:08.184709', 53, '00053', 1),
('2021-12-07 19:58:08.249670', '2021-12-07 19:58:08.249670', 54, '00054', 1),
('2021-12-07 19:58:08.283648', '2021-12-07 19:58:08.283648', 55, '00055', 1),
('2021-12-07 19:58:08.315629', '2021-12-07 19:58:08.315629', 56, '00056', 1),
('2021-12-07 19:58:08.339623', '2021-12-07 19:58:08.339623', 57, '00057', 1),
('2021-12-07 19:58:08.382587', '2021-12-07 19:58:08.382587', 58, '00058', 1),
('2021-12-07 19:58:08.427559', '2021-12-07 19:58:08.427559', 59, '00059', 1),
('2021-12-07 19:58:08.460539', '2021-12-07 19:58:08.460539', 60, '00060', 1),
('2021-12-07 19:58:08.505512', '2021-12-07 19:58:08.505512', 61, '00061', 1),
('2021-12-07 19:58:08.538492', '2021-12-07 19:58:08.539492', 62, '00062', 1),
('2021-12-07 19:58:08.572471', '2021-12-07 19:58:08.572471', 63, '00063', 1),
('2021-12-07 19:58:08.606450', '2021-12-07 19:58:08.606450', 64, '00064', 1),
('2021-12-07 19:58:08.650422', '2021-12-07 19:58:08.650422', 65, '00065', 1),
('2021-12-07 19:58:08.682402', '2021-12-07 19:58:08.682402', 66, '00066', 1),
('2021-12-07 19:58:08.706389', '2021-12-07 19:58:08.706389', 67, '00067', 1),
('2021-12-07 19:58:08.739504', '2021-12-07 19:58:08.739504', 68, '00068', 1),
('2021-12-07 19:58:08.772687', '2021-12-07 19:58:08.772687', 69, '00069', 1),
('2021-12-07 19:58:08.816669', '2021-12-07 19:58:08.816669', 70, '00070', 1),
('2021-12-07 19:58:08.848821', '2021-12-07 19:58:08.848821', 71, '00071', 1),
('2021-12-07 19:58:08.871888', '2021-12-07 19:58:08.872896', 72, '00072', 1),
('2021-12-07 19:58:08.913160', '2021-12-07 19:58:08.913160', 73, '00073', 1),
('2021-12-07 19:58:08.938283', '2021-12-07 19:58:08.938283', 74, '00074', 1),
('2021-12-07 19:58:08.971046', '2021-12-07 19:58:08.971046', 75, '00075', 1),
('2021-12-07 19:58:08.994059', '2021-12-07 19:58:08.994059', 76, '00076', 1),
('2021-12-07 19:58:09.037761', '2021-12-07 19:58:09.037761', 77, '00077', 1),
('2021-12-07 19:58:09.061360', '2021-12-07 19:58:09.061360', 78, '00078', 1),
('2021-12-07 19:58:09.144998', '2021-12-07 19:58:09.144998', 79, '00079', 1),
('2021-12-07 19:58:09.250417', '2021-12-07 19:58:09.250417', 80, '00080', 1),
('2021-12-07 19:58:09.295312', '2021-12-07 19:58:09.295312', 81, '00081', 1),
('2021-12-07 19:58:09.328508', '2021-12-07 19:58:09.328508', 82, '00082', 1),
('2021-12-07 19:58:09.371991', '2021-12-07 19:58:09.371991', 83, '00083', 1),
('2021-12-07 19:58:09.405119', '2021-12-07 19:58:09.406131', 84, '00084', 1),
('2021-12-07 19:58:09.437834', '2021-12-07 19:58:09.438848', 85, '00085', 1),
('2021-12-07 19:58:09.494585', '2021-12-07 19:58:09.495585', 86, '00086', 1),
('2021-12-07 19:58:09.549555', '2021-12-07 19:58:09.549555', 87, '00087', 1),
('2021-12-07 19:58:09.571536', '2021-12-07 19:58:09.571536', 88, '00088', 1),
('2021-12-07 19:58:09.615511', '2021-12-07 19:58:09.616510', 89, '00089', 1),
('2021-12-07 19:58:09.657483', '2021-12-07 19:58:09.657483', 90, '00090', 1),
('2021-12-07 19:58:09.704518', '2021-12-07 19:58:09.704518', 91, '00091', 1),
('2021-12-07 19:58:09.750539', '2021-12-07 19:58:09.750539', 92, '00092', 1),
('2021-12-07 19:58:09.782626', '2021-12-07 19:58:09.782626', 93, '00093', 1),
('2021-12-07 19:58:09.816675', '2021-12-07 19:58:09.816675', 94, '00094', 1),
('2021-12-07 19:58:09.871247', '2021-12-07 19:58:09.871247', 95, '00095', 1),
('2021-12-07 19:58:09.894271', '2021-12-07 19:58:09.894271', 96, '00096', 1),
('2021-12-07 19:58:09.927052', '2021-12-07 19:58:09.927052', 97, '00097', 1),
('2021-12-07 19:58:09.971877', '2021-12-07 19:58:09.971877', 98, '00098', 1),
('2021-12-07 19:58:10.004705', '2021-12-07 19:58:10.004705', 99, '00099', 1),
('2021-12-07 19:58:10.027431', '2021-12-07 19:58:10.027431', 100, '00100', 1),
('2021-12-07 19:58:10.059984', '2021-12-07 19:58:10.060988', 101, '00101', 1),
('2021-12-07 19:58:10.084411', '2021-12-07 19:58:10.084411', 102, '00102', 1),
('2021-12-07 19:58:10.121996', '2021-12-07 19:58:10.121996', 103, '00103', 1),
('2021-12-07 19:58:10.150218', '2021-12-07 19:58:10.150218', 104, '00104', 1),
('2021-12-07 19:58:10.205154', '2021-12-07 19:58:10.205154', 105, '00105', 1),
('2021-12-07 19:58:10.239077', '2021-12-07 19:58:10.239077', 106, '00106', 1),
('2021-12-07 19:58:10.282531', '2021-12-07 19:58:10.282531', 107, '00107', 1),
('2021-12-07 19:58:10.371994', '2021-12-07 19:58:10.371994', 108, '00108', 1),
('2021-12-07 19:58:10.406048', '2021-12-07 19:58:10.406048', 109, '00109', 1),
('2021-12-07 19:58:10.438485', '2021-12-07 19:58:10.438485', 110, '00110', 1),
('2021-12-07 19:58:10.472493', '2021-12-07 19:58:10.472493', 111, '00111', 1),
('2021-12-07 19:58:10.516088', '2021-12-07 19:58:10.516088', 112, '00112', 1),
('2021-12-07 19:58:10.539769', '2021-12-07 19:58:10.539769', 113, '00113', 1),
('2021-12-07 19:58:10.572041', '2021-12-07 19:58:10.572041', 114, '00114', 1),
('2021-12-07 19:58:10.605863', '2021-12-07 19:58:10.605863', 115, '00115', 1),
('2021-12-07 19:58:10.638988', '2021-12-07 19:58:10.638988', 116, '00116', 1),
('2021-12-07 19:58:10.694086', '2021-12-07 19:58:10.694086', 117, '00117', 1),
('2021-12-07 19:58:10.739057', '2021-12-07 19:58:10.740057', 118, '00118', 1),
('2021-12-07 19:58:10.772039', '2021-12-07 19:58:10.773036', 119, '00119', 1),
('2021-12-07 19:58:10.816007', '2021-12-07 19:58:10.816007', 120, '00120', 1),
('2021-12-07 19:58:10.838994', '2021-12-07 19:58:10.838994', 121, '00121', 1),
('2021-12-07 19:58:10.871974', '2021-12-07 19:58:10.871974', 122, '00122', 1),
('2021-12-07 19:58:10.906004', '2021-12-07 19:58:10.906004', 123, '00123', 1),
('2021-12-07 19:58:10.950385', '2021-12-07 19:58:10.950385', 124, '00124', 1),
('2021-12-07 19:58:10.984301', '2021-12-07 19:58:10.984301', 125, '00125', 1),
('2021-12-07 19:58:11.017206', '2021-12-07 19:58:11.017206', 126, '00126', 1),
('2021-12-07 19:58:11.050973', '2021-12-07 19:58:11.050973', 127, '00127', 1),
('2021-12-07 19:58:11.083154', '2021-12-07 19:58:11.084147', 128, '00128', 1),
('2021-12-07 19:58:11.117342', '2021-12-07 19:58:11.117342', 129, '00129', 1),
('2021-12-07 19:58:11.149388', '2021-12-07 19:58:11.149388', 130, '00130', 1),
('2021-12-07 19:58:11.939562', '2021-12-07 19:58:11.939562', 131, '00131', 1),
('2021-12-07 19:58:12.084479', '2021-12-07 19:58:12.084479', 132, '00132', 1),
('2021-12-07 19:58:12.138929', '2021-12-07 19:58:12.139924', 133, '00133', 1),
('2021-12-07 19:58:12.183440', '2021-12-07 19:58:12.183440', 134, '00134', 1),
('2021-12-07 19:58:12.227330', '2021-12-07 19:58:12.227330', 135, '00135', 1),
('2021-12-07 19:58:12.270754', '2021-12-07 19:58:12.270754', 136, '00136', 1),
('2021-12-07 19:58:12.327338', '2021-12-07 19:58:12.327338', 137, '00137', 1),
('2021-12-07 19:58:12.383469', '2021-12-07 19:58:12.383469', 138, '00138', 1),
('2021-12-07 19:58:12.450192', '2021-12-07 19:58:12.450192', 139, '00139', 1),
('2021-12-07 19:58:12.546765', '2021-12-07 19:58:12.546765', 140, '00140', 1),
('2021-12-07 19:58:12.607011', '2021-12-07 19:58:12.607011', 141, '00141', 1),
('2021-12-07 19:58:12.660740', '2021-12-07 19:58:12.660740', 142, '00142', 1),
('2021-12-07 19:58:12.694700', '2021-12-07 19:58:12.694700', 143, '00143', 1),
('2021-12-07 19:58:12.739786', '2021-12-07 19:58:12.739786', 144, '00144', 1),
('2021-12-07 19:58:12.773018', '2021-12-07 19:58:12.773018', 145, '00145', 1),
('2021-12-07 19:58:12.806010', '2021-12-07 19:58:12.806010', 146, '00146', 1),
('2021-12-07 19:58:12.840140', '2021-12-07 19:58:12.840140', 147, '00147', 1),
('2021-12-07 19:58:12.895358', '2021-12-07 19:58:12.896358', 148, '00148', 1),
('2021-12-07 19:58:12.929444', '2021-12-07 19:58:12.929444', 149, '00149', 1),
('2021-12-07 19:58:13.138216', '2021-12-07 19:58:13.138216', 150, '00150', 1),
('2021-12-07 19:58:13.191182', '2021-12-07 19:58:13.191182', 151, '00151', 1),
('2021-12-07 19:58:13.236155', '2021-12-07 19:58:13.236155', 152, '00152', 1),
('2021-12-07 19:58:13.305111', '2021-12-07 19:58:13.305111', 153, '00153', 1),
('2021-12-07 19:58:13.324689', '2021-12-07 19:58:13.324689', 154, '00154', 1),
('2021-12-07 19:58:13.372125', '2021-12-07 19:58:13.372125', 155, '00155', 1),
('2021-12-07 19:58:13.415976', '2021-12-07 19:58:13.415976', 156, '00156', 1),
('2021-12-07 19:58:13.460930', '2021-12-07 19:58:13.461938', 157, '00157', 1),
('2021-12-07 19:58:13.584846', '2021-12-07 19:58:13.584846', 158, '00158', 1),
('2021-12-07 19:58:13.747192', '2021-12-07 19:58:13.747192', 159, '00159', 1),
('2021-12-07 19:58:13.794328', '2021-12-07 19:58:13.794328', 160, '00160', 1),
('2021-12-07 19:58:13.836353', '2021-12-07 19:58:13.836353', 161, '00161', 1),
('2021-12-07 19:58:13.883680', '2021-12-07 19:58:13.884677', 162, '00162', 1),
('2021-12-07 19:58:13.916699', '2021-12-07 19:58:13.916699', 163, '00163', 1),
('2021-12-07 19:58:13.950791', '2021-12-07 19:58:13.950791', 164, '00164', 1),
('2021-12-07 19:58:13.983843', '2021-12-07 19:58:13.983843', 165, '00165', 1),
('2021-12-07 19:58:14.017223', '2021-12-07 19:58:14.017223', 166, '00166', 1),
('2021-12-07 19:58:14.127594', '2021-12-07 19:58:14.127594', 167, '00167', 1),
('2021-12-07 19:58:14.170379', '2021-12-07 19:58:14.170379', 168, '00168', 1),
('2021-12-07 19:58:14.216055', '2021-12-07 19:58:14.216055', 169, '00169', 1),
('2021-12-07 19:58:14.239070', '2021-12-07 19:58:14.239070', 170, '00170', 1),
('2021-12-07 19:58:14.272151', '2021-12-07 19:58:14.272151', 171, '00171', 1),
('2021-12-07 19:58:14.313690', '2021-12-07 19:58:14.313690', 172, '00172', 1),
('2021-12-07 19:58:14.361032', '2021-12-07 19:58:14.361032', 173, '00173', 1),
('2021-12-07 19:58:14.427987', '2021-12-07 19:58:14.427987', 174, '00174', 1),
('2021-12-07 19:58:14.472961', '2021-12-07 19:58:14.472961', 175, '00175', 1),
('2021-12-07 19:58:14.506941', '2021-12-07 19:58:14.506941', 176, '00176', 1),
('2021-12-07 19:58:14.538968', '2021-12-07 19:58:14.538968', 177, '00177', 1),
('2021-12-07 19:58:14.574000', '2021-12-07 19:58:14.574000', 178, '00178', 1),
('2021-12-07 19:58:14.616748', '2021-12-07 19:58:14.616748', 179, '00179', 1),
('2021-12-07 19:58:14.649518', '2021-12-07 19:58:14.649518', 180, '00180', 1),
('2021-12-07 19:58:14.745877', '2021-12-07 19:58:14.745877', 181, '00181', 1),
('2021-12-07 19:58:14.782906', '2021-12-07 19:58:14.782906', 182, '00182', 1),
('2021-12-07 19:58:14.828826', '2021-12-07 19:58:14.828826', 183, '00183', 1),
('2021-12-07 19:58:14.861317', '2021-12-07 19:58:14.861317', 184, '00184', 1),
('2021-12-07 19:58:14.895406', '2021-12-07 19:58:14.895406', 185, '00185', 1),
('2021-12-07 19:58:14.927421', '2021-12-07 19:58:14.927421', 186, '00186', 1),
('2021-12-07 19:58:14.972369', '2021-12-07 19:58:14.972369', 187, '00187', 1),
('2021-12-07 19:58:15.005560', '2021-12-07 19:58:15.005560', 188, '00188', 1),
('2021-12-07 19:58:15.050199', '2021-12-07 19:58:15.050199', 189, '00189', 1),
('2021-12-07 19:58:15.071814', '2021-12-07 19:58:15.071814', 190, '00190', 1),
('2021-12-07 19:58:15.150624', '2021-12-07 19:58:15.150624', 191, '00191', 1),
('2021-12-07 19:58:15.194826', '2021-12-07 19:58:15.194826', 192, '00192', 1),
('2021-12-07 19:58:15.239154', '2021-12-07 19:58:15.239154', 193, '00193', 1),
('2021-12-07 19:58:15.271912', '2021-12-07 19:58:15.271912', 194, '00194', 1),
('2021-12-07 19:58:15.314715', '2021-12-07 19:58:15.314715', 195, '00195', 1),
('2021-12-07 19:58:15.338760', '2021-12-07 19:58:15.338760', 196, '00196', 1),
('2021-12-07 19:58:15.361952', '2021-12-07 19:58:15.361952', 197, '00197', 1),
('2021-12-07 19:58:15.405304', '2021-12-07 19:58:15.405304', 198, '00198', 1),
('2021-12-07 19:58:15.428759', '2021-12-07 19:58:15.428759', 199, '00199', 1),
('2021-12-07 19:58:15.460858', '2021-12-07 19:58:15.460858', 200, '00200', 1),
('2021-12-07 19:58:15.483902', '2021-12-07 19:58:15.483902', 201, '00201', 1),
('2021-12-07 19:58:15.516955', '2021-12-07 19:58:15.516955', 202, '00202', 1),
('2021-12-07 19:58:15.539255', '2021-12-07 19:58:15.539255', 203, '00203', 1),
('2021-12-07 19:58:15.605269', '2021-12-07 19:58:15.605269', 204, '00204', 1),
('2021-12-07 19:58:15.839275', '2021-12-07 19:58:15.839275', 205, '00205', 1),
('2021-12-07 19:58:15.872087', '2021-12-07 19:58:15.872087', 206, '00206', 1),
('2021-12-07 19:58:15.894837', '2021-12-07 19:58:15.894837', 207, '00207', 1),
('2021-12-07 19:58:15.927703', '2021-12-07 19:58:15.927703', 208, '00208', 1),
('2021-12-07 19:58:15.972709', '2021-12-07 19:58:15.972709', 209, '00209', 1),
('2021-12-07 19:58:16.027654', '2021-12-07 19:58:16.027654', 210, '00210', 1),
('2021-12-07 19:58:16.051474', '2021-12-07 19:58:16.051474', 211, '00211', 1),
('2021-12-07 19:58:16.105589', '2021-12-07 19:58:16.105589', 212, '00212', 1),
('2021-12-07 19:58:16.143628', '2021-12-07 19:58:16.143628', 213, '00213', 1),
('2021-12-07 19:58:16.240904', '2021-12-07 19:58:16.240904', 214, '00214', 1),
('2021-12-07 19:58:16.273057', '2021-12-07 19:58:16.273057', 215, '00215', 1),
('2021-12-07 19:58:16.305624', '2021-12-07 19:58:16.305624', 216, '00216', 1),
('2021-12-07 19:58:16.350110', '2021-12-07 19:58:16.350110', 217, '00217', 1),
('2021-12-07 19:58:16.372830', '2021-12-07 19:58:16.372830', 218, '00218', 1),
('2021-12-07 19:58:16.416660', '2021-12-07 19:58:16.416660', 219, '00219', 1),
('2021-12-07 19:58:16.471950', '2021-12-07 19:58:16.471950', 220, '00220', 1),
('2021-12-07 19:58:16.527780', '2021-12-07 19:58:16.527780', 221, '00221', 1),
('2021-12-07 19:58:16.572361', '2021-12-07 19:58:16.573360', 222, '00222', 1),
('2021-12-07 19:58:16.605586', '2021-12-07 19:58:16.606592', 223, '00223', 1),
('2021-12-07 19:58:16.662084', '2021-12-07 19:58:16.662084', 224, '00224', 1),
('2021-12-07 19:58:16.696604', '2021-12-07 19:58:16.696604', 225, '00225', 1),
('2021-12-07 19:58:17.180094', '2021-12-07 19:58:17.180094', 226, '00226', 1),
('2021-12-07 19:58:17.293171', '2021-12-07 19:58:17.293171', 227, '00227', 1),
('2021-12-07 19:58:17.349637', '2021-12-07 19:58:17.349637', 228, '00228', 1),
('2021-12-07 19:58:17.372298', '2021-12-07 19:58:17.372298', 229, '00229', 1),
('2021-12-07 19:58:17.427279', '2021-12-07 19:58:17.427279', 230, '00230', 1),
('2021-12-07 19:58:17.484424', '2021-12-07 19:58:17.484424', 231, '00231', 1),
('2021-12-07 19:58:17.525453', '2021-12-07 19:58:17.525453', 232, '00232', 1),
('2021-12-07 19:58:17.550584', '2021-12-07 19:58:17.550584', 233, '00233', 1),
('2021-12-07 19:58:17.593956', '2021-12-07 19:58:17.593956', 234, '00234', 1),
('2021-12-07 19:58:17.651164', '2021-12-07 19:58:17.651164', 235, '00235', 1),
('2021-12-07 19:58:17.684258', '2021-12-07 19:58:17.684258', 236, '00236', 1),
('2021-12-07 19:58:17.727923', '2021-12-07 19:58:17.727923', 237, '00237', 1),
('2021-12-07 19:58:17.751826', '2021-12-07 19:58:17.751826', 238, '00238', 1),
('2021-12-07 19:58:17.794014', '2021-12-07 19:58:17.794014', 239, '00239', 1),
('2021-12-07 19:58:17.851142', '2021-12-07 19:58:17.851142', 240, '00240', 1),
('2021-12-07 19:58:17.883310', '2021-12-07 19:58:17.884318', 241, '00241', 1),
('2021-12-07 19:58:17.917490', '2021-12-07 19:58:17.918488', 242, '00242', 1),
('2021-12-07 19:58:17.971787', '2021-12-07 19:58:17.971787', 243, '00243', 1),
('2021-12-07 19:58:18.017173', '2021-12-07 19:58:18.017173', 244, '00244', 1),
('2021-12-07 19:58:18.050155', '2021-12-07 19:58:18.050155', 245, '00245', 1),
('2021-12-07 19:58:18.072141', '2021-12-07 19:58:18.073141', 246, '00246', 1),
('2021-12-07 19:58:18.094126', '2021-12-07 19:58:18.094126', 247, '00247', 1),
('2021-12-07 19:58:18.117110', '2021-12-07 19:58:18.117110', 248, '00248', 1),
('2021-12-07 19:58:18.327477', '2021-12-07 19:58:18.327477', 249, '00249', 1),
('2021-12-07 19:58:18.509102', '2021-12-07 19:58:18.509102', 250, '00250', 1),
('2021-12-07 19:58:18.584211', '2021-12-07 19:58:18.584211', 251, '00251', 1),
('2021-12-07 19:58:18.630285', '2021-12-07 19:58:18.630285', 252, '00252', 1),
('2021-12-07 19:58:18.683722', '2021-12-07 19:58:18.684736', 253, '00253', 1),
('2021-12-07 19:58:18.705381', '2021-12-07 19:58:18.706389', 254, '00254', 1),
('2021-12-07 19:58:18.729226', '2021-12-07 19:58:18.729226', 255, '00255', 1),
('2021-12-07 19:58:18.761839', '2021-12-07 19:58:18.761839', 256, '00256', 1),
('2021-12-07 19:58:18.795170', '2021-12-07 19:58:18.796164', 257, '00257', 1),
('2021-12-07 19:58:18.872858', '2021-12-07 19:58:18.872858', 258, '00258', 1),
('2021-12-07 19:58:18.929099', '2021-12-07 19:58:18.929099', 259, '00259', 1),
('2021-12-07 19:58:18.962277', '2021-12-07 19:58:18.962277', 260, '00260', 1),
('2021-12-07 19:58:19.005348', '2021-12-07 19:58:19.006349', 261, '00261', 1),
('2021-12-07 19:58:19.050504', '2021-12-07 19:58:19.050504', 262, '00262', 1),
('2021-12-07 19:58:19.072119', '2021-12-07 19:58:19.072119', 263, '00263', 1),
('2021-12-07 19:58:19.095238', '2021-12-07 19:58:19.095238', 264, '00264', 1),
('2021-12-07 19:58:19.128459', '2021-12-07 19:58:19.129458', 265, '00265', 1),
('2021-12-07 19:58:19.162688', '2021-12-07 19:58:19.162688', 266, '00266', 1),
('2021-12-07 19:58:19.194910', '2021-12-07 19:58:19.195911', 267, '00267', 1),
('2021-12-07 19:58:19.229528', '2021-12-07 19:58:19.229528', 268, '00268', 1),
('2021-12-07 19:58:19.261507', '2021-12-07 19:58:19.261507', 269, '00269', 1),
('2021-12-07 19:58:19.284494', '2021-12-07 19:58:19.284494', 270, '00270', 1),
('2021-12-07 19:58:19.520589', '2021-12-07 19:58:19.520589', 271, '00271', 1),
('2021-12-07 19:58:19.676144', '2021-12-07 19:58:19.676144', 272, '00272', 1),
('2021-12-07 19:58:19.817053', '2021-12-07 19:58:19.818053', 273, '00273', 1),
('2021-12-07 19:58:19.917425', '2021-12-07 19:58:19.917425', 274, '00274', 1),
('2021-12-07 19:58:19.985083', '2021-12-07 19:58:19.985083', 275, '00275', 1),
('2021-12-07 19:58:20.089962', '2021-12-07 19:58:20.089962', 276, '00276', 1),
('2021-12-07 19:58:20.173879', '2021-12-07 19:58:20.173879', 277, '00277', 1),
('2021-12-07 19:58:20.238178', '2021-12-07 19:58:20.238178', 278, '00278', 1),
('2021-12-07 19:58:20.296943', '2021-12-07 19:58:20.296943', 279, '00279', 1),
('2021-12-07 19:58:20.353205', '2021-12-07 19:58:20.353205', 280, '00280', 1),
('2021-12-07 19:58:20.429561', '2021-12-07 19:58:20.429561', 281, '00281', 1),
('2021-12-07 19:58:20.510509', '2021-12-07 19:58:20.510509', 282, '00282', 1),
('2021-12-07 19:58:20.551484', '2021-12-07 19:58:20.551484', 283, '00283', 1),
('2021-12-07 19:58:20.650186', '2021-12-07 19:58:20.650186', 284, '00284', 1),
('2021-12-07 19:58:20.673894', '2021-12-07 19:58:20.673894', 285, '00285', 1),
('2021-12-07 19:58:20.706453', '2021-12-07 19:58:20.706453', 286, '00286', 1),
('2021-12-07 19:58:20.781817', '2021-12-07 19:58:20.781817', 287, '00287', 1),
('2021-12-07 19:58:20.816333', '2021-12-07 19:58:20.816333', 288, '00288', 1),
('2021-12-07 19:58:20.839136', '2021-12-07 19:58:20.839136', 289, '00289', 1),
('2021-12-07 19:58:20.861656', '2021-12-07 19:58:20.861656', 290, '00290', 1),
('2021-12-07 19:58:20.883779', '2021-12-07 19:58:20.883779', 291, '00291', 1),
('2021-12-07 19:58:20.906145', '2021-12-07 19:58:20.906145', 292, '00292', 1),
('2021-12-07 19:58:20.973470', '2021-12-07 19:58:20.973470', 293, '00293', 1),
('2021-12-07 19:58:21.017655', '2021-12-07 19:58:21.017655', 294, '00294', 1),
('2021-12-07 19:58:21.059708', '2021-12-07 19:58:21.059708', 295, '00295', 1),
('2021-12-07 19:58:21.105909', '2021-12-07 19:58:21.106922', 296, '00296', 1),
('2021-12-07 19:58:21.150314', '2021-12-07 19:58:21.150314', 297, '00297', 1),
('2021-12-07 19:58:21.196059', '2021-12-07 19:58:21.196059', 298, '00298', 1),
('2021-12-07 19:58:21.238825', '2021-12-07 19:58:21.238825', 299, '00299', 1),
('2021-12-07 19:58:21.283850', '2021-12-07 19:58:21.284846', 300, '00300', 1),
('2021-12-07 19:58:21.328587', '2021-12-07 19:58:21.328587', 301, '00301', 1),
('2021-12-07 19:58:21.372836', '2021-12-07 19:58:21.373862', 302, '00302', 1),
('2021-12-07 19:58:21.418149', '2021-12-07 19:58:21.418149', 303, '00303', 1),
('2021-12-07 19:58:21.462557', '2021-12-07 19:58:21.462557', 304, '00304', 1),
('2021-12-07 19:58:21.484662', '2021-12-07 19:58:21.484662', 305, '00305', 1),
('2021-12-07 19:58:21.517750', '2021-12-07 19:58:21.517750', 306, '00306', 1),
('2021-12-07 19:58:21.550800', '2021-12-07 19:58:21.550800', 307, '00307', 1),
('2021-12-07 19:58:21.573713', '2021-12-07 19:58:21.573713', 308, '00308', 1),
('2021-12-07 19:58:21.594868', '2021-12-07 19:58:21.594868', 309, '00309', 1),
('2021-12-07 19:58:21.838763', '2021-12-07 19:58:21.838763', 310, '00310', 1),
('2021-12-07 19:58:21.951238', '2021-12-07 19:58:21.951238', 311, '00311', 1),
('2021-12-07 19:58:22.027697', '2021-12-07 19:58:22.027697', 312, '00312', 1),
('2021-12-07 19:58:22.050566', '2021-12-07 19:58:22.050566', 313, '00313', 1),
('2021-12-07 19:58:22.072763', '2021-12-07 19:58:22.072763', 314, '00314', 1),
('2021-12-07 19:58:22.126045', '2021-12-07 19:58:22.126045', 315, '00315', 1),
('2021-12-07 19:58:22.150505', '2021-12-07 19:58:22.150505', 316, '00316', 1),
('2021-12-07 19:58:22.173553', '2021-12-07 19:58:22.173553', 317, '00317', 1),
('2021-12-07 19:58:22.194491', '2021-12-07 19:58:22.194491', 318, '00318', 1),
('2021-12-07 19:58:22.217967', '2021-12-07 19:58:22.217967', 319, '00319', 1),
('2021-12-07 19:58:22.283386', '2021-12-07 19:58:22.283386', 320, '00320', 1),
('2021-12-07 19:58:22.307072', '2021-12-07 19:58:22.307072', 321, '00321', 1),
('2021-12-07 19:58:22.339757', '2021-12-07 19:58:22.339757', 322, '00322', 1),
('2021-12-07 19:58:22.361738', '2021-12-07 19:58:22.361738', 323, '00323', 1),
('2021-12-07 19:58:22.383433', '2021-12-07 19:58:22.383433', 324, '00324', 1),
('2021-12-07 19:58:22.407146', '2021-12-07 19:58:22.407146', 325, '00325', 1),
('2021-12-07 19:58:22.440262', '2021-12-07 19:58:22.440262', 326, '00326', 1),
('2021-12-07 19:58:22.473433', '2021-12-07 19:58:22.473433', 327, '00327', 1),
('2021-12-07 19:58:22.494317', '2021-12-07 19:58:22.495329', 328, '00328', 1),
('2021-12-07 19:58:22.517516', '2021-12-07 19:58:22.517516', 329, '00329', 1),
('2021-12-07 19:58:22.539540', '2021-12-07 19:58:22.539540', 330, '00330', 1),
('2021-12-07 19:58:22.574608', '2021-12-07 19:58:22.574608', 331, '00331', 1),
('2021-12-07 19:58:22.617047', '2021-12-07 19:58:22.617047', 332, '00332', 1),
('2021-12-07 19:58:22.639954', '2021-12-07 19:58:22.639954', 333, '00333', 1),
('2021-12-07 19:58:22.673628', '2021-12-07 19:58:22.673628', 334, '00334', 1),
('2021-12-07 19:58:22.705594', '2021-12-07 19:58:22.705594', 335, '00335', 1),
('2021-12-07 19:58:22.728651', '2021-12-07 19:58:22.728651', 336, '00336', 1),
('2021-12-07 19:58:22.749867', '2021-12-07 19:58:22.749867', 337, '00337', 1),
('2021-12-07 19:58:22.772659', '2021-12-07 19:58:22.772659', 338, '00338', 1),
('2021-12-07 19:58:22.795277', '2021-12-07 19:58:22.795277', 339, '00339', 1),
('2021-12-07 19:58:22.817107', '2021-12-07 19:58:22.817107', 340, '00340', 1),
('2021-12-07 19:58:22.839379', '2021-12-07 19:58:22.839379', 341, '00341', 1),
('2021-12-07 19:58:22.862367', '2021-12-07 19:58:22.862367', 342, '00342', 1),
('2021-12-07 19:58:22.883354', '2021-12-07 19:58:22.883354', 343, '00343', 1),
('2021-12-07 19:58:22.906337', '2021-12-07 19:58:22.906337', 344, '00344', 1),
('2021-12-07 19:58:22.929325', '2021-12-07 19:58:22.929325', 345, '00345', 1),
('2021-12-07 19:58:22.999281', '2021-12-07 19:58:22.999281', 346, '00346', 1),
('2021-12-07 19:58:23.179511', '2021-12-07 19:58:23.180511', 347, '00347', 1),
('2021-12-07 19:58:23.239944', '2021-12-07 19:58:23.239944', 348, '00348', 1),
('2021-12-07 19:58:23.261099', '2021-12-07 19:58:23.261099', 349, '00349', 1),
('2021-12-07 19:58:23.306164', '2021-12-07 19:58:23.306164', 350, '00350', 1),
('2021-12-07 19:58:23.350011', '2021-12-07 19:58:23.351012', 351, '00351', 1),
('2021-12-07 19:58:23.395211', '2021-12-07 19:58:23.395211', 352, '00352', 1),
('2021-12-07 19:58:23.439584', '2021-12-07 19:58:23.439584', 353, '00353', 1),
('2021-12-07 19:58:23.517756', '2021-12-07 19:58:23.517756', 354, '00354', 1),
('2021-12-07 19:58:23.538945', '2021-12-07 19:58:23.538945', 355, '00355', 1),
('2021-12-07 19:58:23.561933', '2021-12-07 19:58:23.561933', 356, '00356', 1),
('2021-12-07 19:58:23.584160', '2021-12-07 19:58:23.585161', 357, '00357', 1),
('2021-12-07 19:58:23.628409', '2021-12-07 19:58:23.628409', 358, '00358', 1),
('2021-12-07 19:58:23.694496', '2021-12-07 19:58:23.694496', 359, '00359', 1),
('2021-12-07 19:58:23.737178', '2021-12-07 19:58:23.738180', 360, '00360', 1),
('2021-12-07 19:58:23.784688', '2021-12-07 19:58:23.784688', 361, '00361', 1),
('2021-12-07 19:58:23.852791', '2021-12-07 19:58:23.852791', 362, '00362', 1),
('2021-12-07 19:58:23.893219', '2021-12-07 19:58:23.893219', 363, '00363', 1),
('2021-12-07 19:58:23.940060', '2021-12-07 19:58:23.940060', 364, '00364', 1),
('2021-12-07 19:58:23.994626', '2021-12-07 19:58:23.994626', 365, '00365', 1),
('2021-12-07 19:58:24.051406', '2021-12-07 19:58:24.051406', 366, '00366', 1),
('2021-12-07 19:58:24.184306', '2021-12-07 19:58:24.184306', 367, '00367', 1),
('2021-12-07 19:58:24.256281', '2021-12-07 19:58:24.257281', 368, '00368', 1),
('2021-12-07 19:58:24.317483', '2021-12-07 19:58:24.317483', 369, '00369', 1),
('2021-12-07 19:58:24.364347', '2021-12-07 19:58:24.364347', 370, '00370', 1),
('2021-12-07 19:58:24.416923', '2021-12-07 19:58:24.416923', 371, '00371', 1),
('2021-12-07 19:58:24.461346', '2021-12-07 19:58:24.461346', 372, '00372', 1),
('2021-12-07 19:58:24.516932', '2021-12-07 19:58:24.516932', 373, '00373', 1),
('2021-12-07 19:58:24.550378', '2021-12-07 19:58:24.550378', 374, '00374', 1),
('2021-12-07 19:58:24.583777', '2021-12-07 19:58:24.583777', 375, '00375', 1),
('2021-12-07 19:58:24.625920', '2021-12-07 19:58:24.625920', 376, '00376', 1),
('2021-12-07 19:58:24.662999', '2021-12-07 19:58:24.663999', 377, '00377', 1),
('2021-12-07 19:58:24.707168', '2021-12-07 19:58:24.707168', 378, '00378', 1),
('2021-12-07 19:58:24.740239', '2021-12-07 19:58:24.740239', 379, '00379', 1),
('2021-12-07 19:58:24.772729', '2021-12-07 19:58:24.772729', 380, '00380', 1),
('2021-12-07 19:58:24.795446', '2021-12-07 19:58:24.795446', 381, '00381', 1),
('2021-12-07 19:58:24.838906', '2021-12-07 19:58:24.838906', 382, '00382', 1),
('2021-12-07 19:58:24.883970', '2021-12-07 19:58:24.883970', 383, '00383', 1),
('2021-12-07 19:58:24.930067', '2021-12-07 19:58:24.930067', 384, '00384', 1),
('2021-12-07 19:58:24.963538', '2021-12-07 19:58:24.963538', 385, '00385', 1),
('2021-12-07 19:58:24.995601', '2021-12-07 19:58:24.995601', 386, '00386', 1),
('2021-12-07 19:58:25.017317', '2021-12-07 19:58:25.017317', 387, '00387', 1),
('2021-12-07 19:58:25.038968', '2021-12-07 19:58:25.038968', 388, '00388', 1),
('2021-12-07 19:58:25.063704', '2021-12-07 19:58:25.064699', 389, '00389', 1),
('2021-12-07 19:58:25.151051', '2021-12-07 19:58:25.151051', 390, '00390', 1),
('2021-12-07 19:58:25.259862', '2021-12-07 19:58:25.259862', 391, '00391', 1),
('2021-12-07 19:58:25.350809', '2021-12-07 19:58:25.350809', 392, '00392', 1),
('2021-12-07 19:58:25.406776', '2021-12-07 19:58:25.406776', 393, '00393', 1),
('2021-12-07 19:58:25.427762', '2021-12-07 19:58:25.427762', 394, '00394', 1),
('2021-12-07 19:58:25.451746', '2021-12-07 19:58:25.451746', 395, '00395', 1),
('2021-12-07 19:58:25.484783', '2021-12-07 19:58:25.484783', 396, '00396', 1),
('2021-12-07 19:58:25.506327', '2021-12-07 19:58:25.506327', 397, '00397', 1),
('2021-12-07 19:58:25.527981', '2021-12-07 19:58:25.527981', 398, '00398', 1),
('2021-12-07 19:58:25.552096', '2021-12-07 19:58:25.552096', 399, '00399', 1),
('2021-12-07 19:58:25.572474', '2021-12-07 19:58:25.572474', 400, '00400', 1),
('2021-12-07 19:58:25.595270', '2021-12-07 19:58:25.595270', 401, '00401', 1),
('2021-12-07 19:58:25.619166', '2021-12-07 19:58:25.619166', 402, '00402', 1),
('2021-12-07 19:58:25.651343', '2021-12-07 19:58:25.651343', 403, '00403', 1),
('2021-12-07 19:58:25.672739', '2021-12-07 19:58:25.672739', 404, '00404', 1),
('2021-12-07 19:58:25.696342', '2021-12-07 19:58:25.696342', 405, '00405', 1),
('2021-12-07 19:58:25.720057', '2021-12-07 19:58:25.720057', 406, '00406', 1),
('2021-12-07 19:58:25.773147', '2021-12-07 19:58:25.773147', 407, '00407', 1),
('2021-12-07 19:58:25.795156', '2021-12-07 19:58:25.795156', 408, '00408', 1),
('2021-12-07 19:58:25.819168', '2021-12-07 19:58:25.819168', 409, '00409', 1),
('2021-12-07 19:58:25.861630', '2021-12-07 19:58:25.861630', 410, '00410', 1),
('2021-12-07 19:58:25.906852', '2021-12-07 19:58:25.907859', 411, '00411', 1),
('2021-12-07 19:58:25.940095', '2021-12-07 19:58:25.940095', 412, '00412', 1),
('2021-12-07 19:58:25.984873', '2021-12-07 19:58:25.984873', 413, '00413', 1),
('2021-12-07 19:58:26.006905', '2021-12-07 19:58:26.006905', 414, '00414', 1),
('2021-12-07 19:58:26.028712', '2021-12-07 19:58:26.029723', 415, '00415', 1),
('2021-12-07 19:58:26.074153', '2021-12-07 19:58:26.074153', 416, '00416', 1),
('2021-12-07 19:58:26.095437', '2021-12-07 19:58:26.096450', 417, '00417', 1),
('2021-12-07 19:58:26.117047', '2021-12-07 19:58:26.118059', 418, '00418', 1),
('2021-12-07 19:58:26.160241', '2021-12-07 19:58:26.160241', 419, '00419', 1),
('2021-12-07 19:58:26.183718', '2021-12-07 19:58:26.184729', 420, '00420', 1),
('2021-12-07 19:58:26.207895', '2021-12-07 19:58:26.207895', 421, '00421', 1),
('2021-12-07 19:58:26.240084', '2021-12-07 19:58:26.241075', 422, '00422', 1),
('2021-12-07 19:58:26.840177', '2021-12-07 19:58:26.840177', 423, '00423', 1),
('2021-12-07 19:58:26.889952', '2021-12-07 19:58:26.889952', 424, '00424', 1),
('2021-12-07 19:58:26.940214', '2021-12-07 19:58:26.940214', 425, '00425', 1),
('2021-12-07 19:58:26.962737', '2021-12-07 19:58:26.963748', 426, '00426', 1),
('2021-12-07 19:58:26.997805', '2021-12-07 19:58:26.997805', 427, '00427', 1),
('2021-12-07 19:58:27.030963', '2021-12-07 19:58:27.030963', 428, '00428', 1),
('2021-12-07 19:58:27.063159', '2021-12-07 19:58:27.063159', 429, '00429', 1),
('2021-12-07 19:58:27.096121', '2021-12-07 19:58:27.097125', 430, '00430', 1),
('2021-12-07 19:58:27.129817', '2021-12-07 19:58:27.129817', 431, '00431', 1),
('2021-12-07 19:58:27.162873', '2021-12-07 19:58:27.163872', 432, '00432', 1),
('2021-12-07 19:58:27.195918', '2021-12-07 19:58:27.195918', 433, '00433', 1),
('2021-12-07 19:58:27.219004', '2021-12-07 19:58:27.219004', 434, '00434', 1),
('2021-12-07 19:58:27.240123', '2021-12-07 19:58:27.240123', 435, '00435', 1),
('2021-12-07 19:58:27.285206', '2021-12-07 19:58:27.285206', 436, '00436', 1),
('2021-12-07 19:58:27.472915', '2021-12-07 19:58:27.472915', 437, '00437', 1),
('2021-12-07 19:58:27.495758', '2021-12-07 19:58:27.495758', 438, '00438', 1),
('2021-12-07 19:58:27.539588', '2021-12-07 19:58:27.539588', 439, '00439', 1),
('2021-12-07 19:58:27.584925', '2021-12-07 19:58:27.584925', 440, '00440', 1),
('2021-12-07 19:58:27.659561', '2021-12-07 19:58:27.659561', 441, '00441', 1),
('2021-12-07 19:58:27.763499', '2021-12-07 19:58:27.763499', 442, '00442', 1),
('2021-12-07 19:58:27.873444', '2021-12-07 19:58:27.873444', 443, '00443', 1),
('2021-12-07 19:58:27.950244', '2021-12-07 19:58:27.950244', 444, '00444', 1),
('2021-12-07 19:58:27.995265', '2021-12-07 19:58:27.995265', 445, '00445', 1),
('2021-12-07 19:58:28.050324', '2021-12-07 19:58:28.050324', 446, '00446', 1),
('2021-12-07 19:58:28.073422', '2021-12-07 19:58:28.073422', 447, '00447', 1),
('2021-12-07 19:58:28.094697', '2021-12-07 19:58:28.094697', 448, '00448', 1),
('2021-12-07 19:58:28.117549', '2021-12-07 19:58:28.117549', 449, '00449', 1),
('2021-12-07 19:58:28.173110', '2021-12-07 19:58:28.174110', 450, '00450', 1),
('2021-12-07 19:58:28.195322', '2021-12-07 19:58:28.195322', 451, '00451', 1),
('2021-12-07 19:58:28.250301', '2021-12-07 19:58:28.250301', 452, '00452', 1),
('2021-12-07 19:58:28.284176', '2021-12-07 19:58:28.284176', 453, '00453', 1),
('2021-12-07 19:58:28.340247', '2021-12-07 19:58:28.340247', 454, '00454', 1),
('2021-12-07 19:58:28.407400', '2021-12-07 19:58:28.407400', 455, '00455', 1),
('2021-12-07 19:58:28.483885', '2021-12-07 19:58:28.483885', 456, '00456', 1),
('2021-12-07 19:58:28.539838', '2021-12-07 19:58:28.539838', 457, '00457', 1),
('2021-12-07 19:58:28.583904', '2021-12-07 19:58:28.583904', 458, '00458', 1),
('2021-12-07 19:58:28.628053', '2021-12-07 19:58:28.628053', 459, '00459', 1),
('2021-12-07 19:58:28.683719', '2021-12-07 19:58:28.683719', 460, '00460', 1),
('2021-12-07 19:58:28.707316', '2021-12-07 19:58:28.707316', 461, '00461', 1),
('2021-12-07 19:58:28.751968', '2021-12-07 19:58:28.751968', 462, '00462', 1),
('2021-12-07 19:58:28.952683', '2021-12-07 19:58:28.952683', 463, '00463', 1),
('2021-12-07 19:58:29.051621', '2021-12-07 19:58:29.051621', 464, '00464', 1),
('2021-12-07 19:58:29.095640', '2021-12-07 19:58:29.095640', 465, '00465', 1),
('2021-12-07 19:58:29.151892', '2021-12-07 19:58:29.151892', 466, '00466', 1),
('2021-12-07 19:58:29.206116', '2021-12-07 19:58:29.206116', 467, '00467', 1),
('2021-12-07 19:58:29.229283', '2021-12-07 19:58:29.229283', 468, '00468', 1),
('2021-12-07 19:58:29.250721', '2021-12-07 19:58:29.250721', 469, '00469', 1),
('2021-12-07 19:58:29.273362', '2021-12-07 19:58:29.273362', 470, '00470', 1),
('2021-12-07 19:58:29.339997', '2021-12-07 19:58:29.339997', 471, '00471', 1),
('2021-12-07 19:58:29.385082', '2021-12-07 19:58:29.385082', 472, '00472', 1),
('2021-12-07 19:58:29.428972', '2021-12-07 19:58:29.428972', 473, '00473', 1),
('2021-12-07 19:58:29.484828', '2021-12-07 19:58:29.484828', 474, '00474', 1),
('2021-12-07 19:58:29.506796', '2021-12-07 19:58:29.506796', 475, '00475', 1),
('2021-12-07 19:58:29.528407', '2021-12-07 19:58:29.528407', 476, '00476', 1),
('2021-12-07 19:58:29.551907', '2021-12-07 19:58:29.552908', 477, '00477', 1),
('2021-12-07 19:58:29.572854', '2021-12-07 19:58:29.572854', 478, '00478', 1),
('2021-12-07 19:58:29.596716', '2021-12-07 19:58:29.596716', 479, '00479', 1),
('2021-12-07 19:58:29.619122', '2021-12-07 19:58:29.619122', 480, '00480', 1),
('2021-12-07 19:58:29.653207', '2021-12-07 19:58:29.653207', 481, '00481', 1),
('2021-12-07 19:58:29.685358', '2021-12-07 19:58:29.685358', 482, '00482', 1),
('2021-12-07 19:58:29.707392', '2021-12-07 19:58:29.707392', 483, '00483', 1),
('2021-12-07 19:58:29.728465', '2021-12-07 19:58:29.729477', 484, '00484', 1),
('2021-12-07 19:58:29.752606', '2021-12-07 19:58:29.752606', 485, '00485', 1),
('2021-12-07 19:58:29.796767', '2021-12-07 19:58:29.796767', 486, '00486', 1),
('2021-12-07 19:58:30.030995', '2021-12-07 19:58:30.032008', 487, '00487', 1),
('2021-12-07 19:58:30.185962', '2021-12-07 19:58:30.185962', 488, '00488', 1),
('2021-12-07 19:58:30.295894', '2021-12-07 19:58:30.295894', 489, '00489', 1),
('2021-12-07 19:58:30.395836', '2021-12-07 19:58:30.395836', 490, '00490', 1),
('2021-12-07 19:58:30.450868', '2021-12-07 19:58:30.450868', 491, '00491', 1),
('2021-12-07 19:58:30.474082', '2021-12-07 19:58:30.474082', 492, '00492', 1),
('2021-12-07 19:58:30.529153', '2021-12-07 19:58:30.529153', 493, '00493', 1),
('2021-12-07 19:58:30.574354', '2021-12-07 19:58:30.574354', 494, '00494', 1),
('2021-12-07 19:58:30.606348', '2021-12-07 19:58:30.606348', 495, '00495', 1),
('2021-12-07 19:58:30.629403', '2021-12-07 19:58:30.629403', 496, '00496', 1),
('2021-12-07 19:58:30.650798', '2021-12-07 19:58:30.650798', 497, '00497', 1),
('2021-12-07 19:58:30.673724', '2021-12-07 19:58:30.673724', 498, '00498', 1),
('2021-12-07 19:58:30.717795', '2021-12-07 19:58:30.717795', 499, '00499', 1),
('2021-12-07 19:58:30.763371', '2021-12-07 19:58:30.763371', 500, '00500', 1),
('2021-12-07 19:58:30.817607', '2021-12-07 19:58:30.817607', 501, '00501', 1),
('2021-12-07 19:58:30.863964', '2021-12-07 19:58:30.863964', 502, '00502', 1),
('2021-12-07 19:58:30.940456', '2021-12-07 19:58:30.941295', 503, '00503', 1),
('2021-12-07 19:58:30.963360', '2021-12-07 19:58:30.963360', 504, '00504', 1),
('2021-12-07 19:58:30.997200', '2021-12-07 19:58:30.997200', 505, '00505', 1),
('2021-12-07 19:58:31.031242', '2021-12-07 19:58:31.031242', 506, '00506', 1),
('2021-12-07 19:58:31.096226', '2021-12-07 19:58:31.096226', 507, '00507', 1),
('2021-12-07 19:58:31.172659', '2021-12-07 19:58:31.173671', 508, '00508', 1),
('2021-12-07 19:58:31.244227', '2021-12-07 19:58:31.244227', 509, '00509', 1),
('2021-12-07 19:58:31.346036', '2021-12-07 19:58:31.346036', 510, '00510', 1),
('2021-12-07 19:58:31.385012', '2021-12-07 19:58:31.385012', 511, '00511', 1),
('2021-12-07 19:58:31.427988', '2021-12-07 19:58:31.427988', 512, '00512', 1),
('2021-12-07 19:58:31.451977', '2021-12-07 19:58:31.451977', 513, '00513', 1),
('2021-12-07 19:58:31.472959', '2021-12-07 19:58:31.472959', 514, '00514', 1),
('2021-12-07 19:58:31.495943', '2021-12-07 19:58:31.495943', 515, '00515', 1),
('2021-12-07 19:58:31.517930', '2021-12-07 19:58:31.517930', 516, '00516', 1),
('2021-12-07 19:58:31.539973', '2021-12-07 19:58:31.539973', 517, '00517', 1),
('2021-12-07 19:58:31.595004', '2021-12-07 19:58:31.595004', 518, '00518', 1),
('2021-12-07 19:58:31.640027', '2021-12-07 19:58:31.640027', 519, '00519', 1),
('2021-12-07 19:58:31.684310', '2021-12-07 19:58:31.684310', 520, '00520', 1),
('2021-12-07 19:58:31.729316', '2021-12-07 19:58:31.729316', 521, '00521', 1),
('2021-12-07 19:58:31.773216', '2021-12-07 19:58:31.773216', 522, '00522', 1),
('2021-12-07 19:58:31.818092', '2021-12-07 19:58:31.818092', 523, '00523', 1),
('2021-12-07 19:58:31.840140', '2021-12-07 19:58:31.840140', 524, '00524', 1),
('2021-12-07 19:58:31.884759', '2021-12-07 19:58:31.884759', 525, '00525', 1),
('2021-12-07 19:58:31.906966', '2021-12-07 19:58:31.906966', 526, '00526', 1),
('2021-12-07 19:58:31.973336', '2021-12-07 19:58:31.973336', 527, '00527', 1),
('2021-12-07 19:58:32.016372', '2021-12-07 19:58:32.016372', 528, '00528', 1),
('2021-12-07 19:58:32.040065', '2021-12-07 19:58:32.041054', 529, '00529', 1),
('2021-12-07 19:58:32.062850', '2021-12-07 19:58:32.062850', 530, '00530', 1),
('2021-12-07 19:58:32.083891', '2021-12-07 19:58:32.083891', 531, '00531', 1),
('2021-12-07 19:58:32.140631', '2021-12-07 19:58:32.140631', 532, '00532', 1),
('2021-12-07 19:58:32.161764', '2021-12-07 19:58:32.161764', 533, '00533', 1),
('2021-12-07 19:58:32.184596', '2021-12-07 19:58:32.184596', 534, '00534', 1),
('2021-12-07 19:58:32.207997', '2021-12-07 19:58:32.207997', 535, '00535', 1),
('2021-12-07 19:58:32.231010', '2021-12-07 19:58:32.231010', 536, '00536', 1),
('2021-12-07 19:58:32.750421', '2021-12-07 19:58:32.750421', 537, '00537', 1),
('2021-12-07 19:58:32.796485', '2021-12-07 19:58:32.796485', 538, '00538', 1),
('2021-12-07 19:58:32.840232', '2021-12-07 19:58:32.840232', 539, '00539', 1),
('2021-12-07 19:58:32.884517', '2021-12-07 19:58:32.884517', 540, '00540', 1),
('2021-12-07 19:58:32.939504', '2021-12-07 19:58:32.939504', 541, '00541', 1),
('2021-12-07 19:58:33.006131', '2021-12-07 19:58:33.006131', 542, '00542', 1),
('2021-12-07 19:58:33.029733', '2021-12-07 19:58:33.029733', 543, '00543', 1),
('2021-12-07 19:58:33.118034', '2021-12-07 19:58:33.118034', 544, '00544', 1),
('2021-12-07 19:58:33.160921', '2021-12-07 19:58:33.160921', 545, '00545', 1),
('2021-12-07 19:58:33.206232', '2021-12-07 19:58:33.206232', 546, '00546', 1),
('2021-12-07 19:58:33.229040', '2021-12-07 19:58:33.229040', 547, '00547', 1),
('2021-12-07 19:58:33.284675', '2021-12-07 19:58:33.284675', 548, '00548', 1),
('2021-12-07 19:58:33.340906', '2021-12-07 19:58:33.340906', 549, '00549', 1),
('2021-12-07 19:58:33.363411', '2021-12-07 19:58:33.363411', 550, '00550', 1),
('2021-12-07 19:58:33.406820', '2021-12-07 19:58:33.406820', 551, '00551', 1),
('2021-12-07 19:58:33.451364', '2021-12-07 19:58:33.451364', 552, '00552', 1),
('2021-12-07 19:58:33.506839', '2021-12-07 19:58:33.506839', 553, '00553', 1),
('2021-12-07 19:58:33.572926', '2021-12-07 19:58:33.572926', 554, '00554', 1),
('2021-12-07 19:58:33.640191', '2021-12-07 19:58:33.640191', 555, '00555', 1),
('2021-12-07 19:58:33.707000', '2021-12-07 19:58:33.707000', 556, '00556', 1),
('2021-12-07 19:58:33.795421', '2021-12-07 19:58:33.795421', 557, '00557', 1),
('2021-12-07 19:58:33.874375', '2021-12-07 19:58:33.874375', 558, '00558', 1),
('2021-12-07 19:58:33.917348', '2021-12-07 19:58:33.917348', 559, '00559', 1),
('2021-12-07 19:58:33.974343', '2021-12-07 19:58:33.974343', 560, '00560', 1),
('2021-12-07 19:58:34.028604', '2021-12-07 19:58:34.028604', 561, '00561', 1),
('2021-12-07 19:58:34.073840', '2021-12-07 19:58:34.074839', 562, '00562', 1),
('2021-12-07 19:58:34.128614', '2021-12-07 19:58:34.128614', 563, '00563', 1),
('2021-12-07 19:58:34.184742', '2021-12-07 19:58:34.184742', 564, '00564', 1),
('2021-12-07 19:58:34.207178', '2021-12-07 19:58:34.207178', 565, '00565', 1),
('2021-12-07 19:58:34.229527', '2021-12-07 19:58:34.229527', 566, '00566', 1),
('2021-12-07 19:58:34.274448', '2021-12-07 19:58:34.274448', 567, '00567', 1),
('2021-12-07 19:58:34.318135', '2021-12-07 19:58:34.318135', 568, '00568', 1),
('2021-12-07 19:58:34.340136', '2021-12-07 19:58:34.340136', 569, '00569', 1),
('2021-12-07 19:58:34.362586', '2021-12-07 19:58:34.362586', 570, '00570', 1),
('2021-12-07 19:58:34.384082', '2021-12-07 19:58:34.384082', 571, '00571', 1),
('2021-12-07 19:58:34.407630', '2021-12-07 19:58:34.407630', 572, '00572', 1),
('2021-12-07 19:58:34.451631', '2021-12-07 19:58:34.451631', 573, '00573', 1),
('2021-12-07 19:58:34.474691', '2021-12-07 19:58:34.474691', 574, '00574', 1),
('2021-12-07 19:58:34.507785', '2021-12-07 19:58:34.507785', 575, '00575', 1),
('2021-12-07 19:58:34.540891', '2021-12-07 19:58:34.540891', 576, '00576', 1),
('2021-12-07 19:58:34.572915', '2021-12-07 19:58:34.572915', 577, '00577', 1),
('2021-12-07 19:58:34.617941', '2021-12-07 19:58:34.617941', 578, '00578', 1),
('2021-12-07 19:58:34.639589', '2021-12-07 19:58:34.639589', 579, '00579', 1),
('2021-12-07 19:58:34.697044', '2021-12-07 19:58:34.697044', 580, '00580', 1),
('2021-12-07 19:58:34.739808', '2021-12-07 19:58:34.739808', 581, '00581', 1),
('2021-12-07 19:58:34.830138', '2021-12-07 19:58:34.830138', 582, '00582', 1),
('2021-12-07 19:58:34.918358', '2021-12-07 19:58:34.918358', 583, '00583', 1),
('2021-12-07 19:58:34.951379', '2021-12-07 19:58:34.952379', 584, '00584', 1),
('2021-12-07 19:58:34.972986', '2021-12-07 19:58:34.973989', 585, '00585', 1),
('2021-12-07 19:58:34.995973', '2021-12-07 19:58:34.996972', 586, '00586', 1),
('2021-12-07 19:58:35.040944', '2021-12-07 19:58:35.040944', 587, '00587', 1),
('2021-12-07 19:58:35.061930', '2021-12-07 19:58:35.061930', 588, '00588', 1),
('2021-12-07 19:58:35.118895', '2021-12-07 19:58:35.118895', 589, '00589', 1),
('2021-12-07 19:58:35.139882', '2021-12-07 19:58:35.139882', 590, '00590', 1),
('2021-12-07 19:58:35.162868', '2021-12-07 19:58:35.162868', 591, '00591', 1),
('2021-12-07 19:58:35.206385', '2021-12-07 19:58:35.206385', 592, '00592', 1),
('2021-12-07 19:58:35.251996', '2021-12-07 19:58:35.251996', 593, '00593', 1),
('2021-12-07 19:58:35.273022', '2021-12-07 19:58:35.273022', 594, '00594', 1),
('2021-12-07 19:58:35.318471', '2021-12-07 19:58:35.319465', 595, '00595', 1),
('2021-12-07 19:58:35.339730', '2021-12-07 19:58:35.339730', 596, '00596', 1),
('2021-12-07 19:58:35.362614', '2021-12-07 19:58:35.362614', 597, '00597', 1),
('2021-12-07 19:58:35.386656', '2021-12-07 19:58:35.386656', 598, '00598', 1),
('2021-12-07 19:58:35.407282', '2021-12-07 19:58:35.407282', 599, '00599', 1),
('2021-12-07 19:58:35.428671', '2021-12-07 19:58:35.428671', 600, '00600', 1),
('2021-12-07 19:58:35.452656', '2021-12-07 19:58:35.452656', 601, '00601', 1),
('2021-12-07 19:58:35.473842', '2021-12-07 19:58:35.473842', 602, '00602', 1),
('2021-12-07 19:58:35.495958', '2021-12-07 19:58:35.495958', 603, '00603', 1),
('2021-12-07 19:58:35.518221', '2021-12-07 19:58:35.518221', 604, '00604', 1),
('2021-12-07 19:58:35.540623', '2021-12-07 19:58:35.540623', 605, '00605', 1),
('2021-12-07 19:58:35.562057', '2021-12-07 19:58:35.562057', 606, '00606', 1),
('2021-12-07 19:58:35.585629', '2021-12-07 19:58:35.585629', 607, '00607', 1),
('2021-12-07 19:58:35.606808', '2021-12-07 19:58:35.606808', 608, '00608', 1),
('2021-12-07 19:58:35.629348', '2021-12-07 19:58:35.629348', 609, '00609', 1),
('2021-12-07 19:58:35.650999', '2021-12-07 19:58:35.650999', 610, '00610', 1),
('2021-12-07 19:58:35.674182', '2021-12-07 19:58:35.674182', 611, '00611', 1),
('2021-12-07 19:58:35.745194', '2021-12-07 19:58:35.746199', 612, '00612', 1),
('2021-12-07 19:58:35.797267', '2021-12-07 19:58:35.797267', 613, '00613', 1),
('2021-12-07 19:58:36.218426', '2021-12-07 19:58:36.218426', 614, '00614', 1),
('2021-12-07 19:58:36.340353', '2021-12-07 19:58:36.340353', 615, '00615', 1),
('2021-12-07 19:58:36.407268', '2021-12-07 19:58:36.407268', 616, '00616', 1),
('2021-12-07 19:58:36.473369', '2021-12-07 19:58:36.473369', 617, '00617', 1),
('2021-12-07 19:58:36.539217', '2021-12-07 19:58:36.539217', 618, '00618', 1),
('2021-12-07 19:58:36.584488', '2021-12-07 19:58:36.584488', 619, '00619', 1),
('2021-12-07 19:58:36.640665', '2021-12-07 19:58:36.640665', 620, '00620', 1),
('2021-12-07 19:58:36.684504', '2021-12-07 19:58:36.684504', 621, '00621', 1),
('2021-12-07 19:58:36.730988', '2021-12-07 19:58:36.730988', 622, '00622', 1),
('2021-12-07 19:58:36.763343', '2021-12-07 19:58:36.763343', 623, '00623', 1),
('2021-12-07 19:58:36.807389', '2021-12-07 19:58:36.807389', 624, '00624', 1),
('2021-12-07 19:58:36.873449', '2021-12-07 19:58:36.873449', 625, '00625', 1),
('2021-12-07 19:58:36.897486', '2021-12-07 19:58:36.897486', 626, '00626', 1),
('2021-12-07 19:58:36.951635', '2021-12-07 19:58:36.951635', 627, '00627', 1),
('2021-12-07 19:58:36.974673', '2021-12-07 19:58:36.974673', 628, '00628', 1),
('2021-12-07 19:58:37.029817', '2021-12-07 19:58:37.029817', 629, '00629', 1),
('2021-12-07 19:58:37.087972', '2021-12-07 19:58:37.087972', 630, '00630', 1),
('2021-12-07 19:58:37.119029', '2021-12-07 19:58:37.119029', 631, '00631', 1),
('2021-12-07 19:58:37.140748', '2021-12-07 19:58:37.141761', 632, '00632', 1),
('2021-12-07 19:58:37.163246', '2021-12-07 19:58:37.163246', 633, '00633', 1),
('2021-12-07 19:58:37.186162', '2021-12-07 19:58:37.186162', 634, '00634', 1),
('2021-12-07 19:58:37.297338', '2021-12-07 19:58:37.297338', 635, '00635', 1),
('2021-12-07 19:58:37.385576', '2021-12-07 19:58:37.385576', 636, '00636', 1),
('2021-12-07 19:58:37.439536', '2021-12-07 19:58:37.440559', 637, '00637', 1),
('2021-12-07 19:58:37.485510', '2021-12-07 19:58:37.485510', 638, '00638', 1),
('2021-12-07 19:58:37.519500', '2021-12-07 19:58:37.519500', 639, '00639', 1),
('2021-12-07 19:58:37.551465', '2021-12-07 19:58:37.551465', 640, '00640', 1),
('2021-12-07 19:58:37.585445', '2021-12-07 19:58:37.585445', 641, '00641', 1),
('2021-12-07 19:58:37.640530', '2021-12-07 19:58:37.641530', 642, '00642', 1),
('2021-12-07 19:58:37.663097', '2021-12-07 19:58:37.663097', 643, '00643', 1),
('2021-12-07 19:58:37.718127', '2021-12-07 19:58:37.718127', 644, '00644', 1),
('2021-12-07 19:58:37.741440', '2021-12-07 19:58:37.741440', 645, '00645', 1),
('2021-12-07 19:58:37.819452', '2021-12-07 19:58:37.819452', 646, '00646', 1),
('2021-12-07 19:58:37.897250', '2021-12-07 19:58:37.897250', 647, '00647', 1),
('2021-12-07 19:58:37.995437', '2021-12-07 19:58:37.995437', 648, '00648', 1),
('2021-12-07 19:58:38.085895', '2021-12-07 19:58:38.085895', 649, '00649', 1);
INSERT INTO `receipts` (`created_at`, `updated_at`, `id`, `receipt`, `status_id`) VALUES
('2021-12-07 19:58:38.142004', '2021-12-07 19:58:38.142004', 650, '00650', 1),
('2021-12-07 19:58:38.219259', '2021-12-07 19:58:38.219259', 651, '00651', 1),
('2021-12-07 19:58:38.351595', '2021-12-07 19:58:38.351595', 652, '00652', 1),
('2021-12-07 19:58:38.513721', '2021-12-07 19:58:38.513721', 653, '00653', 1),
('2021-12-07 19:58:38.607291', '2021-12-07 19:58:38.607291', 654, '00654', 1),
('2021-12-07 19:58:38.685242', '2021-12-07 19:58:38.685242', 655, '00655', 1),
('2021-12-07 19:58:38.773187', '2021-12-07 19:58:38.773187', 656, '00656', 1),
('2021-12-07 19:58:38.818338', '2021-12-07 19:58:38.818338', 657, '00657', 1),
('2021-12-07 19:58:38.851188', '2021-12-07 19:58:38.851188', 658, '00658', 1),
('2021-12-07 19:58:38.885227', '2021-12-07 19:58:38.885227', 659, '00659', 1),
('2021-12-07 19:58:38.918370', '2021-12-07 19:58:38.918370', 660, '00660', 1),
('2021-12-07 19:58:38.952391', '2021-12-07 19:58:38.952391', 661, '00661', 1),
('2021-12-07 19:58:38.973334', '2021-12-07 19:58:38.973334', 662, '00662', 1),
('2021-12-07 19:58:38.996563', '2021-12-07 19:58:38.996563', 663, '00663', 1),
('2021-12-07 19:58:39.017753', '2021-12-07 19:58:39.018753', 664, '00664', 1),
('2021-12-07 19:58:39.040664', '2021-12-07 19:58:39.040664', 665, '00665', 1),
('2021-12-07 19:58:39.062274', '2021-12-07 19:58:39.062274', 666, '00666', 1),
('2021-12-07 19:58:39.085320', '2021-12-07 19:58:39.085320', 667, '00667', 1),
('2021-12-07 19:58:39.107242', '2021-12-07 19:58:39.107242', 668, '00668', 1),
('2021-12-07 19:58:39.129561', '2021-12-07 19:58:39.129561', 669, '00669', 1),
('2021-12-07 19:58:39.152318', '2021-12-07 19:58:39.152318', 670, '00670', 1),
('2021-12-07 19:58:39.174302', '2021-12-07 19:58:39.174302', 671, '00671', 1),
('2021-12-07 19:58:39.196288', '2021-12-07 19:58:39.196288', 672, '00672', 1),
('2021-12-07 19:58:39.219276', '2021-12-07 19:58:39.219276', 673, '00673', 1),
('2021-12-07 19:58:39.240262', '2021-12-07 19:58:39.240262', 674, '00674', 1),
('2021-12-07 19:58:39.263247', '2021-12-07 19:58:39.263247', 675, '00675', 1),
('2021-12-07 19:58:39.286241', '2021-12-07 19:58:39.286241', 676, '00676', 1),
('2021-12-07 19:58:39.329001', '2021-12-07 19:58:39.329001', 677, '00677', 1),
('2021-12-07 19:58:39.462398', '2021-12-07 19:58:39.462398', 678, '00678', 1),
('2021-12-07 19:58:39.741528', '2021-12-07 19:58:39.741528', 679, '00679', 1),
('2021-12-07 19:58:39.878694', '2021-12-07 19:58:39.878694', 680, '00680', 1),
('2021-12-07 19:58:39.951647', '2021-12-07 19:58:39.951647', 681, '00681', 1),
('2021-12-07 19:58:40.193611', '2021-12-07 19:58:40.193611', 682, '00682', 1),
('2021-12-07 19:58:40.261838', '2021-12-07 19:58:40.261838', 683, '00683', 1),
('2021-12-07 19:58:40.352950', '2021-12-07 19:58:40.352950', 684, '00684', 1),
('2021-12-07 19:58:40.429905', '2021-12-07 19:58:40.429905', 685, '00685', 1),
('2021-12-07 19:58:40.474875', '2021-12-07 19:58:40.474875', 686, '00686', 1),
('2021-12-07 19:58:40.573858', '2021-12-07 19:58:40.573858', 687, '00687', 1),
('2021-12-07 19:58:40.598019', '2021-12-07 19:58:40.598019', 688, '00688', 1),
('2021-12-07 19:58:40.640744', '2021-12-07 19:58:40.640744', 689, '00689', 1),
('2021-12-07 19:58:40.664417', '2021-12-07 19:58:40.664417', 690, '00690', 1),
('2021-12-07 19:58:40.718354', '2021-12-07 19:58:40.718354', 691, '00691', 1),
('2021-12-07 19:58:40.741538', '2021-12-07 19:58:40.741538', 692, '00692', 1),
('2021-12-07 19:58:40.785027', '2021-12-07 19:58:40.785027', 693, '00693', 1),
('2021-12-07 19:58:40.807822', '2021-12-07 19:58:40.807822', 694, '00694', 1),
('2021-12-07 19:58:40.952596', '2021-12-07 19:58:40.952596', 695, '00695', 1),
('2021-12-07 19:58:40.973931', '2021-12-07 19:58:40.973931', 696, '00696', 1),
('2021-12-07 19:58:41.020017', '2021-12-07 19:58:41.020017', 697, '00697', 1),
('2021-12-07 19:58:41.085676', '2021-12-07 19:58:41.085676', 698, '00698', 1),
('2021-12-07 19:58:41.220593', '2021-12-07 19:58:41.220593', 699, '00699', 1),
('2021-12-07 19:58:41.287099', '2021-12-07 19:58:41.287099', 700, '00700', 1),
('2021-12-07 19:58:41.353257', '2021-12-07 19:58:41.353257', 701, '00701', 1),
('2021-12-07 19:58:41.406801', '2021-12-07 19:58:41.406801', 702, '00702', 1),
('2021-12-07 19:58:41.474637', '2021-12-07 19:58:41.474637', 703, '00703', 1),
('2021-12-07 19:58:41.518629', '2021-12-07 19:58:41.518629', 704, '00704', 1),
('2021-12-07 19:58:41.640555', '2021-12-07 19:58:41.640555', 705, '00705', 1),
('2021-12-07 19:58:41.663384', '2021-12-07 19:58:41.663384', 706, '00706', 1),
('2021-12-07 19:58:41.707592', '2021-12-07 19:58:41.707592', 707, '00707', 1),
('2021-12-07 19:58:41.763010', '2021-12-07 19:58:41.763010', 708, '00708', 1),
('2021-12-07 19:58:41.808102', '2021-12-07 19:58:41.808102', 709, '00709', 1),
('2021-12-07 19:58:41.829684', '2021-12-07 19:58:41.829684', 710, '00710', 1),
('2021-12-07 19:58:41.851936', '2021-12-07 19:58:41.851936', 711, '00711', 1),
('2021-12-07 19:58:41.897041', '2021-12-07 19:58:41.897041', 712, '00712', 1),
('2021-12-07 19:58:42.042337', '2021-12-07 19:58:42.042337', 713, '00713', 1),
('2021-12-07 19:58:42.237393', '2021-12-07 19:58:42.237393', 714, '00714', 1),
('2021-12-07 19:58:42.307201', '2021-12-07 19:58:42.307201', 715, '00715', 1),
('2021-12-07 19:58:42.330186', '2021-12-07 19:58:42.330186', 716, '00716', 1),
('2021-12-07 19:58:42.374157', '2021-12-07 19:58:42.374157', 717, '00717', 1),
('2021-12-07 19:58:42.419133', '2021-12-07 19:58:42.419133', 718, '00718', 1),
('2021-12-07 19:58:42.463106', '2021-12-07 19:58:42.463106', 719, '00719', 1),
('2021-12-07 19:58:42.540318', '2021-12-07 19:58:42.540318', 720, '00720', 1),
('2021-12-07 19:58:42.585337', '2021-12-07 19:58:42.585337', 721, '00721', 1),
('2021-12-07 19:58:42.752119', '2021-12-07 19:58:42.752119', 722, '00722', 1),
('2021-12-07 19:58:42.775105', '2021-12-07 19:58:42.775105', 723, '00723', 1),
('2021-12-07 19:58:42.796093', '2021-12-07 19:58:42.796093', 724, '00724', 1),
('2021-12-07 19:58:42.819078', '2021-12-07 19:58:42.819078', 725, '00725', 1),
('2021-12-07 19:58:42.840380', '2021-12-07 19:58:42.840380', 726, '00726', 1),
('2021-12-07 19:58:42.886420', '2021-12-07 19:58:42.886420', 727, '00727', 1),
('2021-12-07 19:58:42.952441', '2021-12-07 19:58:42.952441', 728, '00728', 1),
('2021-12-07 19:58:42.996786', '2021-12-07 19:58:42.996786', 729, '00729', 1),
('2021-12-07 19:58:43.040489', '2021-12-07 19:58:43.040489', 730, '00730', 1),
('2021-12-07 19:58:43.063243', '2021-12-07 19:58:43.063243', 731, '00731', 1),
('2021-12-07 19:58:43.085269', '2021-12-07 19:58:43.085269', 732, '00732', 1),
('2021-12-07 19:58:43.107690', '2021-12-07 19:58:43.107690', 733, '00733', 1),
('2021-12-07 19:58:43.129386', '2021-12-07 19:58:43.129386', 734, '00734', 1),
('2021-12-07 19:58:43.153000', '2021-12-07 19:58:43.153000', 735, '00735', 1),
('2021-12-07 19:58:43.173878', '2021-12-07 19:58:43.173878', 736, '00736', 1),
('2021-12-07 19:58:43.220190', '2021-12-07 19:58:43.220190', 737, '00737', 1),
('2021-12-07 19:58:43.254268', '2021-12-07 19:58:43.254268', 738, '00738', 1),
('2021-12-07 19:58:43.373600', '2021-12-07 19:58:43.373600', 739, '00739', 1),
('2021-12-07 19:58:43.429722', '2021-12-07 19:58:43.429722', 740, '00740', 1),
('2021-12-07 19:58:43.451735', '2021-12-07 19:58:43.451735', 741, '00741', 1),
('2021-12-07 19:58:43.474173', '2021-12-07 19:58:43.475184', 742, '00742', 1),
('2021-12-07 19:58:43.585295', '2021-12-07 19:58:43.585295', 743, '00743', 1),
('2021-12-07 19:58:43.696771', '2021-12-07 19:58:43.696771', 744, '00744', 1),
('2021-12-07 19:58:43.885482', '2021-12-07 19:58:43.885482', 745, '00745', 1),
('2021-12-07 19:58:43.940449', '2021-12-07 19:58:43.940449', 746, '00746', 1),
('2021-12-07 19:58:43.996416', '2021-12-07 19:58:43.996416', 747, '00747', 1),
('2021-12-07 19:58:44.062526', '2021-12-07 19:58:44.062526', 748, '00748', 1),
('2021-12-07 19:58:44.108528', '2021-12-07 19:58:44.108528', 749, '00749', 1),
('2021-12-07 19:58:44.162682', '2021-12-07 19:58:44.162682', 750, '00750', 1),
('2021-12-07 19:58:44.218792', '2021-12-07 19:58:44.218792', 751, '00751', 1),
('2021-12-07 19:58:44.273691', '2021-12-07 19:58:44.273691', 752, '00752', 1),
('2021-12-07 19:58:44.296738', '2021-12-07 19:58:44.296738', 753, '00753', 1),
('2021-12-07 19:58:44.407123', '2021-12-07 19:58:44.407123', 754, '00754', 1),
('2021-12-07 19:58:44.429976', '2021-12-07 19:58:44.430977', 755, '00755', 1),
('2021-12-07 19:58:44.474079', '2021-12-07 19:58:44.475086', 756, '00756', 1),
('2021-12-07 19:58:44.497435', '2021-12-07 19:58:44.497435', 757, '00757', 1),
('2021-12-07 19:58:44.518247', '2021-12-07 19:58:44.518247', 758, '00758', 1),
('2021-12-07 19:58:44.541037', '2021-12-07 19:58:44.541037', 759, '00759', 1),
('2021-12-07 19:58:44.563794', '2021-12-07 19:58:44.563794', 760, '00760', 1),
('2021-12-07 19:58:44.629966', '2021-12-07 19:58:44.629966', 761, '00761', 1),
('2021-12-07 19:58:44.686920', '2021-12-07 19:58:44.686920', 762, '00762', 1),
('2021-12-07 19:58:44.729894', '2021-12-07 19:58:44.729894', 763, '00763', 1),
('2021-12-07 19:58:44.751877', '2021-12-07 19:58:44.751877', 764, '00764', 1),
('2021-12-07 19:58:44.851817', '2021-12-07 19:58:44.851817', 765, '00765', 1),
('2021-12-07 19:58:44.896544', '2021-12-07 19:58:44.896544', 766, '00766', 1),
('2021-12-07 19:58:44.951871', '2021-12-07 19:58:44.951871', 767, '00767', 1),
('2021-12-07 19:58:44.974284', '2021-12-07 19:58:44.974284', 768, '00768', 1),
('2021-12-07 19:58:44.995931', '2021-12-07 19:58:44.995931', 769, '00769', 1),
('2021-12-07 19:58:45.040992', '2021-12-07 19:58:45.040992', 770, '00770', 1),
('2021-12-07 19:58:45.095932', '2021-12-07 19:58:45.095932', 771, '00771', 1),
('2021-12-07 19:58:45.141043', '2021-12-07 19:58:45.141043', 772, '00772', 1),
('2021-12-07 19:58:45.162716', '2021-12-07 19:58:45.162716', 773, '00773', 1),
('2021-12-07 19:58:45.186795', '2021-12-07 19:58:45.186795', 774, '00774', 1),
('2021-12-07 19:58:45.207141', '2021-12-07 19:58:45.207141', 775, '00775', 1),
('2021-12-07 19:58:45.229937', '2021-12-07 19:58:45.229937', 776, '00776', 1),
('2021-12-07 19:58:45.273768', '2021-12-07 19:58:45.273768', 777, '00777', 1),
('2021-12-07 19:58:45.296677', '2021-12-07 19:58:45.296677', 778, '00778', 1),
('2021-12-07 19:58:45.318899', '2021-12-07 19:58:45.318899', 779, '00779', 1),
('2021-12-07 19:58:45.341317', '2021-12-07 19:58:45.341317', 780, '00780', 1),
('2021-12-07 19:58:46.208065', '2021-12-07 19:58:46.208065', 781, '00781', 1),
('2021-12-07 19:58:46.274751', '2021-12-07 19:58:46.274751', 782, '00782', 1),
('2021-12-07 19:58:46.330114', '2021-12-07 19:58:46.330114', 783, '00783', 1),
('2021-12-07 19:58:46.418468', '2021-12-07 19:58:46.418468', 784, '00784', 1),
('2021-12-07 19:58:46.464263', '2021-12-07 19:58:46.465254', 785, '00785', 1),
('2021-12-07 19:58:46.485133', '2021-12-07 19:58:46.485133', 786, '00786', 1),
('2021-12-07 19:58:46.531082', '2021-12-07 19:58:46.531082', 787, '00787', 1),
('2021-12-07 19:58:46.551870', '2021-12-07 19:58:46.551870', 788, '00788', 1),
('2021-12-07 19:58:46.598329', '2021-12-07 19:58:46.598329', 789, '00789', 1),
('2021-12-07 19:58:46.632447', '2021-12-07 19:58:46.632447', 790, '00790', 1),
('2021-12-07 19:58:46.697556', '2021-12-07 19:58:46.697556', 791, '00791', 1),
('2021-12-07 19:58:46.731639', '2021-12-07 19:58:46.731639', 792, '00792', 1),
('2021-12-07 19:58:46.786780', '2021-12-07 19:58:46.786780', 793, '00793', 1),
('2021-12-07 19:58:46.997066', '2021-12-07 19:58:46.997066', 794, '00794', 1),
('2021-12-07 19:58:47.140156', '2021-12-07 19:58:47.140156', 795, '00795', 1),
('2021-12-07 19:58:47.329790', '2021-12-07 19:58:47.329790', 796, '00796', 1),
('2021-12-07 19:58:47.386442', '2021-12-07 19:58:47.387441', 797, '00797', 1),
('2021-12-07 19:58:47.408453', '2021-12-07 19:58:47.408453', 798, '00798', 1),
('2021-12-07 19:58:47.463743', '2021-12-07 19:58:47.463743', 799, '00799', 1),
('2021-12-07 19:58:47.518734', '2021-12-07 19:58:47.518734', 800, '00800', 1),
('2021-12-07 19:58:47.541957', '2021-12-07 19:58:47.541957', 801, '00801', 1),
('2021-12-07 19:58:47.585406', '2021-12-07 19:58:47.585406', 802, '00802', 1),
('2021-12-07 19:58:47.630424', '2021-12-07 19:58:47.630424', 803, '00803', 1),
('2021-12-07 19:58:47.652085', '2021-12-07 19:58:47.652085', 804, '00804', 1),
('2021-12-07 19:58:47.675732', '2021-12-07 19:58:47.675732', 805, '00805', 1),
('2021-12-07 19:58:47.742863', '2021-12-07 19:58:47.742863', 806, '00806', 1),
('2021-12-07 19:58:47.796584', '2021-12-07 19:58:47.796584', 807, '00807', 1),
('2021-12-07 19:58:47.819371', '2021-12-07 19:58:47.819371', 808, '00808', 1),
('2021-12-07 19:58:47.875120', '2021-12-07 19:58:47.875120', 809, '00809', 1),
('2021-12-07 19:58:47.897386', '2021-12-07 19:58:47.897386', 810, '00810', 1),
('2021-12-07 19:58:47.952358', '2021-12-07 19:58:47.952358', 811, '00811', 1),
('2021-12-07 19:58:48.152152', '2021-12-07 19:58:48.153156', 812, '00812', 1),
('2021-12-07 19:58:48.185579', '2021-12-07 19:58:48.185579', 813, '00813', 1),
('2021-12-07 19:58:48.208380', '2021-12-07 19:58:48.208380', 814, '00814', 1),
('2021-12-07 19:58:48.375007', '2021-12-07 19:58:48.375007', 815, '00815', 1),
('2021-12-07 19:58:48.430972', '2021-12-07 19:58:48.430972', 816, '00816', 1),
('2021-12-07 19:58:48.474945', '2021-12-07 19:58:48.474945', 817, '00817', 1),
('2021-12-07 19:58:48.509335', '2021-12-07 19:58:48.509335', 818, '00818', 1),
('2021-12-07 19:58:48.531103', '2021-12-07 19:58:48.531103', 819, '00819', 1),
('2021-12-07 19:58:48.552137', '2021-12-07 19:58:48.552137', 820, '00820', 1),
('2021-12-07 19:58:48.597230', '2021-12-07 19:58:48.597230', 821, '00821', 1),
('2021-12-07 19:58:48.619271', '2021-12-07 19:58:48.619271', 822, '00822', 1),
('2021-12-07 19:58:48.641260', '2021-12-07 19:58:48.641260', 823, '00823', 1),
('2021-12-07 19:58:48.663232', '2021-12-07 19:58:48.663232', 824, '00824', 1),
('2021-12-07 19:58:48.707934', '2021-12-07 19:58:48.707934', 825, '00825', 1),
('2021-12-07 19:58:48.753510', '2021-12-07 19:58:48.753510', 826, '00826', 1),
('2021-12-07 19:58:48.796821', '2021-12-07 19:58:48.796821', 827, '00827', 1),
('2021-12-07 19:58:48.818857', '2021-12-07 19:58:48.819854', 828, '00828', 1),
('2021-12-07 19:58:48.863046', '2021-12-07 19:58:48.863046', 829, '00829', 1),
('2021-12-07 19:58:48.927293', '2021-12-07 19:58:48.927293', 830, '00830', 1),
('2021-12-07 19:58:48.962970', '2021-12-07 19:58:48.962970', 831, '00831', 1),
('2021-12-07 19:58:49.007964', '2021-12-07 19:58:49.007964', 832, '00832', 1),
('2021-12-07 19:58:49.029644', '2021-12-07 19:58:49.029644', 833, '00833', 1),
('2021-12-07 19:58:49.174161', '2021-12-07 19:58:49.174161', 834, '00834', 1),
('2021-12-07 19:58:49.229792', '2021-12-07 19:58:49.229792', 835, '00835', 1),
('2021-12-07 19:58:49.274726', '2021-12-07 19:58:49.274726', 836, '00836', 1),
('2021-12-07 19:58:49.382040', '2021-12-07 19:58:49.382040', 837, '00837', 1),
('2021-12-07 19:58:49.419948', '2021-12-07 19:58:49.419948', 838, '00838', 1),
('2021-12-07 19:58:49.463241', '2021-12-07 19:58:49.463241', 839, '00839', 1),
('2021-12-07 19:58:49.508754', '2021-12-07 19:58:49.508754', 840, '00840', 1),
('2021-12-07 19:58:49.529737', '2021-12-07 19:58:49.529737', 841, '00841', 1),
('2021-12-07 19:58:49.585704', '2021-12-07 19:58:49.585704', 842, '00842', 1),
('2021-12-07 19:58:49.608691', '2021-12-07 19:58:49.608691', 843, '00843', 1),
('2021-12-07 19:58:49.630676', '2021-12-07 19:58:49.630676', 844, '00844', 1),
('2021-12-07 19:58:49.652663', '2021-12-07 19:58:49.652663', 845, '00845', 1),
('2021-12-07 19:58:49.675649', '2021-12-07 19:58:49.675649', 846, '00846', 1),
('2021-12-07 19:58:49.696634', '2021-12-07 19:58:49.696634', 847, '00847', 1),
('2021-12-07 19:58:49.752633', '2021-12-07 19:58:49.752633', 848, '00848', 1),
('2021-12-07 19:58:49.797079', '2021-12-07 19:58:49.797079', 849, '00849', 1),
('2021-12-07 19:58:49.818689', '2021-12-07 19:58:49.818689', 850, '00850', 1),
('2021-12-07 19:58:49.842675', '2021-12-07 19:58:49.842675', 851, '00851', 1),
('2021-12-07 19:58:49.863176', '2021-12-07 19:58:49.863176', 852, '00852', 1),
('2021-12-07 19:58:49.885978', '2021-12-07 19:58:49.885978', 853, '00853', 1),
('2021-12-07 19:58:49.908789', '2021-12-07 19:58:49.908789', 854, '00854', 1),
('2021-12-07 19:58:49.930679', '2021-12-07 19:58:49.930679', 855, '00855', 1),
('2021-12-07 19:58:49.951998', '2021-12-07 19:58:49.951998', 856, '00856', 1),
('2021-12-07 19:58:49.976094', '2021-12-07 19:58:49.976094', 857, '00857', 1),
('2021-12-07 19:58:49.997102', '2021-12-07 19:58:49.997102', 858, '00858', 1),
('2021-12-07 19:58:50.019326', '2021-12-07 19:58:50.019326', 859, '00859', 1),
('2021-12-07 19:58:50.041024', '2021-12-07 19:58:50.041024', 860, '00860', 1),
('2021-12-07 19:58:50.064761', '2021-12-07 19:58:50.064761', 861, '00861', 1),
('2021-12-07 19:58:50.086023', '2021-12-07 19:58:50.086023', 862, '00862', 1),
('2021-12-07 19:58:50.181373', '2021-12-07 19:58:50.181373', 863, '00863', 1),
('2021-12-07 19:58:50.320458', '2021-12-07 19:58:50.320458', 864, '00864', 1),
('2021-12-07 19:58:50.458078', '2021-12-07 19:58:50.459089', 865, '00865', 1),
('2021-12-07 19:58:50.607817', '2021-12-07 19:58:50.608829', 866, '00866', 1),
('2021-12-07 19:58:50.675100', '2021-12-07 19:58:50.676111', 867, '00867', 1),
('2021-12-07 19:58:50.720042', '2021-12-07 19:58:50.720042', 868, '00868', 1),
('2021-12-07 19:58:50.764011', '2021-12-07 19:58:50.764011', 869, '00869', 1),
('2021-12-07 19:58:50.785997', '2021-12-07 19:58:50.785997', 870, '00870', 1),
('2021-12-07 19:58:50.874941', '2021-12-07 19:58:50.874941', 871, '00871', 1),
('2021-12-07 19:58:50.897928', '2021-12-07 19:58:50.897928', 872, '00872', 1),
('2021-12-07 19:58:50.919917', '2021-12-07 19:58:50.919917', 873, '00873', 1),
('2021-12-07 19:58:50.941956', '2021-12-07 19:58:50.941956', 874, '00874', 1),
('2021-12-07 19:58:50.963492', '2021-12-07 19:58:50.963492', 875, '00875', 1),
('2021-12-07 19:58:50.986424', '2021-12-07 19:58:50.986424', 876, '00876', 1),
('2021-12-07 19:58:51.008187', '2021-12-07 19:58:51.008187', 877, '00877', 1),
('2021-12-07 19:58:51.030731', '2021-12-07 19:58:51.030731', 878, '00878', 1),
('2021-12-07 19:58:51.053771', '2021-12-07 19:58:51.053771', 879, '00879', 1),
('2021-12-07 19:58:51.075037', '2021-12-07 19:58:51.075037', 880, '00880', 1),
('2021-12-07 19:58:51.096734', '2021-12-07 19:58:51.096734', 881, '00881', 1),
('2021-12-07 19:58:51.120568', '2021-12-07 19:58:51.120568', 882, '00882', 1),
('2021-12-07 19:58:51.141285', '2021-12-07 19:58:51.141285', 883, '00883', 1),
('2021-12-07 19:58:51.164125', '2021-12-07 19:58:51.164125', 884, '00884', 1),
('2021-12-07 19:58:51.221054', '2021-12-07 19:58:51.222046', 885, '00885', 1),
('2021-12-07 19:58:51.264390', '2021-12-07 19:58:51.264390', 886, '00886', 1),
('2021-12-07 19:58:51.308041', '2021-12-07 19:58:51.308041', 887, '00887', 1),
('2021-12-07 19:58:51.412701', '2021-12-07 19:58:51.412701', 888, '00888', 1),
('2021-12-07 19:58:51.475162', '2021-12-07 19:58:51.475162', 889, '00889', 1),
('2021-12-07 19:58:51.519447', '2021-12-07 19:58:51.520450', 890, '00890', 1),
('2021-12-07 19:58:51.617436', '2021-12-07 19:58:51.617436', 891, '00891', 1),
('2021-12-07 19:58:51.719277', '2021-12-07 19:58:51.719277', 892, '00892', 1),
('2021-12-07 19:58:51.763099', '2021-12-07 19:58:51.763099', 893, '00893', 1),
('2021-12-07 19:58:51.809348', '2021-12-07 19:58:51.809348', 894, '00894', 1),
('2021-12-07 19:58:51.852628', '2021-12-07 19:58:51.852628', 895, '00895', 1),
('2021-12-07 19:58:51.897047', '2021-12-07 19:58:51.898040', 896, '00896', 1),
('2021-12-07 19:58:51.964380', '2021-12-07 19:58:51.964380', 897, '00897', 1),
('2021-12-07 19:58:51.985365', '2021-12-07 19:58:51.985365', 898, '00898', 1),
('2021-12-07 19:58:52.008352', '2021-12-07 19:58:52.008352', 899, '00899', 1),
('2021-12-07 19:58:52.030338', '2021-12-07 19:58:52.030338', 900, '00900', 1),
('2021-12-07 19:58:52.086304', '2021-12-07 19:58:52.086304', 901, '00901', 1),
('2021-12-07 19:58:52.140442', '2021-12-07 19:58:52.140442', 902, '00902', 1),
('2021-12-07 19:58:52.231892', '2021-12-07 19:58:52.231892', 903, '00903', 1),
('2021-12-07 19:58:52.315388', '2021-12-07 19:58:52.315388', 904, '00904', 1),
('2021-12-07 19:58:52.385917', '2021-12-07 19:58:52.385917', 905, '00905', 1),
('2021-12-07 19:58:52.883133', '2021-12-07 19:58:52.883133', 906, '00906', 1),
('2021-12-07 19:58:53.119540', '2021-12-07 19:58:53.119540', 907, '00907', 1),
('2021-12-07 19:58:53.385836', '2021-12-07 19:58:53.385836', 908, '00908', 1),
('2021-12-07 19:58:53.443592', '2021-12-07 19:58:53.443592', 909, '00909', 1),
('2021-12-07 19:58:53.498714', '2021-12-07 19:58:53.498714', 910, '00910', 1),
('2021-12-07 19:58:53.553209', '2021-12-07 19:58:53.554211', 911, '00911', 1),
('2021-12-07 19:58:53.663630', '2021-12-07 19:58:53.663630', 912, '00912', 1),
('2021-12-07 19:58:53.709546', '2021-12-07 19:58:53.709546', 913, '00913', 1),
('2021-12-07 19:58:53.752582', '2021-12-07 19:58:53.752582', 914, '00914', 1),
('2021-12-07 19:58:53.797379', '2021-12-07 19:58:53.797379', 915, '00915', 1),
('2021-12-07 19:58:53.818988', '2021-12-07 19:58:53.818988', 916, '00916', 1),
('2021-12-07 19:58:53.863876', '2021-12-07 19:58:53.863876', 917, '00917', 1),
('2021-12-07 19:58:53.885883', '2021-12-07 19:58:53.885883', 918, '00918', 1),
('2021-12-07 19:58:53.952572', '2021-12-07 19:58:53.952572', 919, '00919', 1),
('2021-12-07 19:58:53.975005', '2021-12-07 19:58:53.975005', 920, '00920', 1),
('2021-12-07 19:58:53.997188', '2021-12-07 19:58:53.997188', 921, '00921', 1),
('2021-12-07 19:58:54.019452', '2021-12-07 19:58:54.019452', 922, '00922', 1),
('2021-12-07 19:58:54.041093', '2021-12-07 19:58:54.041093', 923, '00923', 1),
('2021-12-07 19:58:54.064315', '2021-12-07 19:58:54.064315', 924, '00924', 1),
('2021-12-07 19:58:54.085705', '2021-12-07 19:58:54.085705', 925, '00925', 1),
('2021-12-07 19:58:54.108582', '2021-12-07 19:58:54.108582', 926, '00926', 1),
('2021-12-07 19:58:54.152989', '2021-12-07 19:58:54.152989', 927, '00927', 1),
('2021-12-07 19:58:54.174438', '2021-12-07 19:58:54.174438', 928, '00928', 1),
('2021-12-07 19:58:54.330850', '2021-12-07 19:58:54.331849', 929, '00929', 1),
('2021-12-07 19:58:54.421814', '2021-12-07 19:58:54.421814', 930, '00930', 1),
('2021-12-07 19:58:54.464789', '2021-12-07 19:58:54.464789', 931, '00931', 1),
('2021-12-07 19:58:54.485773', '2021-12-07 19:58:54.485773', 932, '00932', 1),
('2021-12-07 19:58:54.508760', '2021-12-07 19:58:54.508760', 933, '00933', 1),
('2021-12-07 19:58:54.563802', '2021-12-07 19:58:54.563802', 934, '00934', 1),
('2021-12-07 19:58:54.619976', '2021-12-07 19:58:54.619976', 935, '00935', 1),
('2021-12-07 19:58:55.053805', '2021-12-07 19:58:55.053805', 936, '00936', 1),
('2021-12-07 19:58:55.074803', '2021-12-07 19:58:55.074803', 937, '00937', 1),
('2021-12-07 19:58:55.120896', '2021-12-07 19:58:55.120896', 938, '00938', 1),
('2021-12-07 19:58:55.163928', '2021-12-07 19:58:55.163928', 939, '00939', 1),
('2021-12-07 19:58:55.209200', '2021-12-07 19:58:55.209200', 940, '00940', 1),
('2021-12-07 19:58:55.253537', '2021-12-07 19:58:55.253537', 941, '00941', 1),
('2021-12-07 19:58:55.298189', '2021-12-07 19:58:55.298189', 942, '00942', 1),
('2021-12-07 19:58:55.375759', '2021-12-07 19:58:55.375759', 943, '00943', 1),
('2021-12-07 19:58:55.430825', '2021-12-07 19:58:55.430825', 944, '00944', 1),
('2021-12-07 19:58:55.775605', '2021-12-07 19:58:55.775605', 945, '00945', 1),
('2021-12-07 19:58:55.819744', '2021-12-07 19:58:55.819744', 946, '00946', 1),
('2021-12-07 19:58:55.908961', '2021-12-07 19:58:55.908961', 947, '00947', 1),
('2021-12-07 19:58:56.075150', '2021-12-07 19:58:56.075150', 948, '00948', 1),
('2021-12-07 19:58:56.176166', '2021-12-07 19:58:56.176166', 949, '00949', 1),
('2021-12-07 19:58:56.235855', '2021-12-07 19:58:56.236867', 950, '00950', 1),
('2021-12-07 19:58:56.336575', '2021-12-07 19:58:56.336575', 951, '00951', 1),
('2021-12-07 19:58:56.387388', '2021-12-07 19:58:56.387388', 952, '00952', 1),
('2021-12-07 19:58:56.407980', '2021-12-07 19:58:56.408992', 953, '00953', 1),
('2021-12-07 19:58:56.431533', '2021-12-07 19:58:56.431533', 954, '00954', 1),
('2021-12-07 19:58:56.453552', '2021-12-07 19:58:56.453552', 955, '00955', 1),
('2021-12-07 19:58:56.475274', '2021-12-07 19:58:56.476287', 956, '00956', 1),
('2021-12-07 19:58:56.497725', '2021-12-07 19:58:56.497725', 957, '00957', 1),
('2021-12-07 19:58:56.520769', '2021-12-07 19:58:56.520769', 958, '00958', 1),
('2021-12-07 19:58:56.541330', '2021-12-07 19:58:56.542342', 959, '00959', 1),
('2021-12-07 19:58:56.565038', '2021-12-07 19:58:56.565038', 960, '00960', 1),
('2021-12-07 19:58:56.586075', '2021-12-07 19:58:56.586075', 961, '00961', 1),
('2021-12-07 19:58:56.608703', '2021-12-07 19:58:56.608703', 962, '00962', 1),
('2021-12-07 19:58:56.631318', '2021-12-07 19:58:56.631318', 963, '00963', 1),
('2021-12-07 19:58:56.870560', '2021-12-07 19:58:56.870560', 964, '00964', 1),
('2021-12-07 19:58:57.030873', '2021-12-07 19:58:57.030873', 965, '00965', 1),
('2021-12-07 19:58:57.053582', '2021-12-07 19:58:57.053582', 966, '00966', 1),
('2021-12-07 19:58:57.075406', '2021-12-07 19:58:57.075406', 967, '00967', 1),
('2021-12-07 19:58:57.097060', '2021-12-07 19:58:57.097060', 968, '00968', 1),
('2021-12-07 19:58:57.120103', '2021-12-07 19:58:57.120103', 969, '00969', 1),
('2021-12-07 19:58:57.141627', '2021-12-07 19:58:57.141627', 970, '00970', 1),
('2021-12-07 19:58:57.164305', '2021-12-07 19:58:57.164305', 971, '00971', 1),
('2021-12-07 19:58:57.186209', '2021-12-07 19:58:57.186209', 972, '00972', 1),
('2021-12-07 19:58:57.209194', '2021-12-07 19:58:57.209194', 973, '00973', 1),
('2021-12-07 19:58:57.253500', '2021-12-07 19:58:57.253500', 974, '00974', 1),
('2021-12-07 19:58:57.352174', '2021-12-07 19:58:57.352174', 975, '00975', 1),
('2021-12-07 19:58:57.419895', '2021-12-07 19:58:57.419895', 976, '00976', 1),
('2021-12-07 19:58:57.442929', '2021-12-07 19:58:57.442929', 977, '00977', 1),
('2021-12-07 19:58:57.463801', '2021-12-07 19:58:57.463801', 978, '00978', 1),
('2021-12-07 19:58:57.486816', '2021-12-07 19:58:57.486816', 979, '00979', 1),
('2021-12-07 19:58:57.509185', '2021-12-07 19:58:57.510176', 980, '00980', 1),
('2021-12-07 19:58:57.531132', '2021-12-07 19:58:57.531132', 981, '00981', 1),
('2021-12-07 19:58:57.552740', '2021-12-07 19:58:57.552740', 982, '00982', 1),
('2021-12-07 19:58:57.576321', '2021-12-07 19:58:57.576321', 983, '00983', 1),
('2021-12-07 19:58:57.597189', '2021-12-07 19:58:57.597189', 984, '00984', 1),
('2021-12-07 19:58:57.620030', '2021-12-07 19:58:57.620030', 985, '00985', 1),
('2021-12-07 19:58:57.641924', '2021-12-07 19:58:57.641924', 986, '00986', 1),
('2021-12-07 19:58:57.664437', '2021-12-07 19:58:57.664437', 987, '00987', 1),
('2021-12-07 19:58:57.686146', '2021-12-07 19:58:57.686146', 988, '00988', 1),
('2021-12-07 19:58:57.709045', '2021-12-07 19:58:57.709045', 989, '00989', 1),
('2021-12-07 19:58:57.730814', '2021-12-07 19:58:57.730814', 990, '00990', 1),
('2021-12-07 19:58:57.754123', '2021-12-07 19:58:57.754123', 991, '00991', 1),
('2021-12-07 19:58:57.775341', '2021-12-07 19:58:57.776350', 992, '00992', 1),
('2021-12-07 19:58:57.797861', '2021-12-07 19:58:57.797861', 993, '00993', 1),
('2021-12-07 19:58:57.819514', '2021-12-07 19:58:57.819514', 994, '00994', 1),
('2021-12-07 19:58:57.865736', '2021-12-07 19:58:57.865736', 995, '00995', 1),
('2021-12-07 19:58:58.033003', '2021-12-07 19:58:58.033003', 996, '00996', 1),
('2021-12-07 19:58:58.131943', '2021-12-07 19:58:58.131943', 997, '00997', 1),
('2021-12-07 19:58:58.175917', '2021-12-07 19:58:58.175917', 998, '00998', 1),
('2021-12-07 19:58:58.220117', '2021-12-07 19:58:58.220117', 999, '00999', 1),
('2021-12-07 19:58:58.264958', '2021-12-07 19:58:58.265958', 1000, '01000', 1);

-- --------------------------------------------------------

--
-- Table structure for table `receipts_shop`
--

CREATE TABLE `receipts_shop` (
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `id` int(11) NOT NULL,
  `receipt` varchar(255) NOT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `receipts_shop`
--

INSERT INTO `receipts_shop` (`created_at`, `updated_at`, `id`, `receipt`, `status_id`) VALUES
('2021-12-31 08:51:44.136023', '2021-12-31 09:25:17.473667', 1, '00001', 2),
('2021-12-31 08:51:44.250957', '2021-12-31 08:51:44.251960', 2, '00002', 1),
('2021-12-31 08:51:44.311938', '2021-12-31 08:51:44.312950', 3, '00003', 1),
('2021-12-31 08:51:44.501850', '2021-12-31 08:51:44.501850', 4, '00004', 1),
('2021-12-31 08:51:44.544842', '2022-01-11 02:56:21.827128', 5, '00005', 2),
('2021-12-31 08:51:44.608752', '2022-01-11 03:00:10.043543', 6, '00006', 2),
('2021-12-31 08:51:44.634736', '2021-12-31 08:51:44.635285', 7, '00007', 1),
('2021-12-31 08:51:44.678400', '2021-12-31 08:51:44.678400', 8, '00008', 1),
('2021-12-31 08:51:44.833250', '2021-12-31 08:51:44.833250', 9, '00009', 1),
('2021-12-31 08:51:44.900962', '2021-12-31 08:51:44.900962', 10, '00010', 1),
('2021-12-31 08:51:44.966920', '2021-12-31 08:51:44.966920', 11, '00011', 1),
('2021-12-31 08:51:45.011893', '2021-12-31 08:51:45.011893', 12, '00012', 1),
('2021-12-31 08:51:45.062515', '2021-12-31 08:51:45.062515', 13, '00013', 1),
('2021-12-31 08:51:45.116475', '2021-12-31 08:51:45.116475', 14, '00014', 1),
('2021-12-31 08:51:45.197425', '2021-12-31 08:51:45.197425', 15, '00015', 1),
('2021-12-31 08:51:45.262444', '2021-12-31 08:51:45.262444', 16, '00016', 1),
('2021-12-31 08:51:45.289469', '2021-12-31 08:51:45.289469', 17, '00017', 1),
('2021-12-31 08:51:45.350441', '2021-12-31 08:51:45.350441', 18, '00018', 1),
('2021-12-31 08:51:45.379450', '2021-12-31 08:51:45.379450', 19, '00019', 1),
('2021-12-31 08:51:45.422465', '2021-12-31 08:51:45.422465', 20, '00020', 1),
('2021-12-31 08:51:45.467467', '2021-12-31 08:51:45.467467', 21, '00021', 1),
('2021-12-31 08:51:45.516476', '2021-12-31 08:51:45.516476', 22, '00022', 1),
('2021-12-31 08:51:45.571486', '2021-12-31 08:51:45.571486', 23, '00023', 1),
('2021-12-31 08:51:45.619495', '2021-12-31 08:51:45.619495', 24, '00024', 1),
('2021-12-31 08:51:45.683486', '2021-12-31 08:51:45.683486', 25, '00025', 1),
('2021-12-31 08:51:45.735516', '2021-12-31 08:51:45.735516', 26, '00026', 1),
('2021-12-31 08:51:45.795544', '2021-12-31 08:51:45.795544', 27, '00027', 1),
('2021-12-31 08:51:46.278452', '2021-12-31 08:51:46.279452', 28, '00028', 1),
('2021-12-31 08:51:46.323424', '2021-12-31 08:51:46.323424', 29, '00029', 1),
('2021-12-31 08:51:46.378392', '2021-12-31 08:51:46.379389', 30, '00030', 1),
('2021-12-31 08:51:46.424361', '2021-12-31 08:51:46.425363', 31, '00031', 1),
('2021-12-31 08:51:46.479328', '2021-12-31 08:51:46.479328', 32, '00032', 1),
('2021-12-31 08:51:46.524304', '2021-12-31 08:51:46.525300', 33, '00033', 1),
('2021-12-31 08:51:46.595258', '2021-12-31 08:51:46.595258', 34, '00034', 1),
('2021-12-31 08:51:46.675208', '2021-12-31 08:51:46.675208', 35, '00035', 1),
('2021-12-31 08:51:46.712200', '2021-12-31 08:51:46.712200', 36, '00036', 1),
('2021-12-31 08:51:46.760182', '2021-12-31 08:51:46.760182', 37, '00037', 1),
('2021-12-31 08:51:46.817742', '2021-12-31 08:51:46.817742', 38, '00038', 1),
('2021-12-31 08:51:46.873589', '2021-12-31 08:51:46.874587', 39, '00039', 1),
('2021-12-31 08:51:46.934625', '2021-12-31 08:51:46.934625', 40, '00040', 1),
('2021-12-31 08:51:46.978654', '2021-12-31 08:51:46.978654', 41, '00041', 1),
('2021-12-31 08:51:47.032657', '2021-12-31 08:51:47.032657', 42, '00042', 1),
('2021-12-31 08:51:47.113607', '2021-12-31 08:51:47.113607', 43, '00043', 1),
('2021-12-31 08:51:47.157586', '2021-12-31 08:51:47.157586', 44, '00044', 1),
('2021-12-31 08:51:47.201748', '2021-12-31 08:51:47.201748', 45, '00045', 1),
('2021-12-31 08:51:47.245716', '2021-12-31 08:51:47.245716', 46, '00046', 1),
('2021-12-31 08:51:47.289736', '2021-12-31 08:51:47.289736', 47, '00047', 1),
('2021-12-31 08:51:47.334697', '2021-12-31 08:51:47.334697', 48, '00048', 1),
('2021-12-31 08:51:47.456697', '2021-12-31 08:51:47.456697', 49, '00049', 1),
('2021-12-31 08:51:47.516692', '2021-12-31 08:51:47.516692', 50, '00050', 1),
('2021-12-31 08:51:47.547713', '2021-12-31 08:51:47.547713', 51, '00051', 1),
('2021-12-31 08:51:47.600713', '2021-12-31 08:51:47.600713', 52, '00052', 1),
('2021-12-31 08:51:47.665751', '2021-12-31 08:51:47.665751', 53, '00053', 1),
('2021-12-31 08:51:47.733738', '2021-12-31 08:51:47.733738', 54, '00054', 1),
('2021-12-31 08:51:47.805690', '2021-12-31 08:51:47.805690', 55, '00055', 1),
('2021-12-31 08:51:47.833672', '2021-12-31 08:51:47.834672', 56, '00056', 1),
('2021-12-31 08:51:47.937811', '2021-12-31 08:51:47.937811', 57, '00057', 1),
('2021-12-31 08:51:48.037750', '2021-12-31 08:51:48.038750', 58, '00058', 1),
('2021-12-31 08:51:48.105708', '2021-12-31 08:51:48.105708', 59, '00059', 1),
('2021-12-31 08:51:48.136707', '2021-12-31 08:51:48.136707', 60, '00060', 1),
('2021-12-31 08:51:48.252734', '2021-12-31 08:51:48.252734', 61, '00061', 1),
('2021-12-31 08:51:48.278719', '2021-12-31 08:51:48.278719', 62, '00062', 1),
('2021-12-31 08:51:48.325691', '2021-12-31 08:51:48.325691', 63, '00063', 1),
('2021-12-31 08:51:48.386298', '2021-12-31 08:51:48.387293', 64, '00064', 1),
('2021-12-31 08:51:48.424219', '2021-12-31 08:51:48.424219', 65, '00065', 1),
('2021-12-31 08:51:48.472677', '2021-12-31 08:51:48.472677', 66, '00066', 1),
('2021-12-31 08:51:48.511656', '2021-12-31 08:51:48.511656', 67, '00067', 1),
('2021-12-31 08:51:48.557642', '2021-12-31 08:51:48.557642', 68, '00068', 1),
('2021-12-31 08:51:48.600830', '2021-12-31 08:51:48.600830', 69, '00069', 1),
('2021-12-31 08:51:48.674645', '2021-12-31 08:51:48.674645', 70, '00070', 1),
('2021-12-31 08:51:48.743650', '2021-12-31 08:51:48.743650', 71, '00071', 1),
('2021-12-31 08:51:48.766576', '2021-12-31 08:51:48.766576', 72, '00072', 1),
('2021-12-31 08:51:48.811570', '2021-12-31 08:51:48.811570', 73, '00073', 1),
('2021-12-31 08:51:48.864586', '2021-12-31 08:51:48.865584', 74, '00074', 1),
('2021-12-31 08:51:48.927546', '2021-12-31 08:51:48.928545', 75, '00075', 1),
('2021-12-31 08:51:48.960545', '2021-12-31 08:51:48.960545', 76, '00076', 1),
('2021-12-31 08:51:49.029624', '2021-12-31 08:51:49.029624', 77, '00077', 1),
('2021-12-31 08:51:49.130597', '2021-12-31 08:51:49.130597', 78, '00078', 1),
('2021-12-31 08:51:49.156582', '2021-12-31 08:51:49.157580', 79, '00079', 1),
('2021-12-31 08:51:49.214548', '2021-12-31 08:51:49.214548', 80, '00080', 1),
('2021-12-31 08:51:49.283505', '2021-12-31 08:51:49.283505', 81, '00081', 1),
('2021-12-31 08:51:49.334476', '2021-12-31 08:51:49.334476', 82, '00082', 1),
('2021-12-31 08:51:49.417424', '2021-12-31 08:51:49.417424', 83, '00083', 1),
('2021-12-31 08:51:49.473387', '2021-12-31 08:51:49.474385', 84, '00084', 1),
('2021-12-31 08:51:49.539356', '2021-12-31 08:51:49.540345', 85, '00085', 1),
('2021-12-31 08:51:49.605305', '2021-12-31 08:51:49.605305', 86, '00086', 1),
('2021-12-31 08:51:49.672263', '2021-12-31 08:51:49.672263', 87, '00087', 1),
('2021-12-31 08:51:49.706244', '2021-12-31 08:51:49.706244', 88, '00088', 1),
('2021-12-31 08:51:49.759216', '2021-12-31 08:51:49.759216', 89, '00089', 1),
('2021-12-31 08:51:49.806181', '2021-12-31 08:51:49.806181', 90, '00090', 1),
('2021-12-31 08:51:49.872141', '2021-12-31 08:51:49.872141', 91, '00091', 1),
('2021-12-31 08:51:50.011055', '2021-12-31 08:51:50.011055', 92, '00092', 1),
('2021-12-31 08:51:50.089035', '2021-12-31 08:51:50.089035', 93, '00093', 1),
('2021-12-31 08:51:50.178008', '2021-12-31 08:51:50.178008', 94, '00094', 1),
('2021-12-31 08:51:50.222980', '2021-12-31 08:51:50.222980', 95, '00095', 1),
('2021-12-31 08:51:50.272009', '2021-12-31 08:51:50.272009', 96, '00096', 1),
('2021-12-31 08:51:50.325994', '2021-12-31 08:51:50.325994', 97, '00097', 1),
('2021-12-31 08:51:50.375964', '2021-12-31 08:51:50.375964', 98, '00098', 1),
('2021-12-31 08:51:50.402971', '2021-12-31 08:51:50.403967', 99, '00099', 1),
('2021-12-31 08:51:50.461946', '2021-12-31 08:51:50.461946', 100, '00100', 1),
('2021-12-31 08:51:50.495957', '2021-12-31 08:51:50.495957', 101, '00101', 1),
('2021-12-31 08:51:50.561938', '2021-12-31 08:51:50.561938', 102, '00102', 1),
('2021-12-31 08:51:50.592598', '2021-12-31 08:51:50.592598', 103, '00103', 1),
('2021-12-31 08:51:50.634580', '2021-12-31 08:51:50.634580', 104, '00104', 1),
('2021-12-31 08:51:50.679567', '2021-12-31 08:51:50.679567', 105, '00105', 1),
('2021-12-31 08:51:50.728574', '2021-12-31 08:51:50.728574', 106, '00106', 1),
('2021-12-31 08:51:50.794168', '2021-12-31 08:51:50.795169', 107, '00107', 1),
('2021-12-31 08:51:50.830168', '2021-12-31 08:51:50.830168', 108, '00108', 1),
('2021-12-31 08:51:50.894156', '2021-12-31 08:51:50.895155', 109, '00109', 1),
('2021-12-31 08:51:50.934132', '2021-12-31 08:51:50.934132', 110, '00110', 1),
('2021-12-31 08:51:51.035069', '2021-12-31 08:51:51.035069', 111, '00111', 1),
('2021-12-31 08:51:51.235955', '2021-12-31 08:51:51.236945', 112, '00112', 1),
('2021-12-31 08:51:51.523708', '2021-12-31 08:51:51.523708', 113, '00113', 1),
('2021-12-31 08:51:51.657668', '2021-12-31 08:51:51.657668', 114, '00114', 1),
('2021-12-31 08:51:51.770597', '2021-12-31 08:51:51.770597', 115, '00115', 1),
('2021-12-31 08:51:51.823561', '2021-12-31 08:51:51.823561', 116, '00116', 1),
('2021-12-31 08:51:51.888524', '2021-12-31 08:51:51.888524', 117, '00117', 1),
('2021-12-31 08:51:51.912507', '2021-12-31 08:51:51.912507', 118, '00118', 1),
('2021-12-31 08:51:51.958481', '2021-12-31 08:51:51.958481', 119, '00119', 1),
('2021-12-31 08:51:52.005449', '2021-12-31 08:51:52.006451', 120, '00120', 1),
('2021-12-31 08:51:52.044429', '2021-12-31 08:51:52.044429', 121, '00121', 1),
('2021-12-31 08:51:52.090398', '2021-12-31 08:51:52.090398', 122, '00122', 1),
('2021-12-31 08:51:52.140366', '2021-12-31 08:51:52.140366', 123, '00123', 1),
('2021-12-31 08:51:52.179342', '2021-12-31 08:51:52.179342', 124, '00124', 1),
('2021-12-31 08:51:52.222339', '2021-12-31 08:51:52.222339', 125, '00125', 1),
('2021-12-31 08:51:52.339654', '2021-12-31 08:51:52.339654', 126, '00126', 1),
('2021-12-31 08:51:52.378625', '2021-12-31 08:51:52.378625', 127, '00127', 1),
('2021-12-31 08:51:52.424628', '2021-12-31 08:51:52.424628', 128, '00128', 1),
('2021-12-31 08:51:52.467601', '2021-12-31 08:51:52.468602', 129, '00129', 1),
('2021-12-31 08:51:52.512574', '2021-12-31 08:51:52.512574', 130, '00130', 1),
('2021-12-31 08:51:52.561543', '2021-12-31 08:51:52.561543', 131, '00131', 1),
('2021-12-31 08:51:52.601518', '2021-12-31 08:51:52.601518', 132, '00132', 1),
('2021-12-31 08:51:52.664481', '2021-12-31 08:51:52.664481', 133, '00133', 1),
('2021-12-31 08:51:52.701458', '2021-12-31 08:51:52.701458', 134, '00134', 1),
('2021-12-31 08:51:52.760421', '2021-12-31 08:51:52.760421', 135, '00135', 1),
('2021-12-31 08:51:52.801396', '2021-12-31 08:51:52.801396', 136, '00136', 1),
('2021-12-31 08:51:52.845369', '2021-12-31 08:51:52.845369', 137, '00137', 1),
('2021-12-31 08:51:52.933631', '2021-12-31 08:51:52.933631', 138, '00138', 1),
('2021-12-31 08:51:52.979289', '2021-12-31 08:51:52.979289', 139, '00139', 1),
('2021-12-31 08:51:53.034795', '2021-12-31 08:51:53.034795', 140, '00140', 1),
('2021-12-31 08:51:53.083812', '2021-12-31 08:51:53.083812', 141, '00141', 1),
('2021-12-31 08:51:53.139569', '2021-12-31 08:51:53.139569', 142, '00142', 1),
('2021-12-31 08:51:53.218214', '2021-12-31 08:51:53.218214', 143, '00143', 1),
('2021-12-31 08:51:53.285220', '2021-12-31 08:51:53.285220', 144, '00144', 1),
('2021-12-31 08:51:53.314203', '2021-12-31 08:51:53.314203', 145, '00145', 1),
('2021-12-31 08:51:53.356194', '2021-12-31 08:51:53.356194', 146, '00146', 1),
('2021-12-31 08:51:53.401201', '2021-12-31 08:51:53.401201', 147, '00147', 1),
('2021-12-31 08:51:53.452430', '2021-12-31 08:51:53.452430', 148, '00148', 1),
('2021-12-31 08:51:53.490426', '2021-12-31 08:51:53.490426', 149, '00149', 1),
('2021-12-31 08:51:53.584249', '2021-12-31 08:51:53.584249', 150, '00150', 1),
('2021-12-31 08:51:53.623266', '2021-12-31 08:51:53.623266', 151, '00151', 1),
('2021-12-31 08:51:53.668048', '2021-12-31 08:51:53.668048', 152, '00152', 1),
('2021-12-31 08:51:53.718067', '2021-12-31 08:51:53.718067', 153, '00153', 1),
('2021-12-31 08:51:53.769033', '2021-12-31 08:51:53.769033', 154, '00154', 1),
('2021-12-31 08:51:53.819004', '2021-12-31 08:51:53.819004', 155, '00155', 1),
('2021-12-31 08:51:53.845988', '2021-12-31 08:51:53.845988', 156, '00156', 1),
('2021-12-31 08:51:53.889964', '2021-12-31 08:51:53.889964', 157, '00157', 1),
('2021-12-31 08:51:53.936931', '2021-12-31 08:51:53.936931', 158, '00158', 1),
('2021-12-31 08:51:53.978904', '2021-12-31 08:51:53.978904', 159, '00159', 1),
('2021-12-31 08:51:54.023878', '2021-12-31 08:51:54.023878', 160, '00160', 1),
('2021-12-31 08:51:54.073858', '2021-12-31 08:51:54.074856', 161, '00161', 1),
('2021-12-31 08:51:54.105827', '2021-12-31 08:51:54.105827', 162, '00162', 1),
('2021-12-31 08:51:54.190774', '2021-12-31 08:51:54.190774', 163, '00163', 1),
('2021-12-31 08:51:54.212761', '2021-12-31 08:51:54.212761', 164, '00164', 1),
('2021-12-31 08:51:54.257734', '2021-12-31 08:51:54.257734', 165, '00165', 1),
('2021-12-31 08:51:54.312698', '2021-12-31 08:51:54.312698', 166, '00166', 1),
('2021-12-31 08:51:54.375687', '2021-12-31 08:51:54.375687', 167, '00167', 1),
('2021-12-31 08:51:54.412426', '2021-12-31 08:51:54.413425', 168, '00168', 1),
('2021-12-31 08:51:54.461420', '2021-12-31 08:51:54.461420', 169, '00169', 1),
('2021-12-31 08:51:54.514406', '2021-12-31 08:51:54.514406', 170, '00170', 1),
('2021-12-31 08:51:54.579387', '2021-12-31 08:51:54.579387', 171, '00171', 1),
('2021-12-31 08:51:54.846224', '2021-12-31 08:51:54.846224', 172, '00172', 1),
('2021-12-31 08:51:54.895221', '2021-12-31 08:51:54.895221', 173, '00173', 1),
('2021-12-31 08:51:54.925260', '2021-12-31 08:51:54.925260', 174, '00174', 1),
('2021-12-31 08:51:54.979756', '2021-12-31 08:51:54.979756', 175, '00175', 1),
('2021-12-31 08:51:55.040735', '2021-12-31 08:51:55.040735', 176, '00176', 1),
('2021-12-31 08:51:55.098746', '2021-12-31 08:51:55.098746', 177, '00177', 1),
('2021-12-31 08:51:55.123728', '2021-12-31 08:51:55.123728', 178, '00178', 1),
('2021-12-31 08:51:55.184723', '2021-12-31 08:51:55.184723', 179, '00179', 1),
('2021-12-31 08:51:55.213742', '2021-12-31 08:51:55.213742', 180, '00180', 1),
('2021-12-31 08:51:55.256472', '2021-12-31 08:51:55.256472', 181, '00181', 1),
('2021-12-31 08:51:55.301460', '2021-12-31 08:51:55.301460', 182, '00182', 1),
('2021-12-31 08:51:55.351434', '2021-12-31 08:51:55.351434', 183, '00183', 1),
('2021-12-31 08:51:55.390407', '2021-12-31 08:51:55.390407', 184, '00184', 1),
('2021-12-31 08:51:55.434379', '2021-12-31 08:51:55.434379', 185, '00185', 1),
('2021-12-31 08:51:55.473354', '2021-12-31 08:51:55.473354', 186, '00186', 1),
('2021-12-31 08:51:55.568297', '2021-12-31 08:51:55.568297', 187, '00187', 1),
('2021-12-31 08:51:55.640259', '2021-12-31 08:51:55.640259', 188, '00188', 1),
('2021-12-31 08:51:55.706211', '2021-12-31 08:51:55.706211', 189, '00189', 1),
('2021-12-31 08:51:55.774190', '2021-12-31 08:51:55.774190', 190, '00190', 1),
('2021-12-31 08:51:55.845501', '2021-12-31 08:51:55.845501', 191, '00191', 1),
('2021-12-31 08:51:55.912475', '2021-12-31 08:51:55.912475', 192, '00192', 1),
('2021-12-31 08:51:55.990501', '2021-12-31 08:51:55.990501', 193, '00193', 1),
('2021-12-31 08:51:56.091469', '2021-12-31 08:51:56.091469', 194, '00194', 1),
('2021-12-31 08:51:56.195425', '2021-12-31 08:51:56.195425', 195, '00195', 1),
('2021-12-31 08:51:56.310368', '2021-12-31 08:51:56.310368', 196, '00196', 1),
('2021-12-31 08:51:56.415404', '2021-12-31 08:51:56.415404', 197, '00197', 1),
('2021-12-31 08:51:56.461008', '2021-12-31 08:51:56.461008', 198, '00198', 1),
('2021-12-31 08:51:56.501982', '2021-12-31 08:51:56.501982', 199, '00199', 1),
('2021-12-31 08:51:56.545954', '2021-12-31 08:51:56.545954', 200, '00200', 1),
('2021-12-31 08:51:56.593930', '2021-12-31 08:51:56.593930', 201, '00201', 1),
('2021-12-31 08:51:56.634197', '2021-12-31 08:51:56.634197', 202, '00202', 1),
('2021-12-31 08:51:56.679214', '2021-12-31 08:51:56.679214', 203, '00203', 1),
('2021-12-31 08:51:56.729439', '2021-12-31 08:51:56.729439', 204, '00204', 1),
('2021-12-31 08:51:57.588483', '2021-12-31 08:51:57.588483', 205, '00205', 1),
('2021-12-31 08:51:57.657477', '2021-12-31 08:51:57.657477', 206, '00206', 1),
('2021-12-31 08:51:57.711890', '2021-12-31 08:51:57.711890', 207, '00207', 1),
('2021-12-31 08:51:57.770332', '2021-12-31 08:51:57.770332', 208, '00208', 1),
('2021-12-31 08:51:57.825395', '2021-12-31 08:51:57.825395', 209, '00209', 1),
('2021-12-31 08:51:57.873642', '2021-12-31 08:51:57.873642', 210, '00210', 1),
('2021-12-31 08:51:57.979018', '2021-12-31 08:51:57.979018', 211, '00211', 1),
('2021-12-31 08:51:58.028996', '2021-12-31 08:51:58.028996', 212, '00212', 1),
('2021-12-31 08:51:58.056975', '2021-12-31 08:51:58.056975', 213, '00213', 1),
('2021-12-31 08:51:58.106750', '2021-12-31 08:51:58.106750', 214, '00214', 1),
('2021-12-31 08:51:58.139762', '2021-12-31 08:51:58.139762', 215, '00215', 1),
('2021-12-31 08:51:58.178386', '2021-12-31 08:51:58.178386', 216, '00216', 1),
('2021-12-31 08:51:58.246756', '2021-12-31 08:51:58.246756', 217, '00217', 1),
('2021-12-31 08:51:58.300901', '2021-12-31 08:51:58.301906', 218, '00218', 1),
('2021-12-31 08:51:58.359865', '2021-12-31 08:51:58.360865', 219, '00219', 1),
('2021-12-31 08:51:58.412833', '2021-12-31 08:51:58.412833', 220, '00220', 1),
('2021-12-31 08:51:58.451811', '2021-12-31 08:51:58.451811', 221, '00221', 1),
('2021-12-31 08:51:58.527761', '2021-12-31 08:51:58.527761', 222, '00222', 1),
('2021-12-31 08:51:58.601716', '2021-12-31 08:51:58.601716', 223, '00223', 1),
('2021-12-31 08:51:58.668674', '2021-12-31 08:51:58.668674', 224, '00224', 1),
('2021-12-31 08:51:58.729638', '2021-12-31 08:51:58.729638', 225, '00225', 1),
('2021-12-31 08:51:58.778633', '2021-12-31 08:51:58.778633', 226, '00226', 1),
('2021-12-31 08:51:58.829662', '2021-12-31 08:51:58.829662', 227, '00227', 1),
('2021-12-31 08:51:58.882624', '2021-12-31 08:51:58.882624', 228, '00228', 1),
('2021-12-31 08:51:58.929510', '2021-12-31 08:51:58.929510', 229, '00229', 1),
('2021-12-31 08:51:58.956511', '2021-12-31 08:51:58.957514', 230, '00230', 1),
('2021-12-31 08:51:59.035498', '2021-12-31 08:51:59.035498', 231, '00231', 1),
('2021-12-31 08:51:59.083505', '2021-12-31 08:51:59.083505', 232, '00232', 1),
('2021-12-31 08:51:59.152499', '2021-12-31 08:51:59.152499', 233, '00233', 1),
('2021-12-31 08:51:59.181537', '2021-12-31 08:51:59.181537', 234, '00234', 1),
('2021-12-31 08:51:59.223517', '2021-12-31 08:51:59.223517', 235, '00235', 1),
('2021-12-31 08:51:59.268520', '2021-12-31 08:51:59.268520', 236, '00236', 1),
('2021-12-31 08:51:59.323542', '2021-12-31 08:51:59.323542', 237, '00237', 1),
('2021-12-31 08:51:59.390407', '2021-12-31 08:51:59.390407', 238, '00238', 1),
('2021-12-31 08:51:59.434384', '2021-12-31 08:51:59.434384', 239, '00239', 1),
('2021-12-31 08:51:59.481420', '2021-12-31 08:51:59.481420', 240, '00240', 1),
('2021-12-31 08:51:59.523433', '2021-12-31 08:51:59.523433', 241, '00241', 1),
('2021-12-31 08:51:59.588419', '2021-12-31 08:51:59.588419', 242, '00242', 1),
('2021-12-31 08:51:59.612441', '2021-12-31 08:51:59.612441', 243, '00243', 1),
('2021-12-31 08:51:59.671435', '2021-12-31 08:51:59.671435', 244, '00244', 1),
('2021-12-31 08:51:59.720446', '2021-12-31 08:51:59.720446', 245, '00245', 1),
('2021-12-31 08:51:59.773411', '2021-12-31 08:51:59.773411', 246, '00246', 1),
('2021-12-31 08:51:59.805396', '2021-12-31 08:51:59.805396', 247, '00247', 1),
('2021-12-31 08:51:59.857362', '2021-12-31 08:51:59.857362', 248, '00248', 1),
('2021-12-31 08:51:59.924322', '2021-12-31 08:51:59.924322', 249, '00249', 1),
('2021-12-31 08:51:59.972291', '2021-12-31 08:51:59.972291', 250, '00250', 1),
('2021-12-31 08:52:00.042248', '2021-12-31 08:52:00.042248', 251, '00251', 1),
('2021-12-31 08:52:00.125196', '2021-12-31 08:52:00.125196', 252, '00252', 1),
('2021-12-31 08:52:00.177164', '2021-12-31 08:52:00.177164', 253, '00253', 1),
('2021-12-31 08:52:00.230137', '2021-12-31 08:52:00.230137', 254, '00254', 1),
('2021-12-31 08:52:00.294118', '2021-12-31 08:52:00.295117', 255, '00255', 1),
('2021-12-31 08:52:00.336098', '2021-12-31 08:52:00.336098', 256, '00256', 1),
('2021-12-31 08:52:00.392333', '2021-12-31 08:52:00.392333', 257, '00257', 1),
('2021-12-31 08:52:00.434340', '2021-12-31 08:52:00.434340', 258, '00258', 1),
('2021-12-31 08:52:00.494339', '2021-12-31 08:52:00.494339', 259, '00259', 1),
('2021-12-31 08:52:00.551495', '2021-12-31 08:52:00.551495', 260, '00260', 1),
('2021-12-31 08:52:00.602333', '2021-12-31 08:52:00.602333', 261, '00261', 1),
('2021-12-31 08:52:00.646358', '2021-12-31 08:52:00.646358', 262, '00262', 1),
('2021-12-31 08:52:00.692375', '2021-12-31 08:52:00.692375', 263, '00263', 1),
('2021-12-31 08:52:00.734552', '2021-12-31 08:52:00.734552', 264, '00264', 1),
('2021-12-31 08:52:00.779388', '2021-12-31 08:52:00.780387', 265, '00265', 1),
('2021-12-31 08:52:00.835229', '2021-12-31 08:52:00.835229', 266, '00266', 1),
('2021-12-31 08:52:00.882731', '2021-12-31 08:52:00.882731', 267, '00267', 1),
('2021-12-31 08:52:00.924388', '2021-12-31 08:52:00.924388', 268, '00268', 1),
('2021-12-31 08:52:00.982366', '2021-12-31 08:52:00.982366', 269, '00269', 1),
('2021-12-31 08:52:01.024356', '2021-12-31 08:52:01.024356', 270, '00270', 1),
('2021-12-31 08:52:01.069327', '2021-12-31 08:52:01.069327', 271, '00271', 1),
('2021-12-31 08:52:01.120370', '2021-12-31 08:52:01.120370', 272, '00272', 1),
('2021-12-31 08:52:01.216339', '2021-12-31 08:52:01.216339', 273, '00273', 1),
('2021-12-31 08:52:01.268372', '2021-12-31 08:52:01.268372', 274, '00274', 1),
('2021-12-31 08:52:01.317342', '2021-12-31 08:52:01.317342', 275, '00275', 1),
('2021-12-31 08:52:01.369318', '2021-12-31 08:52:01.369318', 276, '00276', 1),
('2021-12-31 08:52:01.422280', '2021-12-31 08:52:01.422280', 277, '00277', 1),
('2021-12-31 08:52:01.474244', '2021-12-31 08:52:01.474244', 278, '00278', 1),
('2021-12-31 08:52:01.519218', '2021-12-31 08:52:01.519218', 279, '00279', 1),
('2021-12-31 08:52:01.590173', '2021-12-31 08:52:01.590173', 280, '00280', 1),
('2021-12-31 08:52:01.675081', '2021-12-31 08:52:01.675081', 281, '00281', 1),
('2021-12-31 08:52:01.741041', '2021-12-31 08:52:01.741041', 282, '00282', 1),
('2021-12-31 08:52:01.771039', '2021-12-31 08:52:01.771039', 283, '00283', 1),
('2021-12-31 08:52:01.842071', '2021-12-31 08:52:01.842071', 284, '00284', 1),
('2021-12-31 08:52:01.879048', '2021-12-31 08:52:01.879048', 285, '00285', 1),
('2021-12-31 08:52:01.939062', '2021-12-31 08:52:01.939062', 286, '00286', 1),
('2021-12-31 08:52:01.998063', '2021-12-31 08:52:01.998063', 287, '00287', 1),
('2021-12-31 08:52:02.071057', '2021-12-31 08:52:02.072056', 288, '00288', 1),
('2021-12-31 08:52:02.129521', '2021-12-31 08:52:02.129521', 289, '00289', 1),
('2021-12-31 08:52:02.178501', '2021-12-31 08:52:02.178501', 290, '00290', 1),
('2021-12-31 08:52:02.213496', '2021-12-31 08:52:02.213496', 291, '00291', 1),
('2021-12-31 08:52:02.445359', '2021-12-31 08:52:02.445359', 292, '00292', 1),
('2021-12-31 08:52:02.526498', '2021-12-31 08:52:02.527493', 293, '00293', 1),
('2021-12-31 08:52:02.594490', '2021-12-31 08:52:02.594490', 294, '00294', 1),
('2021-12-31 08:52:02.724487', '2021-12-31 08:52:02.724487', 295, '00295', 1),
('2021-12-31 08:52:02.796457', '2021-12-31 08:52:02.796457', 296, '00296', 1),
('2021-12-31 08:52:02.826447', '2021-12-31 08:52:02.826447', 297, '00297', 1),
('2021-12-31 08:52:02.916399', '2021-12-31 08:52:02.916399', 298, '00298', 1),
('2021-12-31 08:52:02.969350', '2021-12-31 08:52:02.969350', 299, '00299', 1),
('2021-12-31 08:52:03.023315', '2021-12-31 08:52:03.023315', 300, '00300', 1),
('2021-12-31 08:52:03.068288', '2021-12-31 08:52:03.068288', 301, '00301', 1),
('2021-12-31 08:52:03.124257', '2021-12-31 08:52:03.124257', 302, '00302', 1),
('2021-12-31 08:52:03.169226', '2021-12-31 08:52:03.169226', 303, '00303', 1),
('2021-12-31 08:52:03.223194', '2021-12-31 08:52:03.223194', 304, '00304', 1),
('2021-12-31 08:52:03.268193', '2021-12-31 08:52:03.268193', 305, '00305', 1),
('2021-12-31 08:52:03.323180', '2021-12-31 08:52:03.323180', 306, '00306', 1),
('2021-12-31 08:52:03.403485', '2021-12-31 08:52:03.403485', 307, '00307', 1),
('2021-12-31 08:52:03.805345', '2021-12-31 08:52:03.805345', 308, '00308', 1),
('2021-12-31 08:52:03.877352', '2021-12-31 08:52:03.878364', 309, '00309', 1),
('2021-12-31 08:52:03.929743', '2021-12-31 08:52:03.929743', 310, '00310', 1),
('2021-12-31 08:52:03.990756', '2021-12-31 08:52:03.990756', 311, '00311', 1),
('2021-12-31 08:52:04.041773', '2021-12-31 08:52:04.042774', 312, '00312', 1),
('2021-12-31 08:52:04.091047', '2021-12-31 08:52:04.091047', 313, '00313', 1),
('2021-12-31 08:52:04.146515', '2021-12-31 08:52:04.146515', 314, '00314', 1),
('2021-12-31 08:52:04.221536', '2021-12-31 08:52:04.221536', 315, '00315', 1),
('2021-12-31 08:52:04.277620', '2021-12-31 08:52:04.277620', 316, '00316', 1),
('2021-12-31 08:52:04.332603', '2021-12-31 08:52:04.332603', 317, '00317', 1),
('2021-12-31 08:52:04.379557', '2021-12-31 08:52:04.379557', 318, '00318', 1),
('2021-12-31 08:52:04.479497', '2021-12-31 08:52:04.479497', 319, '00319', 1),
('2021-12-31 08:52:04.513475', '2021-12-31 08:52:04.513475', 320, '00320', 1),
('2021-12-31 08:52:04.568442', '2021-12-31 08:52:04.568442', 321, '00321', 1),
('2021-12-31 08:52:04.630407', '2021-12-31 08:52:04.630407', 322, '00322', 1),
('2021-12-31 08:52:04.729342', '2021-12-31 08:52:04.729342', 323, '00323', 1),
('2021-12-31 08:52:04.902346', '2021-12-31 08:52:04.902346', 324, '00324', 1),
('2021-12-31 08:52:05.015490', '2021-12-31 08:52:05.015490', 325, '00325', 1),
('2021-12-31 08:52:05.068523', '2021-12-31 08:52:05.068523', 326, '00326', 1),
('2021-12-31 08:52:05.119504', '2021-12-31 08:52:05.119504', 327, '00327', 1),
('2021-12-31 08:52:05.149487', '2021-12-31 08:52:05.149487', 328, '00328', 1),
('2021-12-31 08:52:05.201490', '2021-12-31 08:52:05.201490', 329, '00329', 1),
('2021-12-31 08:52:05.257479', '2021-12-31 08:52:05.257479', 330, '00330', 1),
('2021-12-31 08:52:05.314486', '2021-12-31 08:52:05.315485', 331, '00331', 1),
('2021-12-31 08:52:05.376444', '2021-12-31 08:52:05.376444', 332, '00332', 1),
('2021-12-31 08:52:05.413462', '2021-12-31 08:52:05.414471', 333, '00333', 1),
('2021-12-31 08:52:05.458462', '2021-12-31 08:52:05.458462', 334, '00334', 1),
('2021-12-31 08:52:05.554442', '2021-12-31 08:52:05.554442', 335, '00335', 1),
('2021-12-31 08:52:05.603466', '2021-12-31 08:52:05.604457', 336, '00336', 1),
('2021-12-31 08:52:05.646430', '2021-12-31 08:52:05.646430', 337, '00337', 1),
('2021-12-31 08:52:05.704768', '2021-12-31 08:52:05.704768', 338, '00338', 1),
('2021-12-31 08:52:05.746736', '2021-12-31 08:52:05.746736', 339, '00339', 1),
('2021-12-31 08:52:05.940617', '2021-12-31 08:52:05.940617', 340, '00340', 1),
('2021-12-31 08:52:06.280752', '2021-12-31 08:52:06.280752', 341, '00341', 1),
('2021-12-31 08:52:06.335452', '2021-12-31 08:52:06.335452', 342, '00342', 1),
('2021-12-31 08:52:06.401973', '2021-12-31 08:52:06.401973', 343, '00343', 1),
('2021-12-31 08:52:06.463956', '2021-12-31 08:52:06.463956', 344, '00344', 1),
('2021-12-31 08:52:06.519939', '2021-12-31 08:52:06.519939', 345, '00345', 1),
('2021-12-31 08:52:06.611903', '2021-12-31 08:52:06.611903', 346, '00346', 1),
('2021-12-31 08:52:06.646823', '2021-12-31 08:52:06.646823', 347, '00347', 1),
('2021-12-31 08:52:06.698821', '2021-12-31 08:52:06.698821', 348, '00348', 1),
('2021-12-31 08:52:06.746809', '2021-12-31 08:52:06.746809', 349, '00349', 1),
('2021-12-31 08:52:06.803853', '2021-12-31 08:52:06.803853', 350, '00350', 1),
('2021-12-31 08:52:06.857786', '2021-12-31 08:52:06.857786', 351, '00351', 1),
('2021-12-31 08:52:06.902776', '2021-12-31 08:52:06.902776', 352, '00352', 1),
('2021-12-31 08:52:06.952746', '2021-12-31 08:52:06.952746', 353, '00353', 1),
('2021-12-31 08:52:07.043789', '2021-12-31 08:52:07.043789', 354, '00354', 1),
('2021-12-31 08:52:07.424681', '2021-12-31 08:52:07.424681', 355, '00355', 1),
('2021-12-31 08:52:07.604570', '2021-12-31 08:52:07.604570', 356, '00356', 1),
('2021-12-31 08:52:07.757379', '2021-12-31 08:52:07.757379', 357, '00357', 1),
('2021-12-31 08:52:07.808387', '2021-12-31 08:52:07.808387', 358, '00358', 1),
('2021-12-31 08:52:07.876392', '2021-12-31 08:52:07.876392', 359, '00359', 1),
('2021-12-31 08:52:07.959400', '2021-12-31 08:52:07.959400', 360, '00360', 1),
('2021-12-31 08:52:08.013425', '2021-12-31 08:52:08.013425', 361, '00361', 1),
('2021-12-31 08:52:08.079652', '2021-12-31 08:52:08.079652', 362, '00362', 1),
('2021-12-31 08:52:08.136497', '2021-12-31 08:52:08.136497', 363, '00363', 1),
('2021-12-31 08:52:08.201563', '2021-12-31 08:52:08.201563', 364, '00364', 1),
('2021-12-31 08:52:08.261579', '2021-12-31 08:52:08.261579', 365, '00365', 1),
('2021-12-31 08:52:08.336572', '2021-12-31 08:52:08.336572', 366, '00366', 1),
('2021-12-31 08:52:08.402551', '2021-12-31 08:52:08.402551', 367, '00367', 1),
('2021-12-31 08:52:08.558831', '2021-12-31 08:52:08.558831', 368, '00368', 1),
('2021-12-31 08:52:08.659661', '2021-12-31 08:52:08.659661', 369, '00369', 1),
('2021-12-31 08:52:08.714595', '2021-12-31 08:52:08.714595', 370, '00370', 1),
('2021-12-31 08:52:08.890477', '2021-12-31 08:52:08.890477', 371, '00371', 1),
('2021-12-31 08:52:08.975424', '2021-12-31 08:52:08.975424', 372, '00372', 1),
('2021-12-31 08:52:09.023394', '2021-12-31 08:52:09.024395', 373, '00373', 1),
('2021-12-31 08:52:09.085366', '2021-12-31 08:52:09.085366', 374, '00374', 1),
('2021-12-31 08:52:09.139325', '2021-12-31 08:52:09.139325', 375, '00375', 1),
('2021-12-31 08:52:09.191292', '2021-12-31 08:52:09.191292', 376, '00376', 1),
('2021-12-31 08:52:09.248260', '2021-12-31 08:52:09.248260', 377, '00377', 1),
('2021-12-31 08:52:09.304012', '2021-12-31 08:52:09.304012', 378, '00378', 1),
('2021-12-31 08:52:09.357998', '2021-12-31 08:52:09.357998', 379, '00379', 1),
('2021-12-31 08:52:09.424987', '2021-12-31 08:52:09.424987', 380, '00380', 1),
('2021-12-31 08:52:09.507703', '2021-12-31 08:52:09.507703', 381, '00381', 1),
('2021-12-31 08:52:09.706329', '2021-12-31 08:52:09.707328', 382, '00382', 1),
('2021-12-31 08:52:10.064534', '2021-12-31 08:52:10.064534', 383, '00383', 1),
('2021-12-31 08:52:10.213448', '2021-12-31 08:52:10.213448', 384, '00384', 1),
('2021-12-31 08:52:10.349362', '2021-12-31 08:52:10.349362', 385, '00385', 1),
('2021-12-31 08:52:10.599208', '2021-12-31 08:52:10.599208', 386, '00386', 1),
('2021-12-31 08:52:10.748118', '2021-12-31 08:52:10.748118', 387, '00387', 1),
('2021-12-31 08:52:10.802640', '2021-12-31 08:52:10.803640', 388, '00388', 1),
('2021-12-31 08:52:10.857487', '2021-12-31 08:52:10.857487', 389, '00389', 1),
('2021-12-31 08:52:10.915484', '2021-12-31 08:52:10.915484', 390, '00390', 1),
('2021-12-31 08:52:10.982500', '2021-12-31 08:52:10.982500', 391, '00391', 1),
('2021-12-31 08:52:11.036456', '2021-12-31 08:52:11.036456', 392, '00392', 1),
('2021-12-31 08:52:11.091488', '2021-12-31 08:52:11.091488', 393, '00393', 1),
('2021-12-31 08:52:11.148762', '2021-12-31 08:52:11.148762', 394, '00394', 1),
('2021-12-31 08:52:11.202741', '2021-12-31 08:52:11.202741', 395, '00395', 1),
('2021-12-31 08:52:11.304672', '2021-12-31 08:52:11.305672', 396, '00396', 1),
('2021-12-31 08:52:11.353660', '2021-12-31 08:52:11.353660', 397, '00397', 1),
('2021-12-31 08:52:11.391655', '2021-12-31 08:52:11.391655', 398, '00398', 1),
('2021-12-31 08:52:11.447621', '2021-12-31 08:52:11.447621', 399, '00399', 1),
('2021-12-31 08:52:11.613668', '2021-12-31 08:52:11.613668', 400, '00400', 1),
('2021-12-31 08:52:11.673700', '2021-12-31 08:52:11.674696', 401, '00401', 1),
('2021-12-31 08:52:11.809493', '2021-12-31 08:52:11.810494', 402, '00402', 1),
('2021-12-31 08:52:11.897440', '2021-12-31 08:52:11.897440', 403, '00403', 1),
('2021-12-31 08:52:11.942411', '2021-12-31 08:52:11.942411', 404, '00404', 1),
('2021-12-31 08:52:12.011383', '2021-12-31 08:52:12.011383', 405, '00405', 1),
('2021-12-31 08:52:12.081324', '2021-12-31 08:52:12.081324', 406, '00406', 1),
('2021-12-31 08:52:12.198254', '2021-12-31 08:52:12.198254', 407, '00407', 1),
('2021-12-31 08:52:12.287077', '2021-12-31 08:52:12.287077', 408, '00408', 1),
('2021-12-31 08:52:12.399055', '2021-12-31 08:52:12.399055', 409, '00409', 1),
('2021-12-31 08:52:12.436002', '2021-12-31 08:52:12.436002', 410, '00410', 1),
('2021-12-31 08:52:12.493026', '2021-12-31 08:52:12.494022', 411, '00411', 1),
('2021-12-31 08:52:12.547906', '2021-12-31 08:52:12.548907', 412, '00412', 1),
('2021-12-31 08:52:12.715894', '2021-12-31 08:52:12.715894', 413, '00413', 1),
('2021-12-31 08:52:12.850891', '2021-12-31 08:52:12.850891', 414, '00414', 1),
('2021-12-31 08:52:12.936857', '2021-12-31 08:52:12.936857', 415, '00415', 1),
('2021-12-31 08:52:12.988119', '2021-12-31 08:52:12.988119', 416, '00416', 1),
('2021-12-31 08:52:13.054125', '2021-12-31 08:52:13.054125', 417, '00417', 1),
('2021-12-31 08:52:13.143146', '2021-12-31 08:52:13.143146', 418, '00418', 1),
('2021-12-31 08:52:13.209108', '2021-12-31 08:52:13.209108', 419, '00419', 1),
('2021-12-31 08:52:13.276073', '2021-12-31 08:52:13.276073', 420, '00420', 1),
('2021-12-31 08:52:13.339033', '2021-12-31 08:52:13.340037', 421, '00421', 1),
('2021-12-31 08:52:13.392004', '2021-12-31 08:52:13.393008', 422, '00422', 1),
('2021-12-31 08:52:13.491950', '2021-12-31 08:52:13.491950', 423, '00423', 1),
('2021-12-31 08:52:13.559894', '2021-12-31 08:52:13.559894', 424, '00424', 1),
('2021-12-31 08:52:13.613861', '2021-12-31 08:52:13.613861', 425, '00425', 1),
('2021-12-31 08:52:13.730443', '2021-12-31 08:52:13.730443', 426, '00426', 1),
('2021-12-31 08:52:13.791437', '2021-12-31 08:52:13.791437', 427, '00427', 1),
('2021-12-31 08:52:13.884431', '2021-12-31 08:52:13.884431', 428, '00428', 1),
('2021-12-31 08:52:13.983421', '2021-12-31 08:52:13.983421', 429, '00429', 1),
('2021-12-31 08:52:14.110735', '2021-12-31 08:52:14.110735', 430, '00430', 1),
('2021-12-31 08:52:14.169728', '2021-12-31 08:52:14.169728', 431, '00431', 1),
('2021-12-31 08:52:14.235720', '2021-12-31 08:52:14.235720', 432, '00432', 1),
('2021-12-31 08:52:14.293746', '2021-12-31 08:52:14.293746', 433, '00433', 1),
('2021-12-31 08:52:14.362548', '2021-12-31 08:52:14.362548', 434, '00434', 1),
('2021-12-31 08:52:14.420533', '2021-12-31 08:52:14.420533', 435, '00435', 1),
('2021-12-31 08:52:14.463514', '2021-12-31 08:52:14.464514', 436, '00436', 1),
('2021-12-31 08:52:14.568566', '2021-12-31 08:52:14.568566', 437, '00437', 1),
('2021-12-31 08:52:14.620366', '2021-12-31 08:52:14.620366', 438, '00438', 1),
('2021-12-31 08:52:14.658348', '2021-12-31 08:52:14.658348', 439, '00439', 1),
('2021-12-31 08:52:14.716321', '2021-12-31 08:52:14.717318', 440, '00440', 1),
('2021-12-31 08:52:14.836239', '2021-12-31 08:52:14.836239', 441, '00441', 1),
('2021-12-31 08:52:14.953167', '2021-12-31 08:52:14.953167', 442, '00442', 1),
('2021-12-31 08:52:15.071096', '2021-12-31 08:52:15.071096', 443, '00443', 1),
('2021-12-31 08:52:15.137053', '2021-12-31 08:52:15.137053', 444, '00444', 1),
('2021-12-31 08:52:15.192019', '2021-12-31 08:52:15.192019', 445, '00445', 1),
('2021-12-31 08:52:15.242986', '2021-12-31 08:52:15.242986', 446, '00446', 1),
('2021-12-31 08:52:15.279990', '2021-12-31 08:52:15.280991', 447, '00447', 1),
('2021-12-31 08:52:15.344951', '2021-12-31 08:52:15.344951', 448, '00448', 1),
('2021-12-31 08:52:15.379930', '2021-12-31 08:52:15.379930', 449, '00449', 1),
('2021-12-31 08:52:15.438897', '2021-12-31 08:52:15.438897', 450, '00450', 1),
('2021-12-31 08:52:15.491898', '2021-12-31 08:52:15.491898', 451, '00451', 1),
('2021-12-31 08:52:15.547867', '2021-12-31 08:52:15.547867', 452, '00452', 1),
('2021-12-31 08:52:15.658851', '2021-12-31 08:52:15.658851', 453, '00453', 1),
('2021-12-31 08:52:15.727282', '2021-12-31 08:52:15.727282', 454, '00454', 1),
('2021-12-31 08:52:15.779899', '2021-12-31 08:52:15.779899', 455, '00455', 1),
('2021-12-31 08:52:15.880268', '2021-12-31 08:52:15.880268', 456, '00456', 1),
('2021-12-31 08:52:15.943243', '2021-12-31 08:52:15.944229', 457, '00457', 1),
('2021-12-31 08:52:15.980718', '2021-12-31 08:52:15.980718', 458, '00458', 1),
('2021-12-31 08:52:16.036533', '2021-12-31 08:52:16.036533', 459, '00459', 1),
('2021-12-31 08:52:16.162329', '2021-12-31 08:52:16.162329', 460, '00460', 1),
('2021-12-31 08:52:16.213296', '2021-12-31 08:52:16.213296', 461, '00461', 1),
('2021-12-31 08:52:16.265777', '2021-12-31 08:52:16.265777', 462, '00462', 1),
('2021-12-31 08:52:16.302761', '2021-12-31 08:52:16.302761', 463, '00463', 1),
('2021-12-31 08:52:16.370719', '2021-12-31 08:52:16.371718', 464, '00464', 1),
('2021-12-31 08:52:16.433681', '2021-12-31 08:52:16.433681', 465, '00465', 1),
('2021-12-31 08:52:16.482653', '2021-12-31 08:52:16.482653', 466, '00466', 1),
('2021-12-31 08:52:16.536617', '2021-12-31 08:52:16.536617', 467, '00467', 1),
('2021-12-31 08:52:16.594118', '2021-12-31 08:52:16.594118', 468, '00468', 1),
('2021-12-31 08:52:16.651081', '2021-12-31 08:52:16.651081', 469, '00469', 1),
('2021-12-31 08:52:16.703056', '2021-12-31 08:52:16.704051', 470, '00470', 1),
('2021-12-31 08:52:16.853971', '2021-12-31 08:52:16.853971', 471, '00471', 1),
('2021-12-31 08:52:17.082404', '2021-12-31 08:52:17.082404', 472, '00472', 1),
('2021-12-31 08:52:17.258343', '2021-12-31 08:52:17.258343', 473, '00473', 1),
('2021-12-31 08:52:17.352311', '2021-12-31 08:52:17.352311', 474, '00474', 1),
('2021-12-31 08:52:17.406284', '2021-12-31 08:52:17.406284', 475, '00475', 1),
('2021-12-31 08:52:17.457270', '2021-12-31 08:52:17.457270', 476, '00476', 1),
('2021-12-31 08:52:17.525229', '2021-12-31 08:52:17.525229', 477, '00477', 1),
('2021-12-31 08:52:17.577246', '2021-12-31 08:52:17.577246', 478, '00478', 1),
('2021-12-31 08:52:17.614225', '2021-12-31 08:52:17.614225', 479, '00479', 1),
('2021-12-31 08:52:17.673250', '2021-12-31 08:52:17.674241', 480, '00480', 1),
('2021-12-31 08:52:17.728235', '2021-12-31 08:52:17.728235', 481, '00481', 1),
('2021-12-31 08:52:17.780206', '2021-12-31 08:52:17.780206', 482, '00482', 1),
('2021-12-31 08:52:17.903126', '2021-12-31 08:52:17.903126', 483, '00483', 1),
('2021-12-31 08:52:17.966087', '2021-12-31 08:52:17.966087', 484, '00484', 1),
('2021-12-31 08:52:18.002065', '2021-12-31 08:52:18.003065', 485, '00485', 1),
('2021-12-31 08:52:18.323401', '2021-12-31 08:52:18.323401', 486, '00486', 1),
('2021-12-31 08:52:18.486873', '2021-12-31 08:52:18.486873', 487, '00487', 1),
('2021-12-31 08:52:18.536841', '2021-12-31 08:52:18.536841', 488, '00488', 1),
('2021-12-31 08:52:18.621541', '2021-12-31 08:52:18.621541', 489, '00489', 1),
('2021-12-31 08:52:18.688601', '2021-12-31 08:52:18.688601', 490, '00490', 1),
('2021-12-31 08:52:18.769582', '2021-12-31 08:52:18.769582', 491, '00491', 1),
('2021-12-31 08:52:18.814586', '2021-12-31 08:52:18.814586', 492, '00492', 1),
('2021-12-31 08:52:18.871554', '2021-12-31 08:52:18.871554', 493, '00493', 1),
('2021-12-31 08:52:18.969420', '2021-12-31 08:52:18.969420', 494, '00494', 1),
('2021-12-31 08:52:19.026407', '2021-12-31 08:52:19.026407', 495, '00495', 1),
('2021-12-31 08:52:19.085375', '2021-12-31 08:52:19.085375', 496, '00496', 1),
('2021-12-31 08:52:19.136337', '2021-12-31 08:52:19.136337', 497, '00497', 1),
('2021-12-31 08:52:19.191328', '2021-12-31 08:52:19.191328', 498, '00498', 1),
('2021-12-31 08:52:19.239301', '2021-12-31 08:52:19.239301', 499, '00499', 1),
('2021-12-31 08:52:19.291268', '2021-12-31 08:52:19.291268', 500, '00500', 1);

-- --------------------------------------------------------

--
-- Table structure for table `receipt_cancelled`
--

CREATE TABLE `receipt_cancelled` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `reasons` longtext NOT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `receipt_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `receipt_status`
--

CREATE TABLE `receipt_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `receipt_status`
--

INSERT INTO `receipt_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'UNUSED', '2021-12-07 18:59:48.081053', '2021-12-07 18:59:48.081053'),
(2, 'USED', '2021-12-07 18:59:48.169224', '2021-12-07 18:59:48.169224');

-- --------------------------------------------------------

--
-- Table structure for table `receipt_types`
--

CREATE TABLE `receipt_types` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `receipt_types`
--

INSERT INTO `receipt_types` (`id`, `title`, `created_at`, `updated_at`) VALUES
(3, 'NONE', '2021-12-07 19:26:40.526582', '2021-12-07 19:26:40.526582'),
(4, 'AUTO', '2021-12-07 19:26:40.604536', '2021-12-07 19:26:40.604536'),
(5, 'MANUAL', '2021-12-07 19:26:40.709471', '2021-12-07 19:26:40.709471');

-- --------------------------------------------------------

--
-- Table structure for table `salary_institution`
--

CREATE TABLE `salary_institution` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `salary_institution`
--

INSERT INTO `salary_institution` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'IPPIS', '2021-12-07 19:02:31.098964', '2021-12-07 19:02:31.098964'),
(2, 'GISMIS', '2021-12-07 19:02:31.161487', '2021-12-07 19:02:31.162498');

-- --------------------------------------------------------

--
-- Table structure for table `sales_category`
--

CREATE TABLE `sales_category` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sales_category`
--

INSERT INTO `sales_category` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'CASH', '2021-12-07 19:04:57.836401', '2021-12-07 19:04:57.836401'),
(2, 'CREDIT', '2021-12-07 19:04:57.892189', '2021-12-07 19:04:57.893188');

-- --------------------------------------------------------

--
-- Table structure for table `savings_uploaded`
--

CREATE TABLE `savings_uploaded` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `particulars` varchar(255) NOT NULL,
  `balance` decimal(20,2) NOT NULL,
  `schedule_amount` decimal(20,2) NOT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL,
  `transaction_id` int(11) NOT NULL,
  `transaction_period_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `savings_uploaded`
--

INSERT INTO `savings_uploaded` (`id`, `created_at`, `updated_at`, `particulars`, `balance`, `schedule_amount`, `processed_by_id`, `status_id`, `transaction_id`, `transaction_period_id`) VALUES
(1, '2021-12-07 23:26:42.713029', '2021-12-13 14:50:47.707128', 'Balance Brought Forward as at 12/08/2021', '120000.00', '2000.00', 9, 2, 351, 1),
(2, '2021-12-13 14:39:36.659258', '2021-12-13 14:50:48.474077', 'Balance Brought Forward as at 12/08/2021', '150000.00', '3000.00', 9, 2, 353, 1),
(4, '2021-12-13 15:04:44.014024', '2021-12-13 15:15:43.745496', 'Balance Brought Forward as at 12/08/2021', '250000.00', '10000.00', 9, 2, 352, 1),
(5, '2021-12-15 05:02:22.538515', '2021-12-15 05:02:26.635599', 'Balance Brought Forward as at 12/08/2021', '500000.00', '0.00', 9, 2, 355, 1),
(6, '2021-12-16 00:07:44.592605', '2021-12-16 00:07:47.274673', 'Balance Brought Forward as at 12/08/2021', '200000.00', '5000.00', 9, 2, 596, 1),
(7, '2021-12-16 12:52:41.789008', '2021-12-16 12:53:24.684742', 'Balance Brought Forward as at 12/08/2021', '200000.00', '20000.00', 9, 2, 358, 1),
(8, '2021-12-16 12:52:52.196286', '2021-12-16 12:53:25.021453', 'Balance Brought Forward as at 12/08/2021', '150000.00', '10000.00', 9, 2, 359, 1),
(9, '2021-12-16 12:53:04.806627', '2021-12-16 12:53:25.247087', 'Balance Brought Forward as at 12/08/2021', '200000.00', '30000.00', 9, 2, 360, 1),
(10, '2021-12-16 12:53:18.314030', '2021-12-16 12:53:25.399333', 'Balance Brought Forward as at 12/08/2021', '120000.00', '3000.00', 9, 2, 361, 1);

-- --------------------------------------------------------

--
-- Table structure for table `savings_upload_status`
--

CREATE TABLE `savings_upload_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `savings_upload_status`
--

INSERT INTO `savings_upload_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'PENDING', '2021-12-07 19:06:41.167400', '2021-12-07 19:06:41.167400'),
(2, 'UPLOADED', '2021-12-07 19:06:41.223493', '2021-12-07 19:06:41.223493'),
(3, 'VERIFIED', '2021-12-07 19:06:41.354815', '2021-12-07 19:06:41.354815');

-- --------------------------------------------------------

--
-- Table structure for table `shares_deduction_savings`
--

CREATE TABLE `shares_deduction_savings` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `savings_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `shares_deduction_savings`
--

INSERT INTO `shares_deduction_savings` (`id`, `created_at`, `updated_at`, `savings_id`) VALUES
(3, '2021-12-13 19:44:02.409529', '2021-12-13 19:44:02.409529', 3);

-- --------------------------------------------------------

--
-- Table structure for table `shares_sales_record`
--

CREATE TABLE `shares_sales_record` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `payment_reference` varchar(255) DEFAULT NULL,
  `receipt` varchar(255) NOT NULL,
  `shares` int(11) NOT NULL,
  `unit_cost` decimal(20,2) DEFAULT NULL,
  `share_amount` decimal(20,2) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `bank_account_id` int(11) DEFAULT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `shares_sales_record`
--

INSERT INTO `shares_sales_record` (`id`, `created_at`, `updated_at`, `payment_reference`, `receipt`, `shares`, `unit_cost`, `share_amount`, `image`, `member_id`, `bank_account_id`, `processed_by_id`, `status_id`) VALUES
(13, '2021-12-14 02:23:10.238936', '2021-12-14 02:23:10.238936', '78878787', '00022', 4, '10000.00', '40000.00', '/media/avatar3_q88tTQ9.png', 363, 1, 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `shares_units`
--

CREATE TABLE `shares_units` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `unit` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `shares_units`
--

INSERT INTO `shares_units` (`id`, `created_at`, `updated_at`, `unit`) VALUES
(1, '2021-12-07 19:07:13.871789', '2021-12-16 07:52:33.213904', 0),
(2, '2021-12-07 19:07:13.915932', '2021-12-16 07:52:33.268923', 1),
(3, '2021-12-07 19:07:14.043276', '2021-12-16 07:52:33.549239', 2),
(4, '2021-12-07 19:07:14.102836', '2021-12-16 07:52:33.610416', 3),
(5, '2021-12-07 19:07:14.175602', '2021-12-16 07:52:33.715500', 4),
(6, '2021-12-07 19:07:14.229941', '2021-12-16 07:52:33.815655', 5),
(7, '2021-12-07 19:07:14.288666', '2021-12-16 07:52:33.899602', 6),
(8, '2021-12-07 19:07:14.313833', '2021-12-16 07:52:34.007541', 7),
(9, '2021-12-07 19:07:14.346600', '2021-12-16 07:52:34.114054', 8),
(10, '2021-12-07 19:07:14.371718', '2021-12-16 07:52:34.205080', 9),
(11, '2021-12-07 19:07:14.406160', '2021-12-16 07:52:34.304424', 10),
(12, '2021-12-07 19:07:14.458128', '2021-12-16 07:52:34.471211', 11),
(13, '2021-12-07 19:07:14.478114', '2021-12-16 07:52:34.572988', 12),
(14, '2021-12-07 19:07:14.525087', '2021-12-16 07:52:34.663121', 13),
(15, '2021-12-07 19:07:14.545073', '2021-12-16 07:52:34.786187', 14),
(16, '2021-12-07 19:07:14.568060', '2021-12-16 07:52:34.850816', 15),
(17, '2021-12-07 19:07:14.600039', '2021-12-16 07:52:34.923008', 16),
(18, '2021-12-07 19:07:14.625027', '2021-12-16 07:52:34.994284', 17),
(19, '2021-12-07 19:07:14.645078', '2021-12-16 07:52:35.051927', 18),
(20, '2021-12-07 19:07:14.744665', '2021-12-16 07:52:35.122878', 19),
(21, '2021-12-07 19:07:14.991075', '2021-12-16 07:52:35.206829', 20),
(22, '2021-12-07 19:07:15.036284', '2021-12-16 07:52:35.268670', 21),
(23, '2021-12-07 19:07:15.058520', '2021-12-16 07:52:35.335020', 22),
(24, '2021-12-07 19:07:15.080539', '2021-12-16 07:52:35.400719', 23),
(25, '2021-12-07 19:07:15.100297', '2021-12-16 07:52:35.494533', 24),
(26, '2021-12-07 19:07:15.126615', '2021-12-16 07:52:35.543874', 25);

-- --------------------------------------------------------

--
-- Table structure for table `shares_upload_status`
--

CREATE TABLE `shares_upload_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `shares_upload_status`
--

INSERT INTO `shares_upload_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'PENDING', '2021-12-07 19:07:57.978734', '2021-12-07 19:07:57.978734'),
(2, 'UPLOADED', '2021-12-07 19:07:58.029706', '2021-12-07 19:07:58.029706'),
(3, 'VERIFIED', '2021-12-07 19:07:58.123769', '2021-12-07 19:07:58.123769');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `middle_name` varchar(50) NOT NULL,
  `address` longtext NOT NULL,
  `phone_number` varchar(50) NOT NULL,
  `admin_id` bigint(20) DEFAULT NULL,
  `gender_id` int(11) DEFAULT NULL,
  `title_id` int(11) DEFAULT NULL,
  `userlevel_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`id`, `created_at`, `updated_at`, `middle_name`, `address`, `phone_number`, `admin_id`, `gender_id`, `title_id`, `userlevel_id`) VALUES
(1, '2021-12-07 19:42:36.634035', '2021-12-07 19:42:36.777968', 'E', 'FETHA', '08087777765', 2, 1, 5, 1),
(2, '2021-12-07 19:43:34.730268', '2021-12-07 19:43:34.830204', 'K', 'FETHA', '54545455454', 3, 1, 7, 1),
(3, '2021-12-07 19:44:25.371651', '2021-12-07 19:44:25.434430', 'O.', 'FETHA', '08064004351', 4, 1, 1, 1),
(4, '2021-12-07 19:45:10.832172', '2021-12-07 19:45:10.944819', 'Ifeanyi', 'FETHA', '01187888888', 5, 1, 1, 1),
(5, '2021-12-07 19:46:16.596302', '2021-12-07 19:46:16.698061', 'Nweke', 'FETHA', '78878767667', 6, 2, 2, 1),
(6, '2021-12-07 19:47:20.736030', '2021-12-07 19:47:20.816816', '', 'FETHA', '08097765655', 7, 1, 1, 1),
(7, '2021-12-07 19:48:22.816645', '2021-12-07 19:48:22.896215', 'Ama', 'FETHA', '87787778787', 8, 2, 2, 1),
(8, '2021-12-07 19:49:28.680440', '2021-12-07 19:49:28.788206', '', 'FETHA', '98887878787', 9, 2, 3, 1),
(9, '2021-12-07 19:50:04.459500', '2021-12-07 19:50:04.686369', '', 'FETHA', '09098877666', 10, 2, 2, 1),
(10, '2021-12-07 19:50:50.967827', '2021-12-31 07:25:03.195958', 'Emmanuella', 'FETHA', '08989898778', 11, 2, 2, 1),
(11, '2021-12-07 19:51:52.608219', '2022-01-11 21:22:08.456116', '', 'FETHA', '08988777776', 12, 2, 2, 2),
(12, '2021-12-07 19:52:49.111042', '2021-12-07 19:52:49.195080', '', 'FETHA', '09090988889', 13, 2, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `standing_order_accounts`
--

CREATE TABLE `standing_order_accounts` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `lock_status_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL,
  `transaction_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `standing_order_accounts`
--

INSERT INTO `standing_order_accounts` (`id`, `created_at`, `updated_at`, `amount`, `lock_status_id`, `status_id`, `transaction_id`) VALUES
(10, '2021-12-13 14:50:47.596235', '2021-12-31 07:35:42.077189', '15000.00', 2, 1, 351),
(11, '2021-12-13 14:50:47.788508', '2021-12-16 00:32:33.476748', '5000.00', 2, 1, 353),
(14, '2021-12-13 15:15:43.532755', '2021-12-16 00:32:36.438862', '15000.00', 2, 1, 352),
(16, '2021-12-14 02:27:14.434798', '2021-12-14 02:27:14.434798', '2000.00', 2, 1, 386),
(17, '2021-12-14 02:27:20.347810', '2021-12-14 02:27:20.347810', '3000.00', 2, 1, 387),
(18, '2021-12-14 02:27:27.535360', '2021-12-14 02:27:27.535360', '2000.00', 2, 1, 388),
(20, '2021-12-16 00:07:46.908263', '2021-12-16 00:32:40.119743', '10000.00', 2, 1, 596),
(21, '2021-12-16 12:53:24.530828', '2021-12-16 12:53:24.530828', '20000.00', 2, 1, 358),
(22, '2021-12-16 12:53:24.749275', '2021-12-16 12:53:24.749275', '10000.00', 2, 1, 359),
(23, '2021-12-16 12:53:25.136655', '2021-12-16 12:53:25.136655', '30000.00', 2, 1, 360),
(24, '2021-12-16 12:53:25.305048', '2021-12-16 12:53:25.305048', '3000.00', 2, 1, 361),
(27, '2022-01-10 17:19:34.816448', '2022-01-10 17:19:34.816448', '10000.00', 2, 1, 372),
(28, '2022-01-10 18:45:48.499842', '2022-01-10 18:45:48.499842', '8000.00', 2, 1, 379);

-- --------------------------------------------------------

--
-- Table structure for table `states`
--

CREATE TABLE `states` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `states`
--

INSERT INTO `states` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'Abia', '2021-12-07 18:56:55.768323', '2021-12-07 18:56:55.768323'),
(2, 'Adamawa', '2021-12-07 18:56:55.831255', '2021-12-07 18:56:55.831255'),
(3, 'Akwa Ibom', '2021-12-07 18:56:55.974986', '2021-12-07 18:56:55.974986'),
(4, 'Anambra', '2021-12-07 18:56:56.020920', '2021-12-07 18:56:56.020920'),
(5, 'Bauchi', '2021-12-07 18:56:56.065125', '2021-12-07 18:56:56.065125'),
(6, 'Bayelsa', '2021-12-07 18:56:56.110101', '2021-12-07 18:56:56.110101'),
(7, 'Benue', '2021-12-07 18:56:56.154067', '2021-12-07 18:56:56.154067'),
(8, 'Borno', '2021-12-07 18:56:56.203037', '2021-12-07 18:56:56.203037'),
(9, 'Cross River', '2021-12-07 18:56:56.221027', '2021-12-07 18:56:56.221027'),
(10, 'Delta', '2021-12-07 18:56:56.364690', '2021-12-07 18:56:56.364690'),
(11, 'Ebonyi', '2021-12-07 18:56:56.387677', '2021-12-07 18:56:56.387677'),
(12, 'Edo', '2021-12-07 18:56:56.411727', '2021-12-07 18:56:56.411727'),
(13, 'Ekiti', '2021-12-07 18:56:56.431909', '2021-12-07 18:56:56.431909'),
(14, 'Enugu', '2021-12-07 18:56:56.453363', '2021-12-07 18:56:56.454362'),
(15, 'Gombe', '2021-12-07 18:56:56.478988', '2021-12-07 18:56:56.478988'),
(16, 'Imo', '2021-12-07 18:56:56.502025', '2021-12-07 18:56:56.502025'),
(17, 'Jigawa', '2021-12-07 18:56:56.656861', '2021-12-07 18:56:56.656861'),
(18, 'Kaduna', '2021-12-07 18:56:56.679470', '2021-12-07 18:56:56.679470'),
(19, 'Kano', '2021-12-07 18:56:56.709657', '2021-12-07 18:56:56.710658'),
(20, 'Katsina', '2021-12-07 18:56:56.754782', '2021-12-07 18:56:56.754782'),
(21, 'Kebbi', '2021-12-07 18:56:56.787614', '2021-12-07 18:56:56.787614'),
(22, 'Kogi', '2021-12-07 18:56:56.837387', '2021-12-07 18:56:56.837387'),
(23, 'Kwara', '2021-12-07 18:56:56.868977', '2021-12-07 18:56:56.868977'),
(24, 'Lagos', '2021-12-07 18:56:56.887128', '2021-12-07 18:56:56.888128'),
(25, 'Nasarawa', '2021-12-07 18:56:56.944939', '2021-12-07 18:56:56.945938'),
(26, 'Niger', '2021-12-07 18:56:56.994620', '2021-12-07 18:56:56.994620'),
(27, 'Ogun', '2021-12-07 18:56:57.036660', '2021-12-07 18:56:57.036660'),
(28, 'Ondo', '2021-12-07 18:56:57.106952', '2021-12-07 18:56:57.106952'),
(29, 'Osun', '2021-12-07 18:56:57.145254', '2021-12-07 18:56:57.145254'),
(30, 'Oyo', '2021-12-07 18:56:57.206848', '2021-12-07 18:56:57.206848'),
(31, 'Plateau', '2021-12-07 18:56:57.246946', '2021-12-07 18:56:57.246946'),
(32, 'Rivers', '2021-12-07 18:56:57.297915', '2021-12-07 18:56:57.297915'),
(33, 'Sokoto', '2021-12-07 18:56:57.454856', '2021-12-07 18:56:57.454856'),
(34, 'Taraba', '2021-12-07 18:56:57.488521', '2021-12-07 18:56:57.488521'),
(35, 'Yobe', '2021-12-07 18:56:57.548505', '2021-12-07 18:56:57.548505'),
(36, 'Zamfara', '2021-12-07 18:56:57.727975', '2021-12-07 18:56:57.727975'),
(37, 'FCT', '2021-12-07 18:56:57.797199', '2021-12-07 18:56:57.798187');

-- --------------------------------------------------------

--
-- Table structure for table `stock`
--

CREATE TABLE `stock` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `code` varchar(255) NOT NULL,
  `item_name` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `unit_selling_price` decimal(20,2) NOT NULL,
  `re_order_level` int(11) NOT NULL,
  `no_in_pack` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `details` varchar(255) DEFAULT NULL,
  `lock_status_id` int(11) NOT NULL,
  `unit_cost_price` decimal(20,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stock`
--

INSERT INTO `stock` (`id`, `created_at`, `updated_at`, `code`, `item_name`, `quantity`, `unit_selling_price`, `re_order_level`, `no_in_pack`, `category_id`, `details`, `lock_status_id`, `unit_cost_price`) VALUES
(917, '2021-12-23 02:18:43.603848', '2022-01-17 03:53:25.135171', '00001', 'BOURNVITA 900G', 435, '2300.00', 2, 6, 57, 'TIN', 2, '0.00'),
(918, '2021-12-23 02:18:43.664589', '2022-01-17 04:03:22.855914', '00002', 'BOURNVITA 500G', 395, '1200.00', 6, 12, 57, 'SACHET', 2, '0.00'),
(919, '2021-12-23 02:18:43.808194', '2021-12-23 02:18:43.808194', '00003', 'OVALTINE 900G', 0, '2650.00', 2, 6, 70, 'TIN', 2, '0.00'),
(920, '2021-12-23 02:18:43.847290', '2021-12-23 02:18:43.847290', '00004', 'OVALTINE 400G', 0, '1500.00', 4, 12, 70, 'TIN', 2, '0.00'),
(921, '2021-12-23 02:18:43.897825', '2021-12-23 02:18:43.897825', '00005', 'OVALTINE 400G', 0, '1200.00', 4, 12, 70, 'SACHET', 2, '0.00'),
(922, '2021-12-23 02:18:43.957847', '2022-01-16 15:43:29.662921', '00006', 'COMPLAIN MILK', 60, '3500.00', 4, 12, 58, 'SACHET', 2, '0.00'),
(923, '2021-12-23 02:18:44.009113', '2021-12-23 02:18:44.009113', '00007', 'COWBELL MILK 900G', 0, '2050.00', 2, 6, 58, 'SACHET', 2, '0.00'),
(924, '2021-12-23 02:18:44.065610', '2022-01-17 04:03:22.646972', '00008', 'COWBELL MILK 380G', 15, '950.00', 4, 12, 58, 'SACHET', 2, '0.00'),
(925, '2021-12-23 02:18:44.132338', '2021-12-23 02:18:44.132338', '00009', 'MILKSI MILK 380G', 0, '950.00', 4, 12, 68, 'SACHET', 2, '0.00'),
(926, '2021-12-23 02:18:44.168883', '2021-12-23 02:18:44.168883', '00010', 'COWBELL CHOCOLATE', 0, '950.00', 4, 12, 58, 'SACHET', 2, '0.00'),
(927, '2021-12-23 02:18:44.224848', '2021-12-23 02:18:44.224848', '00011', '3CROWN MILK', 0, '900.00', 4, 12, 58, 'SACHET', 2, '0.00'),
(928, '2021-12-23 02:18:44.469694', '2021-12-23 02:18:44.469694', '00012', 'MILO 1KG', 0, '2650.00', 2, 6, 68, 'TIN', 2, '0.00'),
(929, '2021-12-23 02:18:44.536665', '2021-12-23 02:18:44.536665', '00013', 'MILO 500G', 0, '1850.00', 4, 12, 68, 'TIN', 2, '0.00'),
(930, '2021-12-23 02:18:44.591618', '2021-12-23 02:18:44.591618', '00014', 'MILO 1KG', 0, '2100.00', 2, 6, 68, 'SACHET', 2, '0.00'),
(931, '2021-12-23 02:18:44.791248', '2021-12-23 02:18:44.791248', '00015', 'MILO 500G', 0, '1200.00', 4, 12, 68, 'SACHET ', 2, '0.00'),
(932, '2021-12-23 02:18:44.847383', '2021-12-23 02:18:44.847383', '00016', 'NAN 1 400G', 0, '2700.00', 4, 12, 69, 'TIN', 2, '0.00'),
(933, '2021-12-23 02:18:44.904026', '2021-12-23 02:18:44.904026', '00017', 'NAN 2 400G', 0, '2700.00', 4, 12, 69, 'TIN', 2, '0.00'),
(934, '2021-12-23 02:18:44.970989', '2021-12-23 02:18:44.970989', '00018', 'LACTOGEN 1 400G', 0, '1800.00', 4, 12, 67, 'TIN', 2, '0.00'),
(935, '2021-12-23 02:18:45.035717', '2022-01-16 15:01:29.830550', '00019', 'CERELAC 1KG', 34, '2700.00', 2, 6, 58, 'TIN', 2, '0.00'),
(936, '2021-12-23 02:18:45.102990', '2022-01-16 15:43:30.221553', '00020', 'GOLDEN MORN 1KG', 50, '1450.00', 4, 6, 62, 'SACHET', 2, '0.00'),
(937, '2021-12-23 02:18:45.158039', '2021-12-23 02:18:45.158039', '00021', 'GOLDEN MORN 500G', 0, '850.00', 4, 12, 62, 'SACHET', 2, '0.00'),
(938, '2021-12-23 02:18:45.214117', '2021-12-23 02:18:45.214117', '00022', 'PEAK MILK 400G', 0, '1900.00', 4, 12, 71, 'TIN', 2, '0.00'),
(939, '2021-12-23 02:18:45.269060', '2021-12-23 02:18:45.269060', '00023', 'PEAK MILK 400G', 0, '1400.00', 4, 12, 71, 'SACHET', 2, '0.00'),
(940, '2021-12-23 02:18:45.338393', '2021-12-23 02:18:45.338393', '00024', 'PEAK MILK 800G', 0, '3200.00', 2, 6, 71, 'SACHET', 2, '0.00'),
(941, '2021-12-23 02:18:45.396617', '2021-12-23 02:18:45.396617', '00025', 'KERRY GOLD FILLED 400G', 0, '2000.00', 4, 12, 66, 'SACHET', 2, '0.00'),
(942, '2021-12-23 02:18:45.449526', '2021-12-23 02:18:45.449526', '00026', 'KERRY GOLD FILLED 900G', 0, '1000.00', 4, 12, 66, 'SACHET', 2, '0.00'),
(943, '2021-12-23 02:18:45.504518', '2021-12-23 02:18:45.504518', '00027', 'NASCO CORNFLASK 350G', 0, '1000.00', 2, 10, 69, 'NASCO CORNFLASK 350G', 2, '0.00'),
(944, '2021-12-23 02:18:45.562714', '2021-12-23 02:18:45.562714', '00028', 'PEAK 123 400G', 0, '1400.00', 4, 12, 71, 'SACHET', 2, '0.00'),
(945, '2021-12-23 02:18:45.625692', '2021-12-23 02:18:45.626694', '00029', 'DANO COOL COW 360G', 0, '2150.00', 4, 12, 59, 'SACHET', 2, '0.00'),
(946, '2021-12-23 02:18:45.683731', '2022-01-16 15:01:30.253707', '00030', 'YALE CABIN', 50, '350.00', 4, 12, 80, 'YALE CABIN', 2, '0.00'),
(947, '2021-12-23 02:18:45.835826', '2021-12-23 02:18:45.835826', '00031', 'DANO COOL COW 800G', 0, '950.00', 4, 12, 59, 'SACHET', 2, '0.00'),
(948, '2021-12-23 02:18:45.964859', '2021-12-23 02:18:45.964859', '00032', 'OXFORD CABIN', 0, '350.00', 4, 12, 70, 'OXFORD CABIN', 2, '0.00'),
(949, '2021-12-23 02:18:46.044015', '2021-12-23 02:18:46.044015', '00033', 'DANO SLIM 400G', 0, '1500.00', 4, 12, 59, 'SACHET', 2, '0.00'),
(950, '2021-12-23 02:18:46.115505', '2021-12-23 02:18:46.115505', '00034', 'YALE BREAD', 0, '150.00', 4, 10, 80, 'YALE BREAD', 2, '0.00'),
(951, '2021-12-23 02:18:46.166771', '2021-12-23 02:18:46.166771', '00035', 'DANO FULL CREAM 400G', 0, '1450.00', 4, 12, 59, 'SACHET', 2, '0.00'),
(952, '2021-12-23 02:18:46.202555', '2021-12-23 02:18:46.202555', '00036', 'PEAK FILLED LIQUID MILK', 0, '270.00', 6, 24, 71, 'TIN', 2, '0.00'),
(953, '2021-12-23 02:18:46.258734', '2021-12-23 02:18:46.258734', '00037', 'COAST LIQUID MILK', 0, '250.00', 6, 24, 58, 'TIN', 2, '0.00'),
(954, '2021-12-23 02:18:46.309460', '2021-12-23 02:18:46.309460', '00038', 'DANO FULL CREAM 800G', 0, '2850.00', 4, 12, 59, 'SACHET', 2, '0.00'),
(955, '2021-12-23 02:18:46.348666', '2022-01-17 04:03:23.201405', '00039', 'LOYA MILK 900G', 20, '2700.00', 4, 6, 67, 'SACHET', 2, '0.00'),
(956, '2021-12-23 02:18:46.424489', '2021-12-23 02:18:46.424489', '00040', 'PEAK FULL CREAM LIQULD MILK', 0, '320.00', 6, 24, 71, 'TIN', 2, '0.00'),
(957, '2021-12-23 02:18:46.481226', '2021-12-23 02:18:46.481226', '00041', '3CROWN MILK LIQUID', 0, '280.00', 6, 24, 58, 'TIN', 2, '0.00'),
(958, '2021-12-23 02:18:46.536287', '2021-12-23 02:18:46.536287', '00042', 'LOYA MILK 380G', 0, '1200.00', 4, 12, 67, 'SACHET', 2, '0.00'),
(959, '2021-12-23 02:18:46.592128', '2021-12-23 02:18:46.592128', '00043', 'FAMILY CUSTARD', 0, '3200.00', 2, 4, 61, 'FAMILY CUSTARD', 2, '0.00'),
(960, '2021-12-23 02:18:46.647161', '2021-12-23 02:18:46.647161', '00044', 'LIPTON', 0, '300.00', 6, 20, 67, 'LIPTON', 2, '0.00'),
(961, '2021-12-23 02:18:46.708053', '2021-12-23 02:18:46.708053', '00045', 'INFINITY CORNFLASK 1KG', 0, '2100.00', 2, 6, 64, 'INFINITY CORNFLASK 1KG', 2, '0.00'),
(962, '2021-12-23 02:18:46.760697', '2021-12-23 02:18:46.760697', '00046', 'INFINITY CORNFLASK 500G', 0, '1200.00', 2, 8, 64, 'INFINITY CORNFLASK 500G', 2, '0.00'),
(963, '2021-12-23 02:18:46.848976', '2021-12-23 02:18:46.848976', '00047', 'TOP TEA', 0, '320.00', 4, 10, 75, 'TOP TEA', 2, '0.00'),
(964, '2021-12-23 02:18:47.158484', '2021-12-23 02:18:47.159483', '00048', 'SOYA PLUS', 0, '1050.00', 2, 6, 74, 'TIN', 2, '0.00'),
(965, '2021-12-23 02:18:47.209456', '2021-12-23 02:18:47.209456', '00049', 'SOYA PLUS', 0, '500.00', 2, 6, 74, 'SACHET', 2, '0.00'),
(966, '2021-12-23 02:18:47.247245', '2022-01-16 15:01:30.391566', '00050', 'PURE COCOA', 20, '1050.00', 2, 6, 71, 'TIN', 2, '0.00'),
(967, '2021-12-23 02:18:47.292542', '2021-12-23 02:18:47.292542', '00051', 'PURE COCOA', 0, '850.00', 5, 12, 71, 'SACHET', 2, '0.00'),
(968, '2021-12-23 02:18:47.359844', '2021-12-23 02:18:47.359844', '00052', 'MY BOY MILK', 0, '2000.00', 4, 12, 68, 'TIN', 2, '0.00'),
(969, '2021-12-23 02:18:47.451257', '2021-12-23 02:18:47.451257', '00053', 'DORGAN SUGAR', 0, '400.00', 10, 50, 59, 'DORGAN SUGAR', 2, '0.00'),
(970, '2021-12-23 02:18:47.505839', '2021-12-23 02:18:47.505839', '00054', 'GOLDEN PENNY SUGAR', 0, '450.00', 10, 50, 62, 'GOLDEN PENNY SUGAR', 2, '0.00'),
(971, '2021-12-23 02:18:47.564995', '2022-01-17 04:03:22.990704', '00055', 'ANGEL WIPES', 130, '700.00', 10, 24, 56, 'ANGEL WIPES', 2, '0.00'),
(972, '2021-12-23 02:18:47.623792', '2021-12-23 02:18:47.623792', '00056', 'MARIO N JULIET WIPES', 0, '650.00', 5, 12, 68, 'MARIO N JULIET WIPES', 2, '0.00'),
(973, '2021-12-23 02:18:47.687460', '2021-12-23 02:18:47.687460', '00057', 'MOLFIX DIAPER 2', 0, '2400.00', 2, 4, 68, 'ECO', 2, '0.00'),
(974, '2021-12-23 02:18:47.726103', '2021-12-23 02:18:47.727104', '00058', 'MOLFIX DIAPER 3', 0, '2400.00', 2, 4, 68, 'ECO', 2, '0.00'),
(975, '2021-12-23 02:18:47.779357', '2021-12-23 02:18:47.780357', '00059', 'MOFLIX DIAPER 2', 0, '5100.00', 1, 3, 68, 'JUMBO', 2, '0.00'),
(976, '2021-12-23 02:18:47.816405', '2021-12-23 02:18:47.816405', '00060', 'MOLFIX DIAPER 3', 0, '5100.00', 1, 3, 68, 'JUMBO', 2, '0.00'),
(977, '2021-12-23 02:18:47.911740', '2021-12-23 02:18:47.911740', '00061', 'MOLFIX DIAPER 4', 0, '5100.00', 1, 3, 68, 'JUMBO', 2, '0.00'),
(978, '2021-12-23 02:18:47.966697', '2021-12-23 02:18:47.967694', '00062', 'KISS KID DIAPER', 0, '5300.00', 1, 3, 66, 'JUMBO', 2, '0.00'),
(979, '2021-12-23 02:18:48.037444', '2021-12-23 02:18:48.037444', '00063', 'VIRONY DIAPER MED', 0, '5400.00', 1, 3, 77, 'JUMBO', 2, '0.00'),
(980, '2021-12-23 02:18:48.150903', '2021-12-23 02:18:48.150903', '00064', 'BEBEM DIAPER', 0, '2400.00', 1, 4, 57, 'ECO', 2, '0.00'),
(981, '2021-12-23 02:18:48.241844', '2021-12-23 02:18:48.241844', '00065', 'SOFTRUX ADULT DIAPER', 0, '2200.00', 4, 12, 74, 'SOFTRUX ADULT DIAPER', 2, '0.00'),
(982, '2021-12-23 02:18:48.358564', '2021-12-23 02:18:48.358564', '00066', 'SOFTWAVE TISSUE', 0, '200.00', 6, 12, 74, 'JUMBO', 2, '0.00'),
(983, '2021-12-23 02:18:48.425281', '2021-12-23 02:18:48.425281', '00067', 'SMART TISSUE', 0, '200.00', 6, 12, 74, 'JUMBO', 2, '0.00'),
(984, '2021-12-23 02:18:48.481336', '2021-12-23 02:18:48.481336', '00068', 'ROSE CARLA TISSUE', 0, '1200.00', 12, 8, 73, 'SMALL', 2, '0.00'),
(985, '2021-12-23 02:18:48.532055', '2021-12-23 02:18:48.532055', '00069', 'FAMILIA TISSUE', 0, '500.00', 10, 8, 61, 'FAMILIA TISSUE', 2, '0.00'),
(986, '2021-12-23 02:18:48.581344', '2022-01-11 04:13:47.144197', '00070', 'ARDEN CARROT SOAP', 127, '2100.00', 6, 12, 56, 'ARDEN CARROT SOAP', 2, '0.00'),
(987, '2021-12-23 02:18:48.638016', '2021-12-23 02:18:48.638016', '00071', 'ROSE PLUS TISSUE', 0, '80.00', 12, 48, 73, 'SMALL', 2, '0.00'),
(988, '2021-12-23 02:18:48.692263', '2021-12-23 02:18:48.692263', '00072', 'SOFTWAVE TISSUE', 0, '60.00', 12, 48, 74, 'SMALL', 2, '0.00'),
(989, '2021-12-23 02:18:48.758637', '2021-12-23 02:18:48.758637', '00073', 'MAMA CARE PAD', 0, '500.00', 6, 12, 68, 'MAMA CARE PAD', 2, '0.00'),
(990, '2021-12-23 02:18:48.832257', '2021-12-23 02:18:48.832257', '00074', 'RIGHTGUARD SPRAY', 0, '1250.00', 2, 6, 73, 'RIGHTGUARD SPRAY', 2, '0.00'),
(991, '2021-12-23 02:18:48.905333', '2021-12-23 02:18:48.905333', '00075', 'RIGHTGUARD SPRAY', 0, '1250.00', 2, 6, 73, 'RIGHTGUARD SPRAY', 2, '0.00'),
(992, '2021-12-23 02:18:49.009096', '2021-12-23 02:18:49.009096', '00076', 'RIGHTGUARD SPRAY', 0, '1250.00', 2, 6, 73, 'RIGHTGUARD SPRAY', 2, '0.00'),
(993, '2021-12-23 02:18:49.110466', '2021-12-23 02:18:49.110466', '00077', 'LEADER SPRAY', 0, '800.00', 2, 6, 67, 'LEADER SPRAY', 2, '0.00'),
(994, '2021-12-23 02:18:49.210316', '2021-12-23 02:18:49.211312', '00078', 'GIVE N TAKE SPRAY', 0, '800.00', 2, 6, 62, 'GIVE N TAKE SPRAY', 2, '0.00'),
(995, '2021-12-23 02:18:49.248605', '2021-12-23 02:18:49.248605', '00079', 'RAWAYA SPRAY', 0, '850.00', 2, 6, 73, 'RAWAYA SPRAY', 2, '0.00'),
(996, '2021-12-23 02:18:49.470938', '2021-12-23 02:18:49.470938', '00080', 'EHSAAS SPRAY', 0, '850.00', 2, 6, 60, 'EHSAAS SPRAY', 2, '0.00'),
(997, '2021-12-23 02:18:49.636568', '2021-12-23 02:18:49.636568', '00081', 'POWER BLACK SPRAY', 0, '850.00', 2, 6, 71, 'POWER BLACK SPRAY', 2, '0.00'),
(998, '2021-12-23 02:18:49.691773', '2021-12-23 02:18:49.691773', '00082', 'ESKODA SPRAY', 0, '900.00', 2, 6, 60, 'ESKODA SPRAY', 2, '0.00'),
(999, '2021-12-23 02:18:49.744347', '2021-12-23 02:18:49.744347', '00083', 'EXPLORE SPRAY', 0, '900.00', 2, 6, 60, 'EXPLORE SPRAY', 2, '0.00'),
(1000, '2021-12-23 02:18:49.813848', '2021-12-23 02:18:49.813848', '00084', 'DRIVE SPRAY', 0, '950.00', 2, 6, 59, 'DRIVE SPRAY', 2, '0.00'),
(1001, '2021-12-23 02:18:49.869967', '2021-12-23 02:18:49.869967', '00085', 'SOILLNG DISH SOAP', 0, '500.00', 2, 12, 74, 'SOILLNG DISH SOAP', 2, '0.00'),
(1002, '2021-12-23 02:18:49.940604', '2021-12-23 02:18:49.940604', '00086', 'EAR BUD ', 0, '200.00', 2, 12, 60, 'EAR BUD ', 2, '0.00'),
(1003, '2021-12-23 02:18:49.981632', '2021-12-23 02:18:49.982630', '00087', 'TOOTH PICK', 0, '50.00', 6, 12, 75, 'TOOTH PICK', 2, '0.00'),
(1004, '2021-12-23 02:18:50.062130', '2021-12-23 02:18:50.062130', '00088', 'SOULMATE RELAXER', 0, '250.00', 6, 24, 74, 'SMALL', 2, '0.00'),
(1005, '2021-12-23 02:18:50.159395', '2021-12-23 02:18:50.159395', '00089', 'DETTOL ANTISEPTIC', 0, '400.00', 6, 48, 59, '75ML', 2, '0.00'),
(1006, '2021-12-23 02:18:50.204530', '2021-12-23 02:18:50.204530', '00090', 'DETTOL ANTISEPTIC', 0, '700.00', 6, 36, 59, '165ML', 2, '0.00'),
(1007, '2021-12-23 02:18:50.270598', '2021-12-23 02:18:50.270598', '00091', 'DETTOL ANTISEPTIC', 0, '1000.00', 6, 18, 59, '250ML', 2, '0.00'),
(1008, '2021-12-23 02:18:50.448041', '2021-12-23 02:18:50.448041', '00092', 'GOOD KNIGNT INSECTIDE', 0, '900.00', 2, 6, 62, 'GOOD KNIGNT INSECTIDE', 2, '0.00'),
(1009, '2021-12-23 02:18:50.580534', '2021-12-23 02:18:50.580534', '00093', 'MORNING FRESH', 0, '350.00', 10, 24, 68, 'SMALL', 2, '0.00'),
(1010, '2021-12-23 02:18:50.691462', '2021-12-23 02:18:50.691462', '00094', 'MORNING FRESH', 0, '650.00', 10, 18, 68, 'MED', 2, '0.00'),
(1011, '2021-12-23 02:18:50.759267', '2021-12-23 02:18:50.759267', '00095', 'MORNING FRESH', 0, '850.00', 2, 12, 68, 'BIG', 2, '0.00'),
(1012, '2021-12-23 02:18:50.825164', '2021-12-23 02:18:50.825164', '00096', 'MOLFIX DIAPER 2', 0, '650.00', 2, 10, 68, 'SMALL', 2, '0.00'),
(1013, '2021-12-23 02:18:50.891780', '2021-12-23 02:18:50.892779', '00097', 'MOLFIX DIAPER 3', 0, '650.00', 2, 10, 68, 'SMALL', 2, '0.00'),
(1014, '2021-12-23 02:18:50.947594', '2021-12-23 02:18:50.947594', '00098', 'MOLFIX DIAPER 1', 0, '650.00', 2, 10, 68, 'SMALL', 2, '0.00'),
(1015, '2021-12-23 02:18:51.003731', '2021-12-23 02:18:51.003731', '00099', 'MOLFIX  PANT DIAPER 3', 0, '700.00', 2, 10, 68, 'SMALL', 2, '0.00'),
(1016, '2021-12-23 02:18:51.055695', '2021-12-23 02:18:51.055695', '00100', 'KLIN DETERGENT', 0, '800.00', 2, 6, 66, '900G', 2, '0.00'),
(1017, '2021-12-23 02:18:51.147260', '2022-01-11 04:08:47.385451', '00101', 'ARIEL DETERGENT', 72, '1800.00', 2, 4, 56, '2KG', 2, '0.00'),
(1018, '2021-12-23 02:18:51.184369', '2021-12-23 02:18:51.184369', '00102', 'WAW DETERGENT', 0, '850.00', 2, 7, 78, '800G', 2, '0.00'),
(1019, '2021-12-23 02:18:51.236504', '2021-12-23 02:18:51.236504', '00103', 'WAW DETERGENT', 0, '150.00', 12, 26, 78, '190G', 2, '0.00'),
(1020, '2021-12-23 02:18:51.299157', '2021-12-23 02:18:51.299157', '00104', 'NITTOL DETERGENT', 0, '750.00', 2, 6, 69, '800G', 2, '0.00'),
(1021, '2021-12-23 02:18:51.369888', '2021-12-23 02:18:51.370891', '00105', 'NITTOL DETERGENT', 0, '150.00', 10, 24, 69, '180G', 2, '0.00'),
(1022, '2021-12-23 02:18:51.437176', '2021-12-23 02:18:51.437176', '00106', 'SO FINE HAIR CREAM', 0, '370.00', 5, 24, 74, 'SMALL', 2, '0.00'),
(1023, '2021-12-23 02:18:51.503285', '2021-12-23 02:18:51.503285', '00107', 'SOULMATE HAIR CREAM', 0, '350.00', 5, 24, 74, 'SMALL', 2, '0.00'),
(1024, '2021-12-23 02:18:51.562407', '2022-01-11 03:58:29.276907', '00108', 'APPLE JELLY', 242, '150.00', 5, 12, 56, 'SMALL', 2, '0.00'),
(1025, '2021-12-23 02:18:51.652411', '2021-12-23 02:18:51.652411', '00109', 'APPLE JELLY BIG', 0, '250.00', 2, 6, 56, 'MED', 2, '0.00'),
(1026, '2021-12-23 02:18:51.742360', '2021-12-23 02:18:51.742360', '00110', 'BLUESEAL VASELINE(BIG)', 0, '900.00', 2, 6, 57, 'BLUESEAL VASELINE(BIG)', 2, '0.00'),
(1027, '2021-12-23 02:18:51.816413', '2021-12-23 02:18:51.816413', '00111', 'BLUESEAL VASELINE(SMALL)', 0, '350.00', 5, 12, 57, 'BLUESEAL VASELINE(SMALL)', 2, '0.00'),
(1028, '2021-12-23 02:18:51.870380', '2021-12-23 02:18:51.870380', '00112', 'FAMILIAR CREAM', 0, '800.00', 2, 6, 61, 'FAMILIAR CREAM', 2, '0.00'),
(1029, '2021-12-23 02:18:51.925344', '2021-12-23 02:18:51.925344', '00113', 'FAMILIAR LOTION', 0, '750.00', 5, 12, 61, 'FAMILIAR LOTION', 2, '0.00'),
(1030, '2021-12-23 02:18:51.977314', '2021-12-23 02:18:51.977314', '00114', 'FAMILIAR JELLY', 0, '800.00', 2, 6, 61, 'FAMILIAR JELLY', 2, '0.00'),
(1031, '2021-12-23 02:18:52.034425', '2021-12-23 02:18:52.034425', '00115', 'VISITA PLUS TUBE', 0, '300.00', 5, 12, 77, 'VISITA PLUS TUBE', 2, '0.00'),
(1032, '2021-12-23 02:18:52.070888', '2021-12-23 02:18:52.070888', '00116', 'BOUGUET POWDER', 0, '600.00', 3, 6, 57, 'BOUGUET POWDER', 2, '0.00'),
(1033, '2021-12-23 02:18:52.125588', '2021-12-23 02:18:52.125588', '00117', 'LEVINA POWDER', 0, '600.00', 3, 6, 67, ' LEVINA POWDER', 2, '0.00'),
(1034, '2021-12-23 02:18:52.235239', '2021-12-23 02:18:52.235239', '00118', 'ENCHANTEAUR POWDER', 0, '600.00', 3, 6, 60, 'ENCHANTEAUR POWDER', 2, '0.00'),
(1035, '2021-12-23 02:18:52.288215', '2021-12-23 02:18:52.288215', '00119', 'PURE SKIN LOTION', 0, '1000.00', 3, 6, 71, 'PURE SKIN LOTION', 2, '0.00'),
(1036, '2021-12-23 02:18:52.324702', '2021-12-23 02:18:52.325705', '00120', 'NIVEA MEN LOTION', 0, '1700.00', 5, 12, 69, 'NIVEA MEN LOTION', 2, '0.00'),
(1037, '2021-12-23 02:18:52.381202', '2021-12-23 02:18:52.381202', '00121', 'DOVE CREAM', 0, '900.00', 3, 6, 59, 'DOVE CREAM', 2, '0.00'),
(1038, '2021-12-23 02:18:52.440558', '2021-12-23 02:18:52.440558', '00122', 'MISS CHERI LOTION', 0, '550.00', 5, 12, 68, 'MISS CHERI LOTION', 2, '0.00'),
(1039, '2021-12-23 02:18:52.494681', '2021-12-23 02:18:52.495677', '00123', 'VASELINE LOTION', 0, '900.00', 5, 12, 77, 'VASELINE LOTION', 2, '0.00'),
(1040, '2021-12-23 02:18:52.550357', '2021-12-23 02:18:52.550357', '00124', 'BABY N ME POWDER', 0, '500.00', 3, 6, 57, 'BABY N ME POWDER', 2, '0.00'),
(1041, '2021-12-23 02:18:52.609615', '2021-12-23 02:18:52.609615', '00125', 'PASSION POWDER', 0, '700.00', 3, 6, 71, 'PASSION POWDER', 2, '0.00'),
(1042, '2021-12-23 02:18:52.791962', '2021-12-23 02:18:52.791962', '00126', 'EVA SOAP', 0, '300.00', 12, 48, 60, 'EVA SOAP', 2, '0.00'),
(1043, '2021-12-23 02:18:53.001252', '2021-12-23 02:18:53.001252', '00127', 'IVORY SOAP', 0, '250.00', 12, 48, 64, 'IVORY SOAP', 2, '0.00'),
(1044, '2021-12-23 02:18:53.126172', '2021-12-23 02:18:53.126172', '00128', 'FRESH GLOW SOAP', 0, '250.00', 12, 48, 61, 'FRESH GLOW SOAP', 2, '0.00'),
(1045, '2021-12-23 02:18:53.189133', '2021-12-23 02:18:53.189133', '00129', 'VISITA SOAP', 0, '350.00', 8, 24, 77, 'VISITA SOAP', 2, '0.00'),
(1046, '2021-12-23 02:18:53.273305', '2021-12-23 02:18:53.274288', '00130', 'DETTOL SOAP BIG', 0, '350.00', 12, 36, 59, 'DETTOL SOAP BIG', 2, '0.00'),
(1047, '2021-12-23 02:18:53.336546', '2021-12-23 02:18:53.336546', '00131', 'DETTOL SOAP SMALL', 0, '250.00', 12, 36, 59, 'DETTOL SOAP SMALL', 2, '0.00'),
(1048, '2021-12-23 02:18:53.373309', '2021-12-23 02:18:53.373309', '00132', 'IMPERIAL LEATHER SOAP', 0, '120.00', 16, 96, 64, 'IMPERIAL LEATHER SOAP', 2, '0.00'),
(1049, '2021-12-23 02:18:53.436405', '2021-12-23 02:18:53.436405', '00133', 'PREMIER COOL SOAP', 0, '120.00', 16, 96, 71, 'PREMIER COOL SOAP', 2, '0.00'),
(1050, '2021-12-23 02:18:53.504544', '2021-12-23 02:18:53.504544', '00134', 'JOY SOAP', 0, '120.00', 16, 96, 65, 'JOY SOAP', 2, '0.00'),
(1051, '2021-12-23 02:18:53.604671', '2021-12-23 02:18:53.604671', '00135', 'TETMOSOL SOAP ', 0, '180.00', 16, 72, 75, 'TETMOSOL SOAP ', 2, '0.00'),
(1052, '2021-12-23 02:18:53.658045', '2021-12-23 02:18:53.658045', '00136', 'TETMOSOL BABY SOAP ', 0, '170.00', 16, 72, 75, 'TETMOSOL BABY SOAP ', 2, '0.00'),
(1053, '2021-12-23 02:18:53.722911', '2021-12-23 02:18:53.722911', '00137', 'EXTRACT SOAP', 0, '650.00', 8, 24, 60, 'EXTRACT SOAP', 2, '0.00'),
(1054, '2021-12-23 02:18:53.760252', '2021-12-23 02:18:53.760252', '00138', 'KK BROTHERS SOAP', 0, '500.00', 5, 18, 66, 'KK BROTHERS SOAP', 2, '0.00'),
(1055, '2021-12-23 02:18:53.826308', '2021-12-23 02:18:53.826308', '00139', 'ZEST SOAP', 0, '350.00', 2, 8, 81, 'ZEST SOAP', 2, '0.00'),
(1056, '2021-12-23 02:18:53.883330', '2021-12-23 02:18:53.883330', '00140', 'DOVE SENSITIVE SOAP', 0, '850.00', 2, 6, 59, 'DOVE SENSITIVE SOAP', 2, '0.00'),
(1057, '2021-12-23 02:18:54.280049', '2021-12-23 02:18:54.280049', '00141', 'DOVE PINK SOAP', 0, '850.00', 2, 6, 59, 'DOVE PINK SOAP', 2, '0.00'),
(1058, '2021-12-23 02:18:54.334014', '2021-12-23 02:18:54.334014', '00142', 'IRISH SPRING SOAP', 0, '400.00', 8, 20, 64, 'IRISH SPRING SOAP', 2, '0.00'),
(1059, '2021-12-23 02:18:54.391980', '2021-12-23 02:18:54.391980', '00143', 'NIVEA ROLL ON', 0, '650.00', 10, 30, 69, 'NIVEA ROLL ON', 2, '0.00'),
(1060, '2021-12-23 02:18:54.459300', '2021-12-23 02:18:54.459300', '00144', 'HARPIC BIG', 0, '1100.00', 4, 12, 63, 'HARPIC BIG', 2, '0.00'),
(1061, '2021-12-23 02:18:54.510995', '2021-12-23 02:18:54.510995', '00145', 'VIVA PLUS SOAP', 0, '250.00', 6, 24, 77, 'VIVA PLUS SOAP', 2, '0.00'),
(1062, '2021-12-23 02:18:54.571537', '2021-12-23 02:18:54.571537', '00146', 'NITTOL SOAP', 0, '120.00', 10, 50, 69, 'NITTOL SOAP', 2, '0.00'),
(1063, '2021-12-23 02:18:54.625611', '2021-12-23 02:18:54.625611', '00147', 'WAW SOAP', 0, '120.00', 10, 50, 78, 'WAW SOAP', 2, '0.00'),
(1064, '2021-12-23 02:18:54.682685', '2021-12-23 02:18:54.682685', '00148', 'F29 SOAP', 0, '120.00', 10, 50, 61, 'F29 SOAP', 2, '0.00'),
(1065, '2021-12-23 02:18:54.734280', '2021-12-23 02:18:54.734280', '00149', 'HARPIC MED', 0, '800.00', 5, 12, 63, 'HARPIC MED', 2, '0.00'),
(1066, '2021-12-23 02:18:54.774455', '2021-12-23 02:18:54.774455', '00150', 'HARPIC SMALL', 0, '350.00', 10, 24, 63, 'HARPIC SMALL', 2, '0.00'),
(1067, '2021-12-23 02:18:54.826039', '2021-12-23 02:18:54.826039', '00151', 'HYPO TOILET SACHET', 0, '50.00', 10, 80, 63, 'HYPO TOILET SACHET', 2, '0.00'),
(1068, '2021-12-23 02:18:54.882739', '2021-12-23 02:18:54.882739', '00152', 'HYPO SACHET', 0, '40.00', 10, 80, 63, 'HYPO SACHET', 2, '0.00'),
(1069, '2021-12-23 02:18:54.937722', '2021-12-23 02:18:54.937722', '00153', 'HYPO SMALL', 0, '450.00', 10, 24, 63, 'HYPO SMALL', 2, '0.00'),
(1070, '2021-12-23 02:18:54.994952', '2021-12-23 02:18:54.994952', '00154', 'HYPO BIG', 0, '800.00', 5, 12, 63, 'HYPO BIG', 2, '0.00'),
(1071, '2021-12-23 02:18:55.184733', '2022-01-12 04:13:53.421310', '00155', 'JIK SMALL ', 200, '450.00', 12, 24, 65, 'JIK SMALL ', 2, '0.00'),
(1072, '2021-12-23 02:18:55.703330', '2021-12-23 02:18:55.703330', '00156', 'JIK BIG', 0, '900.00', 5, 12, 65, 'JIK BIG', 2, '0.00'),
(1073, '2021-12-23 02:18:55.759456', '2021-12-23 02:18:55.759456', '00157', 'SEDORS CAR WASH', 0, '700.00', 5, 12, 74, 'SEDORS CAR WASH', 2, '0.00'),
(1074, '2021-12-23 02:18:55.820088', '2021-12-23 02:18:55.820088', '00158', 'LADY CARE PAD', 0, '450.00', 5, 12, 67, 'LADY CARE PAD', 2, '0.00'),
(1075, '2021-12-23 02:18:55.880772', '2021-12-23 02:18:55.881767', '00159', 'MOLPED PAD', 0, '500.00', 5, 16, 68, 'MOLPED PAD', 2, '0.00'),
(1076, '2021-12-23 02:18:55.951093', '2021-12-23 02:18:55.951093', '00160', 'NDK PAD', 0, '450.00', 5, 16, 69, 'NDK PAD', 2, '0.00'),
(1077, '2021-12-23 02:18:56.002121', '2021-12-23 02:18:56.002121', '00161', 'ALWAYS PAD', 0, '450.00', 3, 8, 56, 'ALWAYS PAD', 2, '0.00'),
(1078, '2021-12-23 02:18:56.037094', '2021-12-23 02:18:56.037094', '00162', 'ALWAYS 2 IN 1 PAD', 0, '800.00', 2, 6, 56, 'ALWAYS 2 IN 1 PAD', 2, '0.00'),
(1079, '2021-12-23 02:18:56.103941', '2021-12-23 02:18:56.103941', '00163', 'ANGEL ZIP PAD', 0, '1050.00', 10, 24, 56, 'ANGEL ZIP PAD', 2, '0.00'),
(1080, '2021-12-23 02:18:56.155961', '2021-12-23 02:18:56.155961', '00164', 'ANGEL PAD', 0, '450.00', 5, 12, 56, 'ANGEL PAD', 2, '0.00'),
(1081, '2021-12-23 02:18:56.192823', '2021-12-23 02:18:56.192823', '00165', 'VIRONY ZIP PAD', 0, '1100.00', 10, 24, 77, 'VIRONY ZIP PAD', 2, '0.00'),
(1082, '2021-12-23 02:18:56.248275', '2021-12-23 02:18:56.248275', '00166', 'CLOSE UP PASTE BIG', 0, '400.00', 10, 50, 58, 'CLOSE UP PASTE BIG', 2, '0.00'),
(1083, '2021-12-23 02:18:56.308563', '2021-12-23 02:18:56.308563', '00167', 'CLOSE UP PASTE SMALL', 0, '200.00', 10, 24, 58, 'CLOSE UP PASTE SMALL', 2, '0.00'),
(1084, '2021-12-23 02:18:56.395483', '2021-12-23 02:18:56.395483', '00168', 'PEPSODENT 123 BIG', 0, '500.00', 10, 50, 71, 'PEPSODENT 123 BIG', 2, '0.00'),
(1085, '2021-12-23 02:18:56.448815', '2021-12-23 02:18:56.448815', '00169', 'PEPSODENT 123 SMALL', 0, '250.00', 10, 24, 71, 'PEPSODENT 123 SMALL', 2, '0.00'),
(1086, '2021-12-23 02:18:56.626653', '2021-12-23 02:18:56.626653', '00170', 'ORAL B PASTE BIG', 0, '500.00', 10, 36, 70, 'ORAL B PASTE BIG', 2, '0.00'),
(1087, '2021-12-23 02:18:56.814243', '2021-12-23 02:18:56.814243', '00171', 'ORAL B PASTE SMALL', 0, '250.00', 10, 36, 70, 'ORAL B PASTE SMALL', 2, '0.00'),
(1088, '2021-12-23 02:18:56.867002', '2021-12-23 02:18:56.867002', '00172', 'ORAL B TOOTH BRUSH', 0, '200.00', 5, 12, 70, 'ORAL B TOOTH BRUSH', 2, '0.00'),
(1089, '2021-12-23 02:18:56.924473', '2021-12-23 02:18:56.924473', '00173', 'BIC SHAVING STICK', 0, '150.00', 10, 50, 57, 'BIC SHAVING STICK', 2, '0.00'),
(1090, '2021-12-23 02:18:56.978254', '2021-12-23 02:18:56.978254', '00174', 'KS  TWIN BRUSH', 0, '250.00', 5, 12, 66, 'KS  TWIN BRUSH', 2, '0.00'),
(1091, '2021-12-23 02:18:57.050316', '2021-12-23 02:18:57.051315', '00175', 'ORAL STANDARD BRUSH', 0, '100.00', 5, 12, 70, 'ORAL STANDARD BRUSH', 2, '0.00'),
(1092, '2021-12-23 02:18:57.118583', '2021-12-23 02:18:57.118583', '00176', 'PERFECT TOOTH BRUSH', 0, '100.00', 5, 12, 71, 'PERFECT TOOTH BRUSH', 2, '0.00'),
(1093, '2021-12-23 02:18:57.173233', '2021-12-23 02:18:57.173233', '00177', 'ORAL WISE CHILDREN BRUSH', 0, '100.00', 5, 12, 70, 'ORAL WISE CHILDREN BRUSH', 2, '0.00'),
(1094, '2021-12-23 02:18:57.240556', '2021-12-23 02:18:57.240556', '00178', 'ROSE BELLE SERVITTE', 0, '150.00', 10, 36, 73, 'ROSE BELLE SERVITTE', 2, '0.00'),
(1095, '2021-12-23 02:18:57.300553', '2021-12-23 02:18:57.300553', '00179', 'DR BROWN FACE MASKS', 0, '100.00', 15, 50, 59, 'DR BROWN FACE MASKS', 2, '0.00'),
(1096, '2021-12-23 02:18:57.337524', '2021-12-23 02:18:57.337524', '00180', 'NAKED TISSUE', 0, '150.00', 5, 12, 69, 'NAKED TISSUE', 2, '0.00'),
(1097, '2021-12-23 02:18:57.395895', '2021-12-23 02:18:57.395895', '00181', 'TOMTOM SWEET', 0, '10.00', 12, 40, 75, 'TOMTOM SWEET', 2, '0.00'),
(1098, '2021-12-23 02:18:57.570189', '2021-12-23 02:18:57.570189', '00182', 'VICKS LEMON SWEET', 0, '10.00', 12, 30, 77, 'VICKS LEMON SWEET', 2, '0.00'),
(1099, '2021-12-23 02:18:57.759017', '2021-12-23 02:18:57.759017', '00183', 'ALPENLIEBE SWEET ', 0, '10.00', 12, 88, 56, 'ALPENLIEBE SWEET ', 2, '0.00'),
(1100, '2021-12-23 02:18:57.916671', '2021-12-23 02:18:57.916671', '00184', 'CENTRE FRESH GUM', 0, '10.00', 12, 88, 58, 'CENTRE FRESH GUM', 2, '0.00'),
(1101, '2021-12-23 02:18:58.092417', '2021-12-23 02:18:58.092417', '00185', 'ECLAIRES SWEET', 0, '10.00', 12, 125, 60, 'ECLAIRES SWEET', 2, '0.00'),
(1102, '2021-12-23 02:18:58.159741', '2021-12-23 02:18:58.159741', '00186', 'DIGESTIVE PLUS BISCUIT', 0, '60.00', 10, 48, 59, 'DIGESTIVE PLUS BISCUIT', 2, '0.00'),
(1103, '2021-12-23 02:18:58.213121', '2021-12-23 02:18:58.213121', '00187', 'CHOCO RINGS', 0, '50.00', 10, 48, 58, 'CHOCO RINGS', 2, '0.00'),
(1104, '2021-12-23 02:18:58.271730', '2021-12-23 02:18:58.271730', '00188', 'LITE CRACKER', 0, '20.00', 10, 72, 67, 'LITE CRACKER', 2, '0.00'),
(1105, '2021-12-23 02:18:58.336985', '2021-12-23 02:18:58.336985', '00189', 'ANGEL DELUX PAD', 0, '100.00', 20, 100, 56, 'ANGEL DELUX PAD', 2, '0.00'),
(1106, '2021-12-23 02:18:58.391010', '2021-12-23 02:18:58.391010', '00190', 'OATS N MILK BISCUIT', 0, '50.00', 10, 48, 70, 'OATS N MILK BISCUIT', 2, '0.00'),
(1107, '2021-12-23 02:18:58.448041', '2021-12-23 02:18:58.448041', '00191', 'POWER MILK BISCUIT', 0, '60.00', 10, 24, 71, 'POWER MILK BISCUIT', 2, '0.00'),
(1108, '2021-12-23 02:18:58.515577', '2021-12-23 02:18:58.515577', '00192', 'PARLE G GOLD', 0, '60.00', 10, 24, 71, 'PARLE G GOLD', 2, '0.00'),
(1109, '2021-12-23 02:18:58.559236', '2021-12-23 02:18:58.559236', '00193', 'GOLDEN MORN 50G', 0, '100.00', 20, 100, 62, 'GOLDEN MORN 50G', 2, '0.00'),
(1110, '2021-12-23 02:18:58.705191', '2021-12-23 02:18:58.705191', '00194', 'MILO SACHET 20G', 0, '70.00', 50, 240, 68, 'MILO SACHET 20G', 2, '0.00'),
(1111, '2021-12-23 02:18:58.937853', '2021-12-23 02:18:58.937853', '00195', 'PEAK FULL CREAM 16G', 0, '80.00', 50, 210, 71, 'PEAK FULL CREAM 16G', 2, '0.00'),
(1112, '2021-12-23 02:18:59.127365', '2021-12-23 02:18:59.127365', '00196', 'GOLDEN PENNY TWIST', 0, '380.00', 10, 20, 62, 'GOLDEN PENNY TWIST', 2, '0.00'),
(1113, '2021-12-23 02:18:59.181333', '2021-12-23 02:18:59.181333', '00197', 'GOLDEN PENNY SPAGETTI ', 0, '380.00', 10, 20, 62, 'GOLDEN PENNY SPAGETTI ', 2, '0.00'),
(1114, '2021-12-23 02:18:59.228306', '2021-12-23 02:18:59.228306', '00198', 'CROWN PRENIUM SPAGETTI ', 0, '380.00', 10, 20, 58, 'CROWN PRENIUM SPAGETTI ', 2, '0.00'),
(1115, '2021-12-23 02:18:59.280269', '2021-12-23 02:18:59.280269', '00199', 'ONGA CUBE', 0, '300.00', 10, 24, 70, 'ONGA CUBE', 2, '0.00'),
(1116, '2021-12-23 02:18:59.337772', '2021-12-23 02:18:59.337772', '00200', 'CROWN SLIM SPAGETTI', 0, '350.00', 10, 20, 58, 'CROWN SLIM SPAGETTI', 2, '0.00'),
(1117, '2021-12-23 02:18:59.406135', '2021-12-23 02:18:59.406135', '00201', 'KNORR CUBE', 0, '750.00', 5, 17, 66, 'KNORR CUBE', 2, '0.00'),
(1118, '2021-12-23 02:18:59.473012', '2021-12-23 02:18:59.473012', '00202', 'KNORR CHICKEN', 0, '750.00', 5, 17, 66, 'KNORR CHICKEN', 2, '0.00'),
(1119, '2021-12-23 02:18:59.530099', '2021-12-23 02:18:59.531099', '00203', 'MAGGI CUBE', 0, '650.00', 10, 21, 68, 'MAGGI CUBE', 2, '0.00'),
(1120, '2021-12-23 02:18:59.586260', '2021-12-23 02:18:59.586260', '00204', 'GINO CUBE', 0, '120.00', 10, 40, 62, 'GINO CUBE', 2, '0.00'),
(1121, '2021-12-23 02:18:59.637221', '2021-12-23 02:18:59.637221', '00205', 'UNCLE PALM SALT', 0, '100.00', 10, 40, 76, 'UNCLE PALM SALT', 2, '0.00'),
(1122, '2021-12-23 02:18:59.739090', '2021-12-23 02:18:59.739090', '00206', 'PLASTIC SPRITE', 0, '200.00', 6, 12, 71, 'PLASTIC SPRITE', 2, '0.00'),
(1123, '2021-12-23 02:18:59.807248', '2021-12-23 02:18:59.807248', '00207', 'PLASTIC COKE', 0, '200.00', 6, 12, 71, 'PLASTIC COKE', 2, '0.00'),
(1124, '2021-12-23 02:18:59.839575', '2021-12-23 02:18:59.839575', '00208', 'PLASTIC FANTA ', 0, '200.00', 6, 12, 71, 'PLASTIC FANTA ', 2, '0.00'),
(1125, '2021-12-23 02:18:59.906474', '2021-12-23 02:18:59.906474', '00209', 'RC DRINKS', 0, '150.00', 6, 12, 73, 'RC DRINKS', 2, '0.00'),
(1126, '2021-12-23 02:18:59.960845', '2021-12-23 02:18:59.960845', '00210', 'NUTRI DRINKS', 0, '250.00', 6, 12, 69, 'NUTRI DRINKS', 2, '0.00'),
(1127, '2021-12-23 02:19:00.095097', '2021-12-23 02:19:00.095097', '00211', 'DUDU DRINK', 0, '250.00', 6, 12, 59, ' DUDU DRINK', 2, '0.00'),
(1128, '2021-12-23 02:19:00.219572', '2021-12-23 02:19:00.219572', '00212', 'EVA WATER BIG', 0, '200.00', 6, 12, 60, 'EVA WATER BIG', 2, '0.00'),
(1129, '2021-12-23 02:19:00.276153', '2021-12-23 02:19:00.276153', '00213', 'EVA WATER SMALL', 0, '100.00', 6, 12, 60, 'EVA WATER SMALL', 2, '0.00'),
(1130, '2021-12-23 02:19:00.326121', '2021-12-23 02:19:00.326121', '00214', 'DUBIC MALT', 0, '200.00', 10, 24, 59, 'DUBIC MALT', 2, '0.00'),
(1131, '2021-12-23 02:19:00.372093', '2021-12-23 02:19:00.372093', '00215', 'BETA MALT', 0, '200.00', 10, 24, 57, 'BETA MALT', 2, '0.00'),
(1132, '2021-12-23 02:19:00.425058', '2021-12-23 02:19:00.425058', '00216', 'AMSTEL MALT ', 0, '200.00', 10, 24, 56, 'AMSTEL MALT ', 2, '0.00'),
(1133, '2021-12-23 02:19:00.492018', '2021-12-23 02:19:00.492018', '00217', 'GUNINESS MALTA', 0, '200.00', 10, 24, 62, 'GUNINESS MALTA', 2, '0.00'),
(1134, '2021-12-23 02:19:00.538241', '2021-12-23 02:19:00.539241', '00218', 'FRESH YOGURT', 0, '250.00', 16, 12, 61, 'FRESH YOGURT', 2, '0.00'),
(1135, '2021-12-23 02:19:00.590503', '2021-12-23 02:19:00.591502', '00219', 'FEARLESS DRINK', 0, '300.00', 6, 12, 61, 'FEARLESS DRINK', 2, '0.00'),
(1136, '2021-12-23 02:19:00.625740', '2021-12-23 02:19:00.625740', '00220', '20 LEAVES EXECRISE BOOK', 0, '80.00', 40, 216, 60, '20 LEAVES EXECRISE BOOK', 2, '0.00'),
(1137, '2021-12-23 02:19:00.692985', '2021-12-23 02:19:00.692985', '00221', '40 LEAVES EXECRISE BOOK', 0, '140.00', 24, 96, 60, '40 LEAVES EXECRISE BOOK', 2, '0.00'),
(1138, '2021-12-23 02:19:00.781880', '2021-12-23 02:19:00.781880', '00222', '60 LEAVES EXECRISE BOOK', 0, '180.00', 24, 72, 60, '60 LEAVES EXECRISE BOOK', 2, '0.00'),
(1139, '2021-12-23 02:19:00.826422', '2021-12-23 02:19:00.826422', '00223', '80 LEAVES EXECRISE BOOK', 0, '220.00', 12, 48, 60, '80 LEAVES EXECRISE BOOK', 2, '0.00'),
(1140, '2021-12-23 02:19:00.870822', '2021-12-23 02:19:00.870822', '00224', 'HIGHER EDUCATION BOOK', 0, '400.00', 10, 30, 63, 'HIGHER EDUCATION BOOK', 2, '0.00'),
(1141, '2021-12-23 02:19:00.926044', '2021-12-23 02:19:00.926044', '00225', 'ST RITA SARDINE', 0, '400.00', 10, 50, 74, 'ST RITA SARDINE', 2, '0.00'),
(1142, '2021-12-23 02:19:00.982155', '2021-12-23 02:19:00.982155', '00226', 'MEGA MACKEREL', 0, '350.00', 10, 50, 68, 'MEGA MACKEREL', 2, '0.00'),
(1143, '2021-12-23 02:19:01.027451', '2021-12-23 02:19:01.027451', '00227', 'HONEY BEES CRUNCHY BISCUIT', 0, '60.00', 10, 48, 63, 'HONEY BEES CRUNCHY BISCUIT', 2, '0.00'),
(1144, '2021-12-23 02:19:01.139913', '2021-12-23 02:19:01.139913', '00228', 'PEN', 0, '80.00', 10, 50, 71, 'PEN', 2, '0.00'),
(1145, '2021-12-23 02:19:01.243423', '2021-12-23 02:19:01.244428', '00229', 'CORRECTION FLULD', 0, '150.00', 6, 12, 58, 'CORRECTION FLULD', 2, '0.00'),
(1146, '2021-12-23 02:19:01.321124', '2021-12-23 02:19:01.321124', '00230', 'PERMNANT MAKER', 0, '150.00', 3, 12, 71, 'PERMNANT MAKER', 2, '0.00'),
(1147, '2021-12-23 02:19:01.382287', '2021-12-23 02:19:01.382287', '00231', 'BOARD MAKER', 0, '150.00', 3, 12, 57, 'BOARD MAKER', 2, '0.00'),
(1148, '2021-12-23 02:19:01.438568', '2021-12-23 02:19:01.438568', '00232', 'FANCY PENCIL', 0, '30.00', 3, 12, 61, 'FANCY PENCIL', 2, '0.00'),
(1149, '2021-12-23 02:19:01.493517', '2021-12-23 02:19:01.493517', '00233', 'HB PENCIL', 0, '50.00', 3, 12, 63, 'HB PENCIL', 2, '0.00'),
(1150, '2021-12-23 02:19:01.549532', '2021-12-23 02:19:01.549532', '00234', 'MASKING TAPE', 0, '300.00', 5, 12, 68, 'MASKING TAPE', 2, '0.00'),
(1151, '2021-12-23 02:19:01.592503', '2021-12-23 02:19:01.592503', '00235', 'SUPERPACK NOODLES', 0, '120.00', 10, 40, 74, '120G', 2, '0.00'),
(1152, '2021-12-23 02:19:01.637476', '2021-12-23 02:19:01.637476', '00236', 'INDOMITABLES NOODLES', 0, '80.00', 10, 40, 64, '70G', 2, '0.00'),
(1153, '2021-12-23 02:19:01.683452', '2021-12-23 02:19:01.683452', '00237', 'TRANSPARENT RULER', 0, '100.00', 4, 12, 75, 'TRANSPARENT RULER', 2, '0.00'),
(1154, '2021-12-23 02:19:01.737621', '2021-12-23 02:19:01.737621', '00238', 'SUPREME NOODLES ', 0, '110.00', 10, 40, 74, '120G', 2, '0.00'),
(1155, '2021-12-23 02:19:01.859869', '2021-12-23 02:19:01.859869', '00239', 'SUPREME NOODLES', 0, '70.00', 10, 40, 74, '70G', 2, '0.00'),
(1156, '2021-12-23 02:19:01.988405', '2021-12-23 02:19:01.989409', '00240', 'SLIPPERS SMALL', 0, '250.00', 20, 100, 74, 'SLIPPERS SMALL', 2, '0.00'),
(1157, '2021-12-23 02:19:02.088174', '2021-12-23 02:19:02.088174', '00241', 'SLIPERS BIG', 0, '350.00', 12, 48, 74, 'SLIPERS BIG', 2, '0.00'),
(1158, '2021-12-23 02:19:02.264361', '2021-12-23 02:19:02.264361', '00242', 'OFFICE FILE', 0, '50.00', 10, 50, 70, 'OFFICE FILE', 2, '0.00'),
(1159, '2021-12-23 02:19:02.372018', '2021-12-23 02:19:02.372018', '00243', 'BOXERS', 0, '600.00', 10, 30, 57, 'BOXERS', 2, '0.00'),
(1160, '2021-12-23 02:19:02.443256', '2021-12-23 02:19:02.443256', '00244', 'COLOURED HANKY', 0, '100.00', 4, 12, 58, 'COLOURED HANKY', 2, '0.00'),
(1161, '2021-12-23 02:19:02.551332', '2021-12-23 02:19:02.551332', '00245', 'WHITE HANKY', 0, '100.00', 4, 12, 78, 'WHITE HANKY', 2, '0.00'),
(1162, '2021-12-23 02:19:02.643212', '2021-12-23 02:19:02.643212', '00246', 'TUMMY NOODLES', 0, '110.00', 10, 40, 75, '120G', 2, '0.00'),
(1163, '2021-12-23 02:19:02.733442', '2021-12-23 02:19:02.733442', '00247', 'TUMMY NOODLES', 0, '75.00', 10, 40, 75, '70G', 2, '0.00'),
(1164, '2021-12-23 02:19:02.781403', '2021-12-23 02:19:02.781403', '00248', 'KINGS OIL', 0, '1500.00', 4, 12, 66, '1LTR', 2, '0.00'),
(1165, '2021-12-23 02:19:02.827378', '2021-12-23 02:19:02.827378', '00249', 'KINGS SACHET OIL', 0, '1300.00', 4, 12, 66, 'KINGS SACHET OIL', 2, '0.00'),
(1166, '2021-12-23 02:19:02.927314', '2021-12-23 02:19:02.927314', '00250', 'KINGS OIL', 0, '3000.00', 3, 6, 66, '2LTR', 2, '0.00'),
(1167, '2022-01-14 00:57:34.445717', '2022-01-14 11:11:53.333615', '00251', 'Mouse', 20, '1500.00', 3, 12, 68, NULL, 1, '0.00'),
(1168, '2022-01-14 03:48:38.642070', '2022-01-14 03:48:38.642070', '00252', 'Keyboard', 0, '2000.00', 3, 12, 66, NULL, 1, '0.00'),
(1169, '2022-01-14 04:16:44.022441', '2022-01-14 04:16:44.022441', '00253', 'Torch Light', 0, '1200.00', 5, 12, 75, NULL, 1, '0.00'),
(1170, '2022-01-14 04:18:58.750379', '2022-01-16 20:49:55.177280', '00254', 'BIG APPLE', 20, '200.00', 48, 150, 56, NULL, 1, '100.00'),
(1171, '2022-01-14 10:11:58.383441', '2022-01-14 11:11:53.589496', '00255', 'SONIA TOMATOES', 10, '8000.00', 5, 24, 74, '210G BY 24 TINS', 1, '0.00'),
(1172, '2022-01-16 20:42:29.717110', '2022-01-16 20:50:20.665320', '00256', 'A TESTER', 0, '300.00', 4, 12, 56, NULL, 1, '200.00');

-- --------------------------------------------------------

--
-- Table structure for table `submission_status`
--

CREATE TABLE `submission_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `submission_status`
--

INSERT INTO `submission_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'PENDING', '2021-12-07 19:00:34.982229', '2021-12-07 19:00:34.982229'),
(2, 'SUBMITTED', '2021-12-07 19:00:35.150149', '2021-12-07 19:00:35.151150');

-- --------------------------------------------------------

--
-- Table structure for table `suppliers`
--

CREATE TABLE `suppliers` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `name` varchar(255) NOT NULL,
  `prefix` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `suppliers`
--

INSERT INTO `suppliers` (`id`, `created_at`, `updated_at`, `name`, `prefix`) VALUES
(15, '2022-01-12 04:57:20.857953', '2022-01-12 15:35:30.614982', 'Mastersoft Technology Ltd.', 'MST'),
(16, '2022-01-16 14:56:48.096934', '2022-01-16 14:56:48.096934', 'Heatbeat Consult', 'HTBC');

-- --------------------------------------------------------

--
-- Table structure for table `suppliers_branches`
--

CREATE TABLE `suppliers_branches` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `address` longtext NOT NULL,
  `phone` varchar(255) NOT NULL,
  `supplier_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `suppliers_branches`
--

INSERT INTO `suppliers_branches` (`id`, `created_at`, `updated_at`, `address`, `phone`, `supplier_id`) VALUES
(3, '2022-01-12 05:57:58.634018', '2022-01-12 06:08:19.801007', 'No 35 Afikpo Road Abakaliki', '08064004344', 15),
(4, '2022-01-12 06:28:00.246269', '2022-01-12 06:28:00.246269', 'Mile 50', '08064004355', 15),
(5, '2022-01-16 14:58:55.202053', '2022-01-16 15:31:07.744935', 'No 35 Afikpo Road, Abakaliki Second Floor', '08039555648', 16);

-- --------------------------------------------------------

--
-- Table structure for table `suppliers_majors`
--

CREATE TABLE `suppliers_majors` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `product` varchar(255) NOT NULL,
  `supplier_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `suppliers_reps`
--

CREATE TABLE `suppliers_reps` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `suppliers_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `suppliers_reps`
--

INSERT INTO `suppliers_reps` (`id`, `created_at`, `updated_at`, `name`, `phone`, `suppliers_id`) VALUES
(3, '2022-01-14 00:15:03.298736', '2022-01-14 00:21:30.365762', 'Nwoke Benjamin Onwe', '08064004355', 15),
(4, '2022-01-14 00:21:46.296812', '2022-01-14 00:21:46.296812', 'Nwankwo Augustus', '08064004344', 15),
(5, '2022-01-14 01:25:02.140669', '2022-01-14 01:25:02.141671', 'Nwibo Mary', '094484878467', 15),
(6, '2022-01-16 14:57:58.758310', '2022-01-16 14:57:58.758310', 'Nwibo Mary', '08095858574', 16);

-- --------------------------------------------------------

--
-- Table structure for table `task_manager`
--

CREATE TABLE `task_manager` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `description` longtext NOT NULL,
  `processed_by_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `ticket_status`
--

CREATE TABLE `ticket_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ticket_status`
--

INSERT INTO `ticket_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'OPEN', '2021-12-07 19:00:47.145019', '2021-12-07 19:00:47.145019'),
(2, 'CLOSED', '2021-12-07 19:00:47.228190', '2021-12-07 19:00:47.228190');

-- --------------------------------------------------------

--
-- Table structure for table `titles`
--

CREATE TABLE `titles` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `titles`
--

INSERT INTO `titles` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'MR.', '2021-12-07 18:56:39.963259', '2021-12-07 18:56:39.963259'),
(2, 'MRS.', '2021-12-07 18:56:40.007723', '2021-12-07 18:56:40.007723'),
(3, 'MISS.', '2021-12-07 18:56:40.107018', '2021-12-07 18:56:40.107018'),
(4, 'DR.', '2021-12-07 18:56:40.141902', '2021-12-07 18:56:40.141902'),
(5, 'PROF', '2021-12-07 18:56:40.163696', '2021-12-07 18:56:40.164696'),
(6, 'BARR.', '2021-12-07 18:56:40.222710', '2021-12-07 18:56:40.223709'),
(7, 'ENGR.', '2021-12-07 18:56:40.243697', '2021-12-07 18:56:40.243697'),
(8, 'ARCH.', '2021-12-07 18:56:40.276676', '2021-12-07 18:56:40.276676'),
(9, 'CHIEF.', '2021-12-07 18:56:40.297664', '2021-12-07 18:56:40.298663'),
(10, 'HON.', '2021-12-07 18:56:40.359626', '2021-12-07 18:56:40.359626');

-- --------------------------------------------------------

--
-- Table structure for table `transaction_adjustment_request`
--

CREATE TABLE `transaction_adjustment_request` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `approved_at` date DEFAULT NULL,
  `effective_date` date DEFAULT NULL,
  `approval_officer_id` int(11) DEFAULT NULL,
  `approval_status_id` int(11) NOT NULL,
  `member_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transaction_adjustment_request`
--

INSERT INTO `transaction_adjustment_request` (`id`, `created_at`, `updated_at`, `amount`, `approved_at`, `effective_date`, `approval_officer_id`, `approval_status_id`, `member_id`, `status_id`) VALUES
(1, '2021-12-15 22:35:12.550354', '2021-12-16 00:32:33.559693', '5000.00', '2021-12-16', '2021-12-15', 6, 2, 353, 2),
(2, '2021-12-15 22:36:46.652703', '2021-12-16 00:32:36.661320', '15000.00', '2021-12-16', '2021-12-15', 6, 2, 352, 2),
(4, '2021-12-16 00:05:46.483362', '2021-12-16 00:32:38.624364', '12000.00', '2021-12-16', '2021-12-16', 6, 2, 354, 2),
(5, '2021-12-16 00:08:21.927766', '2021-12-16 00:32:40.238722', '10000.00', '2021-12-16', '2021-12-16', 6, 2, 596, 2),
(6, '2021-12-16 00:49:50.396249', '2021-12-16 00:50:04.674542', '10000.00', '2021-12-16', '2021-12-16', 6, 2, 355, 2),
(7, '2021-12-31 07:22:17.062402', '2021-12-31 07:36:50.120519', '0.00', '2021-12-31', '2021-12-31', 6, 2, 355, 2),
(8, '2021-12-31 07:44:31.030935', '2021-12-31 07:44:45.120292', '0.00', '2021-12-31', '2021-12-31', 6, 2, 354, 2);

-- --------------------------------------------------------

--
-- Table structure for table `transaction_loan_adjustment_request`
--

CREATE TABLE `transaction_loan_adjustment_request` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `approved_at` date DEFAULT NULL,
  `effective_date` date DEFAULT NULL,
  `approval_officer_id` int(11) DEFAULT NULL,
  `approval_status_id` int(11) NOT NULL,
  `member_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transaction_loan_adjustment_request`
--

INSERT INTO `transaction_loan_adjustment_request` (`id`, `created_at`, `updated_at`, `amount`, `approved_at`, `effective_date`, `approval_officer_id`, `approval_status_id`, `member_id`, `status_id`) VALUES
(3, '2021-12-16 03:44:14.214369', '2021-12-16 04:30:44.922371', '40000.00', '2021-12-16', '2021-12-16', 6, 2, 1, 1),
(5, '2021-12-16 04:22:15.207442', '2021-12-16 04:30:46.782876', '60000.00', '2021-12-16', '2021-12-16', 6, 2, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `transaction_periods`
--

CREATE TABLE `transaction_periods` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `transaction_period` date NOT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transaction_periods`
--

INSERT INTO `transaction_periods` (`id`, `created_at`, `updated_at`, `transaction_period`, `status_id`) VALUES
(1, '2021-12-07 23:12:22.735344', '2021-12-07 23:13:53.199160', '2021-12-08', 2),
(2, '2021-12-31 09:48:25.090224', '2021-12-31 09:48:31.287061', '2021-12-31', 1);

-- --------------------------------------------------------

--
-- Table structure for table `transaction_sources`
--

CREATE TABLE `transaction_sources` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transaction_sources`
--

INSERT INTO `transaction_sources` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'SAVINGS', '2021-12-07 19:03:01.835381', '2021-12-07 19:03:01.835381'),
(2, 'LOAN', '2021-12-07 19:03:01.878591', '2021-12-07 19:03:01.879593'),
(3, 'GENERAL', '2021-12-07 19:03:02.046509', '2021-12-07 19:03:02.046509'),
(4, 'UTILITIES', '2021-12-07 19:03:02.081529', '2021-12-07 19:03:02.081529'),
(5, 'SHOP', '2021-12-31 12:12:49.000000', '2021-12-31 12:12:49.000000');

-- --------------------------------------------------------

--
-- Table structure for table `transaction_status`
--

CREATE TABLE `transaction_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transaction_status`
--

INSERT INTO `transaction_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'UNTREATED', '2021-12-07 18:59:32.576131', '2021-12-07 18:59:32.576131'),
(2, 'TREATED', '2021-12-07 18:59:32.632093', '2021-12-07 18:59:32.632093');

-- --------------------------------------------------------

--
-- Table structure for table `transaction_types`
--

CREATE TABLE `transaction_types` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `code` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `maximum_amount` decimal(20,2) NOT NULL,
  `minimum_amount` decimal(20,2) NOT NULL,
  `duration` smallint(5) UNSIGNED NOT NULL CHECK (`duration` >= 0),
  `interest_rate` smallint(5) UNSIGNED NOT NULL CHECK (`interest_rate` >= 0),
  `rank` int(11) NOT NULL,
  `admin_charges` decimal(20,2) DEFAULT NULL,
  `admin_charges_minimum` decimal(20,2) DEFAULT NULL,
  `default_admin_charges` decimal(20,2) NOT NULL,
  `salary_loan_relationship` int(11) NOT NULL,
  `savings_rate` int(11) NOT NULL,
  `guarantors` int(11) NOT NULL,
  `loan_age` int(11) NOT NULL,
  `share_unit_min` int(11) NOT NULL,
  `share_unit_max` int(11) NOT NULL,
  `admin_charges_rating_id` int(11) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `interest_deduction_id` int(11) DEFAULT NULL,
  `multiple_loan_status_id` int(11) NOT NULL,
  `receipt_type_id` int(11) NOT NULL,
  `source_id` int(11) DEFAULT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transaction_types`
--

INSERT INTO `transaction_types` (`id`, `created_at`, `updated_at`, `code`, `name`, `maximum_amount`, `minimum_amount`, `duration`, `interest_rate`, `rank`, `admin_charges`, `admin_charges_minimum`, `default_admin_charges`, `salary_loan_relationship`, `savings_rate`, `guarantors`, `loan_age`, `share_unit_min`, `share_unit_max`, `admin_charges_rating_id`, `category_id`, `interest_deduction_id`, `multiple_loan_status_id`, `receipt_type_id`, `source_id`, `status_id`) VALUES
(1, '2021-12-07 19:27:59.367810', '2021-12-16 07:55:45.530872', '100', 'MEMBERSHIP', '0.00', '0.00', 0, 0, 0, '2000.00', NULL, '0.00', 0, 0, 0, 0, 1, 2, NULL, NULL, NULL, 1, 4, 3, 1),
(2, '2021-12-07 19:28:42.246244', '2021-12-14 20:47:06.681048', '101', 'ORDINARY SAVINGS', '0.00', '2000.00', 0, 0, 0, NULL, NULL, '0.00', 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, 1, 4, 1, 1),
(3, '2021-12-07 19:29:13.419218', '2021-12-07 19:29:13.419218', '102', 'PROJECT SAVINGS', '0.00', '1000.00', 0, 0, 0, NULL, NULL, '0.00', 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, 1, 3, 1, 1),
(4, '2021-12-07 19:29:45.410484', '2021-12-07 19:29:45.410484', '103', 'XMAS SAVINGS', '0.00', '1000.00', 0, 0, 0, NULL, NULL, '0.00', 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, 1, 3, 1, 1),
(5, '2021-12-07 19:30:11.741450', '2021-12-07 19:30:11.741450', '104', 'LAND SAVINGS', '0.00', '10000.00', 0, 0, 0, NULL, NULL, '0.00', 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, 1, 3, 1, 1),
(6, '2021-12-07 19:30:36.076200', '2021-12-07 19:30:36.076200', '105', 'OTHER SAVINGS', '0.00', '10000.00', 0, 0, 0, NULL, NULL, '0.00', 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, 1, 3, 1, 1),
(7, '2021-12-07 19:31:07.631782', '2021-12-07 19:31:07.631782', '200', 'SALARY UPDATE', '0.00', '0.00', 0, 0, 0, NULL, NULL, '0.00', 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, 1, 3, 3, 1),
(8, '2021-12-07 19:31:33.677197', '2021-12-16 13:28:01.971588', '201', 'SHORT TERM LOAN', '100000.00', '0.00', 3, 5, 0, '2.00', '10000.00', '1000.00', 35, 35, 2, 6, 0, 0, 1, 1, 2, 1, 5, 2, 1),
(9, '2021-12-07 19:32:05.776788', '2021-12-07 19:32:05.776788', '202', 'LONG TERM LOAN', '3000000.00', '0.00', 0, 0, 0, NULL, NULL, '0.00', 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, 1, 5, 2, 1),
(10, '2021-12-07 19:32:37.587963', '2021-12-07 19:32:37.587963', '203', 'SOFT LOAN', '50000.00', '0.00', 0, 0, 0, NULL, NULL, '0.00', 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, 1, 5, 2, 1),
(11, '2021-12-07 19:32:57.749761', '2021-12-07 19:32:57.749761', '300', 'EXCLUSIVENESS', '0.00', '0.00', 0, 0, 0, NULL, NULL, '0.00', 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, 1, 3, 3, 1),
(12, '2021-12-07 19:33:19.849377', '2021-12-07 19:33:19.849377', '400', 'MEMBERS CREDIT PURCHASE', '0.00', '0.00', 0, 0, 0, NULL, NULL, '0.00', 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, 1, 3, 3, 1),
(13, '2021-12-07 19:33:40.107874', '2021-12-07 19:33:40.107874', '500', 'EXTERNAL FASCILITIES', '0.00', '0.00', 0, 0, 0, NULL, NULL, '0.00', 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, 1, 3, 3, 1),
(14, '2021-12-07 19:33:59.041202', '2021-12-07 19:33:59.041202', '600', 'SHOP', '0.00', '0.00', 0, 0, 0, NULL, NULL, '0.00', 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, 1, 5, 5, 1),
(15, '2021-12-07 19:34:26.725002', '2021-12-15 04:49:34.522269', '700', 'SHARES', '0.00', '0.00', 0, 0, 0, NULL, NULL, '0.00', 0, 0, 0, 0, 2, 25, NULL, NULL, NULL, 1, 4, 4, 1),
(16, '2021-12-07 19:34:52.867563', '2021-12-07 19:34:52.867563', '701', 'SHARES INITIAL UPDATE', '0.00', '0.00', 0, 0, 0, NULL, NULL, '0.00', 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, 1, 3, 3, 1),
(17, '2021-12-07 19:35:12.173582', '2021-12-14 04:00:11.508694', '800', 'WELFARE', '0.00', '0.00', 0, 0, 0, NULL, NULL, '0.00', 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, 1, 5, 4, 1),
(18, '2021-12-07 19:35:35.019458', '2021-12-07 19:35:35.019458', '900', 'CASH WITHDRAWAL', '0.00', '0.00', 0, 0, 0, NULL, NULL, '0.00', 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, 1, 3, 3, 1),
(19, '2021-12-07 19:36:06.323242', '2021-12-07 19:38:10.472494', '901', 'TRANSACTION ADJUSTMENT', '3600.00', '3600.00', 0, 0, 0, NULL, NULL, '0.00', 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, 1, 3, 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `users_level`
--

CREATE TABLE `users_level` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users_level`
--

INSERT INTO `users_level` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, '1', '2021-12-07 19:07:30.171470', '2021-12-07 19:07:30.172472'),
(2, '2', '2021-12-07 19:07:30.213904', '2021-12-07 19:07:30.213904');

-- --------------------------------------------------------

--
-- Table structure for table `usertype`
--

CREATE TABLE `usertype` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `code` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usertype`
--

INSERT INTO `usertype` (`id`, `title`, `created_at`, `updated_at`, `code`) VALUES
(1, 'PRESIDENT', '2021-12-07 19:03:34.887239', '2021-12-07 19:03:34.887239', '2'),
(2, 'SECRETARY', '2021-12-07 19:03:34.939515', '2021-12-07 19:03:34.939515', '3'),
(3, 'TREASURER', '2021-12-07 19:03:35.050309', '2021-12-07 19:03:35.050309', '4'),
(4, 'FIN SEC', '2021-12-07 19:03:35.087285', '2021-12-07 19:03:35.087285', '5'),
(5, 'DESK OFFICER', '2021-12-07 19:03:35.139256', '2021-12-07 19:03:35.139256', '6'),
(6, 'SEO', '2021-12-07 19:03:35.195221', '2021-12-07 19:03:35.195221', '7'),
(7, 'SHOP', '2021-12-07 19:03:35.252381', '2021-12-07 19:03:35.252381', '8'),
(8, 'AUDITOR', '2021-12-07 19:03:35.305544', '2021-12-07 19:03:35.305544', '9'),
(9, 'MEMBERS', '2021-12-07 19:03:35.328994', '2021-12-07 19:03:35.328994', '10');

-- --------------------------------------------------------

--
-- Table structure for table `welfare_upload_status`
--

CREATE TABLE `welfare_upload_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `welfare_upload_status`
--

INSERT INTO `welfare_upload_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'PENDING', '2021-12-07 19:08:11.563847', '2021-12-07 19:08:26.233026'),
(2, 'UPLOADED', '2021-12-07 19:08:11.604703', '2021-12-07 19:08:26.294236'),
(3, 'VERIFIED', '2021-12-07 19:08:11.693648', '2021-12-07 19:08:26.341661');

-- --------------------------------------------------------

--
-- Table structure for table `withdrawable_transactions`
--

CREATE TABLE `withdrawable_transactions` (
  `id` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `maturity` int(11) NOT NULL,
  `status_id` int(11) NOT NULL,
  `transaction_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `withdrawable_transactions`
--

INSERT INTO `withdrawable_transactions` (`id`, `created_at`, `updated_at`, `maturity`, `status_id`, `transaction_id`) VALUES
(1, '2021-12-15 05:00:18.594779', '2021-12-15 05:05:27.889794', 1, 2, 6);

-- --------------------------------------------------------

--
-- Table structure for table `withdrawal_status`
--

CREATE TABLE `withdrawal_status` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `withdrawal_status`
--

INSERT INTO `withdrawal_status` (`id`, `title`, `created_at`, `updated_at`) VALUES
(1, 'LOCKED', '2021-12-07 19:09:14.505388', '2021-12-07 19:09:14.505388'),
(2, 'UNLOCKED', '2021-12-07 19:09:14.543329', '2021-12-07 19:09:14.543329');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account_deductions`
--
ALTER TABLE `account_deductions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_accountd_salary_institution_i_d4415472_fk_cooperati` (`salary_institution_id`),
  ADD KEY `cooperative_accountd_transaction_period_i_e8a41bb8_fk_cooperati` (`transaction_period_id`),
  ADD KEY `cooperative_accountd_transaction_status_i_6a4e1add_fk_cooperati` (`transaction_status_id`);

--
-- Indexes for table `account_types`
--
ALTER TABLE `account_types`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `admin_charges`
--
ALTER TABLE `admin_charges`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `admin_master`
--
ALTER TABLE `admin_master`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `admin_id` (`admin_id`);

--
-- Indexes for table `approvable_transactions`
--
ALTER TABLE `approvable_transactions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_approvab_status_id_3919c50f_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_approvab_transaction_id_46ce1115_fk_cooperati` (`transaction_id`);

--
-- Indexes for table `approval_officers`
--
ALTER TABLE `approval_officers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_approval_status_id_3fc776b5_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_approval_transaction_id_3b0ebc8d_fk_cooperati` (`transaction_id`),
  ADD KEY `cooperative_approval_officer_id_5fec8ff4_fk_cooperati` (`officer_id`);

--
-- Indexes for table `approval_status`
--
ALTER TABLE `approval_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auto_receipt`
--
ALTER TABLE `auto_receipt`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `banks`
--
ALTER TABLE `banks`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `cashbook`
--
ALTER TABLE `cashbook`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_cashbook_processed_by_id_75f6c017_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_cashbook_status_id_93f637b1_fk_cooperati` (`status_id`);

--
-- Indexes for table `certifiable_transactions`
--
ALTER TABLE `certifiable_transactions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_certifia_status_id_5c6a0730_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_certifia_transaction_id_b1de7f27_fk_cooperati` (`transaction_id`);

--
-- Indexes for table `certification_officers`
--
ALTER TABLE `certification_officers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_certific_status_id_b2a40928_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_certific_transaction_id_5c5e0dbf_fk_cooperati` (`transaction_id`),
  ADD KEY `cooperative_certific_officer_id_b84ee61c_fk_cooperati` (`officer_id`);

--
-- Indexes for table `certification_status`
--
ALTER TABLE `certification_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `cheque_table`
--
ALTER TABLE `cheque_table`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_cheque_t_approval_status_id_8fe45598_fk_cooperati` (`approval_status_id`),
  ADD KEY `cooperative_cheque_t_bank_id_b69de3d7_fk_cooperati` (`bank_id`),
  ADD KEY `cooperative_cheque_t_sales_id_29bbbe8f_fk_cooperati` (`sales_id`),
  ADD KEY `cooperative_cheque_t_status_id_5b8d9344_fk_cooperati` (`status_id`);

--
-- Indexes for table `compulsory_savings`
--
ALTER TABLE `compulsory_savings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_compulso_transaction_id_20fcbc03_fk_cooperati` (`transaction_id`);

--
-- Indexes for table `cooperative_bank_accounts`
--
ALTER TABLE `cooperative_bank_accounts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_cooperat_account_type_id_64835fb0_fk_cooperati` (`account_type_id`),
  ADD KEY `cooperative_cooperat_bank_id_a491b6dd_fk_cooperati` (`bank_id`);

--
-- Indexes for table `cooperative_shop_ledger`
--
ALTER TABLE `cooperative_shop_ledger`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_cooperat_processed_by_id_138e9a9e_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_cooperat_status_id_7062d84a_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_cooperat_member_id_bb6d14dd_fk_cooperati` (`member_id`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `customer_id` (`customer_id`),
  ADD KEY `cooperative_customer_cust_status_id_0caa2f8b_fk_cooperati` (`cust_status_id`),
  ADD KEY `cooperative_customer_locked_status_id_f438d1f2_fk_cooperati` (`locked_status_id`),
  ADD KEY `cooperative_customer_status_id_49bd06cc_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_customer_ticket_status_id_c8210255_fk_cooperati` (`ticket_status_id`),
  ADD KEY `cooperative_customer_processed_by_id_90b025c4_fk_cooperati` (`processed_by_id`);

--
-- Indexes for table `customer_id`
--
ALTER TABLE `customer_id`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `customuser`
--
ALTER TABLE `customuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `customuser_groups`
--
ALTER TABLE `customuser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cooperative_customuser_g_customuser_id_group_id_b73d6464_uniq` (`customuser_id`,`group_id`),
  ADD KEY `cooperative_customuser_groups_group_id_d17c1a3c_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `customuser_user_permissions`
--
ALTER TABLE `customuser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cooperative_customuser_u_customuser_id_permission_0e94bbf4_uniq` (`customuser_id`,`permission_id`),
  ADD KEY `cooperative_customus_permission_id_92930466_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `daily_sales`
--
ALTER TABLE `daily_sales`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_daily_sa_status_id_4352b06e_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_daily_sa_processed_by_id_2e0e8d92_fk_cooperati` (`processed_by_id`),
  ADD KEY `Daily_Sales_product_id_9911296e_fk_Stock_id` (`product_id`);

--
-- Indexes for table `daily_sales_cash_flow_summary`
--
ALTER TABLE `daily_sales_cash_flow_summary`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_daily_sa_processed_by_id_6c866e8b_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_daily_sa_sales_category_id_62a8e3c2_fk_cooperati` (`sales_category_id`),
  ADD KEY `cooperative_daily_sa_status_id_d2e536a1_fk_cooperati` (`status_id`);

--
-- Indexes for table `daily_sales_summary`
--
ALTER TABLE `daily_sales_summary`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_daily_sa_sale_id_57835ba4_fk_cooperati` (`sale_id`),
  ADD KEY `cooperative_daily_sa_sales_category_id_1c4a4afb_fk_cooperati` (`sales_category_id`),
  ADD KEY `cooperative_daily_sa_status_id_d1d5f49a_fk_cooperati` (`status_id`);

--
-- Indexes for table `data_capture_manager`
--
ALTER TABLE `data_capture_manager`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_datacapt_status_id_b021528a_fk_cooperati` (`status_id`);

--
-- Indexes for table `datejoined_upload_status`
--
ALTER TABLE `datejoined_upload_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `default_password`
--
ALTER TABLE `default_password`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `departments`
--
ALTER TABLE `departments`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `disbursement_officers`
--
ALTER TABLE `disbursement_officers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_disburse_officer_id_4eb840f2_fk_cooperati` (`officer_id`),
  ADD KEY `cooperative_disburse_status_id_6b79cac8_fk_cooperati` (`status_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_cooperative_customuser_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `exclusive_status`
--
ALTER TABLE `exclusive_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `external_fascilities_main`
--
ALTER TABLE `external_fascilities_main`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_external_member_id_9651d4fe_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_external_status_id_063a1558_fk_cooperati` (`status_id`);

--
-- Indexes for table `external_fascilities_temp`
--
ALTER TABLE `external_fascilities_temp`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_external_approval_officer_id_5dc43a05_fk_cooperati` (`approval_officer_id`),
  ADD KEY `cooperative_external_member_id_62b5be5a_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_external_status_id_f3ada386_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_external_transaction_status_i_8ee7c466_fk_cooperati` (`transaction_status_id`);

--
-- Indexes for table `gender`
--
ALTER TABLE `gender`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `general_cash_sales_selected`
--
ALTER TABLE `general_cash_sales_selected`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_general__customer_id_cb4fa064_fk_cooperati` (`customer_id`),
  ADD KEY `cooperative_general__processed_by_id_c27217d4_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_general__product_id_0f7954bd_fk_cooperati` (`product_id`),
  ADD KEY `cooperative_general__status_id_d1290dcd_fk_cooperati` (`status_id`);

--
-- Indexes for table `general_cash_sales_selected_temp`
--
ALTER TABLE `general_cash_sales_selected_temp`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_general__customer_id_93c39a35_fk_cooperati` (`customer_id`),
  ADD KEY `cooperative_general__processed_by_id_89433fb4_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_general__product_id_d92d51d3_fk_cooperati` (`product_id`),
  ADD KEY `cooperative_general__status_id_61287130_fk_cooperati` (`status_id`);

--
-- Indexes for table `interest_deduction_source`
--
ALTER TABLE `interest_deduction_source`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `item_write_off_reasons`
--
ALTER TABLE `item_write_off_reasons`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `lga`
--
ALTER TABLE `lga`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_lga_state_id_39748dcd_fk_cooperative_states_id` (`state_id`);

--
-- Indexes for table `loanbased_savings`
--
ALTER TABLE `loanbased_savings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_loanbase_savings_id_b9d0a986_fk_cooperati` (`savings_id`);

--
-- Indexes for table `loans_cleared`
--
ALTER TABLE `loans_cleared`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_loanscle_loan_id_55855540_fk_cooperati` (`loan_id`),
  ADD KEY `cooperative_loanscle_processed_by_id_caad0a4f_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_loanscle_status_id_b6d5f70d_fk_cooperati` (`status_id`);

--
-- Indexes for table `loans_disbursed`
--
ALTER TABLE `loans_disbursed`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `loan_number` (`loan_number`),
  ADD KEY `cooperative_loansdis_loan_merge_status_id_5f02a31c_fk_cooperati` (`loan_merge_status_id`),
  ADD KEY `cooperative_loansdis_member_id_4ed30f30_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_loansdis_processed_by_id_3872119e_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_loansdis_schedule_status_id_2fa9503c_fk_cooperati` (`schedule_status_id`),
  ADD KEY `cooperative_loansdis_status_id_d74a93f6_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_loansdis_transaction_id_cdd92336_fk_cooperati` (`transaction_id`);

--
-- Indexes for table `loans_repayment_base`
--
ALTER TABLE `loans_repayment_base`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `loan_number` (`loan_number`),
  ADD KEY `cooperative_loansrep_loan_merge_status_id_fc97f5ac_fk_cooperati` (`loan_merge_status_id`),
  ADD KEY `cooperative_loansrep_member_id_385bc815_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_loansrep_processed_by_id_abca3dcd_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_loansrep_status_id_8ec6bfb4_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_loansrep_transaction_id_1d0aa132_fk_cooperati` (`transaction_id`);

--
-- Indexes for table `loans_uploaded`
--
ALTER TABLE `loans_uploaded`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_loansupl_member_id_22014c91_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_loansupl_processed_by_id_b59180fb_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_loansupl_status_id_479cd4ca_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_loansupl_transaction_id_8d3bbba8_fk_cooperati` (`transaction_id`),
  ADD KEY `cooperative_loansupl_transaction_period_i_8bf3f941_fk_cooperati` (`transaction_period_id`);

--
-- Indexes for table `loan_application`
--
ALTER TABLE `loan_application`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_loanappl_applicant_id_9d3be4dc_fk_cooperati` (`applicant_id`),
  ADD KEY `cooperative_loanappl_approval_officer_id_c39a4ef7_fk_cooperati` (`approval_officer_id`),
  ADD KEY `cooperative_loanappl_approval_status_id_72205139_fk_cooperati` (`approval_status_id`),
  ADD KEY `cooperative_loanappl_bank_account_id_3168c967_fk_cooperati` (`bank_account_id`),
  ADD KEY `cooperative_loanappl_certification_office_270327a4_fk_cooperati` (`certification_officer_id`),
  ADD KEY `cooperative_loanappl_certification_status_9f075a41_fk_cooperati` (`certification_status_id`),
  ADD KEY `cooperative_loanappl_nok_id_537ae27d_fk_cooperati` (`nok_id`),
  ADD KEY `cooperative_loanappl_processed_by_id_8ee3fc62_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_loanappl_submission_status_id_a1c79d47_fk_cooperati` (`submission_status_id`),
  ADD KEY `cooperative_loanappl_transaction_status_i_7d4e8f01_fk_cooperati` (`transaction_status_id`);

--
-- Indexes for table `loan_application_guarnators`
--
ALTER TABLE `loan_application_guarnators`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_loanappl_applicant_id_f6551a91_fk_cooperati` (`applicant_id`),
  ADD KEY `cooperative_loanappl_guarantor_id_601f9280_fk_cooperati` (`guarantor_id`),
  ADD KEY `cooperative_loanappl_status_id_d65aa7c0_fk_cooperati` (`status_id`);

--
-- Indexes for table `loan_application_settings`
--
ALTER TABLE `loan_application_settings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_loanappl_applicant_id_4e6bfe1f_fk_cooperati` (`applicant_id`),
  ADD KEY `cooperative_loanappl_status_id_01b4ef9e_fk_cooperati` (`status_id`);

--
-- Indexes for table `loan_category`
--
ALTER TABLE `loan_category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `loan_form_issuance`
--
ALTER TABLE `loan_form_issuance`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `receipt` (`receipt`),
  ADD KEY `cooperative_loanform_applicant_id_3ade63ff_fk_cooperati` (`applicant_id`),
  ADD KEY `cooperative_loanform_processing_status_id_9556b623_fk_cooperati` (`processing_status_id`),
  ADD KEY `cooperative_loanform_status_id_49e75f5b_fk_cooperati` (`status_id`);

--
-- Indexes for table `loan_guarantors`
--
ALTER TABLE `loan_guarantors`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_loanguar_applicant_id_98d9a865_fk_cooperati` (`applicant_id`),
  ADD KEY `cooperative_loanguar_guarantor_id_1494251c_fk_cooperati` (`guarantor_id`);

--
-- Indexes for table `loan_merge_status`
--
ALTER TABLE `loan_merge_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `loan_number`
--
ALTER TABLE `loan_number`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`);

--
-- Indexes for table `loan_request`
--
ALTER TABLE `loan_request`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_loanrequ_loan_id_5eba08b4_fk_cooperati` (`loan_id`),
  ADD KEY `cooperative_loanrequ_member_id_867cd581_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_loanrequ_processed_by_id_d5879392_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_loanrequ_submission_status_id_23cbecad_fk_cooperati` (`submission_status_id`),
  ADD KEY `cooperative_loanrequ_transaction_status_i_a0491541_fk_cooperati` (`transaction_status_id`),
  ADD KEY `cooperative_loanrequ_approval_officer_id_6324264e_fk_cooperati` (`approval_officer_id`),
  ADD KEY `cooperative_loanrequ_approval_status_id_41d717e4_fk_cooperati` (`approval_status_id`),
  ADD KEY `cooperative_loanrequ_certification_office_2ce9adea_fk_cooperati` (`certification_officer_id`),
  ADD KEY `cooperative_loanrequ_certification_status_37d8bf06_fk_cooperati` (`certification_status_id`);

--
-- Indexes for table `loan_request_attachments`
--
ALTER TABLE `loan_request_attachments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_loanrequ_applicant_id_841d2ab9_fk_cooperati` (`applicant_id`),
  ADD KEY `cooperative_loanrequ_processed_by_id_7f4eb144_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_loanrequ_status_id_4f43c832_fk_cooperati` (`status_id`);

--
-- Indexes for table `loan_request_settings`
--
ALTER TABLE `loan_request_settings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_loanrequ_applicant_id_a2225467_fk_cooperati` (`applicant_id`),
  ADD KEY `cooperative_loanrequ_status_id_676ccd1d_fk_cooperati` (`status_id`);

--
-- Indexes for table `loan_schedule_status`
--
ALTER TABLE `loan_schedule_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `loan_upload_status`
--
ALTER TABLE `loan_upload_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `locations`
--
ALTER TABLE `locations`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `locked_status`
--
ALTER TABLE `locked_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `member_id` (`member_id`),
  ADD UNIQUE KEY `phone_number` (`phone_number`),
  ADD UNIQUE KEY `file_no` (`file_no`),
  ADD UNIQUE KEY `ippis_no` (`ippis_no`),
  ADD UNIQUE KEY `admin_id` (`admin_id`),
  ADD KEY `cooperative_members_applicant_id_e09fc337_fk_cooperati` (`applicant_id`),
  ADD KEY `cooperative_members_date_joined_status_i_7bbc22a7_fk_cooperati` (`date_joined_status_id`),
  ADD KEY `cooperative_members_department_id_e65fe22f_fk_cooperati` (`department_id`),
  ADD KEY `cooperative_members_exclusive_status_id_51d36161_fk_cooperati` (`exclusive_status_id`),
  ADD KEY `cooperative_members_gender_id_c4fc6a21_fk_cooperative_gender_id` (`gender_id`),
  ADD KEY `cooperative_members_gross_pay_status_id_85f7b030_fk_cooperati` (`gross_pay_status_id`),
  ADD KEY `cooperative_members_lga_id_bd5a5755_fk_cooperative_lga_id` (`lga_id`),
  ADD KEY `cooperative_members_loan_status_id_a5efab6c_fk_cooperati` (`loan_status_id`),
  ADD KEY `cooperative_members_salary_institution_i_8e67dd09_fk_cooperati` (`salary_institution_id`),
  ADD KEY `cooperative_members_savings_status_id_fda63e18_fk_cooperati` (`savings_status_id`),
  ADD KEY `cooperative_members_shares_status_id_0ce19192_fk_cooperati` (`shares_status_id`),
  ADD KEY `cooperative_members_state_id_0f4a0b68_fk_cooperative_states_id` (`state_id`),
  ADD KEY `cooperative_members_status_id_e237b4c7_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_members_title_id_8fae45ea_fk_cooperative_titles_id` (`title_id`),
  ADD KEY `cooperative_members_welfare_status_id_819be377_fk_cooperati` (`welfare_status_id`);

--
-- Indexes for table `membership_form_sales_record`
--
ALTER TABLE `membership_form_sales_record`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `receipt` (`receipt`),
  ADD KEY `cooperative_membersh_applicant_id_09aa70f8_fk_cooperati` (`applicant_id`),
  ADD KEY `cooperative_membersh_bank_ccount_id_7b8cf7c9_fk_cooperati` (`bank_ccount_id`),
  ADD KEY `cooperative_membersh_processed_by_id_289ad034_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_membersh_status_id_ce6833f4_fk_cooperati` (`status_id`);

--
-- Indexes for table `membership_request`
--
ALTER TABLE `membership_request`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_membersh_salary_institution_i_492342ed_fk_cooperati` (`salary_institution_id`),
  ADD KEY `cooperative_membersh_submission_status_id_2f62e19e_fk_cooperati` (`submission_status_id`),
  ADD KEY `cooperative_membersh_title_id_5cd10778_fk_cooperati` (`title_id`),
  ADD KEY `cooperative_membersh_transaction_status_i_b8ab93fc_fk_cooperati` (`transaction_status_id`),
  ADD KEY `cooperative_membersh_approval_officer_id_7aace850_fk_cooperati` (`approval_officer_id`),
  ADD KEY `cooperative_membersh_approval_status_id_c73ceae4_fk_cooperati` (`approval_status_id`),
  ADD KEY `cooperative_membersh_certification_office_84393212_fk_cooperati` (`certification_officer_id`),
  ADD KEY `cooperative_membersh_certification_status_a1296436_fk_cooperati` (`certification_status_id`),
  ADD KEY `cooperative_membersh_department_id_25061106_fk_cooperati` (`department_id`),
  ADD KEY `cooperative_membersh_gender_id_d6ef02f0_fk_cooperati` (`gender_id`),
  ADD KEY `cooperative_membersh_processed_by_id_e8bcaf78_fk_cooperati` (`processed_by_id`);

--
-- Indexes for table `membership_request_additional_attachment`
--
ALTER TABLE `membership_request_additional_attachment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_membersh_applicant_id_79ec0df6_fk_cooperati` (`applicant_id`),
  ADD KEY `cooperative_membersh_officer_id_293819df_fk_cooperati` (`officer_id`);

--
-- Indexes for table `membership_request_additional_info`
--
ALTER TABLE `membership_request_additional_info`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_membersh_applicant_id_aca32681_fk_cooperati` (`applicant_id`),
  ADD KEY `cooperative_membersh_officer_id_ba6272be_fk_cooperati` (`officer_id`);

--
-- Indexes for table `membership_status`
--
ALTER TABLE `membership_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `members_accounts_domain`
--
ALTER TABLE `members_accounts_domain`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account_number` (`account_number`),
  ADD KEY `cooperative_membersa_member_id_e33a9f29_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_membersa_status_id_81d64d05_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_membersa_transaction_id_80628ced_fk_cooperati` (`transaction_id`);

--
-- Indexes for table `members_bank_accounts`
--
ALTER TABLE `members_bank_accounts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_membersb_status_id_a2d582a5_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_membersb_account_type_id_572c7d8d_fk_cooperati` (`account_type_id`),
  ADD KEY `cooperative_membersb_bank_id_e0c9d15c_fk_cooperati` (`bank_id`),
  ADD KEY `cooperative_membersb_lock_status_id_07dd6b1d_fk_cooperati` (`lock_status_id`),
  ADD KEY `cooperative_membersb_member_id_id_c566b560_fk_cooperati` (`member_id_id`);

--
-- Indexes for table `members_cash_deposits`
--
ALTER TABLE `members_cash_deposits`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_membersc_bank_accounts_id_530235c9_fk_cooperati` (`bank_accounts_id`),
  ADD KEY `cooperative_membersc_processed_by_id_766f6bc7_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_membersc_status_id_20f9931c_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_membersc_transaction_id_69e87d1b_fk_cooperati` (`transaction_id`),
  ADD KEY `cooperative_membersc_member_id_6dcb4f68_fk_cooperati` (`member_id`);

--
-- Indexes for table `members_cash_sales_selected`
--
ALTER TABLE `members_cash_sales_selected`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_members__member_id_f12c1667_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_members__processed_by_id_1bf13b4a_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_members__product_id_571ed9c9_fk_cooperati` (`product_id`),
  ADD KEY `cooperative_members__status_id_e5d21dba_fk_cooperati` (`status_id`);

--
-- Indexes for table `members_cash_withdrawals`
--
ALTER TABLE `members_cash_withdrawals`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_membersc_status_id_5fe65bd5_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_membersc_approval_officer_id_0b628f7d_fk_cooperati` (`approval_officer_id`),
  ADD KEY `cooperative_membersc_approval_status_id_32766724_fk_cooperati` (`approval_status_id`),
  ADD KEY `cooperative_membersc_processed_by_id_0381dd54_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_membersc_member_id_3ff3b2ef_fk_cooperati` (`member_id`);

--
-- Indexes for table `members_cash_withdrawals_application`
--
ALTER TABLE `members_cash_withdrawals_application`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_membersc_approval_officer_id_f874fb7c_fk_cooperati` (`approval_officer_id`),
  ADD KEY `cooperative_membersc_approval_status_id_6dff705e_fk_cooperati` (`approval_status_id`),
  ADD KEY `cooperative_membersc_member_id_31986766_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_membersc_processed_by_id_0e797fd4_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_membersc_status_id_9fc67f2a_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_membersc_certification_status_5d6b2a6d_fk_cooperati` (`certification_status_id`),
  ADD KEY `cooperative_memberscashwith_certification_officer_id_7ca0595e` (`certification_officer_id`);

--
-- Indexes for table `members_cash_withdrawals_main`
--
ALTER TABLE `members_cash_withdrawals_main`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_membersc_channel_id_09ddb831_fk_cooperati` (`channel_id`),
  ADD KEY `cooperative_membersc_coop_account_id_44828073_fk_cooperati` (`coop_account_id`),
  ADD KEY `cooperative_membersc_disbursement_status__e6628d3d_fk_cooperati` (`disbursement_status_id`),
  ADD KEY `cooperative_membersc_member_account_id_1cae9421_fk_cooperati` (`member_account_id`),
  ADD KEY `cooperative_membersc_processed_by_id_a3bc0338_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_membersc_status_id_ae5f6426_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_membersc_disbursement_officer_baba975a_fk_cooperati` (`disbursement_officer_id`),
  ADD KEY `cooperative_membersc_member_id_c981f24f_fk_cooperati` (`member_id`);

--
-- Indexes for table `members_credit_purchase_analysis`
--
ALTER TABLE `members_credit_purchase_analysis`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_members__status_id_06cee9c4_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_members__trans_code_id_6f32a93a_fk_cooperati` (`trans_code_id`);

--
-- Indexes for table `members_credit_purchase_summary`
--
ALTER TABLE `members_credit_purchase_summary`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_members__approval_officer_id_45bcbf04_fk_cooperati` (`approval_officer_id`),
  ADD KEY `cooperative_members__approval_status_id_7eb7cca3_fk_cooperati` (`approval_status_id`),
  ADD KEY `cooperative_members__status_id_ebdfde42_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_members__trans_code_id_b7d61d83_fk_cooperati` (`trans_code_id`);

--
-- Indexes for table `members_credit_sales_external_fascilities`
--
ALTER TABLE `members_credit_sales_external_fascilities`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_members__status_id_d098b648_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_members__trans_code_id_ca69eeb0_fk_cooperati` (`trans_code_id`);

--
-- Indexes for table `members_credit_sales_selected`
--
ALTER TABLE `members_credit_sales_selected`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_members__member_id_4647498d_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_members__processed_by_id_8d645168_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_members__product_id_c6966991_fk_cooperati` (`product_id`),
  ADD KEY `cooperative_members__status_id_ac97f5c5_fk_cooperati` (`status_id`);

--
-- Indexes for table `members_exclusiveness`
--
ALTER TABLE `members_exclusiveness`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_memberse_approval_officer_id_60c75194_fk_cooperati` (`approval_officer_id`),
  ADD KEY `cooperative_memberse_approval_status_id_255fe874_fk_cooperati` (`approval_status_id`),
  ADD KEY `cooperative_memberse_member_id_9f4cbc97_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_memberse_status_id_12f1d9b9_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_memberse_transaction_id_3d1e8e4d_fk_cooperati` (`transaction_id`);

--
-- Indexes for table `members_id_manager`
--
ALTER TABLE `members_id_manager`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `member_id` (`member_id`);

--
-- Indexes for table `members_next_of_kins`
--
ALTER TABLE `members_next_of_kins`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_membersn_lock_status_id_ca6c3505_fk_cooperati` (`lock_status_id`),
  ADD KEY `cooperative_membersn_member_id_e77adf44_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_membersn_relationships_id_5d6cee5b_fk_cooperati` (`relationships_id`),
  ADD KEY `cooperative_membersn_status_id_65064ff6_fk_cooperati` (`status_id`);

--
-- Indexes for table `members_salary_update_request`
--
ALTER TABLE `members_salary_update_request`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_memberss_approved_officer_id_fbd786a3_fk_cooperati` (`approved_officer_id`),
  ADD KEY `cooperative_memberss_member_id_cfb7b908_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_memberss_processing_status_id_1285d45b_fk_cooperati` (`processing_status_id`),
  ADD KEY `cooperative_memberss_status_id_8c5d0bf3_fk_cooperati` (`status_id`);

--
-- Indexes for table `members_share_accounts`
--
ALTER TABLE `members_share_accounts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_memberss_status_id_804f3b7f_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_memberss_processed_by_id_378a6c3d_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_memberss_member_id_e538ebdb_fk_cooperati` (`member_id`);

--
-- Indexes for table `members_share_accounts_main`
--
ALTER TABLE `members_share_accounts_main`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_memberss_member_id_0de1f805_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_memberss_processed_by_id_8f7203f7_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_memberss_status_id_f9127639_fk_cooperati` (`status_id`);

--
-- Indexes for table `members_share_configurations`
--
ALTER TABLE `members_share_configurations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `members_share_initial_update_request`
--
ALTER TABLE `members_share_initial_update_request`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_memberss_approval_officer_id_4f86b8f7_fk_cooperati` (`approval_officer_id`),
  ADD KEY `cooperative_memberss_approval_status_id_c0514aec_fk_cooperati` (`approval_status_id`),
  ADD KEY `cooperative_memberss_member_id_0160727d_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_memberss_processed_by_id_5c1153f6_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_memberss_status_id_5c0c48c0_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_memberss_transaction_id_7b62ba6e_fk_cooperati` (`transaction_id`);

--
-- Indexes for table `members_share_purchase_request`
--
ALTER TABLE `members_share_purchase_request`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_memberss_approval_officer_id_1c925cba_fk_cooperati` (`approval_officer_id`),
  ADD KEY `cooperative_memberss_approval_status_id_8fdd38c6_fk_cooperati` (`approval_status_id`),
  ADD KEY `cooperative_memberss_status_id_a780324b_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_memberss_member_id_77960f0e_fk_cooperati` (`member_id`);

--
-- Indexes for table `members_welfare`
--
ALTER TABLE `members_welfare`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `members_welfare_accounts`
--
ALTER TABLE `members_welfare_accounts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_membersw_processed_by_id_5882d0aa_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_membersw_status_id_a96d75fb_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_membersw_member_id_d18352c7_fk_cooperati` (`member_id`);

--
-- Indexes for table `monthly_deduction_list`
--
ALTER TABLE `monthly_deduction_list`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_monthlyd_member_id_375d7ea7_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_monthlyd_transaction_id_5eb192c8_fk_cooperati` (`transaction_id`),
  ADD KEY `cooperative_monthlyd_transaction_period_i_5ff7681e_fk_cooperati` (`transaction_period_id`),
  ADD KEY `cooperative_monthlyd_transaction_status_i_3dc5d8e3_fk_cooperati` (`transaction_status_id`);

--
-- Indexes for table `monthly_deduction_list_generated`
--
ALTER TABLE `monthly_deduction_list_generated`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_monthlyd_member_id_6cef745c_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_monthlyd_salary_institution_i_55fb0425_fk_cooperati` (`salary_institution_id`),
  ADD KEY `cooperative_monthlyd_transaction_period_i_b96f04dc_fk_cooperati` (`transaction_period_id`),
  ADD KEY `cooperative_monthlyd_transaction_status_i_50f3c119_fk_cooperati` (`transaction_status_id`);

--
-- Indexes for table `monthly_generated_transactions`
--
ALTER TABLE `monthly_generated_transactions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_monthlyg_processed_by_id_52656252_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_monthlyg_transaction_id_60ea583b_fk_cooperati` (`transaction_id`),
  ADD KEY `cooperative_monthlyg_transaction_period_i_d7e43231_fk_cooperati` (`transaction_period_id`),
  ADD KEY `cooperative_monthlyg_transaction_status_i_3b0b995c_fk_cooperati` (`transaction_status_id`);

--
-- Indexes for table `monthly_group_generated_transactions`
--
ALTER TABLE `monthly_group_generated_transactions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_monthlyg_processed_by_id_610b9c8e_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_monthlyg_salary_institution_i_043b8c06_fk_cooperati` (`salary_institution_id`),
  ADD KEY `cooperative_monthlyg_transaction_period_i_0725d14e_fk_cooperati` (`transaction_period_id`),
  ADD KEY `cooperative_monthlyg_transaction_status_i_bcb3cb05_fk_cooperati` (`transaction_status_id`);

--
-- Indexes for table `multiple_loan_status`
--
ALTER TABLE `multiple_loan_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `next_of_kins_maximun`
--
ALTER TABLE `next_of_kins_maximun`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `nok_relationships`
--
ALTER TABLE `nok_relationships`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `non_member_account_deductions`
--
ALTER TABLE `non_member_account_deductions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_nonmembe_salary_institution_i_f75e76ca_fk_cooperati` (`salary_institution_id`),
  ADD KEY `cooperative_nonmembe_transaction_period_i_d4618727_fk_cooperati` (`transaction_period_id`),
  ADD KEY `cooperative_nonmembe_transaction_status_i_ec80c2d5_fk_cooperati` (`transaction_status_id`);

--
-- Indexes for table `norminal_roll`
--
ALTER TABLE `norminal_roll`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_norminal_transaction_status_i_49fb22c0_fk_cooperati` (`transaction_status_id`);

--
-- Indexes for table `payment_channels`
--
ALTER TABLE `payment_channels`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `personal_ledger`
--
ALTER TABLE `personal_ledger`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_personal_member_id_c8e4fdae_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_personal_status_id_77a93bae_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_personal_transaction_id_74e5f476_fk_cooperati` (`transaction_id`);

--
-- Indexes for table `processing_status`
--
ALTER TABLE `processing_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `product_category`
--
ALTER TABLE `product_category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD UNIQUE KEY `code` (`code`);

--
-- Indexes for table `purchases`
--
ALTER TABLE `purchases`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_purchase_product_id_76c92658_fk_cooperati` (`product_id`),
  ADD KEY `cooperative_purchase_status_id_2c51a4e9_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_purchase_purchase_id_d29e58a9_fk_cooperati` (`purchase_id`);

--
-- Indexes for table `purchase_header`
--
ALTER TABLE `purchase_header`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_purchase_branch_id_59820d84_fk_cooperati` (`branch_id`),
  ADD KEY `cooperative_purchase_processed_by_id_4cc4d41d_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_purchase_personnel_id_c1030139_fk_cooperati` (`personnel_id`),
  ADD KEY `cooperative_purchase_status_id_b5d5ab14_fk_cooperati` (`status_id`),
  ADD KEY `purchaseheader_certification_status_c8c121e0_fk_certifica` (`certification_status_id`);

--
-- Indexes for table `purchase_temp`
--
ALTER TABLE `purchase_temp`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_purchase_product_id_7cbc33bf_fk_cooperati` (`product_id`),
  ADD KEY `cooperative_purchase_purchase_id_f3bac57a_fk_cooperati` (`purchase_id`);

--
-- Indexes for table `receipts`
--
ALTER TABLE `receipts`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `receipt` (`receipt`),
  ADD KEY `cooperative_receipts_status_id_82976e34_fk_cooperati` (`status_id`);

--
-- Indexes for table `receipts_shop`
--
ALTER TABLE `receipts_shop`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `receipt` (`receipt`),
  ADD KEY `cooperative_receipts_status_id_69054ec2_fk_cooperati` (`status_id`);

--
-- Indexes for table `receipt_cancelled`
--
ALTER TABLE `receipt_cancelled`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_receipt__processed_by_id_13c6cfa8_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_receipt__receipt_id_89e5e121_fk_cooperati` (`receipt_id`);

--
-- Indexes for table `receipt_status`
--
ALTER TABLE `receipt_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `receipt_types`
--
ALTER TABLE `receipt_types`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `salary_institution`
--
ALTER TABLE `salary_institution`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `sales_category`
--
ALTER TABLE `sales_category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `savings_uploaded`
--
ALTER TABLE `savings_uploaded`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_savingsu_processed_by_id_84233f52_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_savingsu_status_id_e83333a3_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_savingsu_transaction_period_i_4af1913c_fk_cooperati` (`transaction_period_id`),
  ADD KEY `cooperative_savingsu_transaction_id_9d4d82ce_fk_cooperati` (`transaction_id`);

--
-- Indexes for table `savings_upload_status`
--
ALTER TABLE `savings_upload_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `shares_deduction_savings`
--
ALTER TABLE `shares_deduction_savings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_sharesde_savings_id_b0fb65e8_fk_cooperati` (`savings_id`);

--
-- Indexes for table `shares_sales_record`
--
ALTER TABLE `shares_sales_record`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `receipt` (`receipt`),
  ADD KEY `cooperative_sharessa_processed_by_id_67af21d7_fk_cooperati` (`processed_by_id`),
  ADD KEY `cooperative_sharessa_status_id_b9934148_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_sharessa_member_id_65b4b766_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_sharessa_bank_account_id_45e2cff5_fk_cooperati` (`bank_account_id`);

--
-- Indexes for table `shares_units`
--
ALTER TABLE `shares_units`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unit` (`unit`);

--
-- Indexes for table `shares_upload_status`
--
ALTER TABLE `shares_upload_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `admin_id` (`admin_id`),
  ADD KEY `cooperative_staff_gender_id_4cf59a27_fk_cooperative_gender_id` (`gender_id`),
  ADD KEY `cooperative_staff_title_id_cf71f771_fk_cooperative_titles_id` (`title_id`),
  ADD KEY `cooperative_staff_userlevel_id_89a425f0_fk_cooperati` (`userlevel_id`);

--
-- Indexes for table `standing_order_accounts`
--
ALTER TABLE `standing_order_accounts`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cooperative_standingorderaccounts_transaction_id_afc89027_uniq` (`transaction_id`),
  ADD KEY `cooperative_standing_lock_status_id_b8d20134_fk_cooperati` (`lock_status_id`),
  ADD KEY `cooperative_standing_status_id_b21f7356_fk_cooperati` (`status_id`);

--
-- Indexes for table `states`
--
ALTER TABLE `states`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`),
  ADD KEY `cooperative_stock_category_id_98723c47_fk_cooperati` (`category_id`),
  ADD KEY `cooperative_stock_lock_status_id_8e7e7693_fk_cooperati` (`lock_status_id`);

--
-- Indexes for table `submission_status`
--
ALTER TABLE `submission_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `suppliers`
--
ALTER TABLE `suppliers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `suppliers_branches`
--
ALTER TABLE `suppliers_branches`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_supplier_supplier_id_7a8696ef_fk_cooperati` (`supplier_id`);

--
-- Indexes for table `suppliers_majors`
--
ALTER TABLE `suppliers_majors`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_supplier_supplier_id_d6d298ae_fk_cooperati` (`supplier_id`);

--
-- Indexes for table `suppliers_reps`
--
ALTER TABLE `suppliers_reps`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_supplier_suppliers_id_5afac6b5_fk_cooperati` (`suppliers_id`);

--
-- Indexes for table `task_manager`
--
ALTER TABLE `task_manager`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_taskmana_processed_by_id_60704725_fk_cooperati` (`processed_by_id`);

--
-- Indexes for table `ticket_status`
--
ALTER TABLE `ticket_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `titles`
--
ALTER TABLE `titles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `transaction_adjustment_request`
--
ALTER TABLE `transaction_adjustment_request`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_transact_approval_officer_id_ad022a14_fk_cooperati` (`approval_officer_id`),
  ADD KEY `cooperative_transact_approval_status_id_24d0ec5b_fk_cooperati` (`approval_status_id`),
  ADD KEY `cooperative_transact_status_id_1336ce26_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_transact_member_id_d2b30b6b_fk_cooperati` (`member_id`);

--
-- Indexes for table `transaction_loan_adjustment_request`
--
ALTER TABLE `transaction_loan_adjustment_request`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_transact_approval_officer_id_f529142b_fk_cooperati` (`approval_officer_id`),
  ADD KEY `cooperative_transact_approval_status_id_c31dc740_fk_cooperati` (`approval_status_id`),
  ADD KEY `cooperative_transact_member_id_d1e67775_fk_cooperati` (`member_id`),
  ADD KEY `cooperative_transact_status_id_dc690ac3_fk_cooperati` (`status_id`);

--
-- Indexes for table `transaction_periods`
--
ALTER TABLE `transaction_periods`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_transact_status_id_b5de2f45_fk_cooperati` (`status_id`);

--
-- Indexes for table `transaction_sources`
--
ALTER TABLE `transaction_sources`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `transaction_status`
--
ALTER TABLE `transaction_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `transaction_types`
--
ALTER TABLE `transaction_types`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `cooperative_transact_admin_charges_rating_a27914ec_fk_cooperati` (`admin_charges_rating_id`),
  ADD KEY `cooperative_transact_category_id_3ff2d119_fk_cooperati` (`category_id`),
  ADD KEY `cooperative_transact_interest_deduction_i_c2414dd1_fk_cooperati` (`interest_deduction_id`),
  ADD KEY `cooperative_transact_multiple_loan_status_0ef50b91_fk_cooperati` (`multiple_loan_status_id`),
  ADD KEY `cooperative_transact_receipt_type_id_57f2237f_fk_cooperati` (`receipt_type_id`),
  ADD KEY `cooperative_transact_source_id_35239a8d_fk_cooperati` (`source_id`),
  ADD KEY `cooperative_transact_status_id_e7d2f0c2_fk_cooperati` (`status_id`);

--
-- Indexes for table `users_level`
--
ALTER TABLE `users_level`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `usertype`
--
ALTER TABLE `usertype`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD UNIQUE KEY `code` (`code`);

--
-- Indexes for table `welfare_upload_status`
--
ALTER TABLE `welfare_upload_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `withdrawable_transactions`
--
ALTER TABLE `withdrawable_transactions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cooperative_withdraw_status_id_0f11cbcd_fk_cooperati` (`status_id`),
  ADD KEY `cooperative_withdraw_transaction_id_403178d4_fk_cooperati` (`transaction_id`);

--
-- Indexes for table `withdrawal_status`
--
ALTER TABLE `withdrawal_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account_deductions`
--
ALTER TABLE `account_deductions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `account_types`
--
ALTER TABLE `account_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `admin_charges`
--
ALTER TABLE `admin_charges`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `admin_master`
--
ALTER TABLE `admin_master`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `approvable_transactions`
--
ALTER TABLE `approvable_transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `approval_officers`
--
ALTER TABLE `approval_officers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `approval_status`
--
ALTER TABLE `approval_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=577;

--
-- AUTO_INCREMENT for table `auto_receipt`
--
ALTER TABLE `auto_receipt`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `banks`
--
ALTER TABLE `banks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `cashbook`
--
ALTER TABLE `cashbook`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `certifiable_transactions`
--
ALTER TABLE `certifiable_transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `certification_officers`
--
ALTER TABLE `certification_officers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `certification_status`
--
ALTER TABLE `certification_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `cheque_table`
--
ALTER TABLE `cheque_table`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `compulsory_savings`
--
ALTER TABLE `compulsory_savings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `cooperative_bank_accounts`
--
ALTER TABLE `cooperative_bank_accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `cooperative_shop_ledger`
--
ALTER TABLE `cooperative_shop_ledger`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `customer_id`
--
ALTER TABLE `customer_id`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `customuser`
--
ALTER TABLE `customuser`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=228;

--
-- AUTO_INCREMENT for table `customuser_groups`
--
ALTER TABLE `customuser_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customuser_user_permissions`
--
ALTER TABLE `customuser_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `daily_sales`
--
ALTER TABLE `daily_sales`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `daily_sales_cash_flow_summary`
--
ALTER TABLE `daily_sales_cash_flow_summary`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `daily_sales_summary`
--
ALTER TABLE `daily_sales_summary`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `data_capture_manager`
--
ALTER TABLE `data_capture_manager`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `datejoined_upload_status`
--
ALTER TABLE `datejoined_upload_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `default_password`
--
ALTER TABLE `default_password`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `departments`
--
ALTER TABLE `departments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `disbursement_officers`
--
ALTER TABLE `disbursement_officers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=145;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT for table `exclusive_status`
--
ALTER TABLE `exclusive_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `external_fascilities_main`
--
ALTER TABLE `external_fascilities_main`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `external_fascilities_temp`
--
ALTER TABLE `external_fascilities_temp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `gender`
--
ALTER TABLE `gender`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `general_cash_sales_selected`
--
ALTER TABLE `general_cash_sales_selected`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `general_cash_sales_selected_temp`
--
ALTER TABLE `general_cash_sales_selected_temp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `interest_deduction_source`
--
ALTER TABLE `interest_deduction_source`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `item_write_off_reasons`
--
ALTER TABLE `item_write_off_reasons`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `lga`
--
ALTER TABLE `lga`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=775;

--
-- AUTO_INCREMENT for table `loanbased_savings`
--
ALTER TABLE `loanbased_savings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `loans_cleared`
--
ALTER TABLE `loans_cleared`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `loans_disbursed`
--
ALTER TABLE `loans_disbursed`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `loans_repayment_base`
--
ALTER TABLE `loans_repayment_base`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `loans_uploaded`
--
ALTER TABLE `loans_uploaded`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `loan_application`
--
ALTER TABLE `loan_application`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `loan_application_guarnators`
--
ALTER TABLE `loan_application_guarnators`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `loan_application_settings`
--
ALTER TABLE `loan_application_settings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `loan_category`
--
ALTER TABLE `loan_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `loan_form_issuance`
--
ALTER TABLE `loan_form_issuance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `loan_guarantors`
--
ALTER TABLE `loan_guarantors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `loan_merge_status`
--
ALTER TABLE `loan_merge_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `loan_number`
--
ALTER TABLE `loan_number`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `loan_request`
--
ALTER TABLE `loan_request`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `loan_request_attachments`
--
ALTER TABLE `loan_request_attachments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `loan_request_settings`
--
ALTER TABLE `loan_request_settings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `loan_schedule_status`
--
ALTER TABLE `loan_schedule_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `loan_upload_status`
--
ALTER TABLE `loan_upload_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `locations`
--
ALTER TABLE `locations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `locked_status`
--
ALTER TABLE `locked_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `members`
--
ALTER TABLE `members`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=210;

--
-- AUTO_INCREMENT for table `membership_form_sales_record`
--
ALTER TABLE `membership_form_sales_record`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=407;

--
-- AUTO_INCREMENT for table `membership_request`
--
ALTER TABLE `membership_request`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=407;

--
-- AUTO_INCREMENT for table `membership_request_additional_attachment`
--
ALTER TABLE `membership_request_additional_attachment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `membership_request_additional_info`
--
ALTER TABLE `membership_request_additional_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `membership_status`
--
ALTER TABLE `membership_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `members_accounts_domain`
--
ALTER TABLE `members_accounts_domain`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=717;

--
-- AUTO_INCREMENT for table `members_bank_accounts`
--
ALTER TABLE `members_bank_accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `members_cash_deposits`
--
ALTER TABLE `members_cash_deposits`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `members_cash_sales_selected`
--
ALTER TABLE `members_cash_sales_selected`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `members_cash_withdrawals`
--
ALTER TABLE `members_cash_withdrawals`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `members_cash_withdrawals_application`
--
ALTER TABLE `members_cash_withdrawals_application`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `members_cash_withdrawals_main`
--
ALTER TABLE `members_cash_withdrawals_main`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `members_credit_purchase_analysis`
--
ALTER TABLE `members_credit_purchase_analysis`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `members_credit_purchase_summary`
--
ALTER TABLE `members_credit_purchase_summary`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `members_credit_sales_external_fascilities`
--
ALTER TABLE `members_credit_sales_external_fascilities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `members_credit_sales_selected`
--
ALTER TABLE `members_credit_sales_selected`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `members_exclusiveness`
--
ALTER TABLE `members_exclusiveness`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `members_id_manager`
--
ALTER TABLE `members_id_manager`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `members_next_of_kins`
--
ALTER TABLE `members_next_of_kins`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `members_salary_update_request`
--
ALTER TABLE `members_salary_update_request`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `members_share_accounts`
--
ALTER TABLE `members_share_accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `members_share_accounts_main`
--
ALTER TABLE `members_share_accounts_main`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `members_share_configurations`
--
ALTER TABLE `members_share_configurations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `members_share_initial_update_request`
--
ALTER TABLE `members_share_initial_update_request`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `members_share_purchase_request`
--
ALTER TABLE `members_share_purchase_request`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `members_welfare`
--
ALTER TABLE `members_welfare`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `members_welfare_accounts`
--
ALTER TABLE `members_welfare_accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `monthly_deduction_list`
--
ALTER TABLE `monthly_deduction_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `monthly_deduction_list_generated`
--
ALTER TABLE `monthly_deduction_list_generated`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `monthly_generated_transactions`
--
ALTER TABLE `monthly_generated_transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `monthly_group_generated_transactions`
--
ALTER TABLE `monthly_group_generated_transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `multiple_loan_status`
--
ALTER TABLE `multiple_loan_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `next_of_kins_maximun`
--
ALTER TABLE `next_of_kins_maximun`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `nok_relationships`
--
ALTER TABLE `nok_relationships`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `non_member_account_deductions`
--
ALTER TABLE `non_member_account_deductions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `norminal_roll`
--
ALTER TABLE `norminal_roll`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=401;

--
-- AUTO_INCREMENT for table `payment_channels`
--
ALTER TABLE `payment_channels`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `personal_ledger`
--
ALTER TABLE `personal_ledger`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `processing_status`
--
ALTER TABLE `processing_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `product_category`
--
ALTER TABLE `product_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=82;

--
-- AUTO_INCREMENT for table `purchases`
--
ALTER TABLE `purchases`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `purchase_header`
--
ALTER TABLE `purchase_header`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `purchase_temp`
--
ALTER TABLE `purchase_temp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `receipts`
--
ALTER TABLE `receipts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1001;

--
-- AUTO_INCREMENT for table `receipts_shop`
--
ALTER TABLE `receipts_shop`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=501;

--
-- AUTO_INCREMENT for table `receipt_cancelled`
--
ALTER TABLE `receipt_cancelled`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `receipt_status`
--
ALTER TABLE `receipt_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `receipt_types`
--
ALTER TABLE `receipt_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `salary_institution`
--
ALTER TABLE `salary_institution`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `sales_category`
--
ALTER TABLE `sales_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `savings_uploaded`
--
ALTER TABLE `savings_uploaded`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `savings_upload_status`
--
ALTER TABLE `savings_upload_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `shares_deduction_savings`
--
ALTER TABLE `shares_deduction_savings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `shares_sales_record`
--
ALTER TABLE `shares_sales_record`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `shares_units`
--
ALTER TABLE `shares_units`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `shares_upload_status`
--
ALTER TABLE `shares_upload_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `standing_order_accounts`
--
ALTER TABLE `standing_order_accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `states`
--
ALTER TABLE `states`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `stock`
--
ALTER TABLE `stock`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1174;

--
-- AUTO_INCREMENT for table `submission_status`
--
ALTER TABLE `submission_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `suppliers`
--
ALTER TABLE `suppliers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `suppliers_branches`
--
ALTER TABLE `suppliers_branches`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `suppliers_majors`
--
ALTER TABLE `suppliers_majors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `suppliers_reps`
--
ALTER TABLE `suppliers_reps`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `task_manager`
--
ALTER TABLE `task_manager`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ticket_status`
--
ALTER TABLE `ticket_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `titles`
--
ALTER TABLE `titles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `transaction_adjustment_request`
--
ALTER TABLE `transaction_adjustment_request`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `transaction_loan_adjustment_request`
--
ALTER TABLE `transaction_loan_adjustment_request`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `transaction_periods`
--
ALTER TABLE `transaction_periods`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `transaction_sources`
--
ALTER TABLE `transaction_sources`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `transaction_status`
--
ALTER TABLE `transaction_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `transaction_types`
--
ALTER TABLE `transaction_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `users_level`
--
ALTER TABLE `users_level`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `usertype`
--
ALTER TABLE `usertype`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `welfare_upload_status`
--
ALTER TABLE `welfare_upload_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `withdrawable_transactions`
--
ALTER TABLE `withdrawable_transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `withdrawal_status`
--
ALTER TABLE `withdrawal_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `account_deductions`
--
ALTER TABLE `account_deductions`
  ADD CONSTRAINT `cooperative_accountd_salary_institution_i_d4415472_fk_cooperati` FOREIGN KEY (`salary_institution_id`) REFERENCES `salary_institution` (`id`),
  ADD CONSTRAINT `cooperative_accountd_transaction_period_i_e8a41bb8_fk_cooperati` FOREIGN KEY (`transaction_period_id`) REFERENCES `transaction_periods` (`id`),
  ADD CONSTRAINT `cooperative_accountd_transaction_status_i_6a4e1add_fk_cooperati` FOREIGN KEY (`transaction_status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `admin_master`
--
ALTER TABLE `admin_master`
  ADD CONSTRAINT `cooperative_adminmas_admin_id_171473a7_fk_cooperati` FOREIGN KEY (`admin_id`) REFERENCES `customuser` (`id`);

--
-- Constraints for table `approvable_transactions`
--
ALTER TABLE `approvable_transactions`
  ADD CONSTRAINT `cooperative_approvab_status_id_3919c50f_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`),
  ADD CONSTRAINT `cooperative_approvab_transaction_id_46ce1115_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `transaction_types` (`id`);

--
-- Constraints for table `approval_officers`
--
ALTER TABLE `approval_officers`
  ADD CONSTRAINT `cooperative_approval_officer_id_5fec8ff4_fk_cooperati` FOREIGN KEY (`officer_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_approval_status_id_3fc776b5_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`),
  ADD CONSTRAINT `cooperative_approval_transaction_id_3b0ebc8d_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `approvable_transactions` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `cashbook`
--
ALTER TABLE `cashbook`
  ADD CONSTRAINT `cooperative_cashbook_processed_by_id_75f6c017_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_cashbook_status_id_93f637b1_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`);

--
-- Constraints for table `certifiable_transactions`
--
ALTER TABLE `certifiable_transactions`
  ADD CONSTRAINT `cooperative_certifia_status_id_5c6a0730_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`),
  ADD CONSTRAINT `cooperative_certifia_transaction_id_b1de7f27_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `transaction_types` (`id`);

--
-- Constraints for table `certification_officers`
--
ALTER TABLE `certification_officers`
  ADD CONSTRAINT `cooperative_certific_officer_id_b84ee61c_fk_cooperati` FOREIGN KEY (`officer_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_certific_status_id_b2a40928_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`),
  ADD CONSTRAINT `cooperative_certific_transaction_id_5c5e0dbf_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `certifiable_transactions` (`id`);

--
-- Constraints for table `cheque_table`
--
ALTER TABLE `cheque_table`
  ADD CONSTRAINT `cooperative_cheque_t_approval_status_id_8fe45598_fk_cooperati` FOREIGN KEY (`approval_status_id`) REFERENCES `approval_status` (`id`),
  ADD CONSTRAINT `cooperative_cheque_t_bank_id_b69de3d7_fk_cooperati` FOREIGN KEY (`bank_id`) REFERENCES `banks` (`id`),
  ADD CONSTRAINT `cooperative_cheque_t_sales_id_29bbbe8f_fk_cooperati` FOREIGN KEY (`sales_id`) REFERENCES `general_cash_sales_selected_temp` (`id`),
  ADD CONSTRAINT `cooperative_cheque_t_status_id_5b8d9344_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `compulsory_savings`
--
ALTER TABLE `compulsory_savings`
  ADD CONSTRAINT `cooperative_compulso_transaction_id_20fcbc03_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `transaction_types` (`id`);

--
-- Constraints for table `cooperative_bank_accounts`
--
ALTER TABLE `cooperative_bank_accounts`
  ADD CONSTRAINT `cooperative_cooperat_account_type_id_64835fb0_fk_cooperati` FOREIGN KEY (`account_type_id`) REFERENCES `account_types` (`id`),
  ADD CONSTRAINT `cooperative_cooperat_bank_id_a491b6dd_fk_cooperati` FOREIGN KEY (`bank_id`) REFERENCES `banks` (`id`);

--
-- Constraints for table `cooperative_shop_ledger`
--
ALTER TABLE `cooperative_shop_ledger`
  ADD CONSTRAINT `cooperative_cooperat_member_id_bb6d14dd_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members_accounts_domain` (`id`),
  ADD CONSTRAINT `cooperative_cooperat_processed_by_id_138e9a9e_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_cooperat_status_id_7062d84a_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `customers`
--
ALTER TABLE `customers`
  ADD CONSTRAINT `cooperative_customer_cust_status_id_0caa2f8b_fk_cooperati` FOREIGN KEY (`cust_status_id`) REFERENCES `membership_status` (`id`),
  ADD CONSTRAINT `cooperative_customer_locked_status_id_f438d1f2_fk_cooperati` FOREIGN KEY (`locked_status_id`) REFERENCES `locked_status` (`id`),
  ADD CONSTRAINT `cooperative_customer_processed_by_id_90b025c4_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_customer_status_id_49bd06cc_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `receipt_status` (`id`),
  ADD CONSTRAINT `cooperative_customer_ticket_status_id_c8210255_fk_cooperati` FOREIGN KEY (`ticket_status_id`) REFERENCES `ticket_status` (`id`);

--
-- Constraints for table `customuser_groups`
--
ALTER TABLE `customuser_groups`
  ADD CONSTRAINT `cooperative_customus_customuser_id_4dc56fa9_fk_cooperati` FOREIGN KEY (`customuser_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_customuser_groups_group_id_d17c1a3c_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `customuser_user_permissions`
--
ALTER TABLE `customuser_user_permissions`
  ADD CONSTRAINT `cooperative_customus_customuser_id_71c415a7_fk_cooperati` FOREIGN KEY (`customuser_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_customus_permission_id_92930466_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `daily_sales`
--
ALTER TABLE `daily_sales`
  ADD CONSTRAINT `Daily_Sales_product_id_9911296e_fk_Stock_id` FOREIGN KEY (`product_id`) REFERENCES `stock` (`id`),
  ADD CONSTRAINT `cooperative_daily_sa_processed_by_id_2e0e8d92_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_daily_sa_status_id_4352b06e_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `daily_sales_cash_flow_summary`
--
ALTER TABLE `daily_sales_cash_flow_summary`
  ADD CONSTRAINT `cooperative_daily_sa_processed_by_id_6c866e8b_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_daily_sa_sales_category_id_62a8e3c2_fk_cooperati` FOREIGN KEY (`sales_category_id`) REFERENCES `sales_category` (`id`),
  ADD CONSTRAINT `cooperative_daily_sa_status_id_d2e536a1_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `daily_sales_summary`
--
ALTER TABLE `daily_sales_summary`
  ADD CONSTRAINT `cooperative_daily_sa_sale_id_57835ba4_fk_cooperati` FOREIGN KEY (`sale_id`) REFERENCES `daily_sales` (`id`),
  ADD CONSTRAINT `cooperative_daily_sa_sales_category_id_1c4a4afb_fk_cooperati` FOREIGN KEY (`sales_category_id`) REFERENCES `sales_category` (`id`),
  ADD CONSTRAINT `cooperative_daily_sa_status_id_d1d5f49a_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `data_capture_manager`
--
ALTER TABLE `data_capture_manager`
  ADD CONSTRAINT `cooperative_datacapt_status_id_b021528a_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`);

--
-- Constraints for table `disbursement_officers`
--
ALTER TABLE `disbursement_officers`
  ADD CONSTRAINT `cooperative_disburse_officer_id_4eb840f2_fk_cooperati` FOREIGN KEY (`officer_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_disburse_status_id_6b79cac8_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_cooperative_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `customuser` (`id`);

--
-- Constraints for table `external_fascilities_main`
--
ALTER TABLE `external_fascilities_main`
  ADD CONSTRAINT `cooperative_external_member_id_9651d4fe_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `external_fascilities_temp` (`id`),
  ADD CONSTRAINT `cooperative_external_status_id_063a1558_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `external_fascilities_temp`
--
ALTER TABLE `external_fascilities_temp`
  ADD CONSTRAINT `cooperative_external_approval_officer_id_5dc43a05_fk_cooperati` FOREIGN KEY (`approval_officer_id`) REFERENCES `approval_officers` (`id`),
  ADD CONSTRAINT `cooperative_external_member_id_62b5be5a_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_external_status_id_f3ada386_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `approval_status` (`id`),
  ADD CONSTRAINT `cooperative_external_transaction_status_i_8ee7c466_fk_cooperati` FOREIGN KEY (`transaction_status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `general_cash_sales_selected`
--
ALTER TABLE `general_cash_sales_selected`
  ADD CONSTRAINT `cooperative_general__customer_id_cb4fa064_fk_cooperati` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  ADD CONSTRAINT `cooperative_general__processed_by_id_c27217d4_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_general__product_id_0f7954bd_fk_cooperati` FOREIGN KEY (`product_id`) REFERENCES `stock` (`id`),
  ADD CONSTRAINT `cooperative_general__status_id_d1290dcd_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `general_cash_sales_selected_temp`
--
ALTER TABLE `general_cash_sales_selected_temp`
  ADD CONSTRAINT `cooperative_general__customer_id_93c39a35_fk_cooperati` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  ADD CONSTRAINT `cooperative_general__processed_by_id_89433fb4_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_general__product_id_d92d51d3_fk_cooperati` FOREIGN KEY (`product_id`) REFERENCES `stock` (`id`),
  ADD CONSTRAINT `cooperative_general__status_id_61287130_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `lga`
--
ALTER TABLE `lga`
  ADD CONSTRAINT `cooperative_lga_state_id_39748dcd_fk_cooperative_states_id` FOREIGN KEY (`state_id`) REFERENCES `states` (`id`);

--
-- Constraints for table `loanbased_savings`
--
ALTER TABLE `loanbased_savings`
  ADD CONSTRAINT `cooperative_loanbase_savings_id_b9d0a986_fk_cooperati` FOREIGN KEY (`savings_id`) REFERENCES `transaction_types` (`id`);

--
-- Constraints for table `loans_cleared`
--
ALTER TABLE `loans_cleared`
  ADD CONSTRAINT `cooperative_loanscle_loan_id_55855540_fk_cooperati` FOREIGN KEY (`loan_id`) REFERENCES `loans_repayment_base` (`id`),
  ADD CONSTRAINT `cooperative_loanscle_processed_by_id_caad0a4f_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_loanscle_status_id_b6d5f70d_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `loans_disbursed`
--
ALTER TABLE `loans_disbursed`
  ADD CONSTRAINT `cooperative_loansdis_loan_merge_status_id_5f02a31c_fk_cooperati` FOREIGN KEY (`loan_merge_status_id`) REFERENCES `loan_merge_status` (`id`),
  ADD CONSTRAINT `cooperative_loansdis_member_id_4ed30f30_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_loansdis_processed_by_id_3872119e_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_loansdis_schedule_status_id_2fa9503c_fk_cooperati` FOREIGN KEY (`schedule_status_id`) REFERENCES `loan_schedule_status` (`id`),
  ADD CONSTRAINT `cooperative_loansdis_status_id_d74a93f6_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`),
  ADD CONSTRAINT `cooperative_loansdis_transaction_id_cdd92336_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `transaction_types` (`id`);

--
-- Constraints for table `loans_repayment_base`
--
ALTER TABLE `loans_repayment_base`
  ADD CONSTRAINT `cooperative_loansrep_loan_merge_status_id_fc97f5ac_fk_cooperati` FOREIGN KEY (`loan_merge_status_id`) REFERENCES `loan_merge_status` (`id`),
  ADD CONSTRAINT `cooperative_loansrep_member_id_385bc815_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_loansrep_processed_by_id_abca3dcd_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_loansrep_status_id_8ec6bfb4_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`),
  ADD CONSTRAINT `cooperative_loansrep_transaction_id_1d0aa132_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `transaction_types` (`id`);

--
-- Constraints for table `loans_uploaded`
--
ALTER TABLE `loans_uploaded`
  ADD CONSTRAINT `cooperative_loansupl_member_id_22014c91_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_loansupl_processed_by_id_b59180fb_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_loansupl_status_id_479cd4ca_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`),
  ADD CONSTRAINT `cooperative_loansupl_transaction_id_8d3bbba8_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `transaction_types` (`id`),
  ADD CONSTRAINT `cooperative_loansupl_transaction_period_i_8bf3f941_fk_cooperati` FOREIGN KEY (`transaction_period_id`) REFERENCES `transaction_periods` (`id`);

--
-- Constraints for table `loan_application`
--
ALTER TABLE `loan_application`
  ADD CONSTRAINT `cooperative_loanappl_applicant_id_9d3be4dc_fk_cooperati` FOREIGN KEY (`applicant_id`) REFERENCES `loan_form_issuance` (`id`),
  ADD CONSTRAINT `cooperative_loanappl_approval_officer_id_c39a4ef7_fk_cooperati` FOREIGN KEY (`approval_officer_id`) REFERENCES `approval_officers` (`id`),
  ADD CONSTRAINT `cooperative_loanappl_approval_status_id_72205139_fk_cooperati` FOREIGN KEY (`approval_status_id`) REFERENCES `approval_status` (`id`),
  ADD CONSTRAINT `cooperative_loanappl_bank_account_id_3168c967_fk_cooperati` FOREIGN KEY (`bank_account_id`) REFERENCES `members_bank_accounts` (`id`),
  ADD CONSTRAINT `cooperative_loanappl_certification_office_270327a4_fk_cooperati` FOREIGN KEY (`certification_officer_id`) REFERENCES `certification_officers` (`id`),
  ADD CONSTRAINT `cooperative_loanappl_certification_status_9f075a41_fk_cooperati` FOREIGN KEY (`certification_status_id`) REFERENCES `certification_status` (`id`),
  ADD CONSTRAINT `cooperative_loanappl_nok_id_537ae27d_fk_cooperati` FOREIGN KEY (`nok_id`) REFERENCES `members_next_of_kins` (`id`),
  ADD CONSTRAINT `cooperative_loanappl_processed_by_id_8ee3fc62_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_loanappl_submission_status_id_a1c79d47_fk_cooperati` FOREIGN KEY (`submission_status_id`) REFERENCES `submission_status` (`id`),
  ADD CONSTRAINT `cooperative_loanappl_transaction_status_i_7d4e8f01_fk_cooperati` FOREIGN KEY (`transaction_status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `loan_application_guarnators`
--
ALTER TABLE `loan_application_guarnators`
  ADD CONSTRAINT `cooperative_loanappl_applicant_id_f6551a91_fk_cooperati` FOREIGN KEY (`applicant_id`) REFERENCES `loan_application` (`id`),
  ADD CONSTRAINT `cooperative_loanappl_guarantor_id_601f9280_fk_cooperati` FOREIGN KEY (`guarantor_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_loanappl_status_id_d65aa7c0_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `loan_application_settings`
--
ALTER TABLE `loan_application_settings`
  ADD CONSTRAINT `cooperative_loanappl_applicant_id_4e6bfe1f_fk_cooperati` FOREIGN KEY (`applicant_id`) REFERENCES `loan_application` (`id`),
  ADD CONSTRAINT `cooperative_loanappl_status_id_01b4ef9e_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `loan_form_issuance`
--
ALTER TABLE `loan_form_issuance`
  ADD CONSTRAINT `cooperative_loanform_applicant_id_3ade63ff_fk_cooperati` FOREIGN KEY (`applicant_id`) REFERENCES `loan_request` (`id`),
  ADD CONSTRAINT `cooperative_loanform_processing_status_id_9556b623_fk_cooperati` FOREIGN KEY (`processing_status_id`) REFERENCES `processing_status` (`id`),
  ADD CONSTRAINT `cooperative_loanform_status_id_49e75f5b_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `loan_guarantors`
--
ALTER TABLE `loan_guarantors`
  ADD CONSTRAINT `cooperative_loanguar_applicant_id_98d9a865_fk_cooperati` FOREIGN KEY (`applicant_id`) REFERENCES `loan_request` (`id`),
  ADD CONSTRAINT `cooperative_loanguar_guarantor_id_1494251c_fk_cooperati` FOREIGN KEY (`guarantor_id`) REFERENCES `members` (`id`);

--
-- Constraints for table `loan_request`
--
ALTER TABLE `loan_request`
  ADD CONSTRAINT `cooperative_loanrequ_approval_officer_id_6324264e_fk_cooperati` FOREIGN KEY (`approval_officer_id`) REFERENCES `approval_officers` (`id`),
  ADD CONSTRAINT `cooperative_loanrequ_approval_status_id_41d717e4_fk_cooperati` FOREIGN KEY (`approval_status_id`) REFERENCES `approval_status` (`id`),
  ADD CONSTRAINT `cooperative_loanrequ_certification_office_2ce9adea_fk_cooperati` FOREIGN KEY (`certification_officer_id`) REFERENCES `certification_officers` (`id`),
  ADD CONSTRAINT `cooperative_loanrequ_certification_status_37d8bf06_fk_cooperati` FOREIGN KEY (`certification_status_id`) REFERENCES `certification_status` (`id`),
  ADD CONSTRAINT `cooperative_loanrequ_loan_id_5eba08b4_fk_cooperati` FOREIGN KEY (`loan_id`) REFERENCES `transaction_types` (`id`),
  ADD CONSTRAINT `cooperative_loanrequ_member_id_867cd581_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_loanrequ_processed_by_id_d5879392_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_loanrequ_submission_status_id_23cbecad_fk_cooperati` FOREIGN KEY (`submission_status_id`) REFERENCES `submission_status` (`id`),
  ADD CONSTRAINT `cooperative_loanrequ_transaction_status_i_a0491541_fk_cooperati` FOREIGN KEY (`transaction_status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `loan_request_attachments`
--
ALTER TABLE `loan_request_attachments`
  ADD CONSTRAINT `cooperative_loanrequ_applicant_id_841d2ab9_fk_cooperati` FOREIGN KEY (`applicant_id`) REFERENCES `loan_request` (`id`),
  ADD CONSTRAINT `cooperative_loanrequ_processed_by_id_7f4eb144_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_loanrequ_status_id_4f43c832_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `loan_request_settings`
--
ALTER TABLE `loan_request_settings`
  ADD CONSTRAINT `cooperative_loanrequ_applicant_id_a2225467_fk_cooperati` FOREIGN KEY (`applicant_id`) REFERENCES `loan_request` (`id`),
  ADD CONSTRAINT `cooperative_loanrequ_status_id_676ccd1d_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `members`
--
ALTER TABLE `members`
  ADD CONSTRAINT `cooperative_members_admin_id_01ca9538_fk_cooperati` FOREIGN KEY (`admin_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_members_applicant_id_e09fc337_fk_cooperati` FOREIGN KEY (`applicant_id`) REFERENCES `membership_form_sales_record` (`id`),
  ADD CONSTRAINT `cooperative_members_date_joined_status_i_7bbc22a7_fk_cooperati` FOREIGN KEY (`date_joined_status_id`) REFERENCES `datejoined_upload_status` (`id`),
  ADD CONSTRAINT `cooperative_members_department_id_e65fe22f_fk_cooperati` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`),
  ADD CONSTRAINT `cooperative_members_exclusive_status_id_51d36161_fk_cooperati` FOREIGN KEY (`exclusive_status_id`) REFERENCES `exclusive_status` (`id`),
  ADD CONSTRAINT `cooperative_members_gender_id_c4fc6a21_fk_cooperative_gender_id` FOREIGN KEY (`gender_id`) REFERENCES `gender` (`id`),
  ADD CONSTRAINT `cooperative_members_gross_pay_status_id_85f7b030_fk_cooperati` FOREIGN KEY (`gross_pay_status_id`) REFERENCES `processing_status` (`id`),
  ADD CONSTRAINT `cooperative_members_lga_id_bd5a5755_fk_cooperative_lga_id` FOREIGN KEY (`lga_id`) REFERENCES `lga` (`id`),
  ADD CONSTRAINT `cooperative_members_loan_status_id_a5efab6c_fk_cooperati` FOREIGN KEY (`loan_status_id`) REFERENCES `loan_upload_status` (`id`),
  ADD CONSTRAINT `cooperative_members_salary_institution_i_8e67dd09_fk_cooperati` FOREIGN KEY (`salary_institution_id`) REFERENCES `salary_institution` (`id`),
  ADD CONSTRAINT `cooperative_members_savings_status_id_fda63e18_fk_cooperati` FOREIGN KEY (`savings_status_id`) REFERENCES `savings_upload_status` (`id`),
  ADD CONSTRAINT `cooperative_members_shares_status_id_0ce19192_fk_cooperati` FOREIGN KEY (`shares_status_id`) REFERENCES `shares_upload_status` (`id`),
  ADD CONSTRAINT `cooperative_members_state_id_0f4a0b68_fk_cooperative_states_id` FOREIGN KEY (`state_id`) REFERENCES `states` (`id`),
  ADD CONSTRAINT `cooperative_members_status_id_e237b4c7_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`),
  ADD CONSTRAINT `cooperative_members_title_id_8fae45ea_fk_cooperative_titles_id` FOREIGN KEY (`title_id`) REFERENCES `titles` (`id`),
  ADD CONSTRAINT `cooperative_members_welfare_status_id_819be377_fk_cooperati` FOREIGN KEY (`welfare_status_id`) REFERENCES `welfare_upload_status` (`id`);

--
-- Constraints for table `membership_form_sales_record`
--
ALTER TABLE `membership_form_sales_record`
  ADD CONSTRAINT `cooperative_membersh_applicant_id_09aa70f8_fk_cooperati` FOREIGN KEY (`applicant_id`) REFERENCES `membership_request` (`id`),
  ADD CONSTRAINT `cooperative_membersh_bank_ccount_id_7b8cf7c9_fk_cooperati` FOREIGN KEY (`bank_ccount_id`) REFERENCES `cooperative_bank_accounts` (`id`),
  ADD CONSTRAINT `cooperative_membersh_processed_by_id_289ad034_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_membersh_status_id_ce6833f4_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `membership_request`
--
ALTER TABLE `membership_request`
  ADD CONSTRAINT `cooperative_membersh_approval_officer_id_7aace850_fk_cooperati` FOREIGN KEY (`approval_officer_id`) REFERENCES `approval_officers` (`id`),
  ADD CONSTRAINT `cooperative_membersh_approval_status_id_c73ceae4_fk_cooperati` FOREIGN KEY (`approval_status_id`) REFERENCES `approval_status` (`id`),
  ADD CONSTRAINT `cooperative_membersh_certification_office_84393212_fk_cooperati` FOREIGN KEY (`certification_officer_id`) REFERENCES `certification_officers` (`id`),
  ADD CONSTRAINT `cooperative_membersh_certification_status_a1296436_fk_cooperati` FOREIGN KEY (`certification_status_id`) REFERENCES `certification_status` (`id`),
  ADD CONSTRAINT `cooperative_membersh_department_id_25061106_fk_cooperati` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`),
  ADD CONSTRAINT `cooperative_membersh_gender_id_d6ef02f0_fk_cooperati` FOREIGN KEY (`gender_id`) REFERENCES `gender` (`id`),
  ADD CONSTRAINT `cooperative_membersh_processed_by_id_e8bcaf78_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_membersh_salary_institution_i_492342ed_fk_cooperati` FOREIGN KEY (`salary_institution_id`) REFERENCES `salary_institution` (`id`),
  ADD CONSTRAINT `cooperative_membersh_submission_status_id_2f62e19e_fk_cooperati` FOREIGN KEY (`submission_status_id`) REFERENCES `submission_status` (`id`),
  ADD CONSTRAINT `cooperative_membersh_title_id_5cd10778_fk_cooperati` FOREIGN KEY (`title_id`) REFERENCES `titles` (`id`),
  ADD CONSTRAINT `cooperative_membersh_transaction_status_i_b8ab93fc_fk_cooperati` FOREIGN KEY (`transaction_status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `membership_request_additional_attachment`
--
ALTER TABLE `membership_request_additional_attachment`
  ADD CONSTRAINT `cooperative_membersh_applicant_id_79ec0df6_fk_cooperati` FOREIGN KEY (`applicant_id`) REFERENCES `membership_request` (`id`),
  ADD CONSTRAINT `cooperative_membersh_officer_id_293819df_fk_cooperati` FOREIGN KEY (`officer_id`) REFERENCES `customuser` (`id`);

--
-- Constraints for table `membership_request_additional_info`
--
ALTER TABLE `membership_request_additional_info`
  ADD CONSTRAINT `cooperative_membersh_applicant_id_aca32681_fk_cooperati` FOREIGN KEY (`applicant_id`) REFERENCES `membership_request` (`id`),
  ADD CONSTRAINT `cooperative_membersh_officer_id_ba6272be_fk_cooperati` FOREIGN KEY (`officer_id`) REFERENCES `customuser` (`id`);

--
-- Constraints for table `members_accounts_domain`
--
ALTER TABLE `members_accounts_domain`
  ADD CONSTRAINT `cooperative_membersa_member_id_e33a9f29_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_membersa_status_id_81d64d05_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`),
  ADD CONSTRAINT `cooperative_membersa_transaction_id_80628ced_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `transaction_types` (`id`);

--
-- Constraints for table `members_bank_accounts`
--
ALTER TABLE `members_bank_accounts`
  ADD CONSTRAINT `cooperative_membersb_account_type_id_572c7d8d_fk_cooperati` FOREIGN KEY (`account_type_id`) REFERENCES `account_types` (`id`),
  ADD CONSTRAINT `cooperative_membersb_bank_id_e0c9d15c_fk_cooperati` FOREIGN KEY (`bank_id`) REFERENCES `banks` (`id`),
  ADD CONSTRAINT `cooperative_membersb_lock_status_id_07dd6b1d_fk_cooperati` FOREIGN KEY (`lock_status_id`) REFERENCES `locked_status` (`id`),
  ADD CONSTRAINT `cooperative_membersb_member_id_id_c566b560_fk_cooperati` FOREIGN KEY (`member_id_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_membersb_status_id_a2d582a5_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`);

--
-- Constraints for table `members_cash_deposits`
--
ALTER TABLE `members_cash_deposits`
  ADD CONSTRAINT `cooperative_membersc_bank_accounts_id_530235c9_fk_cooperati` FOREIGN KEY (`bank_accounts_id`) REFERENCES `cooperative_bank_accounts` (`id`),
  ADD CONSTRAINT `cooperative_membersc_member_id_6dcb4f68_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_membersc_processed_by_id_766f6bc7_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_membersc_status_id_20f9931c_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`),
  ADD CONSTRAINT `cooperative_membersc_transaction_id_69e87d1b_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `transaction_types` (`id`);

--
-- Constraints for table `members_cash_sales_selected`
--
ALTER TABLE `members_cash_sales_selected`
  ADD CONSTRAINT `cooperative_members__member_id_f12c1667_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_members__processed_by_id_1bf13b4a_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_members__product_id_571ed9c9_fk_cooperati` FOREIGN KEY (`product_id`) REFERENCES `stock` (`id`),
  ADD CONSTRAINT `cooperative_members__status_id_e5d21dba_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `members_cash_withdrawals`
--
ALTER TABLE `members_cash_withdrawals`
  ADD CONSTRAINT `cooperative_membersc_approval_officer_id_0b628f7d_fk_cooperati` FOREIGN KEY (`approval_officer_id`) REFERENCES `approval_officers` (`id`),
  ADD CONSTRAINT `cooperative_membersc_approval_status_id_32766724_fk_cooperati` FOREIGN KEY (`approval_status_id`) REFERENCES `approval_status` (`id`),
  ADD CONSTRAINT `cooperative_membersc_member_id_3ff3b2ef_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members_accounts_domain` (`id`),
  ADD CONSTRAINT `cooperative_membersc_processed_by_id_0381dd54_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_membersc_status_id_5fe65bd5_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `members_cash_withdrawals_application`
--
ALTER TABLE `members_cash_withdrawals_application`
  ADD CONSTRAINT `cooperative_membersc_approval_officer_id_f874fb7c_fk_cooperati` FOREIGN KEY (`approval_officer_id`) REFERENCES `approval_officers` (`id`),
  ADD CONSTRAINT `cooperative_membersc_approval_status_id_6dff705e_fk_cooperati` FOREIGN KEY (`approval_status_id`) REFERENCES `approval_status` (`id`),
  ADD CONSTRAINT `cooperative_membersc_certification_office_7ca0595e_fk_cooperati` FOREIGN KEY (`certification_officer_id`) REFERENCES `certification_officers` (`id`),
  ADD CONSTRAINT `cooperative_membersc_certification_status_5d6b2a6d_fk_cooperati` FOREIGN KEY (`certification_status_id`) REFERENCES `certification_status` (`id`),
  ADD CONSTRAINT `cooperative_membersc_member_id_31986766_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members_accounts_domain` (`id`),
  ADD CONSTRAINT `cooperative_membersc_processed_by_id_0e797fd4_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_membersc_status_id_9fc67f2a_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `members_cash_withdrawals_main`
--
ALTER TABLE `members_cash_withdrawals_main`
  ADD CONSTRAINT `cooperative_membersc_channel_id_09ddb831_fk_cooperati` FOREIGN KEY (`channel_id`) REFERENCES `payment_channels` (`id`),
  ADD CONSTRAINT `cooperative_membersc_coop_account_id_44828073_fk_cooperati` FOREIGN KEY (`coop_account_id`) REFERENCES `cooperative_bank_accounts` (`id`),
  ADD CONSTRAINT `cooperative_membersc_disbursement_officer_baba975a_fk_cooperati` FOREIGN KEY (`disbursement_officer_id`) REFERENCES `disbursement_officers` (`id`),
  ADD CONSTRAINT `cooperative_membersc_disbursement_status__e6628d3d_fk_cooperati` FOREIGN KEY (`disbursement_status_id`) REFERENCES `approval_status` (`id`),
  ADD CONSTRAINT `cooperative_membersc_member_account_id_1cae9421_fk_cooperati` FOREIGN KEY (`member_account_id`) REFERENCES `members_bank_accounts` (`id`),
  ADD CONSTRAINT `cooperative_membersc_member_id_c981f24f_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members_cash_withdrawals_application` (`id`),
  ADD CONSTRAINT `cooperative_membersc_processed_by_id_a3bc0338_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_membersc_status_id_ae5f6426_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `members_credit_purchase_analysis`
--
ALTER TABLE `members_credit_purchase_analysis`
  ADD CONSTRAINT `cooperative_members__status_id_06cee9c4_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`),
  ADD CONSTRAINT `cooperative_members__trans_code_id_6f32a93a_fk_cooperati` FOREIGN KEY (`trans_code_id`) REFERENCES `members_credit_sales_selected` (`id`);

--
-- Constraints for table `members_credit_purchase_summary`
--
ALTER TABLE `members_credit_purchase_summary`
  ADD CONSTRAINT `cooperative_members__approval_officer_id_45bcbf04_fk_cooperati` FOREIGN KEY (`approval_officer_id`) REFERENCES `approval_officers` (`id`),
  ADD CONSTRAINT `cooperative_members__approval_status_id_7eb7cca3_fk_cooperati` FOREIGN KEY (`approval_status_id`) REFERENCES `approval_status` (`id`),
  ADD CONSTRAINT `cooperative_members__status_id_ebdfde42_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`),
  ADD CONSTRAINT `cooperative_members__trans_code_id_b7d61d83_fk_cooperati` FOREIGN KEY (`trans_code_id`) REFERENCES `members_credit_sales_selected` (`id`);

--
-- Constraints for table `members_credit_sales_external_fascilities`
--
ALTER TABLE `members_credit_sales_external_fascilities`
  ADD CONSTRAINT `cooperative_members__status_id_d098b648_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`),
  ADD CONSTRAINT `cooperative_members__trans_code_id_ca69eeb0_fk_cooperati` FOREIGN KEY (`trans_code_id`) REFERENCES `members_credit_sales_selected` (`id`);

--
-- Constraints for table `members_credit_sales_selected`
--
ALTER TABLE `members_credit_sales_selected`
  ADD CONSTRAINT `cooperative_members__member_id_4647498d_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_members__processed_by_id_8d645168_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_members__product_id_c6966991_fk_cooperati` FOREIGN KEY (`product_id`) REFERENCES `stock` (`id`),
  ADD CONSTRAINT `cooperative_members__status_id_ac97f5c5_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `members_exclusiveness`
--
ALTER TABLE `members_exclusiveness`
  ADD CONSTRAINT `cooperative_memberse_approval_officer_id_60c75194_fk_cooperati` FOREIGN KEY (`approval_officer_id`) REFERENCES `approval_officers` (`id`),
  ADD CONSTRAINT `cooperative_memberse_approval_status_id_255fe874_fk_cooperati` FOREIGN KEY (`approval_status_id`) REFERENCES `approval_status` (`id`),
  ADD CONSTRAINT `cooperative_memberse_member_id_9f4cbc97_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_memberse_status_id_12f1d9b9_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`),
  ADD CONSTRAINT `cooperative_memberse_transaction_id_3d1e8e4d_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `transaction_types` (`id`);

--
-- Constraints for table `members_next_of_kins`
--
ALTER TABLE `members_next_of_kins`
  ADD CONSTRAINT `cooperative_membersn_lock_status_id_ca6c3505_fk_cooperati` FOREIGN KEY (`lock_status_id`) REFERENCES `locked_status` (`id`),
  ADD CONSTRAINT `cooperative_membersn_member_id_e77adf44_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_membersn_relationships_id_5d6cee5b_fk_cooperati` FOREIGN KEY (`relationships_id`) REFERENCES `nok_relationships` (`id`),
  ADD CONSTRAINT `cooperative_membersn_status_id_65064ff6_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`);

--
-- Constraints for table `members_salary_update_request`
--
ALTER TABLE `members_salary_update_request`
  ADD CONSTRAINT `cooperative_memberss_approved_officer_id_fbd786a3_fk_cooperati` FOREIGN KEY (`approved_officer_id`) REFERENCES `approval_officers` (`id`),
  ADD CONSTRAINT `cooperative_memberss_member_id_cfb7b908_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_memberss_processing_status_id_1285d45b_fk_cooperati` FOREIGN KEY (`processing_status_id`) REFERENCES `processing_status` (`id`),
  ADD CONSTRAINT `cooperative_memberss_status_id_8c5d0bf3_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `approval_status` (`id`);

--
-- Constraints for table `members_share_accounts`
--
ALTER TABLE `members_share_accounts`
  ADD CONSTRAINT `cooperative_memberss_member_id_e538ebdb_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members_accounts_domain` (`id`),
  ADD CONSTRAINT `cooperative_memberss_processed_by_id_378a6c3d_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_memberss_status_id_804f3b7f_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `members_share_accounts_main`
--
ALTER TABLE `members_share_accounts_main`
  ADD CONSTRAINT `cooperative_memberss_member_id_0de1f805_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_memberss_processed_by_id_8f7203f7_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_memberss_status_id_f9127639_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`);

--
-- Constraints for table `members_share_initial_update_request`
--
ALTER TABLE `members_share_initial_update_request`
  ADD CONSTRAINT `cooperative_memberss_approval_officer_id_4f86b8f7_fk_cooperati` FOREIGN KEY (`approval_officer_id`) REFERENCES `approval_officers` (`id`),
  ADD CONSTRAINT `cooperative_memberss_approval_status_id_c0514aec_fk_cooperati` FOREIGN KEY (`approval_status_id`) REFERENCES `approval_status` (`id`),
  ADD CONSTRAINT `cooperative_memberss_member_id_0160727d_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members_share_accounts` (`id`),
  ADD CONSTRAINT `cooperative_memberss_processed_by_id_5c1153f6_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_memberss_status_id_5c0c48c0_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`),
  ADD CONSTRAINT `cooperative_memberss_transaction_id_7b62ba6e_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `transaction_types` (`id`);

--
-- Constraints for table `members_share_purchase_request`
--
ALTER TABLE `members_share_purchase_request`
  ADD CONSTRAINT `cooperative_memberss_approval_officer_id_1c925cba_fk_cooperati` FOREIGN KEY (`approval_officer_id`) REFERENCES `approval_officers` (`id`),
  ADD CONSTRAINT `cooperative_memberss_approval_status_id_8fdd38c6_fk_cooperati` FOREIGN KEY (`approval_status_id`) REFERENCES `approval_status` (`id`),
  ADD CONSTRAINT `cooperative_memberss_member_id_77960f0e_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members_accounts_domain` (`id`),
  ADD CONSTRAINT `cooperative_memberss_status_id_a780324b_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `members_welfare_accounts`
--
ALTER TABLE `members_welfare_accounts`
  ADD CONSTRAINT `cooperative_membersw_member_id_d18352c7_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members_accounts_domain` (`id`),
  ADD CONSTRAINT `cooperative_membersw_processed_by_id_5882d0aa_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_membersw_status_id_a96d75fb_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `monthly_deduction_list`
--
ALTER TABLE `monthly_deduction_list`
  ADD CONSTRAINT `cooperative_monthlyd_member_id_375d7ea7_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_monthlyd_transaction_id_5eb192c8_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `transaction_types` (`id`),
  ADD CONSTRAINT `cooperative_monthlyd_transaction_period_i_5ff7681e_fk_cooperati` FOREIGN KEY (`transaction_period_id`) REFERENCES `transaction_periods` (`id`),
  ADD CONSTRAINT `cooperative_monthlyd_transaction_status_i_3dc5d8e3_fk_cooperati` FOREIGN KEY (`transaction_status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `monthly_deduction_list_generated`
--
ALTER TABLE `monthly_deduction_list_generated`
  ADD CONSTRAINT `cooperative_monthlyd_member_id_6cef745c_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_monthlyd_salary_institution_i_55fb0425_fk_cooperati` FOREIGN KEY (`salary_institution_id`) REFERENCES `salary_institution` (`id`),
  ADD CONSTRAINT `cooperative_monthlyd_transaction_period_i_b96f04dc_fk_cooperati` FOREIGN KEY (`transaction_period_id`) REFERENCES `transaction_periods` (`id`),
  ADD CONSTRAINT `cooperative_monthlyd_transaction_status_i_50f3c119_fk_cooperati` FOREIGN KEY (`transaction_status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `monthly_generated_transactions`
--
ALTER TABLE `monthly_generated_transactions`
  ADD CONSTRAINT `cooperative_monthlyg_processed_by_id_52656252_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_monthlyg_transaction_id_60ea583b_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `transaction_types` (`id`),
  ADD CONSTRAINT `cooperative_monthlyg_transaction_period_i_d7e43231_fk_cooperati` FOREIGN KEY (`transaction_period_id`) REFERENCES `transaction_periods` (`id`),
  ADD CONSTRAINT `cooperative_monthlyg_transaction_status_i_3b0b995c_fk_cooperati` FOREIGN KEY (`transaction_status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `monthly_group_generated_transactions`
--
ALTER TABLE `monthly_group_generated_transactions`
  ADD CONSTRAINT `cooperative_monthlyg_processed_by_id_610b9c8e_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_monthlyg_salary_institution_i_043b8c06_fk_cooperati` FOREIGN KEY (`salary_institution_id`) REFERENCES `salary_institution` (`id`),
  ADD CONSTRAINT `cooperative_monthlyg_transaction_period_i_0725d14e_fk_cooperati` FOREIGN KEY (`transaction_period_id`) REFERENCES `transaction_periods` (`id`),
  ADD CONSTRAINT `cooperative_monthlyg_transaction_status_i_bcb3cb05_fk_cooperati` FOREIGN KEY (`transaction_status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `non_member_account_deductions`
--
ALTER TABLE `non_member_account_deductions`
  ADD CONSTRAINT `cooperative_nonmembe_salary_institution_i_f75e76ca_fk_cooperati` FOREIGN KEY (`salary_institution_id`) REFERENCES `salary_institution` (`id`),
  ADD CONSTRAINT `cooperative_nonmembe_transaction_period_i_d4618727_fk_cooperati` FOREIGN KEY (`transaction_period_id`) REFERENCES `transaction_periods` (`id`),
  ADD CONSTRAINT `cooperative_nonmembe_transaction_status_i_ec80c2d5_fk_cooperati` FOREIGN KEY (`transaction_status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `norminal_roll`
--
ALTER TABLE `norminal_roll`
  ADD CONSTRAINT `cooperative_norminal_transaction_status_i_49fb22c0_fk_cooperati` FOREIGN KEY (`transaction_status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `personal_ledger`
--
ALTER TABLE `personal_ledger`
  ADD CONSTRAINT `cooperative_personal_member_id_c8e4fdae_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `cooperative_personal_status_id_77a93bae_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`),
  ADD CONSTRAINT `cooperative_personal_transaction_id_74e5f476_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `transaction_types` (`id`);

--
-- Constraints for table `purchases`
--
ALTER TABLE `purchases`
  ADD CONSTRAINT `cooperative_purchase_product_id_76c92658_fk_cooperati` FOREIGN KEY (`product_id`) REFERENCES `stock` (`id`),
  ADD CONSTRAINT `cooperative_purchase_purchase_id_d29e58a9_fk_cooperati` FOREIGN KEY (`purchase_id`) REFERENCES `purchase_header` (`id`),
  ADD CONSTRAINT `cooperative_purchase_status_id_2c51a4e9_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `purchase_header`
--
ALTER TABLE `purchase_header`
  ADD CONSTRAINT `cooperative_purchase_branch_id_59820d84_fk_cooperati` FOREIGN KEY (`branch_id`) REFERENCES `suppliers_branches` (`id`),
  ADD CONSTRAINT `cooperative_purchase_personnel_id_c1030139_fk_cooperati` FOREIGN KEY (`personnel_id`) REFERENCES `suppliers_reps` (`id`),
  ADD CONSTRAINT `cooperative_purchase_processed_by_id_4cc4d41d_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_purchase_status_id_b5d5ab14_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`),
  ADD CONSTRAINT `purchaseheader_certification_status_c8c121e0_fk_certifica` FOREIGN KEY (`certification_status_id`) REFERENCES `certification_status` (`id`);

--
-- Constraints for table `purchase_temp`
--
ALTER TABLE `purchase_temp`
  ADD CONSTRAINT `cooperative_purchase_product_id_7cbc33bf_fk_cooperati` FOREIGN KEY (`product_id`) REFERENCES `stock` (`id`),
  ADD CONSTRAINT `cooperative_purchase_purchase_id_f3bac57a_fk_cooperati` FOREIGN KEY (`purchase_id`) REFERENCES `purchase_header` (`id`);

--
-- Constraints for table `receipts`
--
ALTER TABLE `receipts`
  ADD CONSTRAINT `cooperative_receipts_status_id_82976e34_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `receipt_status` (`id`);

--
-- Constraints for table `receipts_shop`
--
ALTER TABLE `receipts_shop`
  ADD CONSTRAINT `cooperative_receipts_status_id_69054ec2_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `receipt_status` (`id`);

--
-- Constraints for table `receipt_cancelled`
--
ALTER TABLE `receipt_cancelled`
  ADD CONSTRAINT `cooperative_receipt__processed_by_id_13c6cfa8_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_receipt__receipt_id_89e5e121_fk_cooperati` FOREIGN KEY (`receipt_id`) REFERENCES `receipts` (`id`);

--
-- Constraints for table `savings_uploaded`
--
ALTER TABLE `savings_uploaded`
  ADD CONSTRAINT `cooperative_savingsu_processed_by_id_84233f52_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_savingsu_status_id_e83333a3_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`),
  ADD CONSTRAINT `cooperative_savingsu_transaction_id_9d4d82ce_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `members_accounts_domain` (`id`),
  ADD CONSTRAINT `cooperative_savingsu_transaction_period_i_4af1913c_fk_cooperati` FOREIGN KEY (`transaction_period_id`) REFERENCES `transaction_periods` (`id`);

--
-- Constraints for table `shares_deduction_savings`
--
ALTER TABLE `shares_deduction_savings`
  ADD CONSTRAINT `cooperative_sharesde_savings_id_b0fb65e8_fk_cooperati` FOREIGN KEY (`savings_id`) REFERENCES `transaction_types` (`id`);

--
-- Constraints for table `shares_sales_record`
--
ALTER TABLE `shares_sales_record`
  ADD CONSTRAINT `cooperative_sharessa_bank_account_id_45e2cff5_fk_cooperati` FOREIGN KEY (`bank_account_id`) REFERENCES `cooperative_bank_accounts` (`id`),
  ADD CONSTRAINT `cooperative_sharessa_member_id_65b4b766_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members_accounts_domain` (`id`),
  ADD CONSTRAINT `cooperative_sharessa_processed_by_id_67af21d7_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_sharessa_status_id_b9934148_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `staff`
--
ALTER TABLE `staff`
  ADD CONSTRAINT `cooperative_staff_admin_id_6022e122_fk_cooperative_customuser_id` FOREIGN KEY (`admin_id`) REFERENCES `customuser` (`id`),
  ADD CONSTRAINT `cooperative_staff_gender_id_4cf59a27_fk_cooperative_gender_id` FOREIGN KEY (`gender_id`) REFERENCES `gender` (`id`),
  ADD CONSTRAINT `cooperative_staff_title_id_cf71f771_fk_cooperative_titles_id` FOREIGN KEY (`title_id`) REFERENCES `titles` (`id`),
  ADD CONSTRAINT `cooperative_staff_userlevel_id_89a425f0_fk_cooperati` FOREIGN KEY (`userlevel_id`) REFERENCES `users_level` (`id`);

--
-- Constraints for table `standing_order_accounts`
--
ALTER TABLE `standing_order_accounts`
  ADD CONSTRAINT `cooperative_standing_lock_status_id_b8d20134_fk_cooperati` FOREIGN KEY (`lock_status_id`) REFERENCES `locked_status` (`id`),
  ADD CONSTRAINT `cooperative_standing_status_id_b21f7356_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`),
  ADD CONSTRAINT `cooperative_standing_transaction_id_afc89027_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `members_accounts_domain` (`id`);

--
-- Constraints for table `stock`
--
ALTER TABLE `stock`
  ADD CONSTRAINT `cooperative_stock_category_id_98723c47_fk_cooperati` FOREIGN KEY (`category_id`) REFERENCES `product_category` (`id`),
  ADD CONSTRAINT `cooperative_stock_lock_status_id_8e7e7693_fk_cooperati` FOREIGN KEY (`lock_status_id`) REFERENCES `locked_status` (`id`);

--
-- Constraints for table `suppliers_branches`
--
ALTER TABLE `suppliers_branches`
  ADD CONSTRAINT `cooperative_supplier_supplier_id_7a8696ef_fk_cooperati` FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`id`);

--
-- Constraints for table `suppliers_majors`
--
ALTER TABLE `suppliers_majors`
  ADD CONSTRAINT `cooperative_supplier_supplier_id_d6d298ae_fk_cooperati` FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`id`);

--
-- Constraints for table `suppliers_reps`
--
ALTER TABLE `suppliers_reps`
  ADD CONSTRAINT `cooperative_supplier_suppliers_id_5afac6b5_fk_cooperati` FOREIGN KEY (`suppliers_id`) REFERENCES `suppliers` (`id`);

--
-- Constraints for table `task_manager`
--
ALTER TABLE `task_manager`
  ADD CONSTRAINT `cooperative_taskmana_processed_by_id_60704725_fk_cooperati` FOREIGN KEY (`processed_by_id`) REFERENCES `customuser` (`id`);

--
-- Constraints for table `transaction_adjustment_request`
--
ALTER TABLE `transaction_adjustment_request`
  ADD CONSTRAINT `cooperative_transact_approval_officer_id_ad022a14_fk_cooperati` FOREIGN KEY (`approval_officer_id`) REFERENCES `approval_officers` (`id`),
  ADD CONSTRAINT `cooperative_transact_approval_status_id_24d0ec5b_fk_cooperati` FOREIGN KEY (`approval_status_id`) REFERENCES `approval_status` (`id`),
  ADD CONSTRAINT `cooperative_transact_member_id_d2b30b6b_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `members_accounts_domain` (`id`),
  ADD CONSTRAINT `cooperative_transact_status_id_1336ce26_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `transaction_loan_adjustment_request`
--
ALTER TABLE `transaction_loan_adjustment_request`
  ADD CONSTRAINT `cooperative_transact_approval_officer_id_f529142b_fk_cooperati` FOREIGN KEY (`approval_officer_id`) REFERENCES `approval_officers` (`id`),
  ADD CONSTRAINT `cooperative_transact_approval_status_id_c31dc740_fk_cooperati` FOREIGN KEY (`approval_status_id`) REFERENCES `approval_status` (`id`),
  ADD CONSTRAINT `cooperative_transact_member_id_d1e67775_fk_cooperati` FOREIGN KEY (`member_id`) REFERENCES `loans_repayment_base` (`id`),
  ADD CONSTRAINT `cooperative_transact_status_id_dc690ac3_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `transaction_status` (`id`);

--
-- Constraints for table `transaction_periods`
--
ALTER TABLE `transaction_periods`
  ADD CONSTRAINT `cooperative_transact_status_id_b5de2f45_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`);

--
-- Constraints for table `transaction_types`
--
ALTER TABLE `transaction_types`
  ADD CONSTRAINT `cooperative_transact_admin_charges_rating_a27914ec_fk_cooperati` FOREIGN KEY (`admin_charges_rating_id`) REFERENCES `admin_charges` (`id`),
  ADD CONSTRAINT `cooperative_transact_category_id_3ff2d119_fk_cooperati` FOREIGN KEY (`category_id`) REFERENCES `loan_category` (`id`),
  ADD CONSTRAINT `cooperative_transact_interest_deduction_i_c2414dd1_fk_cooperati` FOREIGN KEY (`interest_deduction_id`) REFERENCES `interest_deduction_source` (`id`),
  ADD CONSTRAINT `cooperative_transact_multiple_loan_status_0ef50b91_fk_cooperati` FOREIGN KEY (`multiple_loan_status_id`) REFERENCES `multiple_loan_status` (`id`),
  ADD CONSTRAINT `cooperative_transact_receipt_type_id_57f2237f_fk_cooperati` FOREIGN KEY (`receipt_type_id`) REFERENCES `receipt_types` (`id`),
  ADD CONSTRAINT `cooperative_transact_source_id_35239a8d_fk_cooperati` FOREIGN KEY (`source_id`) REFERENCES `transaction_sources` (`id`),
  ADD CONSTRAINT `cooperative_transact_status_id_e7d2f0c2_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `membership_status` (`id`);

--
-- Constraints for table `withdrawable_transactions`
--
ALTER TABLE `withdrawable_transactions`
  ADD CONSTRAINT `cooperative_withdraw_status_id_0f11cbcd_fk_cooperati` FOREIGN KEY (`status_id`) REFERENCES `withdrawal_status` (`id`),
  ADD CONSTRAINT `cooperative_withdraw_transaction_id_403178d4_fk_cooperati` FOREIGN KEY (`transaction_id`) REFERENCES `transaction_types` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
