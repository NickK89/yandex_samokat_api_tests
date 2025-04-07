import sender_stand_request

# Никита Кузькин, 28-я когорта — Финальный проект. Инженер по тестированию плюс

def test_get_order_status_code_200():
    track_number = sender_stand_request.post_order_and_get_track_number()
    actual_status_code = sender_stand_request.get_order_by_track(track_number).status_code
    expected_status_code = 200

    assert actual_status_code == expected_status_code


