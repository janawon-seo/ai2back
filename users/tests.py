from django.urls import reverse
from rest_framework.test import APITestCase

# Create your tests here.

class UserRegistrationAPIViewTest(APITestCase):
    def test_registration(self):
        url = reverse("user_view")
        user_data = {
            "username" : "sjw",
            "fullname" : "서장원",
            "email" : "sjw@a.com",
            "password" : "qwe123",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.data,{"message": "가입 완료!!"})
        # 더 좋은 컨벤션
        self.assertEqual(response.data,["message"], "가입 완료!!")