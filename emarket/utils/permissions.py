from rest_framework.permissions import BasePermission


class SuperUserPermissao(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_superuser


class EstabelecimentoPermissao(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, "estabelecimento")


class ClientePermissao(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, "cliente")


class EntregadorPermissao(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, "entregador")


class ProprioUsuarioPermissao(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        return request.user == obj


class DonoDoVeiculoPermissao(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        try:
            return request.user.entregador.veiculo == obj
        except Exception:
            return False


class ProprioProdutoSupermercadoPermissao(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        try:
            return obj.estabelecimento == request.user.estabelecimento
        except Exception:
            return False


class ProprioClienteProdutoCarrinhoPermissao(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        try:
            return obj.carrinho.cliente == request.user.cliente
        except Exception:
            return False


class ProprioCarrinhoClientePermissao(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        try:
            return obj.cliente == request.user.cliente
        except Exception:
            return False


class ProprioPedidoClientePermissao(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        try:
            return obj.carrinho.cliente == request.user.cliente
        except Exception:
            return False


class PedidoEstabelecimento(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        try:
            return obj.carrinho.estabelecimento == request.user.estabelecimento
        except Exception:
            return False
