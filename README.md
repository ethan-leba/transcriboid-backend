# Transcriboid

Transcriboid is a musical training web application that I developed over the summer of 2019. It generates melodies by analyzing patterns in midi files, challenges the user to discern the rhythms and melodies using only their ears, and gives them feedback on how accurately they transcribed the melody. You can check it out at [transcriboid.herokuapp.com](transcriboid.herokuapp.com). *The load times are slow, please be patient!*

This repository contains the back-end API written with Flask and Python.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## RESTful API Endpoints

The RESTful API for this project is very simple, and only provides two endpoints:
* [GET](docs/get.md) : `GET /api/get/`
* [COMPARE](docs/compare.md) : `POST /api/compare/`

### Installing

A step by step series of examples that tell you how to get a development env running

Firstly, you need to install the dependencies of the project:

```
pip install -r requirements.txt
```

And then run the project with

```
flask start
```

End with an example of getting some data out of the system or using it for a little demo

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Flask](https://github.com/pallets/flask) - The web framework used

## License

This project is licensed under the MIT License - see the [LICENSE.md](docs/LICENSE.md) file for details

**Ethan Leba**
