from flask import*
import os
app = Flask(__name__)
data = {
  "courses": [
    {
      "course_id": "CSE101",
      "course_name": "Introduction to Computer Science",
      "instructor": "John Smith",
      "enrollment_capacity": 50,
      "enrollment_count": 35
    },
    {
      "course_id": "2",
      "course_name": "Linear Algebra",
      "instructor": "Emily Johnson",
      "enrollment_capacity": 40,
      "enrollment_count": 38
    },
    {
      "course_id": "ENG301",
      "course_name": "Advanced English Writing",
      "instructor": "Sarah Thompson",
      "enrollment_capacity": 25,
      "enrollment_count": 20
    }
  ],
  "students": [
    {
      "student_id": "001",
      "student_name": "Alice Smith",
      "enrolled_courses": ["CSE101", "MAT201"]
    },
    {
      "student_id": "002",
      "student_name": "Bob Johnson",
      "enrolled_courses": ["ENG301"]
    },
    {
      "student_id": "003",
      "student_name": "Eva Davis",
      "enrolled_courses": []
    }
  ]
}


port = int(os.environ.get("PORT",3000))

@app.route('/')
def index():
    return "<h1>Welcome to the course REST API</h1>"

@app.route('/courses',methods=["GET"])
def get():
    return jsonify({'Courses':data})

@app.route('/courses/<int:course_id>',methods=['GET'])
def get_course(course_id):
    return jsonify({'course':data[course_id]})

@app.route('/courses',methods=['POST'])
def create():
    

    data["courses"].append({
    "course_id": "PHY202",
    "course_name": "Physics II",
    "instructor": "Michael Brown",
    "enrollment_capacity": 30,
    "enrollment_count": 15
    })

    return jsonify({'Created':data})

@app.route('/courses/<int:course_id>',methods=['PUT'])
def course_update(course_id):
    courses[course_id]["Description"] = "abc"
    return jsonify({'course':courses[course_id]})

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=port)