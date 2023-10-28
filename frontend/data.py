import aiohttp


base_url = 'http://127.0.0.1:8000'


async def get_async(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
                if response.status == 200:
                     data = await response.json()
                     return data


async def get_categories_data():
    response = await get_async(base_url + '/categories')
    if response:
        return [
            (data['name'], data['imape_path'])
            for data in response["categories"]
            if data['name'] != "clashroyal"
        ]


async def get_products_data(category: str):
    response = await get_async(base_url + f'/products/{category}')
    print(response)
    if response:
        return [
            (data['name'], data['imape_path'])
            for data in response['products']
        ]
