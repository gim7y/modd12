
from django.core.management.base import BaseCommand  # CommandError
from news.models import Post, Categor


class Command(BaseCommand):
    help = 'Обнуляет все посты определенной категории'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        self.stdout.readable()
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Операция прервана'))
        try:
            category = Category.objects.get(name=options['category'])
            # Post.objects.filter(postCategory__name='Education').delete()
            Post.objects.filter(postCategory__name=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news from category {category.name}'))
            # в случае неправильного подтверждения говорим, что в доступе отказано
        except Post.DoesNotExist:  # except OSError as e: # print(e)
            self.stdout.write(self.style.ERROR(f'Could not find category {category.name}'))

