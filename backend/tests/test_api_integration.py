from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
BASE = {'symbol': 'DEMO'}
CONSERVATIVE = {'risk_tolerance': 'CONSERVATIVE', 'investment_horizon': 'LONG_TERM', 'volatility_tolerance': 'LOW'}
AGGRESSIVE = {'risk_tolerance': 'AGGRESSIVE', 'investment_horizon': 'SHORT_TERM', 'volatility_tolerance': 'HIGH'}

def test_api_accepts_profile_and_returns_final_synthesis():
    response = client.post('/api/intelligence/analyze', json={**BASE, 'user_profile': CONSERVATIVE})
    body = response.json()
    assert response.status_code == 200
    assert body['status'] == 'SUCCESS'
    assert body['profile'] == CONSERVATIVE
    assert body['recommendation'] in {'BUY', 'HOLD', 'AVOID', 'INSUFFICIENT_DATA'}
    assert len(body['agents']) == 3 and body['evidence'] and body['decision_trace']
    assert body['run_id'] == body['request_id']

def test_api_uses_default_profile_when_omitted():
    response = client.post('/api/intelligence/analyze', json=BASE)
    assert response.status_code == 200
    assert response.json()['profile']['risk_tolerance'] == 'MODERATE'

def test_api_rejects_malformed_profile():
    response = client.post('/api/intelligence/analyze', json={**BASE, 'user_profile': {**CONSERVATIVE, 'risk_tolerance': 'INVALID'}})
    assert response.status_code == 422

def test_api_personalizes_identical_market_input():
    conservative = client.post('/api/intelligence/analyze', json={**BASE, 'user_profile': CONSERVATIVE}).json()
    aggressive = client.post('/api/intelligence/analyze', json={**BASE, 'user_profile': AGGRESSIVE}).json()
    assert conservative['score'] != aggressive['score'] or conservative['recommendation'] != aggressive['recommendation'] or conservative['risk_level'] != aggressive['risk_level']
