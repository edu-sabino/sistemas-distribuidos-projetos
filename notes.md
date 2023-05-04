Pub / Sub pattern

Entregar msgs para múltiplos consumidores

Muitos microsserviços distintos podem estar interessados na mesma mensagem.

Exemplo: Um usuário é criado numa plataforma, uma mensagem é criada com as informações deste usuário.

Setores como "promoções", "auditoria", "proteção de dados", etc., podem estar interessados em processar a mesma mensagem acima.

O produtor não terá ideia de quantas filas serão criadas, portanto não precisa declarar qual é a fila

As filas serão extintas quando não tiverem mensagens
