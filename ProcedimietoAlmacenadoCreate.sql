use ciudadescolombia;

delimiter //
create procedure CreaUnaConexion(in nodoInput int, in aristaInput int)
begin
	insert into conexiones (nodo,arista) values(nodoInput,aristaInput);
end//
delimiter ;