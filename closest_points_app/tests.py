from django.test import TestCase, Client
from .models import PointSet
from .utils import find_closest_points
from .views import ClosestPointsView
from rest_framework import status

class PointSetTestCase(TestCase):
    def setUp(self):
        PointSet.objects.create(received_points="2,2;-1,30;20,11;4,5", closest_points="2,2;4,5")

    def test_pointset_created(self):
        pointset = PointSet.objects.first()
        self.assertEqual(pointset.received_points, "2,2;-1,30;20,11;4,5")
        self.assertEqual(pointset.closest_points, "2,2;4,5")

class UtilsTestCase(TestCase):
    def test_find_closest_points(self):
        points = [[2,2], [-1,30], [20,11], [4,5]]
        closest_points = find_closest_points(points)
        self.assertEqual(closest_points, [[2,2], [4,5]])

class ClosestPointsViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_closest_points_view(self):
        response = self.client.post('/closest-points/', {"received_points": "2,2;-1,30;20,11;4,5"}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"closest_points": "2,2;4,5"})

    def test_closest_points_view_success(self):
        response = self.client.post('/closest-points/', {"received_points": "2,2;-1,30;20,11;4,5"}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"closest_points": "2,2;4,5"})

    def test_closest_points_view_bad_request(self):
        # No 'received_points' key in JSON body
        response = self.client.post('/closest-points/', {"not_points": "2,2;-1,30;20,11;4,5"}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Malformed points
        response = self.client.post('/closest-points/', {"received_points": "2,2;-1,30;20,11;4,5;bad,point"}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_closest_points_view_not_enough_points(self):
        # Only one point provided
        response = self.client.post('/closest-points/', {"received_points": "2,2"}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class PointSetListViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        PointSet.objects.create(received_points="2,2;-1,30;20,11;4,5", closest_points="2,2;4,5")
        PointSet.objects.create(received_points="3,3;0,0;10,10", closest_points="3,3;0,0")

    def test_pointset_list_view_search(self):
        response = self.client.get('/pointsets/?search=20')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['received_points'], "2,2;-1,30;20,11;4,5")
        self.assertEqual(response.json()[0]['closest_points'], "2,2;4,5")
