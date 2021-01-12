from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from flask_login import UserMixin

db = SQLAlchemy()

class TipoUsuarios(db.Model):
    __tablename__ = 'TipoUsuario'
    IdTipo = Column(Integer, primary_key=True)
    Alumno = Column(String, nullable=False)
    Asesor = Column(String, nullable=False)
    Staff = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        tip = self.query.all()
        return tip
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        tip = self.consultaIndividual()
        db.session.delete(tip)
        db.session.commit()
    def consultaIndividual(self):
        car = self.query.get(self.IdTipo)
        return car
    def get_id(self):
        return self.IdTipo

class Carrera(db.Model):
    __tablename__ = 'Carreras'
    IdCarrera = Column(Integer, primary_key=True)
    Nombre = Column(String, nullable=False)
    Siglas = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        car = self.query.all()
        return car
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        car = self.consultaIndividual()
        db.session.delete(car)
        db.session.commit()
    def consultaIndividual(self):
        car = self.query.get(self.IdCarrera)
        return car
    def get_id(self):
        return self.IdCarrera

class Categoria(db.Model):
    __tablename__ = 'Categorias'
    IdCategoria = Column(Integer, primary_key=True)
    Nombre = Column(String, nullable=False)
    SemestreLimite = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        cat = self.query.all()
        return cat
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        cat = self.consultaIndividual()
        db.session.delete(cat)
        db.session.commit()
    def consultaIndividual(self):
        equi = self.query.get(self.IdCategoria)
        return equi
    def get_id(self):
        return self.IdCategoria

class Equipo(db.Model):
    __tablename__ = 'Equipos'
    IdEquipo = Column(Integer, primary_key=True)
    Nombre = Column(String, nullable=False)
    Integrantes = Column(String, nullable=False)
    Asesor = Column(String, nullable=False)
    IdCategoria = Column(String, ForeignKey('Categorias.IdCategoria'))
    Puntos = Column(Integer, nullable=False )
    ProblemasResueltos = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        equi = self.query.all()
        return equi
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        equi = self.consultaIndividual()
        db.session.delete(equi)
        db.session.commit()
    def consultaIndividual(self):
        equi = self.query.get(self.IdEquipo)
        return equi
    def get_id(self):
        return self.IdEquipo

