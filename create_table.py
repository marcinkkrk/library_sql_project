import mysql.connector

db = mysql.connector.connect(user='root', password = 'root', host='127.0.0.1', port=3306) #połączenie
cursorObject = db.cursor()  #stworzenie kursora

regaly = """
    CREATE TABLE IF NOT EXISTS `dbksiazki`.`regaly` (
  `regal` INT NOT NULL,
  `polka` INT NOT NULL,
  `miejsce` INT NOT NULL,
  `idmiejsca` INT NOT NULL AUTO_INCREMENT,
  UNIQUE INDEX `idmiejsca_UNIQUE` (`idmiejsca` ASC) VISIBLE,
  PRIMARY KEY (`idmiejsca`));
"""
cursorObject.execute(regaly)
print("tabela regaly została utworzona...")

autor = """CREATE TABLE IF NOT EXISTS `dbksiazki`.`autor` (
  `idautor` INT NOT NULL AUTO_INCREMENT,
  `imie` VARCHAR(100) NOT NULL,
  `nazwisko` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idautor`),
  UNIQUE INDEX `idautor_UNIQUE` (`idautor` ASC) VISIBLE)
"""

cursorObject.execute(autor)
print("tabela autor została utworzona...")

ksiazki = """CREATE TABLE IF NOT EXISTS `dbksiazki`.`ksiazki` (
  `isbn` INT NOT NULL,
  `tytul` VARCHAR(200) NOT NULL,
  `oprawa` VARCHAR(45) NOT NULL,
  `strony` INT NOT NULL,
  `stan` VARCHAR(45) NOT NULL,
  `idmiejsca` INT NOT NULL,
  `autor` INT NOT NULL,
  PRIMARY KEY (`isbn`),
  UNIQUE INDEX `idksiazki_UNIQUE` (`isbn` ASC) VISIBLE,
  UNIQUE INDEX `tytul_UNIQUE` (`tytul` ASC) VISIBLE,
  INDEX `fk_ksiazki_regaly_idx` (`idmiejsca` ASC) VISIBLE,
  INDEX `fk_ksiazki_autor1_idx` (`autor` ASC) VISIBLE,
  CONSTRAINT `fk_ksiazki_regaly`
    FOREIGN KEY (`idmiejsca`)
    REFERENCES `dbksiazki`.`regaly` (`idmiejsca`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ksiazki_autor1`
    FOREIGN KEY (`autor`)
    REFERENCES `dbksiazki`.`autor` (`idautor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
"""

cursorObject.execute(ksiazki)
print("tabela ksiazki została utworzona...")


db.close()