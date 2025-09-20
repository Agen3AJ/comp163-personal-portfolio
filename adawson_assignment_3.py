full_name = "Ameir Dawson"
student_email = "ajdawson@aggies.ncat.edu"
hometown = "Fuquay-Varina, NC"
graduation_semester = "Spring 2028"
major = "Computer Engineering, Electrical Engineering"

current_courses = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_courses = ["Pre-Calculus", "Calculus", "English", "Global Business"]
credit_hours = [3, 3, 3, 3]
gpa_history = [3.2, 3.6, 3.4, 3.7]

emergency_contact = ("Mom", "Bernette Dawson", "617-642-7345")
home_address = ("456 Oak Street", "Charlotte, NC", "27526")
instagram_info = ("Instagram", "@agentthree", 174)
twitter_info = ("Twitter", "@AJAgen3_06", 5)
birthday = ("Birthday", 7, 05, 2006)

current_skills = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interests = {"Software development", "Web development", "Data science", "Game development"}
hobbies = {"Gaming", "Drawing", "Reading", "Music"}
entertainment_backlog = {"Dragon Ball", "Sonic the Hedgehog", "Life", "Adventuring"}

course_credits = {"COMP 163": 3, "MATH 150": 3, "ENG 101": 3, "HIS 105": 3}
course_professors = {"COMP 163": "Prof. Rhodes", "MATH 150": "Dr. Lee",
                     "ENG 101": "Dr. Martinez", "HIS 105": "Dr. Brown"}
course_rooms = {"COMP 163": "M-Eric 300", "MATH 150": "Marteena 201",
                "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"}
monthly_budget = {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}
study_hours_per_subject = {"Programming": 10, "Math": 8, "English": 4, "History": 3}
contact_directory = {"Mom": "704-555-0199", "Roommate": "336-555-7821", "Academic Advisor": "336-334-5000"}

total_current_credits = sum(credit_hours)
cumulative_gpa = round(sum(gpa_history) / len(gpa_history), 2)
completed_courses_count = len(completed_courses)
total_weekly_study_hours = sum(study_hours_per_subject.values())
academic_load = total_current_credits + total_weekly_study_hours
monthly_budget_total = sum(monthly_budget.values())
daily_food_budget = round(monthly_budget["Food"] / 30, 2)
annual_budget_projection = monthly_budget_total * 12
study_cost_per_hour = round(monthly_budget["Books"] / total_weekly_study_hours, 2)

instagram_followers = instagram_info[2]
twitter_followers = twitter_info[2]
total_social_media_followers = instagram_followers + twitter_followers

current_skills_count = len(current_skills)
skills_to_learn_count = len(skills_to_learn)
contact_directory_size = len(contact_directory)
entertainment_backlog_count = len(entertainment_backlog)
study_hours_per_credit_ratio = round(total_weekly_study_hours / total_current_credits, 2)

print("** Personal Information **")
print(f"Full name: {full_name}")
print(f"Student email: {student_email}")
print(f"Hometown: {hometown}")
print(f"Graduation semester: {graduation_semester}")
print(f"Major: {major}\n")

print("** Academic Data **")
print(f"Current courses: {current_courses}")
print(f"Completed courses: {completed_courses}")
print(f"Credit hours (per current course): {credit_hours}")
print(f"Semester GPAs: {gpa_history}\n")

print("** Contact Information (tuples; accessed by index) **")
print(f"Emergency contact - label: {emergency_contact[0]}, name: {emergency_contact[1]}, phone: {emergency_contact[2]}")
print(f"Home address: {home_address[0]}, {home_address[1]} {home_address[2]}")
print(f"{instagram_info[0]} handle: {instagram_info[1]}, followers: {instagram_info[2]}")
print(f"{twitter_info[0]} handle: {twitter_info[1]}, followers: {twitter_info[2]}")
print(f"Birthday: {birthday[1]}/{birthday[2]}/{birthday[3]}\n")

print("** Interests & Hobbies (sets) **")
print(f"Current skills: {current_skills}")
print(f"Skills to learn: {skills_to_learn}")
print(f"Career interests: {career_interests}")
print(f"Hobbies: {hobbies}")
print(f"Entertainment backlog: {entertainment_backlog}\n")

print("** Organizational Mapping (dictionaries) **")
print(f"Course credits: {course_credits}")
print(f"Course professors: {course_professors}")
print(f"Course rooms: {course_rooms}")
print(f"Monthly budget breakdown: {monthly_budget}")
print(f"Study hours per subject: {study_hours_per_subject}")
print(f"Contact directory: {contact_directory}\n")

print("** Required Calculations **")
print(f"Total current credits: {total_current_credits}")
print(f"Cumulative GPA (average of semesters): {cumulative_gpa:.2f}")
print(f"Number of completed courses: {completed_courses_count}")
print(f"Total weekly study hours: {total_weekly_study_hours}")
print(f"Academic load (credits + study hours): {academic_load}")
print(f"Monthly budget total: ${monthly_budget_total:.2f}")
print(f"Daily food budget (Food ÷ 30): ${daily_food_budget:.2f}")
print(f"Annual budget projection (monthly total × 12): ${annual_budget_projection:.2f}")
print(f"Study cost per hour (Books ÷ total study hours): ${study_cost_per_hour:.2f}\n")

print("** Analytics Calculations **")
print(f"Total social media followers (Instagram + Twitter): {total_social_media_followers}")
print(f" - Instagram followers: {instagram_followers}")
print(f" - Twitter followers: {twitter_followers}")
print(f"Current skills count: {current_skills_count}")
print(f"Skills-to-learn count: {skills_to_learn_count}")
print(f"Contact directory size (number of contacts): {contact_directory_size}")
print(f"Entertainment backlog count: {entertainment_backlog_count}")
print(f"Study hours per credit ratio: {study_hours_per_credit_ratio} (weekly study hours ÷ total current credits)\n")

