-- Use the project database
USE recipe_project;

-- Insert sample Users
INSERT INTO Users (name, email) VALUES
('Alice Johnson', 'alice@example.com'),
('Bob Smith', 'bob@example.com'),
('Clara Lee', 'clara@example.com'),
('David Park', 'david@example.com'),
('Emma Brown', 'emma@example.com');

-- Insert sample Categories
INSERT INTO Categories (name) VALUES
('Breakfast'),
('Lunch'),
('Dinner'),
('Dessert'),
('Snack');

-- Insert sample Ingredients
INSERT INTO Ingredients (name) VALUES
('Spaghetti'),
('Eggs'),
('Bacon'),
('Parmesan Cheese'),
('Chicken Breast'),
('Olive Oil'),
('Salt'),
('Pepper'),
('Flour'),
('Sugar');

-- Insert sample Recipes
INSERT INTO Recipes (title, description, user_id, category_id) VALUES
('Spaghetti Carbonara', 'Creamy pasta with bacon and cheese', 1, 3),
('Chicken Stir Fry', 'Quick stir-fry with vegetables and chicken', 2, 2),
('Pancakes', 'Fluffy pancakes with syrup', 3, 1),
('Chocolate Cake', 'Rich and moist chocolate cake', 4, 4),
('Grilled Chicken Salad', 'Healthy salad with grilled chicken', 5, 2);

-- Insert sample Recipe_Ingredients
INSERT INTO Recipe_Ingredients (recipe_id, ingredient_id, quantity) VALUES
(1, 1, '200g'),
(1, 2, '2'),
(1, 3, '100g'),
(1, 4, '50g'),
(2, 5, '150g'),
(2, 6, '2 tbsp'),
(2, 7, '1 tsp'),
(2, 8, '1 tsp'),
(3, 2, '1'),
(3, 9, '100g'),
(3, 10, '50g'),
(4, 10, '200g'),
(4, 9, '150g'),
(4, 4, '100g'),
(5, 5, '200g'),
(5, 7, 'Pinch'),
(5, 8, 'Pinch'),
(5, 6, '1 tbsp');

-- Insert sample Ratings
INSERT INTO Ratings (recipe_id, user_id, rating, comment) VALUES
(1, 2, 5, 'Delicious and easy to make!'),
(1, 3, 4, 'Tasty but a bit salty'),
(2, 1, 5, 'Loved the crunch!'),
(3, 4, 3, 'Needed more sugar'),
(4, 1, 5, 'Perfect dessert!'),
(4, 5, 4, 'Very chocolaty, just how I like it'),
(5, 3, 4, 'Healthy and tasty'),
(5, 2, 3, 'Could use more seasoning');


