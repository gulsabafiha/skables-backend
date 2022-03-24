from unicodedata import name
from rest_framework import serializers
from .models import Customuser
from .models import Artist, Medium, Painting, Review, Style, Subject
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, min_length=8, error_messages={
                                      "min_length": "Password must be longer than 8 characters"})
    password2 = serializers.CharField(write_only=True, min_length=8, error_messages={
                                      "min_length": "Password must be longer than 8 characters"})
    name=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Customuser
        fields = ['id','username', 'email', 'password1',
                  'password2', 'phone','name']
    
    def get_name(self,obj):
        name=obj.first_name
        if name == '':
            name=obj.email
        return name

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("Password does not match.")
        return data

    def create(self, validated_data):
        user = Customuser.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],   
           phone=validated_data["phone"],   
        )
        user.set_password(validated_data["password1"])
        user.save()
        return user

class UserSerializerWithToken(UserSerializer):
    token=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Customuser
        fields=['username', 'email', 'password1',
                  'password2', 'phone','token']

    def get_token(self,obj):
        token=RefreshToken.for_user(obj)
        return str(token.access_token)

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'


class MediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medium
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class PaintingSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=False, read_only=True)
    subject = SubjectSerializer(many=True, read_only=True)
    medium = MediumSerializer(many=True, read_only=True)
    style = StyleSerializer(many=True, read_only=True)
    rating = ReviewSerializer(many=False, read_only=True)

    class Meta:
        model = Painting
        fields = ['id', 'name', 'main_image', 'wall_image', 'artist',
                  'price', 'category', 'introduction', 'description', 'shipping',
                  'like', 'views', 'is_feature', 'is_popular', 'is_new', 'is_sale',
                  'sale_percentage', 'style',
                  'subject', 'medium', 'material', 'specification',
                  'size', 'orientation', 'color', 'created_year', 'rating']
