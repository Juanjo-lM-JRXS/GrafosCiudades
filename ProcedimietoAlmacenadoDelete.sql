use ciudadescolombia;

delimiter //
-- Elimina las conexiones de un nodo
create procedure EliminarConexionesNodo(in nodoActual int)
begin
update conexiones set estado=0 where nodo=nodoActual;
call LeerUnaConexion(nodoActual);
end//
delimiter ;