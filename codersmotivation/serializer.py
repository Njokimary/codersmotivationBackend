from rest_framework import serializers
from .models import Post
from authentication.models import User
from rest_framework.response import Response

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# class UpdateProfileView(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = '__all__'
        

    # def validate_email(self, value):
    #     user = self.context['request'].user
    #     if User.objects.exclude(pk=user.pk).filter(email=value).exists():
    #         raise serializers.ValidationError({"email": "This email is already in use."})
    #     return value

    # def validate_username(self, value):
    #     user = self.context['request'].user
    #     if User.objects.exclude(pk=user.pk).filter(username=value).exists():
    #         raise serializers.ValidationError({"username": "This username is already in use."})
    #     return value
                
    # def update(self, instance, validated_data):
    #     user = self.context['request'].user
    #     instance.username = validated_data['username']
    #     instance.avatar = validated_data['avatar']
    #     instance.email = validated_data['email']
    #     instance.bio = validated_data['bio']

    #     instance.save()

    #     return instance
# if user.pk != instance.pk:
        #     raise serializers.ValidationError({"authorize": "You dont have permission for this user."})


# class UserProfileSerializer(serializers.ModelSerializer):
#     """A serializer for our user profile objects."""

#     class Meta:
#         model = Profile
#         fields = ('avatar', 'email', 'username', 'bio')
#         # extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         """Create and return a new user."""

#         user = Profile(
#             email=validated_data['email'],
#             name=validated_data['username']
#         )

#         user.bio(validated_data['bio'])
#         user.save()
