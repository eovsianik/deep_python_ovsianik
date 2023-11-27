from lru_cache import LRUCache


def test_get_values():
    cache1 = LRUCache(2)
    cache1.set("k1", "val1")
    cache1.set("k2", "val2")
    assert cache1.get("k2") == "val2"
    assert cache1.get("k1") == "val1"


def test_set_new_values():
    cache1 = LRUCache(2)
    cache1.set("k1", "val1")
    cache1.set("k2", "val2")
    cache1.set("k1", "VAL1")
    cache1.set("k2", "VAL2")
    assert cache1.get("k2") == "VAL2"
    assert cache1.get("k1") == "VAL1"


def test_get_wrong_value():
    cache2 = LRUCache(2)
    cache2.set("k1", "val1")
    cache2.set("k2", "val2")
    assert cache2.get("k2") == "val2"
    assert cache2.get("k1") == "val1"
    assert cache2.get("k3") is None


def test_donot_get_wrong_value():
    cache3 = LRUCache(2)
    cache3.set("k1", "val1")
    cache3.set("k2", "val2")
    cache3.set("k3", "val3")
    assert cache3.get("k3") == "val3"
    assert cache3.get("k1") is None
    assert cache3.get("k2") == "val2"


def test_several_calls():
    cache4 = LRUCache(3)
    cache4.set("k1", "val1")
    cache4.set("k2", "val2")
    cache4.set("k3", "val3")
    assert cache4.get("k4") is None
    assert cache4.get("k2") == "val2"
    assert cache4.get("k1") == "val1"
    cache4.set("k4", "val4")
    assert cache4.get("k2") == "val2"
    assert cache4.get("k3") is None
    assert cache4.get("k1") == "val1"


def test_lotsof_items():
    cache5 = LRUCache(5)
    cache5.set("k1", "val1")
    cache5.set("k2", "val2")
    cache5.set("k3", "val3")
    cache5.set("k4", "val4")
    cache5.set("k5", "val5")
    assert cache5.get("k6") is None
    assert cache5.get("k2") == "val2"
    assert cache5.get("k1") == "val1"
    cache5.set("k6", "val6")
    assert cache5.get("k2") == "val2"
    assert cache5.get("k3") is None
    assert cache5.get("k1") == "val1"


def test_lotsof_call_for_one():
    cache6 = LRUCache(5)
    cache6.set("k1", "val1")
    cache6.set("k2", "val2")
    cache6.set("k3", "val3")
    cache6.set("k4", "val4")
    cache6.set("k5", "val5")
    assert cache6.get("k5") == "val5"
    assert cache6.get("k5") == "val5"
    assert cache6.get("k5") == "val5"
    assert cache6.get("k5") == "val5"
    assert cache6.get("k5") == "val5"
    assert cache6.get("k1") == "val1"
    assert cache6.get("k2") == "val2"
    assert cache6.get("k3") == "val3"
    assert cache6.get("k4") == "val4"


def test_all_new():
    cache7 = LRUCache(5)
    cache7.set("k1", "val1")
    cache7.set("k2", "val2")
    cache7.set("k3", "val3")
    cache7.set("k4", "val4")
    cache7.set("k5", "val5")
    assert cache7.get("k5") == "val5"
    assert cache7.get("k1") == "val1"
    assert cache7.get("k2") == "val2"
    assert cache7.get("k3") == "val3"
    assert cache7.get("k4") == "val4"
    cache7.set("k6", "val6")
    cache7.set("k7", "val7")
    cache7.set("k8", "val8")
    cache7.set("k9", "val9")
    cache7.set("k10", "val10")
    assert cache7.get("k4") is None
    assert cache7.get("k5") is None
    assert cache7.get("k3") is None
    assert cache7.get("k2") is None
    assert cache7.get("k1") is None
    assert cache7.get("k6") == "val6"
    assert cache7.get("k7") == "val7"
    assert cache7.get("k8") == "val8"
    assert cache7.get("k9") == "val9"
    assert cache7.get("k10") == "val10"


def test_like_in_task():
    cache8 = LRUCache(2)
    cache8.set("k1", "val1")
    cache8.set("k2", "val2")
    assert cache8.get("k3") is None
    assert cache8.get("k2") == "val2"
    assert cache8.get("k1") == "val1"
    cache8.set("k3", "val3")
    assert cache8.get("k3") == "val3"
    assert cache8.get("k2") is None
    assert cache8.get("k1") == "val1"


def test_lrucashe_size_is_one():
    cache9 = LRUCache(1)
    cache9.set("k1", "val1")
    assert cache9.get("k1") == "val1"
    cache9.set("k2", "val2")
    assert cache9.get("k1") is None
    assert cache9.get("k2") == "val2"
    cache9.set("k3", "val3")
    assert cache9.get("k3") == "val3"
    assert cache9.get("k2") is None
    assert cache9.get("k1") is None


def test_chage_value_not_key():
    cache10 = LRUCache(4)
    cache10.set("k1", "val1")
    cache10.set("k2", "val2")
    cache10.set("k3", "val3")
    cache10.set("k4", "val4")
    assert cache10.get("k1") == "val1"
    assert cache10.get("k2") == "val2"
    assert cache10.get("k3") == "val3"
    assert cache10.get("k4") == "val4"
    cache10.set("k1", "new_value")
    cache10.set("k5", "val5")
    assert cache10.get("k1") == "new_value"
    assert cache10.get("k2") is None
    assert cache10.get("k3") == "val3"
    assert cache10.get("k4") == "val4"
    assert cache10.get("k5") == "val5"
