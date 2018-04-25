# Chalice demo

Simple demo of Chalice for testing setting up AWS lambda and API gateway. Just for learning purposes, do not use in the real world. 

Sets up two endpoints:

- `GET /`: returns a JSON object `{ hello: world }`
- `POST /contact/{who}`: accepts a JSON object and stores it in the specified S3 bucket/folder under the `who` key
