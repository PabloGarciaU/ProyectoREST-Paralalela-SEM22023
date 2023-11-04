from flask_restx import Resource, Namespace
#from .api_models import course_model, student_model, course_imput_model, student_input_model # clases de prueba
from .api_models import salas_model, salas_input_model # clases de la api salas
from .extensions import db
#from .models import Course, Student
from .models import Salas # clase de la api salas

ns = Namespace("api")

# Inicio endpoints de prueba

"""

@ns.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}
    
@ns.route("/courses")
class CoursesAPI(Resource):
    @ns.marshal_list_with(course_model)
    def get(self):
        return Course.query.all()
    
    @ns.expect(course_imput_model)
    @ns.marshal_with(course_model)
    def post(self):
        print(ns.payload)
        course = Course(name=ns.payload["name"])
        db.session.add(course)
        db.session.commit()
        return course, 201
    
@ns.route("/courses/<int:id>")
class CourseAPI(Resource):
    @ns.marshal_with(course_model)
    def get(self, id):
        return Course.query.get_or_404(id)
    
    def delete(self, id):
        course = Course.query.get_or_404(id)
        db.session.delete(course)
        db.session.commit()
        return "", 204
    
    @ns.expect(course_imput_model)
    @ns.marshal_with(course_model)
    def put(self, id):
        course = Course.query.get_or_404(id)
        course.name = ns.payload["name"]
        db.session.add(course)
        db.session.commit()
        return course, 200

@ns.route("/students")
class StudentsAPI(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()
    
    @ns.expect(student_input_model)
    @ns.marshal_with(student_model)
    def post(self):
        student = Student(name=ns.payload["name"], course_id=ns.payload["course_id"])
        db.session.add(student)
        db.session.commit()
        return student, 201
    
# Fin endpoints de prueba

"""

# Inicio endpoints de salas

@ns.route("/salas/<string:codigo>") # operacion get para obtener una sala por su codigo
class SalasAPI(Resource):
    @ns.marshal_list_with(salas_model)
    def get(self, codigo):
        return salas.query.get_or_404(codigo)
    
    def delete(self, codigo):
        salas = salas.query.get_or_404(codigo)
        db.session.delete(salas)
        db.session.commit()
        return "", 204

@ns.route("/salas") # operacion get para obtener todas las salas
class SalasAPI(Resource):
    @ns.marshal_list_with(salas_model)
    def get(self):
        return salas.query.all()
    
    @ns.expect(salas_input_model)
    @ns.marshal_with(salas_model)
    def post(self):
        salas = salas(codigo=ns.payload["codigo"], nombre=ns.payload["nombre"], capacidad=ns.payload["capacidad"])
        db.session.add(salas)
        db.session.commit()
        return salas, 201
    
# Fin endpoints de salas

# Inicio endpoints de reservas