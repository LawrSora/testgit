from models.active_record_entity import ActiveRecordEntity

class Articles(ActiveRecordEntity):
    __tableneme__ = 'articles'
    author_id = None
    name = None
    text = None
    create_at = None