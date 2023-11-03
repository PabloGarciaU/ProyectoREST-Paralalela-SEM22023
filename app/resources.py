from flask_restx import Resource, Namespace

from .api_models import course_model, student_model, course_imput_model, student_input_model
from .extensions import db
from .models import Course, Student

ns = Namespace("api")

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