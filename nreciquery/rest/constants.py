class GetParams:

    INGREDIENTS= "ingredients"
    SEASONING = "seasonings"
    MATCH_ANY_LEVEL = "match_any_level"

    def __setattr__(self, key, value):
        pass

class MatchLevel:
    BOTH = 'both'
    INGREDIENTS_ONLY = 'ingredient'
    SEASONING_ONLY = 'seasoning'

    def __setattr__(self, key, value):
        pass