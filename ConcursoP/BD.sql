create  database ConcursoP;
use ConcursoP;

/*==============================================================*/
/* Table: Alumnos                                                 */
/*==============================================================*/
create table Alumnos
(
   IdAlumno  int auto_increment not null,
   Nombre  varchar(150) not null,
   Sexo    varchar(15) not null,
   Telefono varchar(10) not null,
   Email   varchar(150) not null,
   IdTipo   int not null,
   Contraseña    varchar(15) not null,
   NumeroControl varchar(8) not null,
   Semestre      varchar(1) not null,
   IdCarrera      int not null,
   IdEquipo   int not null,
   NombreAsesor   varchar(150) not null,
   constraint pk_IdAlumno primary key (IdAlumno)
);
/*==============================================================*/
/* Table: Carreras                                                 */
/*==============================================================*/
create table Carreras
(
   IdCarrera  int auto_increment not null,
   Nombre  varchar(150) not null,
   Siglas    varchar(5) not null,
   constraint pk_IdCarrera primary key (IdCarrera)
);
/*==============================================================*/
/* Table: TipoUsuario                                                */
/*==============================================================*/
create table TipoUsuario
(
   IdTipo  int auto_increment not null,
   Alumno  varchar(150) not null,
   Asesor    varchar(250) not null,
   Staff varchar(150) not null,
   constraint pk_IdTipo primary key (IdTipo)
);
/*==============================================================*/
/* Table: Staff                                                 */
/*==============================================================*/
create table Staff
(
   IdStaff  int auto_increment not null,
   Nombre  varchar(150) not null,
   Sexo    varchar(15) not null,
   Telefono varchar(10) not null,
   Email   varchar(150) not null,
   IdTipo   int not null,
   Estatus varchar(15) not null,
   Contraseña    varchar(15) not null,
   constraint pk_IdStaff primary key (IdStaff)
);
/*==============================================================*/
/* Table: Equipos                                                 */
/*==============================================================*/
create table Equipos
(
   IdEquipo  int auto_increment not null,
   Nombre  varchar(150) not null,
   Integrantes    varchar(150) not null,
   Asesor varchar(150) not null,
   IdCategoria  int not null,
   Puntos   varchar(3) not null,
   ProblemasResueltos    varchar(200) not null,
   constraint pk_IdEquipo primary key (IdEquipo)
);
/*==============================================================*/
/* Table: ProblemasResueltos                                                 */
/*==============================================================*/
create table ProblemasResueltos
(
   IdProblema  int auto_increment not null,
   Tiempo  time not null,
   constraint pk_IdProblema primary key (IdProblema)
);
/*==============================================================*/
/* Table: Categorias                                                 */
/*==============================================================*/
create table Categorias
(
   IdCategoria  int auto_increment not null,
   Nombre  varchar(150) not null,
   SemestreLimite    varchar(1) not null,
   constraint pk_IdCategoria primary key (IdCategoria)
);
/*==============================================================*/
/* Table: Ediciones                                                 */
/*==============================================================*/
create table Ediciones
(
   IdEdicion  int auto_increment not null,
   Nombre  varchar(150) not null,
   FechaRegistro    date not null,
   FechaEvento date not null,
   constraint pk_IdEdicion primary key (IdEdicion)
);
/*==============================================================*/
/* Table: Banco                                                 */
/*==============================================================*/
create table Banco
(
   IdBanco  int auto_increment not null,
   Nombre  varchar(150) not null,
   Puntos    varchar(5) not null,
   Tiempo time not null,
   Descripcion   varchar(150) not null,
   ColorGlobo   varchar(20) not null,
   constraint pk_IdBanco primary key (IdBanco)
);
/*==============================================================*/
/* Table: Docente                                                 */
/*==============================================================*/
create table Docentes
(
   IdDocente  int auto_increment not null,
   Nombre  varchar(150) not null,
   Sexo    varchar(15) not null,
   Telefono varchar(10) not null,
   Email   varchar(150) not null,
   Estatus   varchar(15) not null,
   Contraseña    varchar(15) not null,
   IdTipo   int not null,
   NumeroDocente varchar(8) not null,
   Escolaridad      varchar(150) not null,
   Especialidad        varchar(150) not null,
   Cedula   varchar(150) not null,
   IdCarrera   int not null,
   constraint pk_IdDocente primary key (IdDocente)
);
/*==============================================================*/
/* Restricciones FK	alter													                                             */
/*==============================================================*/
alter table Alumnos add constraint carreraAl foreign key (IdCarrera)
      references Carreras (IdCarrera);
