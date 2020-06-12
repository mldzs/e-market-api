from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from fcm_django.api.rest_framework import FCMDeviceViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .carrinho.views import CarrinhoViewSet
from .categoria.views import CategoriaViewSet
from .marca.views import MarcaViewSet
from .pedido.views import PedidoViewSet
from .produto.views import ProdutoCarrinhoViewSet, ProdutoViewSet, TipoProdutoViewSet
from .usuario.views import EstabelecimentoViewSet, ClienteViewSet, EntregadorViewSet, EnderecoViewSet, TokenLogin
from .veiculo.views import VeiculoViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r"marcas", MarcaViewSet)
router.register(r"veiculos", VeiculoViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"enderecos", EnderecoViewSet)
router.register(r"estabelecimentos", EstabelecimentoViewSet)
router.register(r"clientes", ClienteViewSet)
router.register(r"entregadores", EntregadorViewSet)
router.register(r"tipos-produto", TipoProdutoViewSet)
router.register(r"produtos", ProdutoViewSet)
router.register(r"produtos-carrinho", ProdutoCarrinhoViewSet)
router.register(r"carrinho", CarrinhoViewSet)
router.register(r"pedidos", PedidoViewSet)
router.register(r"devices", FCMDeviceViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="E-Market API",
        default_version="v1",
        description="API to E-Market App",
        contact=openapi.Contact(email="s.mieldazis@hotmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("token/", TokenLogin.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
