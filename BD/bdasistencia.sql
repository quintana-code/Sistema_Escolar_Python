-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 05-06-2026 a las 05:09:01
-- Versión del servidor: 8.3.0
-- Versión de PHP: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bdasistencia`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumno`
--

DROP TABLE IF EXISTS `alumno`;
CREATE TABLE IF NOT EXISTS `alumno` (
  `IdAlumno` varchar(30) NOT NULL COMMENT 'No. control',
  `Nombre` varchar(100) NOT NULL,
  `Grupo` varchar(50) NOT NULL,
  PRIMARY KEY (`IdAlumno`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `alumno`
--

INSERT INTO `alumno` (`IdAlumno`, `Nombre`, `Grupo`) VALUES
('24801515', 'Quintana Hernandez  abril elizabeth', '4A'),
('24151813', 'Aaaron nano Leon', '4A'),
('18131215', 'abril elizabeth ramos osorio', '4A');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asistencia`
--

DROP TABLE IF EXISTS `asistencia`;
CREATE TABLE IF NOT EXISTS `asistencia` (
  `IdAsistencia` int NOT NULL AUTO_INCREMENT,
  `Fecha` date NOT NULL,
  `Estado` varchar(50) NOT NULL,
  `IdAlumno` varchar(30) NOT NULL,
  `IdMateria` int NOT NULL,
  PRIMARY KEY (`IdAsistencia`),
  KEY `fk_asistencia_alumno` (`IdAlumno`),
  KEY `fk_asistencia_materia` (`IdMateria`)
) ENGINE=MyISAM AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `asistencia`
--

INSERT INTO `asistencia` (`IdAsistencia`, `Fecha`, `Estado`, `IdAlumno`, `IdMateria`) VALUES
(46, '2026-06-04', 'Presente', '18131215', 3),
(45, '2026-06-04', 'Presente', '24151813', 3),
(44, '2026-06-04', 'Retardo', '24801515', 3),
(43, '2026-06-04', 'Ausente', '18131215', 1),
(42, '2026-06-04', 'Ausente', '24151813', 1),
(41, '2026-06-04', 'Ausente', '24801515', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupo`
--

DROP TABLE IF EXISTS `grupo`;
CREATE TABLE IF NOT EXISTS `grupo` (
  `IdGrupo` int NOT NULL AUTO_INCREMENT,
  `NombreGrupo` varchar(150) NOT NULL,
  `Carrera` varchar(150) NOT NULL,
  `semestre` int NOT NULL,
  PRIMARY KEY (`IdGrupo`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupo_alumno`
--

DROP TABLE IF EXISTS `grupo_alumno`;
CREATE TABLE IF NOT EXISTS `grupo_alumno` (
  `IdAlumno` varchar(30) NOT NULL,
  `IdGrupo` int NOT NULL,
  KEY `fk_asistencia_alumnos` (`IdAlumno`),
  KEY `fk_grupo_alumno_grupo` (`IdGrupo`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horario`
--

DROP TABLE IF EXISTS `horario`;
CREATE TABLE IF NOT EXISTS `horario` (
  `IdHorario` int NOT NULL AUTO_INCREMENT,
  `Dia` date NOT NULL,
  `Hora` time NOT NULL,
  `IdMateria` int NOT NULL,
  `IdGrupo` int NOT NULL,
  PRIMARY KEY (`IdHorario`),
  KEY `fk_grupo_materia_materia` (`IdMateria`),
  KEY `fk_grupo_materia_grupo` (`IdGrupo`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materia`
--

DROP TABLE IF EXISTS `materia`;
CREATE TABLE IF NOT EXISTS `materia` (
  `IdMateria` int NOT NULL AUTO_INCREMENT,
  `NombreMateria` varchar(150) NOT NULL,
  `IdUsuario` int NOT NULL,
  PRIMARY KEY (`IdMateria`),
  KEY `fk_usuario_usuario` (`IdUsuario`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `materia`
--

INSERT INTO `materia` (`IdMateria`, `NombreMateria`, `IdUsuario`) VALUES
(1, 'POO', 1),
(2, 'algebra', 5),
(3, 'Redes', 3),
(4, 'Calculo I.', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE IF NOT EXISTS `usuario` (
  `IdUsuario` int NOT NULL AUTO_INCREMENT,
  `NombreUsuario` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Password` varchar(150) NOT NULL,
  `Rol` varchar(150) NOT NULL,
  PRIMARY KEY (`IdUsuario`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`IdUsuario`, `NombreUsuario`, `Password`, `Rol`) VALUES
(1, 'Juan Carlos', '12345', 'Maestro'),
(2, 'Pepito morales', '123admin', 'Admin'),
(3, 'José martinez', '123maestro', 'Maestro'),
(4, 'Josue ochoa Ramirez', 'maestro123', 'Maestro');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
