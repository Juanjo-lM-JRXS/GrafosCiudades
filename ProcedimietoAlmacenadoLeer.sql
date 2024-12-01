use ciudadescolombia;

delimiter //
-- conocer las conexines de un nodo
create procedure LeerUnaConexion(in nodoInput int)
begin
select x.nodo ,c.CiudadNombre, x.arista, x.estado
from ciudades as c join conexiones as xCreaUnaConexion
on c.CiudadID=x.nodo where c.CiudadID=nodoInput;
end//
delimiter ;