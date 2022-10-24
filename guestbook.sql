-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2022-01-24 08:36:49
-- 伺服器版本： 10.4.22-MariaDB
-- PHP 版本： 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫: `test`
--

-- --------------------------------------------------------

--
-- 資料表結構 `guestbook`
--

CREATE TABLE `guestbook` (
  `id` int(11) NOT NULL,
  `title` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `msg` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `nickname` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 傾印資料表的資料 `guestbook`
--

INSERT INTO `guestbook` (`id`, `title`, `msg`, `nickname`) VALUES
(3, '3333', 'kkkkkk', ''),
(5, '55', 'gggggg', ''),
(7, 'test', 'test', ''),
(8, '搶頭香', 'I got it!!!!', 'JC');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `guestbook`
--
ALTER TABLE `guestbook`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `guestbook`
--
ALTER TABLE `guestbook`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
