from flask_restx import fields

from .extensions import api

# modelos de prueba 

student_model = api.model("Student", {
    "id": fields.Integer,
    "name": fields.String,
    #"course_id": fields.Nested(course_model)
})

course_model = api.model("Course", {
    "id": fields.Integer,
    "name": fields.String,
    "students": fields.List(fields.Nested(student_model))
})

course_imput_model = api.model("CourseInput", {
    "name": fields.String(required=True)
})

student_input_model = api.model("StudentInput", {
    "name": fields.String(required=True),
    "course_id": fields.Integer(required=True)
})

