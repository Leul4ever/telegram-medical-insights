from api.schemas import ProductMention, ChannelActivity

def test_product_mention_schema():
    data = {"term": "paracetamol", "count": 50}
    obj = ProductMention(**data)
    assert obj.term == "paracetamol"
    assert obj.count == 50

def test_channel_activity_schema():
    data = {"date": "2024-01-01", "message_count": 10}
    obj = ChannelActivity(**data)
    assert obj.date == "2024-01-01"
    assert obj.message_count == 10
