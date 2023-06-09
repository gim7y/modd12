from django.core.management.base import BaseCommand  # CommandError
from news.models import Post, Category


class Command(BaseCommand):
    help = 'Обнуляет все посты определенной категории'

    def handle(self, *args, **options):
        cat = Category.objects.all()
        self.stdout.write('Список ваших категорий:')
        cat_list = []
        for i in cat:
            cat_list.append(i.name)
            print(i.name)
        self.stdout.readable()
        self.stdout.write(self.style.SUCCESS('Введите название категории для удаления постов'))
        answer1 = input()

        if answer1 not in cat_list:
            self.stdout.write(self.style.ERROR('Нет такой категории'))
            return
        self.stdout.write(f'Удалить все посты категории {answer1}? yes/no')
        answer2 = input()

        if answer2 != 'yes':
            self.stdout.write(self.style.ERROR('Операция отменена'))
        try:
            Post.objects.filter(postCategory__name=answer1).delete()
            self.stdout.write(self.style.SUCCESS(f'Все посты категории {answer1} удалены'))
        except Exception:
            self.stdout.write(self.style.ERROR(f'Не удалось удалить посты категории {answer1} \n инфо ошибки {Exception}'))
