import importlib

from django.test import TestCase

from authentication.models import USER_TYPE_CHOICES, User


class TestCreation(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Get list of  types of user tuples defined in authentication/models.py
        cls._list_of_tuples_user_types = [(t[0], t[1]) for t in USER_TYPE_CHOICES]
        # Get biggest number and create inexistent type of user
        cls._inexistent_user_type = cls._list_of_tuples_user_types[-1][0] + 1

    def test_create_user_and_profile(self):

        print("########## test_create_user_and_profile ##########")

        # If we do not put the "with self . . ." line, it will actually raise an
        # error.
        # So with the line, the test will pass, it means, it is true that the
        # creation is failing.

        """ Create user without user type """

        with self.assertRaises(ValueError):
            User.objects.create_user('t02@g.com', password='x')

        """ User with an inexistent user type """

        with self.assertRaises(ValueError):
            User.objects.create_user(
                't02@g.com', password='x', user_type=self._inexistent_user_type
            )

        """ Creation of a user """

        # self.assertTrue(User.objects.create_user('tester02@hotmail.com',
        #                                         password='x',user_type=1))

        """ Creation of a user and profiles """

        # Create one user of each type, and see if their profiles are created.
        # CAVEAT: User choices must be same name as the class in entities models
        list_of_usr_count_before = []
        list_of_usr_count_after = []
        for t in self._list_of_tuples_user_types:
            list_of_usr_count_before += [
                getattr(
                    importlib.import_module("entities.models"), t[1]
                ).objects.count()
            ]
            User.objects.create_user(
                'usr{}@hotmail.com'.format(t[0]), password='x', user_type=t[0]
            )
            list_of_usr_count_after += [
                getattr(
                    importlib.import_module("entities.models"), t[1]
                ).objects.count()
            ]
        # Check that the amount of user types objects were created
        print('List before: {}'.format(list_of_usr_count_before))
        print('List after: {}'.format(list_of_usr_count_after))

        self.assertTrue(len(list_of_usr_count_before) == len(list_of_usr_count_after))
        self.assertTrue(
            sum(list_of_usr_count_after) - sum(list_of_usr_count_before)
            == len(self._list_of_tuples_user_types)
        )
        # Check if one of each was created. For every elem is +1
        self.assertTrue(
            all(
                [
                    b == (a + 1)
                    for (a, b) in zip(list_of_usr_count_before, list_of_usr_count_after)
                ]
            )
        )

        return

    def print_usr_counts(self, message=""):
        print(message)
        for t in self._list_of_tuples_user_types:
            print(
                'Class: {}, Count: {}'.format(
                    t[1],
                    getattr(
                        importlib.import_module("entities.models"), t[1]
                    ).objects.count(),
                )
            )

    def test_utility(self):
        print("########## test_utility ##########")
        from djangofiltertest.utilities_test import create_insert_test_users

        self.print_usr_counts(message='-- Before creating test users')
        create_insert_test_users()
        self.print_usr_counts(message='-- After creating test users')
