def test_crud_flow(client):
    # CREATE
    resp = client.post("/tasks", json={"title": "Test", "description": "First task"})
    assert resp.status_code == 200
    task = resp.json()
    task_id = task["id"]

    # GET
    resp = client.get(f"/tasks/{task_id}")
    assert resp.status_code == 200
    assert resp.json()["title"] == "Test"

    # LIST
    resp = client.get("/tasks")
    assert resp.status_code == 200
    assert len(resp.json()) >= 1

    # UPDATE
    resp = client.put(f"/tasks/{task_id}", json={"status": "в работе"})
    assert resp.status_code == 200
    assert resp.json()["status"] == "в работе"

    # DELETE
    resp = client.delete(f"/tasks/{task_id}")
    assert resp.status_code == 200
    assert resp.json()["ok"] is True

    # GET after delete
    resp = client.get(f"/tasks/{task_id}")
    assert resp.status_code == 404
