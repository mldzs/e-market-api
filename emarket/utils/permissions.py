from rest_framework.permissions import BasePermission


class SuperUserPermissao(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_superuser


class EstabelecimentoPermissao(BasePermission):
    def has_permission(self, request, view):
        try:
            request.user.estabelecimento
            return True
        except Exception:
            return False


class ClientePermissao(BasePermission):
    def has_permission(self, request, view):
        try:
            request.user.cliente
            return True
        except Exception:
            return False


class EntregadorPermissao(BasePermission):
    def has_permission(self, request, view):
        try:
            request.user.entregador
            return True
        except Exception:
            return False


class ProprioUsuarioPermissao(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        return request.user == obj


class DonoDoVeiculoPermissao(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        try:
            return request.user.entregador.veiculo == obj
        except:
            return False


class ProprioProdutoSupermercadoPermissao(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        try:
            return obj.estabelecimento == request.user.estabelecimento
        except:
            return False


class ProprioClienteProdutoCarrinhoPermissao(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        try:
            return obj.carrinho.cliente == request.user.cliente
        except:
            return False


class ProprioCarrinhoClientePermissao(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        try:
            return obj.cliente == request.user.cliente
        except:
            return False
