
books_list = [
    {'title':'one', 'author': 'john', 'genre': 'science'},
    {'title':'two', 'author': 'smith', 'genre': 'fantasy'},
    {'title':'three', 'author': 'wills', 'genre': 'fiction'},
    {'title':'four', 'author': 'john', 'genre': 'fiction'},
    {'title':'five', 'author': 'freeman', 'genre': 'history'},
    ]

for book in books_list:
    print(book)

user_genre = input('Enter Genre (history, science, fantasy, fiction): ')

while user_genre.isdigit() or user_genre not in ['history', 'science', 'fantasy', 'fiction']:
        user_genre = input('Enter Genre (history, science, fantasy, fiction): ')
        
titles_per_genre = [dict['title'] for dict in books_list if dict['genre'] == user_genre]

print(f'Titles for Genre ({user_genre}): {titles_per_genre}')