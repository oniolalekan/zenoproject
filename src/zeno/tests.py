from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from zeno.models import ZenoItem

# Create your tests here.
def createItem(client):
  url = reverse('zenoitem-list')
  data = {'zenoid': 37393}
  return client.post(url, data, format='json')

class TestCreateZenoItem(APITestCase):
  """
  Ensure we can create a new zeno item
  """
  def setUp(self):
    self.response = createItem(self.client)

  def test_received_201_created_status_code(self):
    self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

  def test_received_location_header_hyperlink(self):
    self.assertRegexpMatches(self.response['Location'], '^http://.+/zenos/[\d]+$')

  def test_item_was_created(self):
    self.assertEqual(ZenoItem.objects.count(), 1)

  def test_item_has_correct_zenoid(self):
    self.assertEqual(ZenoItem.objects.get().zenoid, 37393)

class TestUpdateZenoItem(APITestCase):
  """
  Ensure we can update an existing zeno item using PUT
  """
  def setUp(self):
    response = createItem(self.client)
    self.assertEqual(ZenoItem.objects.get().timestamp, None)
    url = response['Location']
    data = {'zenoid': 37393, 'timestamp': "08:34.4"}
    self.response = self.client.put(url, data, format='json')

  def test_received_200_created_status_code(self):
    self.assertEqual(self.response.status_code, status.HTTP_200_OK)

  def test_item_was_updated(self):
    self.assertEqual(ZenoItem.objects.get().timestamp, "08:34.4")

class TestPatchZenoItem(APITestCase):
  """
  Ensure we can update an existing zeno item using PATCH
  """
  def setUp(self):
    response = createItem(self.client)
    self.assertEqual(ZenoItem.objects.get().timestamp, None)
    url = response['Location']
    data = {'zenoid': 37393, 'timestamp': "08:34.4"}
    self.response = self.client.patch(url, data, format='json')

  def test_received_200_ok_status_code(self):
    self.assertEqual(self.response.status_code, status.HTTP_200_OK)

  def test_item_was_updated(self):
    self.assertEqual(ZenoItem.objects.get().timestamp, "08:34.4")

class TestDeleteZenoItem(APITestCase):
  """
  Ensure we can delete a zeno item
  """
  def setUp(self):
    response = createItem(self.client)
    self.assertEqual(ZenoItem.objects.count(), 1)
    url = response['Location']
    self.response = self.client.delete(url)

  def test_received_204_no_content_status_code(self):
    self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

  def test_the_item_was_deleted(self):
    self.assertEqual(ZenoItem.objects.count(), 0)

class TestDeleteAllItems(APITestCase):
  """
  Ensure we can delete all zeno items
  """
  def setUp(self):
    createItem(self.client)
    createItem(self.client)
    self.assertEqual(ZenoItem.objects.count(), 2)
    self.response = self.client.delete(reverse('zenoitem-list'))

  def test_received_204_no_content_status_code(self):
    self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

  def test_all_items_were_deleted(self):
    self.assertEqual(ZenoItem.objects.count(), 0)