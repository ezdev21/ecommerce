# Ecommerce project

**make sure to configure php configuration file(php.ini) upload_max_filesize!!**

![ecommerce](https://user-images.githubusercontent.com/78965149/183610848-2dce1449-40a4-41f0-8acd-ed3a8ca60550.png)

## Installation

clone the project `git clone https://github.com/ezra02/ecommerce`

install componser dependencies `composer update`

copy .env files `cp .env.example .env`

generate key `php artisan key:generate`

migrate database `php artisan migrate`

start server `php artisan serve`

## Installation using docker

`docker-compose build ecommerce`

`docker-compose up -d`

`docker-compose exec ecommerce php artisan key:generate`

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
Contact me here or by email ezrafikadu02@gmail.com
