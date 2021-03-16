# EDMS prototype

Adapted by [NdagiStanley](https://github.com/NdagiStanley) for CTS

#### Initial Steps
- Clone this repo
  ```
  git clone https://github.com/NdagiStanley/edms.git
  ```

- Go to the project directory
  ```
  cd edms
  ```
- Build the Docker image
  ```
  docker build .
  ```
- Build the Docker image using docker-compose
  ```
  docker-compose build
  ```
- Migrate the models to database
  ```
  docker-compose run --rm app sh -c 'python manage.py makemigrations'
  docker-compose run --rm app sh -c 'python manage.py migrate'
  ```


#### To run the server
-   ```
    docker-compose up
    ```
#### To create a superuser
- ```
  docker-compose run --rm app sh -c 'python manage.py createsuperuser'
  ```
- Login to admin page to log in:
  <http://localhost:8000/admin/>


#### To run the tests
- ```
  docker-compose run --rm app sh -c 'python manage.py test'
  ```

### Routes

1. Django Admin page:   <http://localhost:8000/admin/>
1. API root:            <http://localhost:80/api/>
1. Mayan Dashboard:     <http://localhost:80/>
