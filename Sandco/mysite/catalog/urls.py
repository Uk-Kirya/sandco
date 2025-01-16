from django.urls import path

from .views import (
    HomeView,
    LibraryView,
    CompanyView,
    OriginsView,
    AboutProductView,
    ProjectsView,
    TeamView,
    NewsView,
    ContactsView,
    PolicyView,
    NewsDetailsView,
    ProjectDetailView,
    LibraryDetailView,
    ProductDetailsView,
    SendApplication,
    ApplicationSuccessView,
    ProductApplicationView,
)

app_name = "catalog"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("policy/", PolicyView.as_view(), name="policy"),
    path("library/", LibraryView.as_view(), name="library"),
    path("library/<slug:slug>", LibraryDetailView.as_view(), name="library-details"),
    path("products/<slug:slug>", ProductDetailsView.as_view(), name="product-details"),
    path("company/", CompanyView.as_view(), name="company"),
    path("company/origins/", OriginsView.as_view(), name="origins"),
    path("company/about-product/", AboutProductView.as_view(), name="about-product"),
    path("company/projects/", ProjectsView.as_view(), name="projects"),
    path("company/projects/<slug:slug>", ProjectDetailView.as_view(), name="project-details"),
    path("company/team/", TeamView.as_view(), name="team"),
    path("blog/", NewsView.as_view(), name="blog"),
    path("blog/<slug:slug>", NewsDetailsView.as_view(), name="blog-details"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("application/", SendApplication.as_view(), name="application"),
    path("product-application/", ProductApplicationView.as_view(), name="product-application"),
    path("application-success/", ApplicationSuccessView.as_view(), name="application_success"),
]