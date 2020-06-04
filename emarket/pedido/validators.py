from rest_framework.exceptions import ValidationError


class MesmoUsuarioCarrinhoERequisicao:
    requires_context = True

    def __call__(self, value, serializer_field):
        request = serializer_field.context.get("request")
        user = request.user

        if user != value.cliente.usuario:
            raise ValidationError({"message": "Você não pode adicionar um carrinho que não é seu!"})
