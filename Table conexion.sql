use ciudadescolombia;
drop table conexiones;
create table conexiones(
	conexionesID int primary key auto_increment,
    nodo int,
    arista int,
    foreign key (nodo) references ciudades(CiudadID),
    foreign key (arista) references ciudades(CiudadID)
);

insert into conexiones (nodo,arista) values(1,7);

select * from conexiones;