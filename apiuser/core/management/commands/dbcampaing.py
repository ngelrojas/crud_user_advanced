from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import CategoryCampaing, TagCampaing
from core.models import Campaing, Like, News
from core.models import Reward, Payment, User
from core.models import Comment, SubComment, Currency


class Command(BaseCommand):
    help = 'create campaings'

    def success(self, message):
        return self.stdout.write(
                self.style.SUCCESS(message)
        )

    def warning(self, warning):
        return self.stdout.write(
                self.style.WARNING(warning)
        )

    def error(self, error):
        return self.stdout.write(
                self.style.ERROR(error)
        )
 
    def handle(self, *args, **options):
        self.warning(
                'if something goes wrong after fixtures installations,\
                        pelase use: python manage.py flush.'
        )

        with transaction.atomic():
            """get users"""
            user_creator_1 = User.objects.get(email='jhondoe@yopmail.com')
            user_creator_2 = User.objects.get(email='merydoe@yopmail.com')
            user_contributor_1 = User.objects.get(email='maricolucas@yopmail.com')
            user_contributor_2 = User.objects.get(email='marinalucas@yopmail.com')
            currency_one = Currency.objects.get(name='Bolivianos')
            """create tags"""
            tag_1 = TagCampaing.objects.create(
                   name='python'
            )
            tag_2 = TagCampaing.objects.create(
                    name='javascript'
            )
            tag_3 = TagCampaing.objects.create(
                    name='clojure'
            )
            self.success('tags created')
            """create campaing"""
            campaing_1 = Campaing.objects.create(
                   title='first campaing',
                   slug='first-campaing',
                   city='santa cruz',
                   budget=100,
                   qty_days=50,
                   facebook='facebook.com/firts1',
                   twitter='twitter.com/first1',
                   linkedin='linkedin.com/first1',
                   instagram='instagram.com/first1',
                   website='first1.com',
                   video='https://www.youtube.com/watch?v=DCCDKQH7BmA',
                   excerpt='this is a excerpt for this campaibng.',
                   description='this is a lot description for this campaing',
                   public_at='2020-12-03 12:52:00',
                   status_campaing=1,
                   is_complete=False,
                   user=user_creator_1,
                   currencies=currency_one
            )
            campaing_1.tags.add(tag_1, tag_3)
            campaing_2 = Campaing.objects.create(
                   title='second campaing',
                   slug='second-campaing',
                   city='la paz',
                   budget=300,
                   qty_days=50,
                   facebook='facebook.com/firts2',
                   twitter='twitter.com/first2',
                   linkedin='linkedin.com/first2',
                   instagram='instagram.com/first2',
                   website='first2.com',
                   video='https://www.youtube.com/watch?v=DCCDKQH7BmA',
                   excerpt='this is a excerpt for this campaibng.',
                   description='this is a lot description for this campaing',
                   public_at='2020-10-05 12:52:00',
                   status_campaing=1,
                   is_complete=False,
                   user=user_creator_2,
                   currencies=currency_one
            )
            campaing_2.tags.add(tag_2, tag_1)
            self.success('campaing created.')
            """create category"""
            category_1 = CategoryCampaing.objects.create(
                    name='technology'
            )
            category_1.campaing.add(campaing_1)

            category_2 = CategoryCampaing.objects.create(
                    name='nature'
            )
            category_2.campaing.add(campaing_2)

            self.success('categories created.')

            """create likes"""
            like_one = Like.objects.create(
                    liked=True,
                    user=user_contributor_1,
                    campaing=campaing_1
            )
            like_two = Like.objects.create(
                    liked=True,
                    user=user_contributor_1,
                    campaing=campaing_2
            )
            like_three = Like.objects.create(
                    liked=True,
                    user=user_contributor_2,
                    campaing=campaing_1
            )
            self.success('likes created.')

            """create rewards"""
            reward_one = Reward.objects.create(
                    title='reward camp 1',
                    price=12.50,
                    delivery_data='2020-02-20 12:45',
                    delivery_place='somewhere',
                    description='somewhere',
                    campaing=campaing_1
            )
            reward_two = Reward.objects.create(
                    title='reward camp 1',
                    price=123.50,
                    delivery_data='2020-05-20 12:45',
                    delivery_place='somewhere',
                    description='somewhere',
                    campaing=campaing_1
            )
            reward_three = Reward.objects.create(
                    title='reward camp 2',
                    price=912.50,
                    delivery_data='2020-06-22 12:45',
                    delivery_place='somewhere',
                    description='somewhere',
                    campaing=campaing_2
            )

            reward_four = Reward.objects.create(
                    title='reward camp 2',
                    price=668.50,
                    delivery_data='2020-07-21 12:45',
                    delivery_place='somewhere',
                    description='somewhere',
                    campaing=campaing_2
            )

            self.success('rewards created.')

            """create payments"""
            payment_one = Payment.objects.create(
                   name='paypal',
                   campaing=campaing_1,
                   reward=reward_one,
                   user=user_contributor_1,
                   type_payment=1,
                   status_payment=3,
                   budget_partial=reward_one.price
            )
            payment_two = Payment.objects.create(
                   name='paypal',
                   campaing=campaing_1,
                   reward=reward_two,
                   user=user_contributor_1,
                   type_payment=1,
                   status_payment=3,
                   budget_partial=reward_two.price
            )
            payment_three = Payment.objects.create(
                   name='paypal',
                   campaing=campaing_2,
                   reward=reward_three,
                   user=user_contributor_1,
                   type_payment=1,
                   status_payment=2,
                   budget_partial=reward_three.price
            )
            self.success('payment created.')
            """news related a campaing"""
            news_1 = News.objects.create(
                    title="some title",
                    description="some description about campaing.",
                    campaing=campaing_1
            )
            news_2= News.objects.create(
                    title="some title two",
                    description="some two description about campaing.",
                    campaing=campaing_1
            )
            news_3= News.objects.create(
                    title="some title three",
                    description="some three description about campaing.",
                    campaing=campaing_1
            )
            self.success('news created.')
            """comment about campaing"""
            comment_1 = Comment.objects.create(
                    description="some comments about campaing.",
                    created_at="2019-10-5 12:15",
                    user=user_contributor_1
            )
            comment_2 = Comment.objects.create(
                    description="some two comments about campaing.",
                    created_at="2019-10-5 12:15",
                    user=user_contributor_1
            )
            self.success('comments created.')
            """subcomment about comment"""
            sub_comment_1_1 = SubComment.objects.create(
                    description="some answer about comment.",
                    created_at="2019-5-5 12:23",
                    comment=comment_1
            )
            sub_comment_1_2 = SubComment.objects.create(
                    description="some two answer about comment.",
                    created_at="2019-5-5 12:23",
                    comment=comment_1
            )
            sub_comment_2_1 = SubComment.objects.create(
                    description="some answer about comment above.",
                    created_at="2019-6-5 12:12",
                    comment=comment_2
            )
