from django.shortcuts import get_object_or_404
from .models import Product
from rest_framework import authentication, generics, mixins, permissions
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .permissions import IsStaffEditorPermission


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]
    
    
    def perform_create(self, serializers):
        # print(serializers.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if content is None:
            content = title
        serializer.save(content=content)
    

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # lookup_field = "pk" 
    
    
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    lookup_field = "pk"
    
    
    def perform_update(self, serializer):
        instance = serializer.save()
        
        if not instance.content:
            instance.content = content.title
            

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    lookup_field = "pk"
    
    
    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)
        
    
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
    def perform_create(self, serializer):
        # print(serializers.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if content is None:
            content = title
        serializer.save(content=content)

class ProductMixinView(mixins.CreateModelMixin,mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    
    
    
    def get(self, request, *args, **kwargs): # HTTP GET Method
        return self.list(request, *args, **kwargs)
        


    def post(self, request, *args, **kwargs): # HTTP post Method
        return   self.create(request, *args,  **kwargs)
    
    
    def perform_create(self, serializer):
        # print(serializers.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if content is None:
            content = "This is a single view doing cool stuff"
        serializer.save(content=content)
    
@api_view(["GET", "POST"])    
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    
    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data 
            return Response(data)
    #  list view
    queryset = Product.objects.all()
    data = ProductSerializer(queryset, many=True).data
    return Response(data)
    
    
    if method == "POST":
    # create item
        serializer = ProductSerializer(data= requst.data)
        if serializers.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"Invaild": "Not good data"}, status=400)
        

    
    
    

    
