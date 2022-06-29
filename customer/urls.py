from django.urls import path
from customer import views
urlpatterns=[
    path("home",views.CustomerIndex.as_view(),name="custhome"),
    path("accounts/register",views.SignUp.as_view(),name="signup"),
    path("accounts/login",views.SignIn.as_view(),name="login"),
    path("accounts/logout",views.signout,name="signout"),
    path("accounts/password/reset",views.PasswordResetView.as_view(),name="passwordreset"),
    path("carts/items/add/<int:id>",views.AddToCart,name="addtocart"),
    path("carts/all",views.ViewMyCart.as_view(),name="viewmycart"),
    path("carts/remove/<int:id>",views.remove_from_cart,name="remove"),
    path("order/add<int:c_id>/<int:p_id>",views.OrderCreateView.as_view(),name="ordercreate"),
    path("orders/all",views.OrdresListView.as_view(),name="listorders"),
    path("orders/reviews/add/<int:id>",views.CreateReview.as_view(),name="review"),
    path("accounts/views/detailview/<int:id>",views.DetailallViews.as_view(),name="detailview")

]