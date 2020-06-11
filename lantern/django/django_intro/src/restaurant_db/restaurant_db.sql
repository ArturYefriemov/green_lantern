CREATE TABLE Country(
    country_id INT PRIMARY KEY,
    country_name VARCHAR(30) NOT NULL
);


CREATE TABLE City(
    city_id INT PRIMARY KEY,
    city_name VARCHAR(30) NOT NULL,
    country_id INT REFERENCES Country(country_id) NOT NULL
);


CREATE TABLE Restaurant(
    restaurant_id INT PRIMARY KEY,
    restaurant_name VARCHAR(30) NOT NULL,
    restaurant_address VARCHAR(60) NOT NULL,
    restaurant_number VARCHAR(13) NOT NULL ,UNIQUE,
    country_id INT REFERENCES Country(id) NOT NULL,
    city_id INT REFERENCES City(id) NOT NULL,
    menu_id INT REFERENCES Menu(id) NOT NULL
    );

CREATE TABLE Menu(
    menu_id INT PRIMARY KEY,
    menu_name VARCHAR(50) NOT NULL
    );

CREATE TABLE Dish(
    dish_id INT PRIMARY KEY,
    dish_name VARCHAR(50) NOT NULL,
    ingredients VARCHAR NOT NULL,
    weight INT NOT NULL,
    price FLOAT NOT NULL
    );

CREATE TABLE RestaurantMenu(
    menu_id INT REFERENCES Menu(menu_id) NOT NULL,
    dish_id INT REFERENCES Dish(dish_id) NOT NULL
    );


CREATE TABLE Employee(
	employee_id INT PRIMARY KEY,
	employee_first_name VARCHAR(30) NOT NULL,
	employee_last_name VARCHAR(30) NOT NULL,
	employee_birthday DATE,
	employee_phone_number VARCHAR(13) NOT NULL, UNIQUE,
	employee_address VARCHAR(50) NOT NULL,
	employee_salary FLOAT NOT NULL,
	employee_work_experience VARCHAR(50) NOT NULL,
	restaurant_id INT REFERENCES Restaurant(restaurant_id) NOT NULL
	);





