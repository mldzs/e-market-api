from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .carrinho.views import CarrinhoViewSet
from .categoria.views import CategoriaViewSet
from .marca.views import MarcaViewSet
from .pedido.views import PedidoViewSet
from .produto.views import ProdutoCarrinhoViewSet, ProdutoViewSet, TipoProdutoViewSet
from .usuario.views import EstabelecimentoViewSet, ClienteViewSet, EntregadorViewSet, EnderecoViewSet
from .veiculo.views import VeiculoViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r'marcas', MarcaViewSet)
router.register(r'veiculos', VeiculoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'estabelecimentos', EstabelecimentoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'entregadores', EntregadorViewSet)
router.register(r'tipos-produto', TipoProdutoViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'produtos-carrinho', ProdutoCarrinhoViewSet)
router.register(r'carrinho', CarrinhoViewSet)
router.register(r'pedidos', PedidoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
