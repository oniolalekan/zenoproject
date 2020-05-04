from zeno.models import ZenoItem
from zeno.serializers import ZenoItemSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.decorators import list_route
from rest_framework.response import Response

# Create your views here.
class ZenoItemViewSet(viewsets.ModelViewSet):
  queryset = ZenoItem.objects.all()
  serializer_class = ZenoItemSerializer

  def perform_create(self, serializer):
    # Save instance to get primary key and then update URL
    instance = serializer.save()
    instance.url = reverse('zenoitem-detail', args=[instance.pk], request=self.request)
    instance.save()

  # Deletes all zeno items
  def delete(self, request):
    ZenoItem.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT) 