class Alumno(UserMixin, db.Model):
    __tablename__ = 'Alumnos'
    IdAlumno = Column(Integer, primary_key=True)
    Nombre = Column(String, nullable=False)
    Sexo = Column(String, nullable=False)
    Telefono = Column(String, nullable=False)
    Email = Column(String, nullable=False)
    IdTipo = Column(Integer, ForeignKey('TipoUsuario.IdTipo'))
    Contraseña = Column(String, nullable=False)
    NumeroControl = Column(String, nullable=False)
    Semestre = Column(String, nullable=False)
    IdCarrera = Column(Integer, ForeignKey('Carreras.IdCarrera'))
    IdEquipo = Column(Integer, ForeignKey('Equipos.IdEquipo'))
    NombreAsesor = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        alum = self.query.all()
        return alum
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        alum = self.consultaIndividual()
        db.session.delete(alum)
        db.session.commit()
    def consultaIndividual(self):
        alum = self.query.get(self.IdAlumno)
        return alum
    @property
    def password(self):
        raise AttributeError('El atributo password no es de lectura')
    def validarPassword(self, Contraseña):
        pwd = self.query.filter_by(Contraseña=Contraseña).first()
        return pwd
    def is_authenticated(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.IdAlumno
    def validar(self, Email, Contraseña):
        alum = Alumno.query.filter_by(Email=Email).first()
        if alum != None:
            if alum.validarPassword(Contraseña):
                return alum
        else:
            return None

class Docentes(UserMixin, db.Model):
    __tablename__ = 'Docentes'
    IdDocente = Column(Integer, primary_key=True)
    Nombre = Column(String, nullable=False)
    Sexo = Column(String, nullable=False)
    Telefono = Column(String, nullable=False)
    Email = Column(String, nullable=False)
    Estatus = Column(String, nullable=False)
    Contraseña = Column(String, nullable=False)
    IdTipo = Column(Integer, ForeignKey('TipoUsuario.IdTipo'))
    NumeroDocente = Column(String, nullable=False)
    Escolaridad = Column(String, nullable=False)
    Especialidad = Column(String, nullable=False)
    Cedula = Column(String, nullable=False)
    IdCarrera = Column(Integer, ForeignKey('Carreras.IdCarrera'))

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        doc = self.query.all()
        return doc
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        doc = self.consultaIndividual()
        db.session.delete(doc)
        db.session.commit()
    def consultaIndividual(self):
        doc = self.query.get(self.IdDocente)
        return doc
    @property
    def password(self):
        raise AttributeError('El atributo password no es de lectura')
    def validarPassword(self, Contraseña):
        pwd = self.query.filter_by(Contraseña=Contraseña).first()
        return pwd
    def is_authenticated(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.IdDocente
    def validar(self, Email, Contraseña):
        doc = Docentes.query.filter_by(Email=Email).first()
        if doc != None:
            if doc.validarPassword(Contraseña):
                return doc
        else:
            return None

class Staf(UserMixin, db.Model):
    __tablename__ = 'Staff'
    IdStaff = Column(Integer, primary_key=True)
    Nombre = Column(String, nullable=False)
    Sexo = Column(String, nullable=False)
    Telefono = Column(String, nullable=False)
    Email = Column(String, nullable=False)
    IdTipo = Column(Integer, ForeignKey('TipoUsuario.IdTipo'))
    Estatus = Column(String, nullable=False)
    Contraseña = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        stf = self.query.all()
        return stf
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        stf = self.consultaIndividual()
        db.session.delete(stf)
        db.session.commit()
    def consultaIndividual(self):
        car = self.query.get(self.IdStaff)
        return car
    def get_id(self):
        return self.IdStaff
    @property
    def password(self):
        raise AttributeError('El atributo password no es de lectura')
    def validarPassword(self, Contraseña):
        pwd = self.query.filter_by(Contraseña=Contraseña).first()
        return pwd
    def is_authenticated(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.IdStaff
    def validar(self, Email, Contraseña):
        staf = Staf.query.filter_by(Email=Email).first()
        if staf != None:
            if staf.validarPassword(Contraseña):
                return staf
        else:
            return None

class ProblemasResuelto(db.Model):
    __tablename__ = 'ProblemasResueltos'
    IdProblema = Column(Integer, primary_key=True)
    Tiempo = Column(Time, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        Pro = self.query.all()
        return Pro
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        Pro = self.consultaIndividual()
        db.session.delete(Pro)
        db.session.commit()
    def consultaIndividual(self):
        equi = self.query.get(self.IdProblema)
        return equi
    def get_id(self):
        return self.IdProblema

class Edicion(db.Model):
    __tablename__ = 'Ediciones'
    IdEdicion = Column(Integer, primary_key=True)
    Nombre = Column(String, nullable=False)
    FechaRegistro = Column(Date, nullable=False)
    FechaEvento = Column(Date, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        edi = self.query.all()
        return edi
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        edi = self.consultaIndividual()
        db.session.delete(edi)
        db.session.commit()
    def consultaIndividual(self):
        equi = self.query.get(self.IdEdicion)
        return equi
    def get_id(self):
        return self.IdEdicion

class Bancos(db.Model):
    __tablename__ = 'Banco'
    IdBanco = Column(Integer, primary_key=True)
    Nombre = Column(String, nullable=False)
    Puntos = Column(String, nullable=False)
    Tiempo = Column(Time, nullable=False)
    Descripcion = Column(String, nullable=False)
    ColorGlobo = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        ban = self.query.all()
        return ban
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        ban = self.consultaIndividual()
        db.session.delete(ban)
        db.session.commit()
    def consultaIndividual(self):
        ban = self.query.get(self.IdBanco)
        return ban
    def get_id(self):
        return self.IdBanco

