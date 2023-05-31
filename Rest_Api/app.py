from flask import*
import os
app = Flask(__name__)
courses =  [
    {
      "course_id": "0",
      "course_name": "Introduction to Computer Science",
      "instructor": "John Smith",
      "enrollment_capacity": 50,
      "enrollment_count": 35
    },
    {
      "course_id": "1",
      "course_name": "Linear Algebra",
      "instructor": "Emily Johnson",
      "enrollment_capacity": 40,
      "enrollment_count": 38
    },
    {
      "course_id": "2",
      "course_name": "Advanced English Writing",
      "instructor": "Sarah Thompson",
      "enrollment_capacity": 25,
      "enrollment_count": 20
    }
  ]

port = int(os.environ.get("PORT",3000))

@app.route('/')
def index():
    return "<h1>Welcome to the course REST API</h1>"

@app.route('/courses',methods=["GET"])
def get():
    return jsonify({'Courses':courses})

@app.route('/courses/<int:course_id>',methods=['GET'])
def get_course(course_id):
    return jsonify({'course':courses[course_id]})

@app.route('/courses',methods=['POST'])
def create():
    course = {
      "course_id": "3",
      "course_name": "Machine Learning",
      "instructor": "Geoffery Hintoln",
      "enrollment_capacity": 25,
      "enrollment_count": 20
    }
    courses.add(course)
    return jsonify({'Created':course})

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=port)