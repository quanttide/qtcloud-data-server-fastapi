"""
Unittests for dataset endpoints
"""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_datasets():
    """
    Test list datasets
    :return:
    """
    response = client.get('/datasets/')
    assert response.status_code == 200
    assert response.json() == []


def test_create_dataset():
    """
    Test create dataset
    :return:
    """
    dataset_data = {
        'name': 'test',
        'verbose_name': '测试数据集',
        'readme': '这是一个测试数据集',
    }
    response = client.post('/datasets/', json=dataset_data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data['id'] is not None
    assert response_data['created_at'] is not None
    assert response_data['updated_at'] is not None
    assert response_data['name'] == dataset_data['name']
    assert response_data['verbose_name'] == dataset_data['verbose_name']
    assert response_data['readme'] == dataset_data['readme']


def test_delete_dataset():
    """
    Test delete dataset
    """
    # not found
    response = client.delete('/datasets/test/')
    assert response.status_code == 404
