import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    pq = PriorityQueue()
    pq.enqueue({"name_file": "longo", "qtd_linhas": 12})
    pq.enqueue({"name_file": "curto", "qtd_linhas": 2})
    pq.enqueue({"name_file": "medio", "qtd_linhas": 7})
    assert len(pq) == 3
    result = pq.search(1)
    assert result["name_file"] == "longo"
    assert result["qtd_linhas"] == 12
    assert len(pq) == 3
    remove1 = pq.dequeue()
    assert len(pq) == 2
    assert remove1["name_file"] == 'curto'
    remove2 = pq.dequeue()
    assert len(pq) == 1
    assert remove2["name_file"] == 'longo'
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        pq.search(2)