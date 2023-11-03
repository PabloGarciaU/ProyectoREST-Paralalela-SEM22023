from flask_restx import Resource, Namespace

from .api_models import course_model, student_model
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
    
@ns.route("/students")
class StudentsAPI(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()