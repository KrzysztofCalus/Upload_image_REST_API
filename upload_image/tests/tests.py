import pytest

from upload_image.models import ImageModel, UserModel, PlansModel


@pytest.mark.django_db
def test_thumbnails(client, set_up):
    response = client.get("/images", {}, format='json')
    assert response.status_code == 200
    assert ImageModel.objects.count() == len(response.data)


@pytest.mark.django_db
def test_api(client, set_up):
    response = client.get(f"/images", format='json')
    assert response.status_code == 200
    for field in ("thumbnail_200", "thumbnail_400", "original_image"):
        assert field in response.data

@pytest.mark.django_db
def test_add_cinema(client, set_up):
    image_count = ImageModel.objects.count()
    response = client.post("/images", "test_image.png", format='json')
    assert response.status_code == 201
    assert ImageModel.objects.count() == image_count + 1
