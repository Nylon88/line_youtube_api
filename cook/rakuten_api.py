import requests

class RecipeInfo:
    def __init__(self, categoryName: list, parentCategoryId: list, categoryId: list, categoryUrl):
        self.categoryName = categoryName
        self.parentCategoryID = parentCategoryId
        self.categoryId = categoryId
        self.categoryUrl = categoryUrl


def get_ranking_recipe():
    url =  'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?format=json&categoryId=30&applicationId=1054933723764738598'
    # params = pass
    response = requests.get(url).json()
    print(response)


def get_category_list(category_type):
    categoryName, parentCategoryId, categoryId, categoryUrl = [], [], [], []
    url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?format=json&categoryType={}&applicationId=1054933723764738598'.format(category_type)
    response = requests.get(url).json()

    if category_type == 'large':
        for value in response['result'][category_type]:
            categoryName.append(value['categoryName'])
            categoryUrl.append(value['categoryUrl'])
            categoryId.append(value['categoryId'])
        print(response['result'][category_type][0])
        
        reciepe_info_large = RecipeInfo(categoryName=categoryName, parentCategoryId=None, 
                                        categoryId=categoryId, categoryUrl=categoryUrl)
        return reciepe_info_large

    for value in response['result'][category_type]:
        categoryName.append(value['categoryName'])
        parentCategoryId.append(value['parentCategoryId'])
        categoryUrl.append(value['categoryUrl'])
        categoryId.append(value['categoryId'])

    reciepe_info_ms = RecipeInfo(categoryName=categoryName, parentCategoryId=parentCategoryId,
                              categoryId=categoryId, categoryUrl=categoryUrl)
     
    return reciepe_info_ms


if __name__ == '__main__':
    recipe_info = get_category_list('large')




