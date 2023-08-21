# Flask MongoDB CRUD Application

This is a simple Flask application that demonstrates CRUD (Create, Read, Update, Delete) operations using MongoDB as the database. The application provides REST API endpoints to manage user data.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)


## Prerequisites

Before running this application, ensure you have the following installed:

- Docker: To containerize the Flask app and MongoDB.
- MongoDB Compass (optional): To visually explore the MongoDB database.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/flask-mongo-crud.git
   cd flask-mongo-crud
   ```

2. Build and run the Docker containers:

   ```bash
   docker-compose up -d
   ```

3. Access the application by visiting http://localhost:5000 in your browser.

## Usage

- To test the API, you can use tools like `curl`, Postman, or any other API client.
- For database management and exploration, you can use MongoDB Compass to connect to the MongoDB instance running in the Docker container.

## Endpoints

### `GET /hello`

Returns a "hello world" message.

![Hello Endpoint](/images/hello_tester.png)

---

### `POST /user`

Adds a new user to the database.

![User Creation](/images/post_request.png)

---

### `GET /users`

Retrieves a list of all users.

![Get Users](/images/Get_Request.png)

---

### `GET /user/<id>`

Retrieves details of a user by ID.

![Get User by ID](/images/GetBy_Id_request.png)

---

### `PUT /user/<id>`

Updates a user's information.

![Update User](/images/PUT_Request.png)

After Update the new User Information.

![After Update](/images/After_put.png)

---

### `DELETE /user/<id>`

Deletes a user by ID.

![Delete User](/images/Delete_Request.png)

![After Delete](/images/After_Delete.png)


## Troubleshooting

- If you encounter issues with connectivity or data retrieval, refer to the Troubleshooting section in the `README.md` or documentation.
- If you are facing any issues with building images , use this command :
 ```bash
   docker build -t flask-mongo-crud:latest .
   ```

- If you are facing difficulties in checking docker container database ,use the following command to get the container Id :
```bash
   docker ps
   ```
- It will give you the container id ,then use the following command to access the container :
```bash
   docker exec -it < your mongo-container Id > /bin/bash
   ``` 
- After that use "mongosh" command to access mongo db and you will get a mongo shell
 



## Contributing

Contributions are welcome! If you find a bug or have suggestions for improvement, please feel free to submit a pull request.


