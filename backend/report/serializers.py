# from django.http import HttpRequest
from rest_framework import serializers
# from rest_framework.exceptions import ValidationError
# from rest_framework.generics import get_object_or_404
# from rest_framework.validators import UniqueValidator

from report.models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('employee', 'order', 'item_order', 'execution_time', 'image')
        # exclude = ['id', ]
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }


# class ReviewsSerializer(serializers.ModelSerializer):
#     title = serializers.SlugRelatedField(
#         slug_field='name',
#         read_only=True,
#     )
#     author = serializers.SlugRelatedField(
#         default=serializers.CurrentUserDefault(),
#         slug_field='username',
#         read_only=True
#     )

#     def get_author(self, request: HttpRequest) -> User:
#         return self.context.get('request').user

#     def get_title(self, request: HttpRequest) -> Title:
#         return get_object_or_404(
#             Title,
#             pk=self.context.get('view').kwargs.get('title_id'),
#         )

#     def validate(self, data):
#         if self.context.get('request').method == 'POST':
#             if Review.objects.filter(
#                     title=self.get_title(self),
#                     author=self.get_author(self),
#             ).exists():
#                 raise ValidationError(
#                     'На одно произведение можно оставить только один отзыв',
#                 )
#         return data
