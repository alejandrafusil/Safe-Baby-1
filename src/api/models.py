from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    roles_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    profile = db.relationship("Profile", backref="user", uselist=False)
    role = db.relationship("Rol", backref="user", uselist=False)
    datos_babies = db.relationship("DatosBaby")
    chats = db.relationship('Chat', secondary="participantes_chats")
    messages = db.relationship('Message', backref="user", lazy=True)


    def __repr__(self):
        return '<User %r>' % self.email

    def get_datos_babies(self):
        return list(map(lambda x:x.serialize(), self.datos_babies))
        
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "roles_id":self.roles_id,
            "profile":self.profile.serialize(),
            "role":self.role.serialize(),
            "datos_babies":self.get_datos_babies()
            #"chats": self.get_chats()
            #"messages": self.get_messages() 
            
            # do not serialize the password, its a security breach
        }

    #definiendo comandos para guardar actualizar y eliminar desde models y usarlo en mis endpoints como ejemplo: user.save()
    def save(self):
        db.session.add(self)
        db.session.commit()

    def updade(self):
        db.session.commit(self)
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Rol(db.Model):
    __tablename__= 'roles'
    id = db.Column(db.Integer, primary_key=True)
    rol_name = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Rol %r>' % self.rol_name

    def serialize(self):
        return {
            "id": self.id,
            "rol_name": self.rol_name
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def updade(self):
        db.session.commit(self)
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Profile(db.Model):
    __tablename__= 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    apellido = db.Column(db.String(120), nullable=False)
    avatar = db.Column(db.String(200), nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<Profile %r>' % self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "avatar": self.avatar,
            "users_id": self.users_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def updade(self):
        db.session.commit(self)
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class DatosBaby(db.Model):
    __tablename__= 'datos_baby'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    apellido = db.Column(db.String(120), nullable=False)
    edad = db.Column(db.String(120), nullable=False)
    genero = db.Column(db.String(120), nullable=False)
    estatura = db.Column(db.String(50), nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    datos_actividades= db.relationship("Actividad", secondary="logros_bebes")
    
    def __repr__(self):
        return '<DatosBaby %r>' % self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "genero": self.genero,
            "estatura": self.estatura,
            "users_id": self.users_id,
            "datos_actividades": self.datos_actividades
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def updade(self):
        db.session.commit(self)
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Actividad(db.Model):
    __tablename__= 'actividades'
    id = db.Column(db.Integer, primary_key=True)
    etapas = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return '<Actividad %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "etapas": self.etapas,
            "descripcion": self.descripcion,
            "datos_babies": self.datos_babies
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def updade(self):
        db.session.commit(self)
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class LogroBebe(db.Model):
    __tablename__= 'logros_bebes'    
    actividades_id = db.Column(db.Integer, db.ForeignKey('actividades.id'), nullable=False, primary_key=True)
    datos_baby_id = db.Column(db.Integer, db.ForeignKey('datos_baby.id'), nullable=False, primary_key=True)

    def __repr__(self):
        return '<LogroBebe %r>' % self.actividades_id

    def serialize(self):
        return {
            "actividades_id": self.actividades_id,
            "datos_baby_id": self.datos_baby_id,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def updade(self):
        db.session.commit(self)
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Etapa(db.Model):
    __tablename__= 'etapas'    
    actividades_id = db.Column(db.Integer, db.ForeignKey('actividades.id'), nullable=False, primary_key=True)
    datos_baby_id = db.Column(db.Integer, db.ForeignKey('datos_baby.id'), nullable=False, primary_key=True)
    actividades = db.relationship("Actividad")
    datos_babies = db.relationship("DatosBaby")

    def __repr__(self):
        return '<Etapa %r>' % self.actividades_id

    def serialize(self):
        return {
            "actividades_id": self.actividades_id,
            "actividades": self.actividades,
            "datos_baby_id": self.datos_baby_id,
            "datos_babies": self.datos_babies
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def updade(self):
        db.session.commit(self)
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Chat(db.Model):
    __tablename__= 'chats'
    id = db.Column(db.Integer, primary_key=True)
    nombre_sala = db.Column(db.String(120), unique=True, nullable=False)
    participantes = db.relationship('User', secondary="participantes_chats")
    Message = db.relationship('Message', backref="chat", lazy=True)

  

    def __repr__(self):
        return '<Chat %r>' % self.nombre_sala

    def serialize(self):
        return {
            "id": self.id,
            "nombre_sala": self.nombre_sala,
            "participantes": self.participantes,
            "Message": self.Message
        }

    def get_participantes(self):
        return list(map(lambda x: x.serialize(), self.participantes))

    def get_messages(self):
        return list(map(lambda x: x.serialize(), self.messages))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

        
class ParticipanteChat(db.Model):
    __tablename__= 'participantes_chats'
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey('chats.id'), nullable=False)

 
class Message(db.Model):
    __tablename__= 'messages'
    id = db.Column(db.Integer, primary_key=True)
    chats_id =  db.Column(db.Integer, db.ForeignKey('chats.id'), nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.String(120), unique=True, nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "message": self.message,
            "user": self.user.name
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

