CREATE PROCEDURE `ConsultaCiudadId` (in id int)
BEGIN
	select c.CiudadNombre from ciudades as c where c.CiudadID = id;
END
