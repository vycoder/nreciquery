# nreciquery
Recipe lookup API for given n ingredients. This project is written to try out and learn Django and Django Rest Framework. The idea was to create an application that will provide you recipes from the current ingredients you have in the fridge.

## Getting Started
All read operations are issued via get requests. Ingredients and seasonings are the parameters from which to filter the recipes.
* ingredients - these are the main ingredients of that recipe requires.
* seasonings - spices, sauces, etc.
* match_any_level - the level of matching to apply on the results.

### Query recipes by ingredients
Using only an ingredient parameter will perform exact matching on ingredients but any matching on seasoning. Lists should be delimited by the '|' character.
```
server-url/recipes?ingredients=Beef|Pork
```
This will pull up all recipes that only contain Beef and Pork regardless of what the seasonings are.

### Query recipes on both ingredients and seasonings
By default, the API performs an exact matching if no match_any_level parameter was given.
```
server-url/recipes?ingredients=Beef|Pork&seasonings=Ketchup|Mustard
```
This will fetch all recipes that only contains Beef and Pork as ingredients with Ketchup and Mustard as seasonings.

### Query with match_any_level
match_any_level parameter could have any of the following values: ```both, ingredients, seasonings```

* both - matches any recipes that contains any of the given list of ingredients or seasonings.
```
server-url/recipes?ingredients=Beef|Pork&seasonings=Mustard|Ketchup&match_any_level=both
```
This will return all recipes that contains any of the following: Beef, Pork, Mustard, and Ketchup.

* ingredient - applies match any on ingredients but performs exact matching on seasonings.
```
server-url/recipes?ingredients=Beef|Pork&seasonings=Mustard|Ketchup&match_any_level=ingredient
```
This fetch only the recipes having both Mustard and Ketchup as seasoning but having a Pork OR Beef as its ingredients.

* seasonings - applies match any on seasonings but performs exact matching on ingredients.
```
server-url/recipes?ingredients=Beef|Pork&seasonings=Mustard|Ketchup&match_any_level=seasonings
```
This fetch only the recipes that contains both Pork and Beef having Mustard OR Ketchup as its seasonings.

### Querying without ingredients
Ingredients are mandatory, if one fails to add an ```ingredients``` parameter, the whole recipe list will be fetched regardless if there's a ```seasoning``` or ```match_any_leve``` parameters.
