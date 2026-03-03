
# The Ecommerce project

![ecommerce](https://user-images.githubusercontent.com/78965149/183610848-2dce1449-40a4-41f0-8acd-ed3a8ca60550.png)

## Installation

clone the project `git clone https://github.com/ezdev21/ecommerce`

## Client Installation

navigate to client directory `cd client`

install node dependencies `npm install`

run in development mode `npm run dev`

## Server Installation

navigate to server directory: `cd server`

install and configure postgres database

Create a Python virtual environment

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

install python dependencies: `pipenv install`

setup credentials in the .env file from postgres databse

```bash
cp .env.example .env   # Linux/macOS
copy .env.example .env # Windows CMD
```

migrate the database

```bash
py manage.py makemigrations
py manage.py migrate
```

run in development mode: `py manage.py runserver`

## Installation using docker

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License.

<!-- CONTACT -->
## Contact
Contact me here or by email ezradev21@gmail.com
