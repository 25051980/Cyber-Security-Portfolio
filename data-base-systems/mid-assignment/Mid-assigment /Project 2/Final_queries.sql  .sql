-- 1. Insert a new recipe
INSERT INTO Recipes (title, description, user_id, category_id)
VALUES ('Lemon Tart', 'Tangy dessert with lemon curd', 3, 1);

-- 2. Update an existing recipe
UPDATE Recipes
SET description = 'Grilled chicken with Mediterranean herbs'
WHERE title = 'Grilled Chicken';

-- 3. Delete a recipe
DELETE FROM Recipes
WHERE title = 'Bruschetta';

-- 4. Select with filtering
SELECT *
FROM Recipes
WHERE category_id = 1 AND title LIKE '%Cake%';

-- 5. Join query: Recipes with ingredients
SELECT R.title AS recipe, I.name AS ingredient, RI.quantity
FROM Recipes R
JOIN Recipe_Ingredients RI ON R.recipe_id = RI.recipe_id
JOIN Ingredients I ON RI.ingredient_id = I.ingredient_id;

-- 6. Aggregation: Highest-rated recipe
SELECT R.title, MAX(RA.rating) AS highest_rating
FROM Recipes R
JOIN Ratings RA ON R.recipe_id = RA.recipe_id
GROUP BY R.recipe_id
ORDER BY highest_rating DESC
LIMIT 1;

-- 7. Subquery: Users with more than 1 recipe
SELECT name, email
FROM Users
WHERE user_id IN (
    SELECT user_id
    FROM Recipes
    GROUP BY user_id
    HAVING COUNT(*) > 1
);
