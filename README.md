### Progect: Currency Converter Mini Project
### Author: Confy-Code

This is a simple **currency conversion web application** built with **Python (Flask)**.  
The application allows users to convert amounts between different currencies using real-time exchange rates.

The project uses **HTML templates**, **CSS for styling**, and is **deployed live on Render**.

---

## Project Description

The Currency Converter provides a clean web interface where users can:
- Enter an amount
- Select source and target currencies (Example: from **USD* to **EUR*)
- Instantly view the converted value

#### Notice: 
     Exchange rates are fetched dynamically from an external currency API.

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- External Currency Exchange API
- Render (Deployment)

---

## Project Structure

<img width="556" height="390" alt="structure" src="https://github.com/user-attachments/assets/0404b7f9-26cc-4e89-8b18-2e0b7f917e77" />


---

## Installation & Setup

#### 1. Clone the repository####

     git clone https://github.com/Confy-Code/CurrencyChanger.git####

         cd CurrencyChanger

#### 2. Create your own virtual environment(optional)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

#### 3.Install the progect's dependencies
pip install -r requirements.txt

#### Run the application and open your localhost adress via browser
python server_serve.py


## Deployment

Hosted on Render via link: https://currencychanger-u5yn.onrender.com

Environment variables are configured via the Render dashboard
Application is started using the main server file





