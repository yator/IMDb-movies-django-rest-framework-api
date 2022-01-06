from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.utils.serializer_helpers import ReturnDict
from watch_list.models import Review, StreamPlatform, WatchList
from rest_framework import status
from watch_list.api.serializers import ReviewSerializer, StreamPlaformSerializer, WatchListSerializer
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from watch_list.api.permissions import AdminOrReadOnly,ReviewUserReadOnly
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly



class ReviewCreate(generics.CreateAPIView):
      serializer_class=ReviewSerializer

      def get_queryset(self):

          return Review.objects.all()

      def perform_create(self, serializer):
          pk=self.kwargs.get('pk')
          watchlist = WatchList.objects.get(pk=pk)

          review_user=self.request.user
          review_queryset=Review.objects.filter(watchlist=watchlist,review_user=review_user)

          if review_queryset.exists():
              raise ValidationError("you have already reviewed this movie")

          serializer.save(watchlist=watchlist,review_user=review_user)


class ReviewListAV(generics.ListAPIView):
    #    queryset =Review.objects.all()
       serializer_class=ReviewSerializer
       permission_classes = [IsAuthenticated]


       def get_queryset(self):
           pk = self.kwargs['pk']
           return Review.objects.filter(watchlist=pk)

class ReviewDetailsAV(generics.RetrieveUpdateDestroyAPIView):
      queryset = Review.objects.all() 
      serializer_class=ReviewSerializer  
      permission_classes = [AdminOrReadOnly]



# class ReviewListAV(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#      queryset =Review.objects.all()
#      serializer_class=ReviewSerializer
#      def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#      def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ReviewDetailsAV(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Review.objects.all() 
#     serializer_class=ReviewSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


        

class StreamPlatformListAV(APIView):
    def get(self,request):
        stream_platforms =StreamPlatform.objects.all()
        serializer = StreamPlaformSerializer(stream_platforms,many=True,)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer = StreamPlaformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

class StreamPlaformDetailAV(APIView):
    def get(self, request,pk):
        try:
            stream_platform=StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"error":"stream does not exist"},status=status.HTTP_404_NOT_FOUND)    
        serializer=StreamPlaformSerializer(stream_platform)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self, request,pk):
        stream_platform=StreamPlatform.objects.get(pk=pk)
        serializer=StreamPlaformSerializer(stream_platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    def delete(self,request,pk):
        stream_platform=StreamPlatform.objects.get(pk=pk)
        stream_platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WatchListAV(APIView):
     
     def get(self, request):
         movies = WatchList.objects.all()
         serializer = WatchListSerializer(movies,many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)

     def post(self, request):
         serializer= WatchListSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
         else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class WatchDetailsAV(APIView):     

    def get(self, request,pk): 

        try:
            watchlist=WatchList.objects.get(pk=pk) 
        except WatchList.DoesNotExist:
            return Response({'error':'movie not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=WatchListSerializer(watchlist)
        return Response(serializer.data,status=status.HTTP_200_OK) 

    def put(self, request,pk):
        watchlist=WatchList.objects.get(pk=pk)    
        serializer = WatchListSerializer(watchlist,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors)    
    def delete(self,request,pk):
        watchlist =WatchList.objects.get(pk=pk)
        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        


