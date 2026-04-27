# Selenium Automation Testing Project

## 📌 Overview
This project is an automation testing framework built using Selenium WebDriver and Pytest.
It follows Page Object Model (POM) design pattern.

## 📁 Project Structure
- pages/ → Page Object Model classes
- tests/ → Test cases
- utils/ → WebDriver setup
- screenshots/ → Test evidence (failed screenshots)

## ⚙️ Tools Used
- Python
- Selenium
- Pytest

## 🚀 How to Run Project

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run tests
pytest -v

### 3. Generate report (optional)
pytest --html=report.html

## 📸 Test Evidence
- login_fail.png → screenshot when login test fails

## 🧠 Notes
This project was created for learning automation testing (Selenium + Pytest + POM).
