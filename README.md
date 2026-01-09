# Client-API

This project is a **Currency Converter application** built using **Python**.  
It started as a simple Python script and was extended into a **robust web application** with a backend, database support, interactive UI, and automated test cases.

## Features

- Currency conversion using live exchange rates
  
- Flask-based web application
  
- REST API for currency conversion
  
- Input validation and error handling
  
- Interactive frontend using HTML & JavaScript
  
- Automated test cases with pytest
  
- Modular and clean project structure

## Technologies Used

- **Python**
- **Flask** (Web Framework)
- **Requests** (API calls)
- **SQLite** (Database – optional extension)
- **HTML / JavaScript**
- **Pytest** (Testing)

## Project Structure

Client API/

│── client.py # Core logic (validation & API calls)

│── app.py # Flask web application (main code)

│── database.py # Database initialization (optional)

│── requirements.txt

├── templates/

│ └── index.html # Web UI

├── static/

│ └── script.js # JavaScript for interaction

├── test/

│ └── test_client.py # Unit test cases

## Installation & Setup

1. create an vertual environment
   python -m venv myvenv
   
2. activate vertual environment
   myvenv\Scripts\activate

3. install dependancies
   pip install flask requests pytest
   
4. run the application 
   python app.py

## output 

Conversion Successful

10 USD = 899.9 INR

## terminal output screensshoot 

<img width="1565" height="495" alt="Screenshot 2026-01-09 101643" src="https://github.com/user-attachments/assets/49e9d810-0f87-4a9d-8f59-709ee9851eb1" />

## Conclusion
This project demonstrates a complete currency conversion system built with Python and Flask. It includes input validation, API integration, an interactive web interface, and automated test cases. The application follows clean coding practices and reflects real-world backend development concepts.



