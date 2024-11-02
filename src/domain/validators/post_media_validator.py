from src.domain.entities.post_media import PostMedia, MediaType

def validate_post_media(post_media_list: list[PostMedia]) -> bool:
    """
    Valida as regras de mídia para posts:
    - Máximo 4 mídias por post
    - Posições devem ser sequenciais (0-3)
    """
    if not post_media_list:
        return True

    if len(post_media_list) > 4:
        raise ValueError("Posts podem ter no máximo 4 mídias")

    positions = [media.position for media in post_media_list]
    if positions != list(range(len(positions))):
        raise ValueError("Posições das mídias devem ser sequenciais")

    # Validação opcional: verificar se todos os campos obrigatórios estão preenchidos
    for media in post_media_list:
        if not media.url:
            raise ValueError("URL da mídia é obrigatória")
        if not media.media_type:
            raise ValueError("Tipo de mídia é obrigatório")
        if not media.content_type:
            raise ValueError("Content-type da mídia é obrigatório")
        if media.position is None:
            raise ValueError("Posição da mídia é obrigatória")
        if media.position < 0 or media.position > 3:
            raise ValueError("Posição da mídia deve estar entre 0 e 3")

    return True

def validate_media_type(media_type: str) -> bool:
    """
    Valida se o tipo de mídia é suportado
    """
    try:
        MediaType(media_type)
        return True
    except ValueError as exc:
        raise ValueError(f"Tipo de mídia '{media_type}' não suportado. Use {[t.value for t in MediaType]}") from exc
