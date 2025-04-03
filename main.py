from datetime import datetime

from flask import Flask, jsonify, render_template, request

from data import aboutMe, getCurrentData, getEducation, getProjectsData, getSkills

app = Flask('app')

#to make the data available throughout the site
@app.context_processor
def add_shared_data():
  contact_info = getCurrentData()
  current_year = datetime.now().year
  return {"contact_info": contact_info, "current_year": current_year}

#home
@app.route('/')
def index():
  about_me, experience = aboutMe()

  return render_template(
      'index.html',
      about_me=about_me,
      experience=experience,
  )

#education
@app.route('/education')
def education():
  #get education data from getEducation()
  education = getEducation()
  return render_template('education.html', education = education)

#skills
@app.route('/skills')
def skills():
  #get skills data from getSkills()
  skills = getSkills()
  return render_template('skills.html', skills = skills)

#projects
@app.route('/projects')
def projects():
  #get project data from getProjects()
  projects = getProjectsData()
  return render_template('projects.html', projects = projects)

#contact
@app.route('/contact', methods=['GET', 'POST'])
def contactme():
  #check if the required method is POST
  if request.method == 'POST':
    #no condition to check if the user entered data, in the server side, as there is: required mentioned in the input field
    
    #display success message
    return jsonify({'status': 'success', 'message': 'Your message has been sent successfully!'})

  return render_template('contact_me.html')

app.run(host='0.0.0.0', port=8080)
