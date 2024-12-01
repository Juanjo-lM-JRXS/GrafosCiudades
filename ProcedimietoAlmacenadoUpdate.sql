use ciudadescolombia;

delimiter //
-- Actualiza las conexiones de un nodo
create procedure ActualizaLasAristasNodo(in nodoActual int, in aristaOld int, in aristaNew int)
begin
update conexiones set arista=aristaNew where arista=aristaOld and nodo=nodoActual;
call LeerUnaConexion(nodoActual);
end//
delimiter ;