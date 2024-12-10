# **Job Portal**

A web-based job portal built with Django that enables employers to post jobs and manage applicants while allowing employees to search for and apply to jobs.

---

## **Features**

### **For Employers:**
- Register and manage profiles.
- Post and manage job listings.
- View applicants for job postings.
- Mark job positions as filled.
- Access a personalized dashboard.

### **For Employees:**
- Register and manage profiles.
- Search for jobs by title and location.
- View job details.
- Apply for job postings.
- Update profile information.

---

## **Tech Stack**
- **Backend:** Python, Django
- **Database:** SQLite (default Django database; can be replaced with PostgreSQL or MySQL)
- **Frontend:** HTML, CSS, Bootstrap (optional)
- **Other Tools:** Django Template Engine

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/job-portal.git
cd job-portal
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Run the Development Server**
```bash
python manage.py runserver
```

### **6. Access the Application**
Open your browser and visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---


## **Usage**

### **1. Employer Workflow:**
- Register as an employer.
- Log in and access the dashboard.
- Post new jobs and manage existing job listings.
- View and manage applicants.

### **2. Employee Workflow:**
- Register as an employee.
- Log in and update your profile.
- Search for jobs and view job details.
- Apply for jobs that match your qualifications.

---

## **Contributing**
Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and submit a pull request.

---

## **Screenshots**

### **1. Employer Dashboard**
![Employer Dashboard](https://via.placeholder.com/800x400)

### **2. Job Search Page**
![Job Search](https://via.placeholder.com/800x400)

---

## **Future Enhancements**
- Add job recommendations based on user profiles.
- Implement email notifications for job applications and approvals.
- Add advanced filters for job search (e.g., by salary, job type).

---