alter table Alumnos add constraint EquipoAl foreign key (IdEquipo)
      references Equipos (IdEquipo);
alter table Alumnos add constraint TipoAl foreign key (IdTipo)
      references TipoUsuario (IdTipo);
alter table Staff add constraint TipoStaff foreign key (IdTipo)
      references TipoUsuario (IdTipo);
alter table Equipos add constraint CatAl foreign key (IdCategoria)
      references Categorias (IdCategoria);
alter table Docentes add constraint DocentesCar foreign key (IdCarrera)
      references Carreras (IdCarrera);
alter table Docentes add constraint TipoDocentes foreign key (IdTipo)
      references TipoUsuario (IdTipo);

      
      
CREATE USER 'concurso'@'localhost' IDENTIFIED BY 'hola.123';
GRANT ALL PRIVILEGES ON ConcursoP.Alumnos TO 'concurso'@'localhost';
GRANT ALL PRIVILEGES ON ConcursoP.Docentes TO 'concurso'@'localhost';
GRANT ALL PRIVILEGES ON ConcursoP.Carreras TO 'concurso'@'localhost';
GRANT ALL PRIVILEGES ON ConcursoP.Equipos TO 'concurso'@'localhost';
GRANT ALL PRIVILEGES ON ConcursoP.Categorias TO 'concurso'@'localhost';
GRANT ALL PRIVILEGES ON ConcursoP.TipoUsuario TO 'concurso'@'localhost';
GRANT ALL PRIVILEGES ON ConcursoP.Banco TO 'concurso'@'localhost';
GRANT ALL PRIVILEGES ON ConcursoP.ProblemasResueltos TO 'concurso'@'localhost';
GRANT ALL PRIVILEGES ON ConcursoP.Staff TO 'concurso'@'localhost';
GRANT ALL PRIVILEGES ON ConcursoP.Ediciones TO 'concurso'@'localhost';


insert into TipoUsuario(IdTipo,Alumno,Asesor,Staff) 
values(1,"Alumno","No","No");
insert into TipoUsuario(IdTipo,Alumno,Asesor,Staff) 
values(2,"No","Docente","No");
insert into TipoUsuario(IdTipo,Alumno,Asesor,Staff) 
values(3,"No","No","Staff");

insert into Carreras(IdCarrera,Nombre,Siglas) 
values(1,"Ing. Sistemas Computacionales","ISC");
insert into Carreras(IdCarrera,Nombre,Siglas) 
values(2,"Ing. Telecomunicaciones","ITICS");

insert into Categorias(IdCategoria,Nombre,SemestreLimite) 
values(1,"Master","8");

insert into Equipos(IdEquipo,Nombre,Integrantes,Asesor,IdCategoria,Puntos,ProblemasResueltos) 
values(1,"Joshua's","Hugo Calvillo,Josue Rodriguez,Moroleon","Roberto Zinzun",1,"100","10");

   
insert into Alumnos(IdAlumno,Nombre,Sexo,Telefono,Email,IdTipo,Contraseña,NumeroControl,Semestre,IdCarrera,IdEquipo,NombreAsesor) 
values(1,"Josue Rodriguez","Masculino","3511352489","alumno@gmail.com",1,"Hola.123","123123","1","1",1,"Roberto Zinzun");

insert into Docentes(IdDocente,Nombre,Sexo,Telefono,Email,Estatus,Contraseña,IdTipo,NumeroDocente,Escolaridad,Especialidad,Cedula,IdCarrera) 
values(1,"Roberto Zinzun","Masculino","3511352459","docente@gmail.com","Activo","Hola.123",2,"124124","1","Programacion Web","123412341234",1);
select * from Alumnos;
select * from Docentes;