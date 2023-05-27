# Visualisation-Edt
 
# General project description:
- This is an application that displays the timetable of courses by analyzing the structure of data stored in an XML file and then converting it into an object-relational mapping (ORM) model to display the timetable for users to view.

- The application is written in Python language, using the Django framework (version 4.2) and integrated with the fullcalendar.io library to display the timetable. Additionally, the application also utilizes several libraries such as Bootstrap, CSS, jQuery, Swal, etc.

- The project is based on the original project: https://github.com/bessantoy/Calendar-viewer, but with additional enhancements aimed at improving speed.

- Sample XML files for testing the application are located in the media directory

- The sample XML files are validated against the XML schema structure at: https://ua-usp.github.io/timetabling/schema

- The project includes both backend and frontend components.

# Application screenshots:
<img width="1439" alt="Screenshot 2023-05-27 at 03 04 57" src="https://github.com/ngominhthoai/Visualisation-Edt/assets/44940464/df6c7167-531b-421c-b48d-1ba7a34fbf36">

# Schema (diagram) of the tables in the database: 

[schema.pdf](https://github.com/ngominhthoai/Visualisation-Edt/files/11580734/schema.pdf)

![348390561_966638904362619_5868854456923449215_n (1)](https://github.com/ngominhthoai/Visualisation-Edt/assets/44940464/7d3058ff-471f-42ab-aeb5-766be47dcac7)



# Installation and usage:

To use this application, please follow the steps below:

1. Ensure that Python is installed:
   - Minimum version required: 3.10
   - You can download Python from the official website: https://www.python.org/downloads/

2. Install the required dependencies:
   - Open a terminal or command prompt.
   - Navigate to the project directory.
   - Run the following command to install the necessary packages:
     ```
     pip install -r requirements.txt
     ```

3. Set up a virtual environment (optional but recommended):
   - Create a virtual environment using a tool like `venv` or `conda`.
   - Activate the virtual environment.

4. Create a superuser (admin):
   - Run the following command in the terminal:
     ```
     python manage.py createsuperuser
     ```
   - Follow the prompts to set a username and password for the admin account.

5. Run the application:
   - Execute the following command in the terminal:
     ```
     python manage.py runserver
     ```
   - The application should now be running locally at http://localhost:8000/.

6. Access the application:
   - Open a web browser.
   - Visit http://localhost:8000/ to access the application.
   - Use the admin credentials created in step 4 to log in and access the admin panel.

Please note that these instructions assume a basic familiarity with command-line tools and Python development. Adjustments may be necessary depending on your specific environment and requirements.

If you encounter any issues during installation or usage, please refer to the project's documentation or seek assistance from the project's support channels.
