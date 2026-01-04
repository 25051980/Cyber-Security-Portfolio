-- 🔐 TEST 1: Foreign key constraint
-- Attempt to insert a recipe with a non-existent user_id (should fail)
INSERT INTO Recipes (title, description, user_id, category_id)
VALUES ('Test Recipe - Invalid User', 'This should fail', 999, 1);

-- 🔑 TEST 2: Primary key uniqueness
-- Attempt to insert a user with an existing user_id (should fail)
INSERT INTO Users (user_id, name, email)
VALUES (1, 'Sam Tester', 'sam@example.com');

-- ✉️ TEST 3: UNIQUE constraint on email
-- Attempt to insert a user with an existing email (should fail)
INSERT INTO Users (name, email)
VALUES ('Duplicate Email', 'sam@example.com');

-- ✅ TEST 4: CHECK constraint on rating
-- Attempt to insert a rating outside valid range (should fail)
INSERT INTO Ratings (recipe_id, user_id, rating, comment)
VALUES (1, 1, 10, 'This should fail');  -- Rating must be between 1 and 5

-- ⚙️ TEST 5: SHOW INDEX command to verify optimisation
SHOW INDEX FROM Recipes;
SHOW INDEX FROM Ratings;
SHOW INDEX FROM Recipe_Ingredients;
