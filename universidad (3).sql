-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-08-2024 a las 00:58:06
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cursos`
--

CREATE TABLE IF NOT EXISTS `cursos` (
  `ID_curso` int(10) NOT NULL,
  `Nombrecurso` varchar(20) NOT NULL,
  `Codigocurso` int(10) NOT NULL,
  `Departamento` varchar(80) NOT NULL,
  PRIMARY KEY (`Codigocurso`,`ID_curso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cursos`
--

INSERT INTO `cursos` (`ID_curso`, `Nombrecurso`, `Codigocurso`, `Departamento`) VALUES
(84500, 'Calculo I', 54700, 'Antioquia'),
(84500, 'Física Mecánica', 54701, 'Antioquia'),
(84500, 'Ingles', 54702, 'Antioquia'),
(84500, 'Humanidades', 54703, 'Antioquia\r\n'),
(84500, 'Probabilidad y Estad', 54704, 'Antioquia');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

CREATE TABLE IF NOT EXISTS `departamentos` (
  `IdDepartamentos` int(10) NOT NULL,
  `NombreDepartamento` varchar(60) NOT NULL,
  PRIMARY KEY (`IdDepartamentos`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `departamentos`
--

INSERT INTO `departamentos` (`IdDepartamentos`, `NombreDepartamento`) VALUES
(103043, 'Antioquia'),
(103052, 'Huila'),
(103054, 'Guajira '),
(103090, 'Caldas'),
(107001, 'Boyacá');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE IF NOT EXISTS `empleados` (
  `ID_empleado` int(11) NOT NULL,
  `Nombre` varchar(80) NOT NULL,
  `Num Identificación` int(11) NOT NULL,
  `Correo` varchar(80) NOT NULL,
  `Telefono` int(10) NOT NULL,
  PRIMARY KEY (`Telefono`,`ID_empleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`ID_empleado`, `Nombre`, `Num Identificación`, `Correo`, `Telefono`) VALUES
(57502, 'Armando Casas de Bareto', 1032096129, 'Armandorr@uni.edu.co', 0),
(57501, 'Angela María', 1032096138, 'Angelamaria@uni.edu.co', 300505120),
(57503, 'Enrique Villa ', 1032096142, 'EnriqueV@uni.edu.co', 300505132),
(57504, 'Alfonso de Jesús', 1032096193, 'AlfonsoJ@uni.edu.co', 300505199),
(57500, 'Rogelio Monarca', 1032096139, 'Rogeliomonarca12@Uni.edu.co', 312877420);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE IF NOT EXISTS `estudiantes` (
  `IdEstudiante` int(10) NOT NULL,
  `NombreEstudiante` varchar(20) NOT NULL,
  `ApellidoEstudiante` varchar(20) NOT NULL,
  `FechaNacimiento` date NOT NULL,
  `Genero` varchar(1) NOT NULL,
  `CorreoEstudiante` varchar(200) NOT NULL,
  `Telefono` int(11) NOT NULL,
  `Direccion` varchar(150) NOT NULL,
  PRIMARY KEY (`IdEstudiante`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`IdEstudiante`, `NombreEstudiante`, `ApellidoEstudiante`, `FechaNacimiento`, `Genero`, `CorreoEstudiante`, `Telefono`, `Direccion`) VALUES
(12564, 'Luis Antonio', 'Morales Morales', '0000-00-00', 'H', 'luismorales@uni.edu.co', 312877433, 'Calle 10 #45-36, El Poblado'),
(12565, 'Miguel María', 'Ramírez Velo', '0000-00-00', 'H', 'Miguelramirez@uni.edu.co', 300505132, 'Carrera 70 #45D-45, Laureles'),
(12566, 'Josefina Varvara ', 'Castillo de Flores', '0000-00-00', 'M', 'josefinaflores@uni.edu.co', 300505121, 'Calle 5 #36-24, Barrio Manila'),
(12567, 'Clara Inés', 'Rendon Córdoba', '0000-00-00', 'M', 'clararendon@uni.edu.co', 312871324, 'Carrera 32 #10A-15, El Poblado'),
(12568, 'Rolleiro de Jesús', 'Moreno Betancurt', '0000-00-00', 'H', 'rolleiromoreno@uni.edu.co', 300505130, 'Carrera 84 #32AA-26, Belén');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesores`
--

CREATE TABLE IF NOT EXISTS `profesores` (
  `IdProfesores` int(10) NOT NULL,
  `NombreProfesor` varchar(20) NOT NULL,
  `ApellidoProfesor` varchar(20) NOT NULL,
  `CorreoProfesor` text NOT NULL,
  `Telefono` int(11) NOT NULL,
  PRIMARY KEY (`IdProfesores`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `profesores`
--

INSERT INTO `profesores` (`IdProfesores`, `NombreProfesor`, `ApellidoProfesor`, `CorreoProfesor`, `Telefono`) VALUES
(20437, 'Natalia Gomez', 'Castilla Morales', 'nataliamorales@uni.edu.co', 321871093),
(20438, 'Carlos ', 'Alfonso López', 'Alfonsolopez@uni.edu.co', 300100143),
(21437, 'Juan David', 'Sánchez Perez', 'juanperez@uni.edu.co', 300505100),
(24770, 'Néstor David', 'Álzate Carmona', 'nestorcarmona@uni.edu.co', 314765098),
(24771, 'Luis Crlos', 'Muñoz Rendon', 'luiscarlos@uni.edu.co', 301456798);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
