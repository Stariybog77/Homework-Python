my_family = ['Я', 'Мама', 'Папа']

my_family_height = [
    ['Я', 180],
    ['Мама', 165],
    ['Папа', 175],
]

print('Рост отца -', my_family_height[2][1], 'см')

total_height = (
    my_family_height[0][1] +
    my_family_height[1][1] +
    my_family_height[2][1]
)

print('Общий рост моей семьи -', total_height, 'см')