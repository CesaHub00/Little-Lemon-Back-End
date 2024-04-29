# Little-Lemon-Back-End
End of Coursera's [*Meta Back-End Developer*](https://www.coursera.org/professional-certificates/meta-back-end-developer) course.

The main goal is to build the Little Lemon restaurant booking API.

There are 2 models:
- Menu (table with the items in the menu)
- Booking (table with the info about the reservation)

The serializer convert Django model instances into Python data types that can be easily rendered into JSON, XML or other types.

In the view.py there are structure that takes a web request and returns a responses.

---
### Getting Started
### Available Scripts

In the project directory, 

`$ cd Little-Lemon-Back-End/littlelemon`

you can run:

#### `python manage.py makemigration` and/or `python manage.py migrate`

To save the models in models.py to the database.

#### `python manage.py runserver`

Open [http://localhost:3000](http://127.0.0.1:8000/) to view it in the browser.

You can change the url to see the admin panel *(admin/)* or the menu *(restaurant/menu)*; all the path are in the urls.py file in the project folder and in the restaurant folder.

#### `python manage.py test`

To test models, serializers and views in the test.py file.
