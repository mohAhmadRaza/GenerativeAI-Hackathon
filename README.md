# Hotel Management API

This is a Django-based REST API for managing hotel room availability and user queries. The project includes endpoints to get user queries, check hotel room availability, and book hotel rooms.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Setup Instructions](#setup-instructions)
3. [Usage](#usage)
4. [API Endpoints](#api-endpoints)
5. [Testing](#testing)
6. [Contributing](#contributing)
7. [License](#license)

## Project Overview

The Hotel Management API provides the following functionalities:
- Retrieve all user queries.
- Check availability of hotel rooms.
- Book a hotel room.

## Setup Instructions

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment**

   - **Windows:**

     ```bash
     .\env\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source env/bin/activate
     ```

4. **Install Dependencies**

   Make sure you have a `.env` file in your project root directory with the following content:
   
   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   ```

   Then install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations**

   Create the necessary database tables:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser**

   To access the Django admin interface:

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

## Usage

1. **Access the Admin Interface**

   Open your browser and go to:

   ```
   http://127.0.0.1:8000/admin/
   ```

   Log in with the superuser credentials you created. You can manage the `HotelRoom` and `UserQuery` models here.

2. **Test the API Endpoints**

   You can use a tool like Postman or `curl` to test the following endpoints:

   - **GET** `/api/userQuery/` - Retrieve all user queries.
   - **GET** `/api/hotelRoomsAvailability/` - Check availability of hotel rooms.
   - **POST** `/api/bookHotelRoom/` - Book a hotel room.

## API Endpoints

### Retrieve User Queries

- **URL:** `/api/userQuery/`
- **Method:** `GET`
- **Response:** List of user queries.

### Check Hotel Rooms Availability

- **URL:** `/api/hotelRoomsAvailability/`
- **Method:** `GET`
- **Response:** List of available hotel rooms.

### Book a Hotel Room

- **URL:** `/api/bookHotelRoom/`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "room_id": 1
  }
  ```

- **Response:**

  ```json
  {
    "message": "Room booked successfully!"
  }
  ```

## Testing

To test the API endpoints, you can use Postman or `curl`:

- **Postman:** Open Postman, create a new request, and specify the URL and HTTP method. Use the `GET` or `POST` request as needed.

- **curl:** Use the command line tool `curl` to send requests. For example:

  ```bash
  curl -X GET http://127.0.0.1:8000/api/userQuery/
  ```

## Contributing

Feel free to submit pull requests or open issues to contribute to this project.
