from django.db import models

class Recipe(TimestampedModel):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор',
        help_text='укажите автора',
    )
    name = models.CharField(
        'название рецепта',
        max_length=200,
        help_text='укажите название рецепта',
    )
    image = models.ImageField(
        'изображение',
        upload_to='recipes/',
        help_text='добавьте изображение',
    )
    text = models.TextField(
        'текстовое описание',
        help_text='введите текстовое описание',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientAmount',
        verbose_name='ингредиенты',
        help_text='выберите ингредиенты',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='теги',
        help_text='выберите теги',
    )
    cooking_time = models.IntegerField(
        'время приготовления (в минутах)',
        validators=[
            MinValueValidator(1, message='значение должно быть больше 1'),
        ],
        help_text='укажите время приготовления (в минутах)',
    )

    class Meta:
        default_related_name = 'recipes'
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'
