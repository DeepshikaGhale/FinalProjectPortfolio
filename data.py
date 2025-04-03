# project data
def getProjectsData():
  projects = [
    {
      'name': 'SMS API',
      'description': "This project involves building a web application using Flask that connects to various external APIs, retrieves data, constructs a message using the gathered information, and sends the message via SMS using the Twilio API. The goal is to showcase integration with multiple APIs, real-time messaging capabilities, and user interaction through a web interface.",
      'architectureImage': '../static/images/sms.png',
      'resultImage': '../static/images/sms_result.jpeg',  
      'image':'',
      'file':'',
      'link': 'https://replit.com/@A00272439/MountainousImpeccableDehardwarization'
    },
    {
      'name': 'Research Paper',
      'description': "Research Paper on Dairy cows by province 2003 to 2023. An overview of the trends in dairy cow populations across Canadian provinces from 2003 to 2023. It outlines significant fluctuations, highlighting British Columbia's recovery after a decline, Alberta's steady growth, and the decreases observed in Saskatchewan and New Brunswick. Additionally, it notes the variations in Manitoba and Ontario, emphasizing the differing patterns in dairy farming across the provinces.",
      'architectureImage': '',
      'resultImage': '',  
      'image':'',
      'file':'../static/files/researchpaper.pdf',
      'link': ''
    },
    {
      'name': 'Infographics',
      'description': "Infographics graphic from a “Low Income Among Persons With A Disability in Canada.” This report comes from Statistics Canada, which is part of the insights on Canadian Society Series. The data in the overview of the study can be used to create the infographic, which should explore the key variables in the overview.",
      'architectureImage': '',
      'resultImage': '',  
      'image':'',
      'file':'../static/files/infographics.pdf',
      'link': ''
    },
    {
      'name': 'Geoprocessing spatial data in ArcGIS Pro',
      'description': "The project, conducted for GIS 1025, focuses on geoprocessing spatial data in ArcGIS Pro to analyze six convenience store robberies in Coniston, Ontario, that occurred within 37 minutes on July 30, 2024. The analysis involved creating a 250-meter buffer around the robbery locations, revealing an area of approximately 1,144,537.39 square meters that police need to cover for ground searches. An intersection analysis between local roads and rivers identified ten river and road crossings, aiding in understanding potential escape routes. The convenience stores were labeled by the time of day to illustrate the sequence of events, which indicated the order of the robberies. Additionally, two bridges—William Avenue and Walter Street—were highlighted for investigation by the marine unit, based on reported suspicious activity. The findings were presented in a final map layout titled “Convenience Store Robbery/Shooting in Coniston,” providing law enforcement with critical geographic insights to aid their investigation.",
      'architectureImage': '',
      'resultImage': '',  
      'image':'',
      'file':'../static/files/spatial.pdf',
      'link': ''
    },
  ]
  return projects

# present data
def getCurrentData():
  contact_info = {
    'email': "deepshikaghale99@gmail.com",
    'phone': '437 123 4566',
    'github': 'https://github.com/DeepshikaGhale'
  }

  return contact_info

# about me and experience data
def aboutMe():
  about_me = "I am currently pursuing Business Analytics at Cambrian College. My key skills and interest lies in mobile application development, designing UI/UX and working with data."

  experience = [
      {
          'name': 'Cambrian College R&D Electrical Department',
          'position': 'Research Assistant',
          'image': '../static/images/cambrian.png',
          'timeline': "May 2024 - Running"
      },
      {
          'name': 'Ekbana Solutions Pte. Ltd',
          'position': 'Associate Flutter Developer',
          'image': '../static/images/ekbana.jpeg',
          'timeline': "April 2022 - Nov 2022"
      },
      {
          'name': 'Ekbana Solutions Pte. Ltd',
          'position': 'Flutter Developer Intern',
          'image': '../static/images/ekbana.jpeg',
          'timeline': "Jan 2022 - April 2022"
      },
  ]
  return about_me, experience

# education data
def getEducation():
  education = [
    {
        'name': 'Cambrian College R&D Electrical Department',
        'level': 'Postgraduate Degree, Business Analytics',
        'image': '../static/images/cambrian.png',
        'timeline': "March 2024 - Running",
        'description': [
          'I am currently pursuing Business Analytics at Cambrian College.'
        ]
    },
    {
        'name': 'Cambrian College R&D Electrical Department',
        'level': 'Postgraduate Degree, Mobile Application',
        'image': '../static/images/cambrian.png',
        'timeline': "Jan 2023 - Oct 2023",
        'description':[
          "Build application using .NET MAUI",
          "iOS application development using Storyboard in Xcode",
          "Developed web application using .NET 6",
          "Developed Android application using Kotlin",
          "Co-op at UGOTGAME",
          "Ranked 3rd place in Hackathon for Flutter project"
        ]
    },
    {
        'name': 'Herald College Kathmandu',
        'level': "Bachelor's degree, Information Technology",
        'image': '../static/images/herald.png',
        'timeline': "Jan 2018 - July 2021",
        'description': [
          "Build application using .NET MAUI",
          "iOS application development using Storyboard in Xcode",
          "Developed web application using .NET 6",
          "Developed Android application using Kotlin",
          "Co-op at UGOTGAME",
          "Ranked 3rd place in Hackathon for Flutter project",
          "Built and designed Android e-commerce application with product recommendation as my final year project",
          "Dataset analysis using structured and unstructured database",
          "Web designing using Python",
          "Game development and machine learning",
          "UI/UX designing using Adobe XD",
          "Designed posters for college community"
        ]
    }
  ]
  return education

# skills data
def getSkills():
  skills = [
    {
      'name':'Dart',
      'description': 'I have about 2 years of experience on working with Dart, as I have worked in a several flutter projects.'
    },
    {
      'name':'Flutter',
      'description': 'I have about 2 years of working experience on working with Flutter framework for developing application in cross-platforms.'
    },
    {
      'name': 'Figma',
      'description': 'I have designed UI/UX for both mobile and web versions during my academic as well as career journey.'
    },
    {
      'name': 'SQL',
      'description': 'I have academic experience on working with SQL databases. However, I have not worked with SQL in my real-world projects.'
    },
    {
      'name':'Python',
      'description':'Being a data analytics student, I have a good understanding of Python programming language. I have worked on several projects using Python. I have also worked on several projects using R programming language during my academic tenure.'
    },
    {
      'name':'Firebase',
      'description': 'I have exercised different components of Firebase such as: Firebase Realtime Database, Firebase Authentication, Firebase Cloud Storage, Firebase Firestore and Firebase Notifcation. I have developed my initial projects by using firebase.'
    },
    {
      'name': 'Android',
      'description': 'I have also got some level of experience on working with Android Studio. The final year project for my Bachelor’s degree was an android mobile application using Android Studio.'
    }
  ]
  return skills
