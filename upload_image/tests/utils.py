from upload_image.models import ImageModel, PlansModel, UserModel


def create_plan():
    PlansModel.objects.create(
        name="test_plan",
        thumbnail_200=True,
        thumbnail_400=False,
        original_image=False,
        link=False
    )


def create_user():
    UserModel.objects.create(
        user=10,
        plan=2
    )


def create_image():
    ImageModel.objects.create(
        owner=2,
        image="test.png"
    )
