# nreciquery
Recipe lookup API for given n ingredients. This project is written to try out and learn Django and Django Rest Framework. The idea was to create an application that will provide you recipes from the current ingredients you have in the fridge.

## Getting Started
All read operations are issued via get requests. Ingredients and seasonings are the parameters from which to filter the recipes.
* ingredients - these are the main ingredients of that recipe requires.
* seasonings - spices, sauces, etc.
* match_any_level - the level of matching to apply on the results.

By default, the API will return only the recipes that has the same ingredients and seasonings, exact matching. The user should not be given a recipe from which they have a missing ingredient. Although, one can override it by providing an appropriate match_any_level value.
* both - matches any recipes that contains any of the given list of ingredients or seasonings.
```
server-url/recipes?ingredients=Beef|Pork&match_any_level=both&condiments=Mustard|Ketchup
```
Thi will return all recipe that contains any of the following: Beef, Pork, Mustard, and Ketchup.