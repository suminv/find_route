from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from routes.forms import RouteForm
from routes.views import home
from cities.models import City
from cities.views import CityDetailView
from trains.models import Train
from routes.utils import dfs_paths, get_graph


class AllTestsCase(TestCase):

    def setUp(self) -> None:
        self.city_A = City.objects.create(name='A')
        self.city_B = City.objects.create(name='B')
        self.city_C = City.objects.create(name='C')
        self.city_D = City.objects.create(name='D')
        self.city_E = City.objects.create(name='E')
        lst = [
            Train(name='t1', from_city=self.city_A, to_city=self.city_B,
                  travel_time=9),
            Train(name='t2', from_city=self.city_B, to_city=self.city_D,
                  travel_time=8),
            Train(name='t3', from_city=self.city_A, to_city=self.city_C,
                  travel_time=7),
            Train(name='t4', from_city=self.city_C, to_city=self.city_B,
                  travel_time=6),
            Train(name='t5', from_city=self.city_B, to_city=self.city_E,
                  travel_time=3),
            Train(name='t6', from_city=self.city_B, to_city=self.city_A,
                  travel_time=11),
            Train(name='t7', from_city=self.city_A, to_city=self.city_C,
                  travel_time=10),
            Train(name='t8', from_city=self.city_E, to_city=self.city_D,
                  travel_time=5),
            Train(name='t9', from_city=self.city_D, to_city=self.city_E,
                  travel_time=4)
        ]
        Train.objects.bulk_create(lst)

    def test_model_city_duplicate(self):
        """Testing duplicate create city"""
        city = City(name="A")
        with self.assertRaises(ValidationError):
            city.full_clean()

    def test_model_train_duplicate(self):
        """Testing duplicate create train"""
        train = Train(name='t1', from_city=self.city_A, to_city=self.city_B,
                      travel_time=129)
        with self.assertRaises(ValidationError):
            train.full_clean()

    def test_model_train_train_duplicate(self):
        """Testing duplicate create route"""
        train = Train(name='t1234', from_city=self.city_A, to_city=self.city_B,
                      travel_time=9)
        with self.assertRaises(ValidationError):
            train.full_clean()
        try:
            train.full_clean()
        except ValidationError as e:
            self.assertEqual({'__all__': ['Please change the travel time!']}, e.message_dict)
            self.assertIn('Please change the travel time!', e.messages)

    def test_home_routes_views(self):
        """Testing address home,
         exist template,
         match function"""
        response = self.client.get(reverse('home'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, template_name='routes/route.html')
        self.assertEqual(response.resolver_match.func, home)

    def test_cbv_detail_views(self):
        """Testing address detail,
         exist template,
         match function by name"""
        response = self.client.get(reverse('cities:detail', kwargs={'pk': self.city_A.id}))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, template_name='cities/detail.html')
        self.assertEqual(response.resolver_match.func.__name__, CityDetailView.as_view().__name__)

    def test_find_all_routes(self):
        """Testing the make graph and searching routes."""
        qs = Train.objects.all()
        graph = get_graph(qs)
        all_routes = list(dfs_paths(graph, self.city_A.id, self.city_E.id))
        self.assertEqual(len(all_routes), 4)

    def test_valid_route_form(self):
        """Checking valid form """
        data = {
            'from_city': self.city_A.id,
            'to_city': self.city_B.id,
            'cities': [self.city_E.id, self.city_B],
            'travelling_time': 9,
        }
        form = RouteForm(data=data)
        self.assertTrue(form.is_valid())

    def test_message_error_more_time(self):
        """Testing message : Travel time more than specified"""
        data = {
            'from_city': self.city_A.id,
            'to_city': self.city_E.id,
            'cities': [self.city_C.id],
            'travelling_time': 9,
        }
        response = self.client.post('/find_routes/', data)
        self.assertContains(response, 'Travel time more than specified.', 1, 200)

    def test_message_error_through_city(self):
        """Testing message : The route does not exist through the city."""
        data = {
            'from_city': self.city_B.id,
            'to_city': self.city_E.id,
            'cities': [self.city_C.id],
            'travelling_time': 600,
        }
        response = self.client.post('/find_routes/', data)
        self.assertContains(response, 'The route does not exist through the city.', 1, 200)

