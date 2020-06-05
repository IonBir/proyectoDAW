-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3305
-- Tiempo de generación: 05-06-2020 a las 20:54:23
-- Versión del servidor: 5.7.26
-- Versión de PHP: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `proyecto`
--



-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `favoritos`
--

DROP TABLE IF EXISTS `favoritos`;
CREATE TABLE IF NOT EXISTS `favoritos` (
  `user_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `movie_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `genre_id` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `movie_poster` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `favoritos`
--

INSERT INTO `favoritos` (`user_id`, `movie_id`, `movie_name`, `genre_id`, `movie_poster`) VALUES
(46, 385103, 'Scoob!', 'Family', 'jHo2M1OiH9Re33jYtUQdfzPeUkx'),
(46, 338762, 'Bloodshot', 'Action', '8WUVHemHFH2ZIP6NWkwlHWsyrEL'),
(46, 686245, 'Survive the Night', 'Action', 'niyXFhGIk4W2WTcX2Eod8vx2Mfe'),
(46, 475557, 'Joker', 'Crime', 'udDclJoHjfjb8Ekgsd4FDteOkCU'),
(46, 495764, 'Birds of Prey (and the Fantabulous Emancipation of One Harley Quinn)', 'Action', 'h4VB6m0RwcicVEZvzftYZyKXs6K');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genre`
--

DROP TABLE IF EXISTS `genre`;
CREATE TABLE IF NOT EXISTS `genre` (
  `id` int(11) NOT NULL,
  `genre_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `genre`
--

INSERT INTO `genre` (`id`, `genre_name`) VALUES
(28, 'Action'),
(12, 'Adventure'),
(16, 'Animation'),
(35, 'Comedy'),
(80, 'Crime'),
(99, 'Documentary'),
(18, 'Drama'),
(10751, 'Family'),
(14, 'Fantasy'),
(36, 'History'),
(27, 'Horror'),
(10402, 'Music'),
(9648, 'Mystery'),
(10749, 'Romance'),
(878, 'Science Fiction'),
(10770, 'TV Movie'),
(53, 'Thriller'),
(10752, 'War'),
(37, 'Western');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `preferencias`
--

DROP TABLE IF EXISTS `preferencias`;
CREATE TABLE IF NOT EXISTS `preferencias` (
  `user_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`genre_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `review`
--

DROP TABLE IF EXISTS `review`;
CREATE TABLE IF NOT EXISTS `review` (
  `review_id` int(255) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `user_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `movie_id` int(11) NOT NULL,
  `review_text` text COLLATE utf8_unicode_ci NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`review_id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `review`
--

INSERT INTO `review` (`review_id`, `user_id`, `user_name`, `movie_id`, `review_text`, `date`) VALUES
(1, 3, '', 11, 'this is a review for star wars', '2020-05-25 17:29:29'),
(2, 3, '', 11, 'this is a review for star wars', '2020-05-25 17:29:29'),
(3, 11, '', 46, 'test for comment', '2020-05-25 17:29:29'),
(4, 11, '', 46, 'test for comment', '2020-05-25 17:29:29'),
(5, 11, '', 46, '', '2020-05-25 17:29:29'),
(6, 13475, '', 46, '', '2020-05-25 17:29:29'),
(7, 46, '', 13475, 'review for stark trek', '2020-05-25 17:29:29'),
(8, 46, '', 13475, 'review for stark trek 2', '2020-05-25 17:29:29'),
(9, 46, '', 13475, 'review for stark trek 2', '2020-05-25 17:29:29'),
(10, 46, '', 13475, 'review for stark trek 2', '2020-05-25 17:29:29'),
(11, 46, '', 13475, 'this comment now works.', '2020-05-25 17:29:29'),
(12, 46, '', 157336, 'This movie is very nice. 10/10', '2020-05-25 17:29:29'),
(13, 46, '', 10375, 'review', '2020-05-25 17:29:29'),
(14, 46, '', 10375, 'this review works\r\n', '2020-05-25 17:29:29'),
(15, 46, '', 10373, 'edtgswg', '2020-05-25 17:29:29'),
(16, 46, '', 385103, 'review works?', '2020-05-25 17:29:29'),
(17, 46, '', 338762, 'review', '2020-05-25 17:29:29'),
(18, 46, '', 454626, 'Esto es una reseña', '2020-05-25 17:29:29'),
(19, 46, '', 330457, 'testing timestamp', '2020-05-25 17:29:55'),
(20, 46, '', 201, 'What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills.\r\n\r\nI am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words.\r\n\r\nYou think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands.\r\n\r\nNot only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue.\r\n\r\nBut you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it.\r\n\r\nYou’re fucking dead, kiddo.', '2020-05-25 17:43:13'),
(21, 46, '', 495764, 'Esta pelicula es una mierda\r\n', '2020-05-29 19:43:06'),
(22, 46, '', 475557, '', '2020-05-31 09:06:35'),
(23, 46, 'abc', 508439, 'test review', '2020-05-31 11:07:13');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 NOT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `id_2` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=51 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `name`, `password`, `email`) VALUES
(20, 'changed', '1234567', 'qaAMNprueba@email.com'),
(26, 'changed', '1234567', '3asfd@yahoo.com'),
(46, 'abcd', 'pbkdf2:sha256:150000$emEUckhW$8f1f17943805f8fe81e730b17a8d52af76042d567e6d703637ded3b333bfa9eb', 'user@gmail.net'),
(45, 'awsdqw', 'pbkdf2:sha256:150000$31NHWMzt$27ba0ab2cd3e30a50bed88c8b22b98b62e26d05328dcf702378d17f02a2326a5', 'b2g@hmail.com'),
(44, 'comerei', 'pbkdf2:sha256:150000$UIyQkTFA$d016ae2696cd411eebc1d613bb07d873190fcfea1d51e4c7796667985cad6794', '2g@hmail.com'),
(43, 'comer1', 'pbkdf2:sha256:150000$PuWbdIC4$2fa75b0b23143d24d492186f12f4bccf2702e8c87b4a6a9a8411f43c29d3ada4', 'com1234'),
(42, 'comer', 'pbkdf2:sha256:150000$UWNUqL4k$85177a7a193246ccf79d3236e52c92ca122403b5629060e4cbb29868650ed1bb', 'g@hmail.com'),
(47, 'abcd', 'pbkdf2:sha256:150000$7ujgrlKm$941b1b4d0930d7ff427beced323f1f641001331a4db4709da29981b36898a12c', 'asdf@hm.com'),
(48, 'abc', 'pbkdf2:sha256:150000$5xL4oPCD$d3d96e3dc94d8dd38e17eb180724108322fd9663d21add950859e1e3339056e8', 'sadfgsg@hm.com'),
(49, 'jerr', 'pbkdf2:sha256:150000$XY6Vu6ny$88545bd30ed53fe6379cf9c7d590db8c3a6ccf231ee31e73ad22b06779fe3ccd', 'sdfgsdg@gm.com'),
(50, 'user', 'pbkdf2:sha256:150000$IthRQQwS$55b77cf632a6b1d38248673927c8ec6d7198cb252f3d6bf55e5ba69acabf4b8f', 'adsfdas@gmail.com');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
