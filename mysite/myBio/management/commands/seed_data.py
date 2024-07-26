from django.core.management.base import BaseCommand
from myBio.models import Resume

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Clear existing data
        Resume.objects.all().delete()

        # Create new resume entry
        Resume.objects.create(
            name="David Franco",
            email="david7franco@outlook.com",
            phone="(856)-278-0205",
            summary="Experienced software developer with a strong background in building web applications using Django and Python.",
            experience="Applications and Integrations Developer - Student Worker June 2023 - June 2024\n\
            Rowan University IRT - Software Development and System Services Glassboro, NJ\n\
            • Successfully refactored and optimized multiple data feeds by leveraging and extending to the Python library ProfPy, reducing technical debt while facilitating future feed upgrades\n\
            • Created SQL Queries in OracleDB using Banner tables to ensure that scripts critical to Rowan University’s finance and admissions office ran smoothly and data was populated into the tables\n\
            • Collaborated closely with Database Administrators for the successful migration of servers from Oracle 19c to Oracle 21c, actively participating in refactoring and migrating processes, such as upgrading repositories to use oracleDB instead of cx Oracle\n\
            • Managed and tracked tickets and issues using Jira, while consistently meeting project deadlines\n\
            IT Specialist April 2022 - June 2023\n\
            Rowan University IRT - Technology Services Glassboro, NJ\n\
            • Successfully closed and resolved over 250 hardware and software incidents initiated by Rowan University’s faculty and students since April 2022\n\
            • Proficiently managed incident resolution and maintained the hardware database utilizing ServiceNow\n\
            • Tasked with training new student employees, showcasing trust in handling crucial responsibilities\n\
            • Conducted excellent written and verbal communication skills",
            education="Rowan University Glassboro, NJ\n\
            Bachelors of Sciences in Computer Science May 2024\n\
            Concentration: Cyber Security Defense",
            skills="Programming Languages: Java, Python, SQL, C/C++, JavaScript\n\
            Developer Tools: Git, GitHub, Bash Script, MySQL, OracleDB\n\
            Technologies/Frameworks: HTML/CSS, Django, AngularJS, HammerSpoon, AppMan Job Scheduler",
            projects="ReziBo ticket Management — HTML/CSS, Django, SQLite3, JavaScript — GitHub Link Dec. 2023\n\
            • As Scrum Master/Lead Software Developer, orchestrated project phases from planning to deployment using the Agile framework, facilitating task assignments to team members, and ensuring adherence to deadlines for sprints, resulting in the successful completion of the project within the stipulated timeline\n\
            • Designed an offline database schema to store tickets, users, relationships between tickets and users, along with annotations to a ticket, extended Django’s user class to create different types of users who serve different purposes\n\
            • Using Django’s forms feature, developed multiple forms for users to sign up, create a ticket, edit ticket information, or edit user information\n\
            • Leveraged Django’s robust features to architect a user-friendly ticket management platform, implementing functionalities including ticket management, ticket creation, priority setting, due date tracking, and user authentication\n\
            Iglesia Soli Deo Gloria — HTML/CSS, Django, SQLite3 — GitHub Link Present\n\
            • Developing a website for a small church based in Clementon, NJ using the Python Django framework, with HTML/CSS and Bootstrap-V5 elements included\n\
            • Designing an offline database schema to manage user donations, track individual church contributions, handle contact information, and implement a comment section for Pastor responses to congregation inquiries\n\
            • Creating functionality requested by stakeholder, which includes developing a donations page, sermons up-loader page, and more, utilizing multiple Django modules\n\
            WorkForcePro — HTML/CSS, Angular, MySQL — GitHub Link Mar. 2023\n\
            • Collaborated with a team of 7 students to aid as Product Owner/Developer in the development and implementation of WorkForcePro to enhance employee management processes and improve overall organizational efficiency\n\
            • Developed user roles and permissions utilizing Angular Framework libraries, allowing managers and admins to securely access and manage the software’s various features and functions\n\
            • Designed offline local host MySQL database into the software, providing secure data storage and retrieval functionality. Created a Schema to parse and store information for different tables, such as users, roles, and designation",
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with resume data'))
