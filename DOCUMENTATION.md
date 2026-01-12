
#### Author: Confy-Code
# Currency Converter – Technical Documentation

## 1. Overview

This document explains the internal structure and working of the **Currency Converter Mini Project**.  
The application is built with **Flask**, uses a simple modular design, and integrates an external currency exchange API.

---

## 2. Application Flow

1. User opens the home page (`frontexch.html`)
2. User enters:
   - Amount
   - Source currency (labeled as From:)
   - Target currency (labeled as To:)
3. Form data is submitted to the Flask backend
4. Backend calls the exchange service (using the API call in exchange.py file)
5. Currency conversion is calculated(using the server_serve.py file)
6. Result is rendered on `for_server.html`

---

## 3. Backend Files

### `server_serve.py`
This is the **main Flask server file**.

**Responsibilities:**
- Initialize the Flask application
- Define application routes
- Handle form submissions
- Render HTML templates

---

### `exchange.py`
This file fetches the real_time exchange rates from exchange-API for later calculations.

**Responsibilities:**
- Communicate with the external currency exchange API
- Fetch real-time exchange rates
- Test the local stdout on computer.

---

## 4. Frontend Files

### `frontexch.html`
- Home page of the application
- Contains the currency conversion form

### `for_server.html`
- Displays the converted currency amount
- Shows selected currencies and input amount

---

### `static/style.css`
- Handles all styling and layout
- Improves visual appearance and usability

---

## 5. External API Integration

The application uses an external currency exchange API to retrieve real-time exchange rates.

**Key Points:**
- API key is required (unless you use the already-deployed version)
- Requests are handled inside `exchange.py`
- API responses are parsed and validated before use

---

## 6. Environment Variables

The environment variables are required:(in this case the API keys are private by intention)

---
## 7. Error Handling

- Invalid user inputs are handled gracefully
- API request failures return user-friendly messages
- Server-side errors are logged for debugging

---

## 8. Limitations

- Supports only real-time exchange rates
- No historical data support
- No user authentication required

## 9. Future Enhancements

- Add historical currency conversion
- Improve UI/UX
- Add automated tests
- Add caching for API responses
- AI chatbot (trained on tax conversions of countries, currencies, ...)
- User authetication
- Add the analysis of the currency fluctuations

---

## 10. Conclusion

This project demonstrates a clean and simple Flask-based web application with API integration and template rendering.  

It is suitable for beginners and small-scale deployment.


