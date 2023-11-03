from flask_restx import fields

from .extensions import api

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





