CREATE DATABASE app_cortinas

DROP TABLE IF EXISTS `bobina`;

CREATE TABLE `bobina` (
  `id_lote` int NOT NULL,
  `cortina_id_codigo` int NOT NULL,
  `endereco_id_endereco` varchar(45) NOT NULL,
  `data_cadastro` date NOT NULL,
  `metragem` int NOT NULL,
  PRIMARY KEY (`id_lote`),
  KEY `fk_bobina_cortinas_idx` (`cortina_id_codigo`),
  KEY `fk_bobina_endereco1_idx` (`endereco_id_endereco`),
  CONSTRAINT `fk_bobina_cortinas` FOREIGN KEY (`cortina_id_codigo`) REFERENCES `cortina` (`id_codigo`),
  CONSTRAINT `fk_bobina_endereco1` FOREIGN KEY (`endereco_id_endereco`) REFERENCES `endereco` (`id_endereco`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOCK TABLES `bobina` WRITE;
UNLOCK TABLES;
DROP TABLE IF EXISTS `cortina`;
CREATE TABLE `cortina` (
  `id_codigo` int NOT NULL,
  `descricao` varchar(45) NOT NULL,
  PRIMARY KEY (`id_codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `cortina` WRITE;
UNLOCK TABLES;

DROP TABLE IF EXISTS `endereco`;
CREATE TABLE `endereco` (
  `id_endereco` varchar(45) NOT NULL,
  `tipo_endereco` varchar(45) NOT NULL,
  PRIMARY KEY (`id_endereco`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `endereco` WRITE;
UNLOCK TABLES;

DROP TABLE IF EXISTS `historico`;

CREATE TABLE `historico` (
  `id_historico` int NOT NULL,
  `bobina_id_lote` int NOT NULL,
  `user_id_user` int NOT NULL,
  `endereco_antigo` varchar(45) NOT NULL,
  `date_mov` date NOT NULL,
  `tipo_mov` varchar(45) NOT NULL,
  `metragem_antiga` int NOT NULL,
  PRIMARY KEY (`id_historico`),
  KEY `fk_historico_bobina1_idx` (`bobina_id_lote`),
  KEY `fk_historico_user1_idx` (`user_id_user`),
  KEY `fk_historico_bobina2_idx` (`endereco_antigo`),
  CONSTRAINT `fk_historico_bobina1` FOREIGN KEY (`bobina_id_lote`) REFERENCES `bobina` (`id_lote`),
  CONSTRAINT `fk_historico_user1` FOREIGN KEY (`user_id_user`) REFERENCES `user` (`id_user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `historico` WRITE;
UNLOCK TABLES;

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id_user` int NOT NULL,
  `user` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`id_user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOCK TABLES `user` WRITE;
UNLOCK TABLES;